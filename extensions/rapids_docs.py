# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# SPDX-License-Identifier: Apache-2.0

"""Data-driven rendering and notice support for the RAPIDS documentation portal."""

from __future__ import annotations

import email.utils
import html
import json
import shutil
from datetime import UTC, datetime
from pathlib import Path
from xml.etree import ElementTree

import frontmatter
import yaml
from bs4 import BeautifulSoup
from dateutil import parser as date_parser
from jinja2 import Environment, FileSystemLoader, StrictUndefined


def _source_dir(app) -> Path:
    return Path(app.srcdir)


def _date(value) -> datetime:
    if isinstance(value, datetime):
        return value
    if hasattr(value, "year") and hasattr(value, "month") and hasattr(value, "day"):
        return datetime(value.year, value.month, value.day)
    return date_parser.parse(str(value))


def _long_date(value) -> str:
    parsed = _date(value)
    return f"{parsed.strftime('%B')} {parsed.day}, {parsed.year}"


def _short_date(value) -> str:
    parsed = _date(value)
    return f"{parsed.strftime('%a, %b')} {parsed.day}, {parsed.year}"


def _load_data(app) -> dict:
    data_dir = _source_dir(app) / "_data"
    with (data_dir / "docs.yml").open() as file:
        docs = yaml.safe_load(file)
    with (data_dir / "platform_support.yml").open() as file:
        platform_support = yaml.safe_load(file)
    with (data_dir / "releases.json").open() as file:
        releases = json.load(file)
    with (data_dir / "previous_releases.json").open() as file:
        previous_releases = json.load(file)

    notices = []
    for path in sorted((_source_dir(app) / "notices").glob("r[dgs]n[0-9][0-9][0-9][0-9].md")):
        post = frontmatter.load(path)
        metadata = dict(post.metadata)
        metadata["docname"] = f"notices/{path.stem}"
        metadata["body"] = post.content
        notices.append(metadata)

    return {
        "docs": docs,
        "notices": notices,
        "platform_support": platform_support,
        "previous_releases": previous_releases,
        "releases": releases,
    }


def _version_label(project: dict, version_name: str, releases: dict) -> str:
    override = project.get("version-overrides", {}).get(version_name)
    if override:
        return str(override)
    version_key = "ucxx_version" if "ucxx" in project["path"].lower() else "version"
    return str(releases[version_name][version_key])


def _api_docs(data: dict, section: str) -> str:
    blocks = []
    for project in data["docs"][section].values():
        if project.get("hidden", False):
            continue
        versions = []
        for name in ("stable", "nightly", "legacy"):
            if project["versions"].get(name) == 1:
                label = _version_label(project, name, data["releases"])
                versions.append(f"**[{name} ({label})](/api/{project['path']}/{name}/)**")
        links = []
        if project.get("cllink"):
            links.append(f"**[changelog]({project['cllink']})**")
        links.append(f"**[github]({project['ghlink']})**")
        blocks.append(
            "\n".join(
                [
                    f"### {project['name']}",
                    "",
                    project["desc"],
                    "",
                    "#### DOCS" + (" " + " | ".join(versions) if versions else ""),
                    "",
                    "#### LINKS " + " | ".join(links),
                ]
            )
        )
    return "\n\n".join(blocks)


def _compute_capability(cuda: dict) -> str:
    capabilities = []
    for capability in cuda["compute_capability"]:
        sms = capability["sm"]
        if not isinstance(sms, list):
            sms = [sms]
        capabilities.append(f"{capability['name']} ({', '.join(map(str, sms))})")
    return ", ".join(capabilities) + " or newer"


