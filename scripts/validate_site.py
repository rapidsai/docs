#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# SPDX-License-Identifier: Apache-2.0

"""Validate the rendered RAPIDS portal and optional assembled documentation tree."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
SOURCE_NOTICES = ROOT / "notices"

REQUIRED_PAGES = [
    "index.html",
    "LICENSE",
    "SECURITY.md",
    "404.html",
    "api/index.html",
    "contributing/index.html",
    "install/index.html",
    "maintainers/index.html",
    "notices/index.html",
    "notices/rdn/index.html",
    "notices/rgn/index.html",
    "notices/rsn/index.html",
    "notices/feed.xml",
    "platform-support/index.html",
    "releases/schedule/index.html",
    "resources/index.html",
    "user-guide/index.html",
    "visualization/index.html",
    "assets/css/custom_nvidia.css",
    "assets/js/custom.js",
    "licenses/CubinLinker.txt",
    "licenses/cugraph-ops-EULA.txt",
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("site", type=Path)
    parser.add_argument("--full", action="store_true")
    args = parser.parse_args()

    missing = [relative for relative in REQUIRED_PAGES if not (args.site / relative).exists()]
    notice_ids = sorted(path.stem for path in SOURCE_NOTICES.glob("r[dgs]n[0-9][0-9][0-9][0-9].md"))
    notice_pages = list((args.site / "notices").glob("r[dgs]n[0-9][0-9][0-9][0-9]/index.html"))
    if len(notice_pages) != len(notice_ids):
        missing.append(f"expected {len(notice_ids)} notice pages, found {len(notice_pages)}")

    feed = ElementTree.parse(args.site / "notices" / "feed.xml")
    feed_items = feed.findall("./channel/item")
    if len(feed_items) != len(notice_ids):
        missing.append(f"expected {len(notice_ids)} RSS items, found {len(feed_items)}")

    search_index = (args.site / "searchindex.js").read_text(errors="ignore")
    missing_search_notices = [
        notice_id for notice_id in notice_ids if f"notices/{notice_id}" not in search_index
    ]
    if missing_search_notices:
        missing.append(f"{len(missing_search_notices)} individual notices are absent from search")

    home = (args.site / "index.html").read_text(errors="ignore")
    required_branding = [
        "nvidia-logo-horiz",
        "https://github.com/rapidsai/docs",
        "018e2d71-40f3-7e89-90b8-e10ec6012ab0-test",
        "assets.adobedtm.com",
        "fa-download",
        "fa-list-check",
        "fa-book",
        "fa-code",
        "fa-chart-bar",
        "fa-cloud",
        "fa-wrench",
        "fa-bullhorn",
        'class="fab fa-github"',
        "fa-slack",
        "fa-stack-overflow",
    ]
    missing.extend(
        f"home page branding/telemetry: {value}" for value in required_branding if value not in home
    )
    if "fa-twitter" in home or "fa-x-twitter" in home:
        missing.append("Twitter/X icon remains on the home page")

    analytics = (args.site / "_static" / "js" / "portal-analytics.js").read_text()
    if "G-DLJNCEWKZD" not in analytics or "_satellite.pageBottom" not in analytics:
        missing.append("GA4 or Adobe page-bottom telemetry is missing")

    # Imported API docs may include upstream source links and template examples.
    # Limit portal-specific checks to portal and deployment pages.
    html_files = [
        path
        for path in args.site.rglob("*.html")
        if "_static" not in path.parts and not path.is_relative_to(args.site / "api")
    ]
    stale_liquid = [path for path in html_files if "{%" in path.read_text(errors="ignore")]
    if stale_liquid:
        missing.append(f"Liquid syntax remains in {len(stale_liquid)} rendered files")

    markdown_links = []
    for path in html_files:
        for href in re.findall(r'href=["\']([^"\']+)["\']', path.read_text(errors="ignore")):
            link = urlsplit(href)
            if not (link.scheme or link.netloc) and link.path.endswith(".md"):
                markdown_links.append(f"{path.relative_to(args.site)}: {href}")
    if markdown_links:
        missing.append("same-site Markdown links remain:\n  " + "\n  ".join(markdown_links))

    if args.full:
        full_paths = [
            "api/cudf/stable",
            "api/cudf/latest",
            "api/cudf/nightly",
            "deployment/stable/index.html",
            "deployment/nightly/index.html",
        ]
        missing.extend(relative for relative in full_paths if not (args.site / relative).exists())

    if missing:
        raise SystemExit("Site validation failed:\n- " + "\n- ".join(missing))

    print(f"Validated {len(html_files)} HTML files and {len(notice_pages)} notices")


if __name__ == "__main__":
    main()
