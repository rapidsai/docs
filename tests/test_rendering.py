# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
from types import SimpleNamespace

from docutils import nodes

from extensions import rapids_docs
from extensions.rapids_docs import api, lifecycle, notices, platform_support, releases, urls
from extensions.rapids_docs import data as portal_data

ROOT = Path(__file__).resolve().parents[1]
APP = SimpleNamespace(srcdir=str(ROOT))


def test_api_docs() -> None:
    data = portal_data._load_data(APP)
    stable_version = data["releases"]["stable"]["version"]
    nightly_version = data["releases"]["nightly"]["version"]
    legacy_version = data["releases"]["legacy"]["version"]

    rendered = api._api_docs(data, "apis")
    assert f"Stable ({stable_version})" in rendered
    assert "/api/cudf/stable/" in rendered
    assert "::::{grid} 1 1 1 1" in rendered
    assert ":::{grid-item-card} cuDF" in rendered
    assert "**Documentation:**" in rendered
    assert "[GitHub]" in rendered
    assert "DOCS" not in rendered
    assert rendered.index(f"Nightly ({nightly_version})") < rendered.index(
        f"Stable ({stable_version})"
    )
    assert rendered.index(f"Stable ({stable_version})") < rendered.index(
        f"Legacy ({legacy_version})"
    )

    inactive = api._api_docs(data, "inactive-projects")
    inactive_project = next(
        project
        for project in data["docs"]["inactive-projects"].values()
        if not project.get("hidden", False) and project["versions"].get("stable") == 1
    )
    inactive_version = api._version_label(inactive_project, "stable", data["releases"])
    assert f"Stable ({inactive_version})" in inactive


def test_platform_support() -> None:
    data = portal_data._load_data(APP)
    platform = platform_support._platform_support(data)
    platform_release = data["platform_support"]["releases"][0]
    assert f"RAPIDS {platform_release['version']}" in platform
    assert f"CUDA {platform_release['cuda'][0]['major']}" in platform
    assert 'class="fas fa-desktop"' in platform
    assert 'class="fab fa-linux"' in platform
    assert 'class="fab fa-windows"' in platform
    assert 'class="fab fa-python"' in platform
    assert 'class="fas fa-microchip"' in platform
    assert 'class="fas fa-hammer"' in platform
    for release in data["platform_support"]["releases"]:
        anchor = f"#rapids-{str(release['version']).replace('.', '-')}"
        if release.get("nightly"):
            anchor += "-nightly"
        assert anchor in platform


def test_release_schedules() -> None:
    data = portal_data._load_data(APP)
    nightly_version = data["releases"]["nightly"]["version"]
    schedules = releases._current_schedules(data)
    assert f"Release v{nightly_version} Schedule" in schedules
    assert "PROPOSED" in schedules
    previous_version = data["previous_releases"][0]["version"]
    assert f"Release v{previous_version} Schedule" in releases._previous_schedules(data)


def test_standard_jinja_syntax_and_raw_blocks() -> None:
    app = SimpleNamespace(srcdir=str(ROOT))
    app.rapids_portal_data = portal_data._load_data(app)
    template = lifecycle._jinja_environment(app).from_string(
        "{{ releases.stable.version }}\n{% raw %}${{ matrix.PY_VER }}{% endraw %}\n"
    )

    rendered = template.render(lifecycle._context(app))
    stable_version = app.rapids_portal_data["releases"]["stable"]["version"]

    assert rendered == stable_version + "\n${{ matrix.PY_VER }}\n"


def test_toctree_url_rewriting() -> None:
    app = SimpleNamespace(
        config=SimpleNamespace(html_baseurl="https://docs.example.com/datascience/")
    )
    source = ["```{toctree}\n:hidden:\n\nDeployment Guides </deployment/stable/>\n```\n"]

    urls._rewrite_toctree_urls(app, "index", source)

    assert source == [
        "```{toctree}\n:hidden:\n\n"
        "Deployment Guides <https://docs.example.com/datascience/deployment/stable/>\n```\n"
    ]