def _platform_support(data: dict) -> str:
    releases = data["platform_support"]["releases"]
    links = ", ".join(
        f"[{release['version']}{' (nightly)' if release.get('nightly') else ''}]"
        f"(#rapids-{str(release['version']).replace('.', '')})"
        for release in releases
    )
    sections = [f"**Releases:** {links}"]
    for release in releases:
        title = f"## RAPIDS {release['version']}"
        if release.get("nightly"):
            title += " (nightly)"
        cuda_headers = [f"CUDA {cuda['major']}" for cuda in release["cuda"]]
        cuda_rows = [
            (
                "Toolkit",
                [
                    f"{cuda['toolkit_min']}"
                    + (
                        f" - {cuda['toolkit_max']}"
                        if cuda["toolkit_min"] != cuda["toolkit_max"]
                        else ""
                    )
                    for cuda in release["cuda"]
                ],
            ),
            ("Driver", [f"{cuda['driver_min']}+" for cuda in release["cuda"]]),
            ("Compute Capability", [_compute_capability(cuda) for cuda in release["cuda"]]),
        ]
        table = [
            "| | " + " | ".join(cuda_headers) + " |",
            "|:--|" + "|".join(":--" for _ in cuda_headers) + "|",
        ]
        table.extend(f"| **{name}** | " + " | ".join(values) + " |" for name, values in cuda_rows)
        sections.append(
            "\n".join(
                [
                    "---",
                    "",
                    title,
                    "",
                    '### <i class="fas fa-desktop" aria-hidden="true"></i> Operating Systems',
                    "",
                    f'- <i class="fab fa-linux" aria-hidden="true"></i> '
                    f"**Linux (glibc {release['glibc_min']}+):** {', '.join(release['cpu_arch'])} "
                    f"(tested on {', '.join(release['os_support'])})",
                    '- <i class="fab fa-windows" aria-hidden="true"></i> '
                    "**Windows:** Supported via [WSL](/install/#wsl2) with a compatible Linux distribution",
                    "",
                    '### <i class="fab fa-python" aria-hidden="true"></i> Python',
                    "",
                    f"**{', '.join(release['python'])}**",
                    "",
                    '### <i class="fas fa-microchip" aria-hidden="true"></i> CUDA',
                    "",
                    *table,
                    "",
                    '### <i class="fas fa-hammer" aria-hidden="true"></i> Source Builds',
                    "",
                    "| Dependency | Version |",
                    "|:--|:--|",
                    f"| **GCC** | {release['source_build']['gcc']} |",
                    f"| **CCCL** | {release['source_build']['cccl']} |",
                    f"| **nvCOMP** | {release['source_build']['nvcomp']} |",
                ]
            )
        )
    return "\n\n".join(sections)


def _schedule_table(release: dict) -> str:
    rows = [
        ("Development", release["dev"]),
        (
            "[Burn Down](/releases/process/#burn-down) (cuDF/RMM/rapids-cmake/raft/dask-cuda/KvikIO/ucxx/rapidsmpf/nvForest)",
            release["cudf_burndown"],
        ),
        ("[Burn Down](/releases/process/#burn-down) (others)", release["other_burndown"]),
        (
            "[Code Freeze/Testing](/releases/process/#code-freeze) (cuDF/RMM/rapids-cmake/raft/dask-cuda/KvikIO/ucxx/rapidsmpf/nvForest)",
            release["cudf_codefreeze"],
        ),
        (
            "[Code Freeze/Testing](/releases/process/#code-freeze) (others)",
            release["other_codefreeze"],
        ),
        ("[Release](/releases/process/#releasing)", release["release"]),
    ]
    output = ["| Phase | Start | End | Duration |", "|:--|:--|:--|:--|"]
    output.extend(
        f"| {name} | {_short_date(values['start'])} | {_short_date(values['end'])} | {values['days']} days |"
        for name, values in rows
    )
    return "\n".join(output)


def _current_schedules(data: dict) -> str:
    releases = data["releases"]
    return "\n\n".join(
        [
            f"## Release v{releases['nightly']['version']} Schedule",
            "**NOTE:** *Dates are subject to change at any time. Completed release schedules are posted "
            "[here](/releases/schedule/).*",
            _schedule_table(releases["nightly"]),
            f"## *PROPOSED* Release v{releases['next_nightly']['version']} Schedule",
            _schedule_table(releases["next_nightly"]),
        ]
    )


def _old_project_group(version: str) -> str:
    group = "cuDF/RMM"
    if version >= "23.06":
        group += "/rapids-cmake/"
        if version <= "24.12":
            group += "cugraph-ops/"
        group += "raft"
    return group


