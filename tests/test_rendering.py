# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
from types import SimpleNamespace

from extensions import rapids_docs

ROOT = Path(__file__).resolve().parents[1]
APP = SimpleNamespace(srcdir=str(ROOT))


def test_data_driven_content() -> None:
    data = rapids_docs._load_data(APP)
    stable_version = data["releases"]["stable"]["version"]
    nightly_version = data["releases"]["nightly"]["version"]

    api = rapids_docs._api_docs(data, "apis")
    assert f"stable ({stable_version})" in api
    assert "/api/cudf/stable/" in api

    inactive = rapids_docs._api_docs(data, "inactive-projects")
    inactive_project = next(
        project
        for project in data["docs"]["inactive-projects"].values()
        if not project.get("hidden", False) and project["versions"].get("stable") == 1
    )
    inactive_version = rapids_docs._version_label(inactive_project, "stable", data["releases"])
    assert f"stable ({inactive_version})" in inactive

    platform = rapids_docs._platform_support(data)
    platform_release = data["platform_support"]["releases"][0]
    assert f"RAPIDS {platform_release['version']}" in platform
    assert f"CUDA {platform_release['cuda'][0]['major']}" in platform
    assert 'class="fas fa-desktop"' in platform
    assert 'class="fab fa-linux"' in platform
    assert 'class="fab fa-windows"' in platform
    assert 'class="fab fa-python"' in platform
    assert 'class="fas fa-microchip"' in platform
    assert 'class="fas fa-hammer"' in platform

    schedules = rapids_docs._current_schedules(data)
    assert f"Release v{nightly_version} Schedule" in schedules
    assert "PROPOSED" in schedules


def test_standard_jinja_syntax_and_raw_blocks() -> None:
    app = SimpleNamespace(srcdir=str(ROOT))
    app.rapids_portal_data = rapids_docs._load_data(app)
    template = rapids_docs._jinja_environment(app).from_string(
        "{{ releases.stable.version }}\n{% raw %}${{ matrix.PY_VER }}{% endraw %}\n"
    )

    rendered = template.render(rapids_docs._context(app))
    stable_version = app.rapids_portal_data["releases"]["stable"]["version"]

    assert rendered == stable_version + "\n${{ matrix.PY_VER }}\n"


def test_notice_metadata_and_indexes() -> None:
    data = rapids_docs._load_data(APP)
    source_notices = list((ROOT / "notices").glob("r[dgs]n[0-9][0-9][0-9][0-9].md"))
    assert len(data["notices"]) == len(source_notices)

    support_notices = rapids_docs._notice_table(data, "rsn")
    support_notice = next(notice for notice in data["notices"] if notice["notice_type"] == "rsn")
    assert f"RSN {support_notice['notice_id']}" in support_notices
    assert support_notice["title"] in support_notices

    pinned = rapids_docs._notice_table(data, pinned=True)
    pinned_notice = next(notice for notice in data["notices"] if notice.get("notice_pin"))
    assert f"{pinned_notice['notice_type'].upper()} {pinned_notice['notice_id']}" in pinned


def test_github_alert_conversion() -> None:
    source = "> [!WARNING]\n> Do not report security vulnerabilities publicly!\n"
    converted = rapids_docs._convert_github_alerts(source)

    assert converted == ("```{warning}\nDo not report security vulnerabilities publicly!\n```\n")
