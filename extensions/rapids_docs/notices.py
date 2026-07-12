# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# SPDX-License-Identifier: Apache-2.0

"""Render notices and generate their RSS feed."""

import email.utils
import html
from datetime import UTC, datetime
from pathlib import Path
from xml.etree import ElementTree

from bs4 import BeautifulSoup

from .dates import _date, _long_date

_NOTICE_STATUS_COLORS = {"blue", "green", "purple", "red", "yellow"}


def _notice_date(notice: dict) -> datetime:
    return _date(notice.get("notice_updated") or notice["notice_created"])


def _notice_status_label(notice: dict) -> str:
    color = str(notice.get("notice_status_color", "blue")).lower()
    if color not in _NOTICE_STATUS_COLORS:
        color = "blue"
    status = html.escape(str(notice["notice_status"]))
    return f'<span class="notice-status-label notice-status-{color}">{status}</span>'


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
            f"| **{notice['notice_type'].upper()} {notice['notice_id']}**<br>{_notice_status_label(notice)} "
            f"| [{notice['title']}](/notices/{Path(notice['docname']).name}/) "
            f"| {notice['notice_topic']} | {notice['notice_rapids_version']} | {_long_date(updated)} |"
        )
    return "\n".join(output)


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
            f"| **Status** | {_notice_status_label(metadata)} |",
            f"| **Topic** | {metadata['notice_topic']} |",
            f"| **RAPIDS Version** | {metadata['notice_rapids_version']} |",
            f"| **Created** | {_long_date(metadata['notice_created'])} |",
            f"| **Updated** | {updated_display} |",
            "",
        ]
    )


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