def _previous_schedules(data: dict) -> str:
    sections = []
    for release in data["previous_releases"]:
        output = [f"### Release v{release['version']} Schedule", ""]
        if release.get("dev"):
            rows = [("Development", release["dev"])]
            group_suffix = (
                " (cuDF/RMM/rapids-cmake/raft/dask-cuda/KvikIO/ucxx/rapidsmpf)"
                if release.get("other_burndown")
                else ""
            )
            rows.append(
                (
                    f"[Burn Down](/releases/process/#burn-down){group_suffix}",
                    release.get("cudf_burndown") or release["burndown"],
                )
            )
            if release.get("other_burndown"):
                rows.append(
                    (
                        "[Burn Down](/releases/process/#burn-down) (others)",
                        release["other_burndown"],
                    )
                )
            if release.get("cudf_codefreeze"):
                rows.append(
                    (
                        f"[Code Freeze/Testing](/releases/process/#code-freeze){group_suffix}",
                        release["cudf_codefreeze"],
                    )
                )
                rows.append(
                    (
                        "[Code Freeze/Testing](/releases/process/#code-freeze) (others)",
                        release["other_codefreeze"],
                    )
                )
            else:
                rows.append(
                    ("[Code Freeze/Testing](/releases/process/#code-freeze)", release["codefreeze"])
                )
            rows.append(("[Release](/releases/process/#releasing)", release["release"]))
            output.extend(["| Phase | Start | End | Duration |", "|:--|:--|:--|:--|"])
            output.extend(
                f"| {name} | {_short_date(values['start'])} | {_short_date(values['end'])} | {values['days']} days |"
                for name, values in rows
            )
        elif release.get("date"):
            output.extend(
                ["| Phase | Date |", "|:--|:--|", f"| Release | {_short_date(release['date'])} |"]
            )
        else:
            group = _old_project_group(release["version"])
            rows = [
                (f"Development ({group})", release["cudf_dev"]),
                ("Development (others)", release["other_dev"]),
                (f"[Burn Down](/releases/process/#burn-down) ({group})", release["cudf_burndown"]),
                ("[Burn Down](/releases/process/#burn-down) (others)", release["other_burndown"]),
                (
                    f"[Code Freeze/Testing](/releases/process/#code-freeze) ({group})",
                    release["cudf_codefreeze"],
                ),
                (
                    "[Code Freeze/Testing](/releases/process/#code-freeze) (others)",
                    release["other_codefreeze"],
                ),
                ("[Release](/releases/process/#releasing)", release["release"]),
            ]
            output.extend(["| Phase | Start | End | Duration |", "|:--|:--|:--|:--|"])
            output.extend(
                f"| {name} | {_short_date(values['start'])} | {_short_date(values['end'])} | {values['days']} days |"
                for name, values in rows
            )
        sections.append("\n".join(output))
    return "\n\n".join(sections)


def _notice_date(notice: dict) -> datetime:
    return _date(notice.get("notice_updated") or notice["notice_created"])


def _notice_table(data: dict, notice_type: str | None = None, pinned: bool = False) -> str:
    notices = data["notices"]
    if notice_type:
        notices = [notice for notice in notices if notice["notice_type"] == notice_type]
    if pinned:
        notices = [
            notice for notice in notices if str(notice.get("notice_pin", "")).lower() == "true"
        ]
    notices = sorted(notices, key=_notice_date, reverse=True)
    if not notices:
        return "## No current notices"
    output = [
        "| Notice | Title | Topic | RAPIDS Version | Updated |",
        "|:--|:--|:--|:--|:--|",
    ]
    for notice in notices:
        updated = notice.get("notice_updated")
        if not updated or _date(updated).date() == _date(notice["notice_created"]).date():
            updated = notice["notice_created"]
        output.append(
            f"| **{notice['notice_type'].upper()} {notice['notice_id']}**<br>**{notice['notice_status']}** "
            f"| [{notice['title']}](/notices/{Path(notice['docname']).name}/) "
            f"| {notice['notice_topic']} | {notice['notice_rapids_version']} | {_long_date(updated)} |"
        )
    return "\n".join(output)


def _jinja_environment(app) -> Environment:
    return Environment(
        loader=FileSystemLoader(app.srcdir),
        undefined=StrictUndefined,
        autoescape=False,
        variable_start_string="<<!",
        variable_end_string="!>>",
        block_start_string="[%",
        block_end_string="%]",
        comment_start_string="[#%",
        comment_end_string="%#]",
        keep_trailing_newline=True,
    )


def _context(app) -> dict:
    data = app.rapids_portal_data
    return {
        **data,
        "api_docs": lambda section: _api_docs(data, section),
        "current_schedules": lambda: _current_schedules(data),
        "notice_table": lambda notice_type=None, pinned=False: _notice_table(
            data, notice_type, pinned
        ),
        "platform_support_content": lambda: _platform_support(data),
        "previous_schedules": lambda: _previous_schedules(data),
    }


def _builder_inited(app) -> None:
    app.rapids_portal_data = _load_data(app)
    app.rapids_portal_jinja = _jinja_environment(app)


def _notice_header(metadata: dict) -> str:
    updated = metadata.get("notice_updated")
    if not updated or _date(updated).date() == _date(metadata["notice_created"]).date():
        updated_display = "N/A"
    else:
        updated_display = _long_date(updated)
    return "\n".join(
        [
            "---",
            "orphan: true",
            "---",
            f"# {metadata['notice_type'].upper()} {metadata['notice_id']} - {metadata['title']}",
            "",
            "| | |",
            "|:--|:--|",
            f"| **Author** | {metadata['notice_author']} |",
            f"| **Status** | **{metadata['notice_status']}** |",
            f"| **Topic** | {metadata['notice_topic']} |",
            f"| **RAPIDS Version** | {metadata['notice_rapids_version']} |",
            f"| **Created** | {_long_date(metadata['notice_created'])} |",
            f"| **Updated** | {updated_display} |",
            "",
        ]
    )


