# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# SPDX-License-Identifier: Apache-2.0

import importlib.util
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "ci" / "customization" / "customize_doc.py"
SPEC = importlib.util.spec_from_file_location("customize_doc", MODULE_PATH)
customize_doc = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(customize_doc)


def test_nvidia_theme_selector_injection(tmp_path: Path) -> None:
    page = tmp_path / "api" / "cudf" / "26.06" / "index.html"
    page.parent.mkdir(parents=True)
    page.write_text(
        """<!doctype html><html><head>
        <link rel="stylesheet" href="_static/styles/nvidia-sphinx-theme.css">
        </head><body><aside class="bd-sidebar"></aside></body></html>"""
    )

    lib_map = {"cudf": {"stable": "/api/cudf/stable/", "nightly": None, "legacy": None}}
    versions = {"stable": "26.06"}
    customize_doc.main(
        filepath=str(page),
        lib_path_dict=lib_map,
        project_name="cudf",
        versions_dict=versions,
        selector_project_names={"cudf"},
    )

    soup = BeautifulSoup(page.read_text(), "html.parser")
    assert soup.select_one("#rapids-pydata-container") is not None
    assert soup.select_one("#nvidia-selector-css")["href"] == "/assets/css/custom_nvidia.css"
    assert soup.select_one("#rapids-selector-js")["src"] == "/assets/js/custom.js"
