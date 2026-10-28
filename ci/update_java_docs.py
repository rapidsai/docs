#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Enable a registered Java project's published docs without losing YAML comments."""

import argparse
import json
import re
from pathlib import Path

import yaml


def normalize_version(version: str) -> str:
    if not re.fullmatch(r"[0-9]{2}\.[0-9]{2}(\.[0-9]+)?", version):
        raise ValueError("Version must be YY.MM or YY.MM.P")
    major, minor, *patch = version.split(".")
    return f"{major}.{minor}.{int(patch[0]) if patch else 0}"


def update_docs(root: Path, project: str, version: str) -> bool:
    version = normalize_version(version)
    registry = json.loads((root / "ci/java-docs-projects.json").read_text())
    if project not in registry or not re.fullmatch(r"[a-z][a-z0-9-]+", project):
        raise ValueError(f"Unregistered Java docs project: {project}")
    docs_path = root / "_data/docs.yml"
    versions_path = root / "ci/customization/projects-to-versions.json"
    source = docs_path.read_text()
    docs = yaml.safe_load(source)
    mapping = json.loads(versions_path.read_text())
    entry = docs["apis"][project]
    current = entry.get("version-overrides", {}).get("stable") or mapping[project].get("stable")
    if current and tuple(map(int, normalize_version(str(current)).split("."))) > tuple(
        map(int, version.split("."))
    ):
        # A delayed older release must not move the stable docs backwards.
        return False
    section = re.search(rf"^  {re.escape(project)}:\n.*?(?=^\S|^  \S|\Z)", source, re.M | re.S)
    if section is None:
        raise ValueError(f"Cannot locate YAML block for {project}")
    block, count = re.subn(r"^(      stable:) [01]$", r"\1 1", section[0], flags=re.M)
    if count != 1:
        raise ValueError(f"Cannot locate stable switch for {project}")
    overrides = re.search(r"^    version-overrides:\n(?:^      .*\n)*", block, re.M)
    if overrides:
        replacement, count = re.subn(
            r"^      stable:.*$", f'      stable: "{version}"', overrides[0], flags=re.M
        )
        if count == 0:
            replacement += f'      stable: "{version}"\n'
        block = block[: overrides.start()] + replacement + block[overrides.end() :]
    else:
        block = block.replace(
            "    versions:\n",
            f'    version-overrides:\n      stable: "{version}"\n    versions:\n',
            1,
        )
    updated = source[: section.start()] + block + source[section.end() :]
    expected = docs
    expected["apis"][project]["versions"]["stable"] = 1
    expected["apis"][project].setdefault("version-overrides", {})["stable"] = version
    if yaml.safe_load(updated) != expected:
        raise ValueError("YAML edit changed unexpected project settings")
    mapping[project]["stable"] = version
    docs_path.write_text(updated)
    versions_path.write_text(json.dumps(mapping, indent=2) + "\n")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project")
    parser.add_argument("version")
    args = parser.parse_args()
    update_docs(Path(__file__).resolve().parents[1], args.project, args.version)


if __name__ == "__main__":
    main()
