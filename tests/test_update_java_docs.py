# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from ci.update_java_docs import update_docs


@pytest.fixture
def docs_root(tmp_path):
    source = Path(__file__).resolve().parents[1]
    for name in (
        "_data/docs.yml",
        "_data/releases.json",
        "ci/java-docs-projects.json",
        "ci/customization/projects-to-versions.json",
        "ci/generate-projects-to-versions.py",
    ):
        destination = tmp_path / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(source / name, destination)
    return tmp_path


def test_stable_link_keeps_exact_maven_version_after_regeneration(docs_root):
    project = "cuvs-java"
    version = "99.12.1"
    update_docs(root=docs_root, project=project, version=version)
    subprocess.run(
        [sys.executable, "ci/generate-projects-to-versions.py"], cwd=docs_root, check=True
    )

    mapping = json.loads((docs_root / "ci/customization/projects-to-versions.json").read_text())
    assert mapping[project]["stable"] == version


def test_late_release_keeps_newer_stable_link(docs_root):
    project = "cuvs-java"
    update_docs(root=docs_root, project=project, version="99.12.1")
    docs_config = docs_root / "_data/docs.yml"
    original = docs_config.read_text()

    assert not update_docs(root=docs_root, project=project, version="99.10.9")

    assert docs_config.read_text() == original
    mapping = json.loads((docs_root / "ci/customization/projects-to-versions.json").read_text())
    assert mapping[project]["stable"] == "99.12.1"
