# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

from ci.update_java_docs import normalize_version, update_docs


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


def test_release_patch_survives_generator_and_rerun(docs_root):
    assert update_docs(docs_root, "cudf-java", "99.12.01")
    expected = (docs_root / "ci/customization/projects-to-versions.json").read_text()
    subprocess.run(
        [sys.executable, "ci/generate-projects-to-versions.py"], cwd=docs_root, check=True
    )
    assert (docs_root / "ci/customization/projects-to-versions.json").read_text() == expected
    original_yaml = (docs_root / "_data/docs.yml").read_text()
    assert update_docs(docs_root, "cudf-java", "99.12.1")
    assert (docs_root / "_data/docs.yml").read_text() == original_yaml


def test_delayed_release_cannot_downgrade_stable(docs_root):
    update_docs(docs_root, "cudf-java", "99.12.1")
    original = (docs_root / "_data/docs.yml").read_text()
    assert not update_docs(docs_root, "cudf-java", "99.10.9")
    assert (docs_root / "_data/docs.yml").read_text() == original
    mapping = json.loads((docs_root / "ci/customization/projects-to-versions.json").read_text())
    assert mapping["cudf-java"]["stable"] == "99.12.1"


def test_only_registered_project_changes(docs_root):
    before = yaml.safe_load((docs_root / "_data/docs.yml").read_text())
    update_docs(docs_root, "cudf-java", "99.12.1")
    after = yaml.safe_load((docs_root / "_data/docs.yml").read_text())
    after["apis"]["cudf-java"] = before["apis"]["cudf-java"]
    assert after == before


@pytest.mark.parametrize("project", ["unknown-java", "../cudf-java", "cudf-java\n"])
def test_unregistered_project_is_rejected(docs_root, project):
    with pytest.raises(ValueError, match="Unregistered"):
        update_docs(docs_root, project, "99.12.1")


@pytest.mark.parametrize("version", ["26.12.0-SNAPSHOT", "26.12.1/../../", "v26.12.1", "26.12\n"])
def test_invalid_version_is_rejected(version):
    with pytest.raises(ValueError):
        normalize_version(version)
