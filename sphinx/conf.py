# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import datetime
import os
import sys

sys.path.insert(0, os.path.abspath("../extensions"))

project = "NVIDIA RAPIDS Documentation"
html_title = project
author = "NVIDIA"
copyright = f"{datetime.date.today().year}, NVIDIA"

extensions = [
    "myst_parser",
    "notfound.extension",
    "rapids_docs",
    "sphinx_copybutton",
    "sphinx_design",
]

source_suffix = {".md": "markdown"}
master_doc = "index"
include_patterns = [
    "404.md",
    "SECURITY.md",
    "api.md",
    "index.md",
    "contributing/**",
    "install/**",
    "maintainers/**",
    "notices/**",
    "platform-support/**",
    "releases/**",
    "resources/**",
    "user-guide/**",
    "visualization/**",
]
templates_path = ["_templates"]

myst_enable_extensions = [
    "attrs_inline",
    "colon_fence",
    "deflist",
    "html_image",
]
myst_heading_anchors = 6
# Portal content intentionally uses root-relative links so the same sources work in
# both the portal-only build and the S3-assembled production tree. MyST should
# preserve those hrefs instead of trying to resolve them as Sphinx documents.
myst_all_links_external = True

html_theme = "nvidia_sphinx_theme"
html_static_path = ["_static"]
html_extra_path = ["../_redirects"]
html_baseurl = "https://docs.rapids.ai/"
html_scaled_image_link = False

html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/rapidsai/docs",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        }
    ],
    "navbar_align": "right",
    "show_toc_level": 2,
}

html_css_files = ["css/custom.css"]
html_js_files = [
    (
        "https://cdn.cookielaw.org/scripttemplates/otSDKStub.js",
        {
            "charset": "UTF-8",
            "data-document-language": "true",
            "data-domain-script": "018e2d71-40f3-7e89-90b8-e10ec6012ab0-test",
        },
    ),
    "https://images.nvidia.com/aem-dam/Solutions/ot-js/ot-custom.js",
    "https://assets.adobedtm.com/5d4962a43b79/814eb6e9b4e1/launch-4bc07f1e0b0b.min.js",
    "js/portal-analytics.js",
]

copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True
copybutton_line_continuation_character = "\\"

notfound_pagename = "404"
notfound_urls_prefix = None
