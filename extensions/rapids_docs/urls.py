# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Rewrite root-relative portal URLs for the configured site base URL."""

import re

from docutils import nodes

from .routes import _site_url

_HTML_URL_RE = re.compile(r"(?P<attribute>\b(?:href|src)=['\"])(?P<url>/(?!/)[^'\"]*)")
_TOCTREE_RE = re.compile(r"^```\{toctree\}\n.*?^```$", re.MULTILINE | re.DOTALL)
_TOCTREE_ENTRY_RE = re.compile(
    r"^(?P<prefix>\s*.*<)(?P<url>/(?!/)[^>]+)(?P<suffix>>\s*)$", re.MULTILINE
)


def _rewrite_url(url: str, base_url: str, data: dict | None = None) -> str:
    return _site_url(base_url, url, data)


def _rewrite_html_urls(text: str, base_url: str, data: dict | None = None) -> str:
    return _HTML_URL_RE.sub(
        lambda match: match["attribute"] + _rewrite_url(match["url"], base_url, data), text
    )


def _rewrite_toctree_urls(app, docname: str, source: list[str]) -> None:
    base_url = app.config.html_baseurl
    if not base_url:
        return
    data = getattr(app, "rapids_portal_data", None)

    def rewrite_toctree(match: re.Match) -> str:
        return _TOCTREE_ENTRY_RE.sub(
            lambda entry: (
                entry["prefix"] + _rewrite_url(entry["url"], base_url, data) + entry["suffix"]
            ),
            match[0],
        )

    source[0] = _TOCTREE_RE.sub(rewrite_toctree, source[0])


def _rewrite_absolute_urls(app, doctree, docname: str) -> None:
    base_url = app.config.html_baseurl
    if not base_url:
        return
    data = getattr(app, "rapids_portal_data", None)

    for node in doctree.findall(nodes.reference):
        uri = node.get("refuri", "")
        if uri.startswith("/") and not uri.startswith("//"):
            node["refuri"] = _rewrite_url(uri, base_url, data)

    for node in doctree.findall(nodes.raw):
        if node.get("format") != "html":
            continue
        text = _rewrite_html_urls(node.astext(), base_url, data)
        if text != node.astext():
            node.rawsource = text
            node.clear()
            node += nodes.Text(text)


def _rewrite_theme_urls(app, pagename: str, templatename: str, context: dict, doctree) -> None:
    base_url = app.config.html_baseurl
    if not base_url:
        return
    data = getattr(app, "rapids_portal_data", None)

    pathto = context["pathto"]
    css_tag = context["css_tag"]
    js_tag = context["js_tag"]
    toctree = context["toctree"]

    def rewrite_path(*args, **kwargs) -> str:
        return _rewrite_url(pathto(*args, **kwargs), base_url, data)

    context["pathto"] = rewrite_path
    context["css_tag"] = lambda css: _rewrite_html_urls(css_tag(css), base_url, data)
    context["js_tag"] = lambda js: _rewrite_html_urls(js_tag(js), base_url, data)
    context["toctree"] = lambda **kwargs: _rewrite_html_urls(
        toctree(**kwargs) or "", base_url, data
    )
    for key in ("favicon_url", "logo_url"):
        if key in context:
            context[key] = _rewrite_url(context[key], base_url, data)
