# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# SPDX-License-Identifier: Apache-2.0

"""Manage Sphinx lifecycle events and source rendering."""

import re
from pathlib import Path

import frontmatter
from jinja2 import Environment, FileSystemLoader, StrictUndefined

from .api import _api_docs
from .data import _load_data
from .notices import _notice_header, _notice_table
from .platform_support import _platform_support
from .releases import _current_schedules, _previous_schedules


def _jinja_environment(app) -> Environment:
    return Environment(
        loader=FileSystemLoader(app.srcdir),
        undefined=StrictUndefined,
        autoescape=False,
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


_GITHUB_ALERT_RE = re.compile(
    r"^> \[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\n((?:>.*(?:\n|$))*)",
    re.MULTILINE,
)


def _convert_github_alerts(text: str) -> str:
    """Convert GitHub alerts to MyST admonitions for the rendered portal."""

    def replace(match: re.Match) -> str:
        body = "\n".join(
            line.removeprefix("> ").removeprefix(">") for line in match.group(2).splitlines()
        )
        return f"```{{{match.group(1).lower()}}}\n{body}\n```\n"

    return _GITHUB_ALERT_RE.sub(replace, text)


def _source_read(app, docname: str, source: list[str]) -> None:
    raw = source[0]
    if docname.startswith("notices/") and Path(docname).name[:3] in {"rdn", "rgn", "rsn"}:
        post = frontmatter.loads(raw)
        raw = _notice_header(post.metadata) + post.content
    elif docname == "SECURITY":
        raw = "---\norphan: true\n---\n\n" + _convert_github_alerts(raw)
    template = app.rapids_portal_jinja.from_string(raw)
    source[0] = template.render(_context(app))
