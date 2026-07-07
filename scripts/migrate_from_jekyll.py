#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# SPDX-License-Identifier: Apache-2.0

"""One-time content migration from the pinned RAPIDS Jekyll snapshot."""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

SOURCE = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/rapidsai-docs-jekyll-upstream-main")
DESTINATION = Path(__file__).resolve().parents[1]


def split_front_matter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    _, front_matter, body = text.split("---\n", 2)
    return front_matter, body.lstrip("\n")


def title_from_front_matter(front_matter: str) -> str:
    match = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', front_matter, re.MULTILINE)
    return match.group(1) if match else ""


def route_for(source_path: str) -> str:
    path = Path(source_path)
    if path.suffix == ".md":
        path = path.with_suffix("")
    parts = list(path.parts)
    if parts and parts[-1] == "index":
        parts.pop()
    route = "/" + "/".join(parts)
    return route.rstrip("/") + "/" if route != "/" else route


def convert_labels(lines: list[str]) -> list[str]:
    colors = {
        "yellow": "warning",
        "green": "success",
        "blue": "info",
        "purple": "primary",
    }
    converted: list[str] = []
    for line in lines:
        match = re.fullmatch(
            r"\{:\s*\.label\s+\.label-(yellow|green|blue|purple)\s*}", line.strip()
        )
        if match and converted:
            label = converted.pop().strip()
            converted.append(f"{{bdg-{colors[match.group(1)]}}}`{label}`")
            continue
        if re.fullmatch(r"\{:\s*[^}]*}", line.strip()):
            continue
        converted.append(line)
    return converted


def convert_markdown(text: str, title: str) -> str:
    text = text.replace("{{ page.title }}", title)
    text = text.replace("{{ site.data.releases.stable.version }}", "{{ releases.stable.version }}")
    text = text.replace(
        "{{ site.data.releases.nightly.version }}", "{{ releases.nightly.version }}"
    )
    text = text.replace("{{ site.social.slack.url }}", "https://rapids.ai/slack-invite")
    text = text.replace("{{ 'notices/feed.xml' | absolute_url }}", "/notices/feed.xml")
    text = re.sub(
        r"\{%\s*link\s+([^%]+?)\s*%}",
        lambda match: route_for(match.group(1).strip()),
        text,
    )
    text = re.sub(r'\{:\s*target="_blank"\s*}', "", text)
    text = re.sub(
        r"\{%\s*include\s+([A-Za-z0-9_.-]+)\.html(?:\s+[^%]*)?%}",
        lambda match: '{% include "_includes/' + match.group(1) + '.html" %}',
        text,
    )
    text = "\n".join(convert_labels(text.splitlines())) + "\n"
    text = re.sub(r"\n1\. TOC\n(?:\n)?", "\n", text)
    return text


def migrate_page(relative_path: Path) -> None:
    source_path = SOURCE / relative_path
    front_matter, body = split_front_matter(source_path.read_text())
    title = title_from_front_matter(front_matter)
    converted = convert_markdown(body, title)
    destination = DESTINATION / relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(converted)


def migrate_notice(source_path: Path) -> None:
    front_matter, body = split_front_matter(source_path.read_text())
    converted = convert_markdown(body, title_from_front_matter(front_matter))
    destination = DESTINATION / "notices" / source_path.name
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(f"---\n{front_matter}---\n\n{converted}")


def main() -> None:
    for filename in ["404.md", "SECURITY.md", "api.md", "index.md"]:
        migrate_page(Path(filename))

    for directory in [
        "contributing",
        "install",
        "maintainers",
        "notices",
        "platform-support",
        "releases",
        "resources",
        "user-guide",
        "visualization",
    ]:
        for source_path in sorted((SOURCE / directory).rglob("*.md")):
            migrate_page(source_path.relative_to(SOURCE))

    for source_path in sorted((SOURCE / "_notices").glob("*.md")):
        migrate_notice(source_path)

    for directory in ["licenses"]:
        target = DESTINATION / directory
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(SOURCE / directory, target)


if __name__ == "__main__":
    main()