def test_notice_metadata_and_indexes() -> None:
    data = portal_data._load_data(APP)
    source_notices = list((ROOT / "notices").glob("r[dgs]n[0-9][0-9][0-9][0-9].md"))
    assert len(data["notices"]) == len(source_notices)

    support_notices = notices._notice_table(data, "rsn")
    support_notice = next(notice for notice in data["notices"] if notice["notice_type"] == "rsn")
    assert f"RSN {support_notice['notice_id']}" in support_notices
    assert support_notice["title"] in support_notices
    assert 'class="notice-status-label notice-status-green">Completed</span>' in support_notices
    assert 'class="notice-status-label notice-status-yellow">In Progress</span>' in support_notices

    pinned = notices._notice_table(data, pinned=True)
    pinned_notice = next(notice for notice in data["notices"] if notice.get("notice_pin"))
    assert f"{pinned_notice['notice_type'].upper()} {pinned_notice['notice_id']}" in pinned


def test_notice_status_labels() -> None:
    assert (
        notices._notice_status_label({"notice_status": "Completed", "notice_status_color": "green"})
        == '<span class="notice-status-label notice-status-green">Completed</span>'
    )
    assert (
        notices._notice_status_label(
            {"notice_status": "In Progress", "notice_status_color": "yellow"}
        )
        == '<span class="notice-status-label notice-status-yellow">In Progress</span>'
    )
    assert (
        notices._notice_status_label(
            {"notice_status": "<Unknown>", "notice_status_color": "invalid"}
        )
        == '<span class="notice-status-label notice-status-blue">&lt;Unknown&gt;</span>'
    )


def test_github_alert_conversion() -> None:
    source = "> [!WARNING]\n> Do not report security vulnerabilities publicly!\n"
    converted = lifecycle._convert_github_alerts(source)

    assert converted == ("```{warning}\nDo not report security vulnerabilities publicly!\n```\n")


def test_absolute_url_rewriting() -> None:
    app = SimpleNamespace(
        config=SimpleNamespace(html_baseurl="https://docs.example.com/datascience/")
    )
    reference = nodes.reference("", "Guide", refuri="/user-guide/")
    raw = nodes.raw(
        "", '<a href="/notices/feed.xml"><img src="/assets/rss.svg"></a>', format="html"
    )
    doctree = nodes.container("", reference, raw)

    urls._rewrite_absolute_urls(app, doctree, "index")

    assert reference["refuri"] == "https://docs.example.com/datascience/user-guide/"
    assert (
        raw.astext()
        == '<a href="https://docs.example.com/datascience/notices/feed.xml"><img src="https://docs.example.com/datascience/assets/rss.svg"></a>'
    )


def test_theme_url_rewriting() -> None:
    app = SimpleNamespace(
        config=SimpleNamespace(html_baseurl="https://docs.example.com/datascience/")
    )
    context = {
        "pathto": lambda *args, **kwargs: "/_static/theme.css",
        "css_tag": lambda css: '<link href="/_static/theme.css">',
        "js_tag": lambda js: '<script src="/_static/theme.js"></script>',
        "toctree": lambda **kwargs: '<a href="/install/">Installation Guide</a>',
        "favicon_url": "/_static/favicon.png",
    }

    urls._rewrite_theme_urls(app, "index", "page.html", context, None)

    assert context["pathto"]("_static/theme.css", resource=True) == (
        "https://docs.example.com/datascience/_static/theme.css"
    )
    assert (
        context["css_tag"](None)
        == '<link href="https://docs.example.com/datascience/_static/theme.css">'
    )
    assert (
        context["js_tag"](None)
        == '<script src="https://docs.example.com/datascience/_static/theme.js"></script>'
    )
    assert context["toctree"]() == (
        '<a href="https://docs.example.com/datascience/install/">Installation Guide</a>'
    )
    assert context["favicon_url"] == "https://docs.example.com/datascience/_static/favicon.png"


def test_extension_setup() -> None:
    connections = []
    app = SimpleNamespace(connect=lambda event, callback: connections.append((event, callback)))

    metadata = rapids_docs.setup(app)

    assert [event for event, _ in connections] == [
        "builder-inited",
        "source-read",
        "source-read",
        "doctree-resolved",
        "html-page-context",
        "build-finished",
        "build-finished",
    ]
    assert metadata == {
        "version": "1.0",
        "parallel_read_safe": False,
        "parallel_write_safe": True,
    }