def _source_read(app, docname: str, source: list[str]) -> None:
    raw = source[0]
    if docname.startswith("notices/") and Path(docname).name[:3] in {"rdn", "rgn", "rsn"}:
        post = frontmatter.loads(raw)
        raw = _notice_header(post.metadata) + post.content
    template = app.rapids_portal_jinja.from_string(raw)
    source[0] = template.render(_context(app))


def _rss_date(value) -> str:
    parsed = _date(value)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=UTC)
    return email.utils.format_datetime(parsed)


def _build_rss(app, exception) -> None:
    if exception is not None or app.builder.name not in {"html", "dirhtml"}:
        return
    data = app.rapids_portal_data
    ElementTree.register_namespace("atom", "http://www.w3.org/2005/Atom")
    rss = ElementTree.Element("rss", version="2.0")
    channel = ElementTree.SubElement(rss, "channel")
    ElementTree.SubElement(channel, "title").text = "NVIDIA RAPIDS Documentation - Notices"
    ElementTree.SubElement(
        channel, "description"
    ).text = "Notices communicate and document changes in RAPIDS for contributors, developers, users, and the community."
    ElementTree.SubElement(channel, "link").text = "https://docs.rapids.ai/notices/"
    ElementTree.SubElement(
        channel,
        "{http://www.w3.org/2005/Atom}link",
        href="https://docs.rapids.ai/notices/feed.xml",
        rel="self",
        type="application/rss+xml",
    )
    now = email.utils.format_datetime(datetime.now(UTC))
    ElementTree.SubElement(channel, "pubDate").text = now
    ElementTree.SubElement(channel, "lastBuildDate").text = now
    ElementTree.SubElement(channel, "generator").text = "Sphinx"

    for notice in sorted(data["notices"], key=_notice_date, reverse=True):
        item = ElementTree.SubElement(channel, "item")
        ElementTree.SubElement(item, "title").text = str(notice["title"])
        output_path = Path(app.outdir) / notice["docname"] / "index.html"
        if output_path.exists():
            soup = BeautifulSoup(output_path.read_text(), "html.parser")
            article = soup.select_one("article.bd-article") or soup.select_one("main")
            description = article.decode_contents() if article else notice["body"]
        else:
            description = notice["body"]
        ElementTree.SubElement(item, "description").text = html.unescape(description)
        published = notice.get("notice_updated") or notice["notice_created"]
        ElementTree.SubElement(item, "pubDate").text = _rss_date(published)
        url = f"https://docs.rapids.ai/notices/{Path(notice['docname']).name}/"
        ElementTree.SubElement(item, "link").text = url
        ElementTree.SubElement(item, "guid", isPermaLink="true").text = url
        for category in [*notice.get("tags", []), *notice.get("categories", [])]:
            ElementTree.SubElement(item, "category").text = str(category)

    output = Path(app.outdir) / "notices" / "feed.xml"
    output.parent.mkdir(parents=True, exist_ok=True)
    ElementTree.ElementTree(rss).write(output, encoding="utf-8", xml_declaration=True)


def _copy_portal_files(app, exception) -> None:
    """Copy trees whose root paths are part of the published site interface."""
    if exception is not None or app.builder.name not in {"html", "dirhtml"}:
        return
    source_dir = _source_dir(app)
    output_dir = Path(app.outdir)
    for directory in ("assets", "licenses"):
        shutil.copytree(
            source_dir / directory,
            output_dir / directory,
            dirs_exist_ok=True,
        )
    for filename in ("LICENSE", "SECURITY.md"):
        shutil.copy2(source_dir.parent / filename, output_dir / filename)

    # ``dirhtml`` correctly creates pretty URLs everywhere except the hosting
    # platform's required top-level error document. sphinx-notfound-page has
    # already rewritten this page's resource and navigation links as absolute.
    shutil.copy2(output_dir / "404" / "index.html", output_dir / "404.html")


def setup(app):
    app.connect("builder-inited", _builder_inited)
    app.connect("source-read", _source_read)
    app.connect("build-finished", _build_rss)
    app.connect("build-finished", _copy_portal_files)
    return {"version": "1.0", "parallel_read_safe": False, "parallel_write_safe": True}
