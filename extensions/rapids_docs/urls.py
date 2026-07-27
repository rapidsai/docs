# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# SPDX-License-Identifier: Apache-2.0

"""Rewrite root-relative portal URLs for the configured site base URL."""

import re
from urllib.parse import urljoin

from docutils import nodes

_HTML_URL_RE = re.compile(r"(?P<attribute>\b(?:href|src)=['\"])(?P<url>/(?!/)[^'\"]*)")
_TOCTREE_RE = re.compile(r"^```\{toctree\}\n.*?^```$", re.MULTILINE | re.DOTALL)
_TOCTREE_ENTRY_RE = re.compile(
    r"^(?P<prefix>\s*.*<)(?P<url>/(?!/)[^>]+)(?P<suffix>>\s*)$", re.MULTILINE
)


def _absolute_url(base_url: str, url: str) -> str:
    return urljoin(base_url.rstrip("/") + "/", url.lstrip("/"))


def _rewrite_url(url: str, base_url: str) -> str:
    if url.startswith("/") and not url.startswith("//"):
        return _absolute_url(base_url, url)
    return url


def _rewrite_html_urls(text: str, base_url: str) -> str:
    return _HTML_URL_RE.sub(
        lambda match: match["attribute"] + _rewrite_url(match["url"], base_url), text
    )


def _rewrite_toctree_urls(app, docname: str, source: list[str]) -> None:
    base_url = app.config.html_baseurl
    if not base_url:
        return

    def rewrite_toctree(match: re.Match) -> str:
        return _TOCTREE_ENTRY_RE.sub(
            lambda entry: entry["prefix"] + _absolute_url(base_url, entry["url"]) + entry["suffix"],
            match[0],
        )

    source[0] = _TOCTREE_RE.sub(rewrite_toctree, source[0])


def _rewrite_absolute_urls(app, doctree, docname: str) -> None:
    base_url = app.config.html_baseurl
    if not base_url:
        return

    for node in doctree.findall(nodes.reference):
        uri = node.get("refuri", "")
        if uri.startswith("/") and not uri.startswith("//"):
            node["refuri"] = _absolute_url(base_url, uri)

    for node in doctree.findall(nodes.raw):
        if node.get("format") != "html":
            continue
        text = _rewrite_html_urls(node.astext(), base_url)
        if text != node.astext():
            node.rawsource = text
            node.clear()
            node += nodes.Text(text)


def _rewrite_theme_urls(app, pagename: str, templatename: str, context: dict, doctree) -> None:
    base_url = app.config.html_baseurl
    if not base_url:
        return

    pathto = context["pathto"]
    css_tag = context["css_tag"]
    js_tag = context["js_tag"]
    toctree = context["toctree"]

    def rewrite_path(*args, **kwargs) -> str:
        return _rewrite_url(pathto(*args, **kwargs), base_url)

    context["pathto"] = rewrite_path
    context["css_tag"] = lambda css: _rewrite_html_urls(css_tag(css), base_url)
    context["js_tag"] = lambda js: _rewrite_html_urls(js_tag(js), base_url)
    context["toctree"] = lambda **kwargs: _rewrite_html_urls(toctree(**kwargs) or "", base_url)
    for key in ("favicon_url", "logo_url"):
        if key in context:
            context[key] = _rewrite_url(context[key], base_url)
