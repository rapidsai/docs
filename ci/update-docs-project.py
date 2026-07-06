#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import argparse
import json
import re
import sys
from pathlib import Path

from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import DoubleQuotedScalarString


ROOT = Path(__file__).resolve().parents[1]
DOCS_PATH = ROOT / "_data" / "docs.yml"
RELEASES_PATH = ROOT / "_data" / "releases.json"
DOC_GROUPS = ("apis", "libs", "inactive-projects")
CHANNELS = ("legacy", "stable", "nightly")


def find_project(docs, project_name):
    matches = [
        docs[group][project_name]
        for group in DOC_GROUPS
        if project_name in docs.get(group, {})
    ]
    if len(matches) != 1:
        raise ValueError(
            f"expected exactly one docs.yml entry for {project_name}, found {len(matches)}"
        )
    return matches[0]


def validate_version(channel, version, releases):
    base_version = releases[channel]["version"]
    if channel == "nightly":
        if version != base_version:
            raise ValueError(
                f"nightly docs version must match the nightly release {base_version}"
            )
        return base_version

    if not re.fullmatch(rf"{re.escape(base_version)}(?:\.\d+)?", version):
        raise ValueError(
            f"{channel} docs version must be {base_version} or a point release of it"
        )
    return base_version


def main():
    parser = argparse.ArgumentParser(
        description="Enable a project's docs channel with an optional point release."
    )
    parser.add_argument("--project", required=True)
    parser.add_argument("--channel", choices=CHANNELS, required=True)
    parser.add_argument("--version", required=True)
    args = parser.parse_args()

    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 1000
    try:
        docs = yaml.load(DOCS_PATH)
        with RELEASES_PATH.open(encoding="utf-8") as file:
            releases = json.load(file)
        base_version = validate_version(args.channel, args.version, releases)
        project = find_project(docs, args.project)
        project["versions"][args.channel] = 1

        overrides = project.get("version-overrides")
        if args.version == base_version:
            if overrides is not None:
                overrides.pop(args.channel, None)
                if not overrides:
                    del project["version-overrides"]
        else:
            if overrides is None:
                project.insert(len(project), "version-overrides", {})
                overrides = project["version-overrides"]
            overrides[args.channel] = DoubleQuotedScalarString(args.version)

        with DOCS_PATH.open("w", encoding="utf-8") as file:
            yaml.dump(docs, file)
    except (OSError, KeyError, TypeError, ValueError) as error:
        print(f"Docs catalog update failed: {error}", file=sys.stderr)
        return 1

    print(f"Enabled {args.project} {args.channel} docs for version {args.version}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
