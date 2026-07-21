# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# SPDX-License-Identifier: Apache-2.0

"""Data-driven rendering and notice support for the RAPIDS documentation portal."""

from .lifecycle import _builder_inited, _source_read
from .notices import _build_rss
from .output import _copy_portal_files
from .urls import _rewrite_absolute_urls, _rewrite_theme_urls, _rewrite_toctree_urls


def setup(app):
    app.connect("builder-inited", _builder_inited)
    app.connect("source-read", _source_read)
    app.connect("source-read", _rewrite_toctree_urls)
    app.connect("doctree-resolved", _rewrite_absolute_urls)
    app.connect("html-page-context", _rewrite_theme_urls)
    app.connect("build-finished", _build_rss)
    app.connect("build-finished", _copy_portal_files)
    return {"version": "1.0", "parallel_read_safe": False, "parallel_write_safe": True}
