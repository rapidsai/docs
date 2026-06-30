#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import argparse
import importlib.util
import subprocess
import sys
from pathlib import Path

import yaml

from data_utils import DataError, json_text, load_yaml, version_tuple


ROOT = Path(__file__).resolve().parents[1]
CALENDAR_PATH = ROOT / "_data" / "release_calendar.yml"
PLATFORM_PATH = ROOT / "_data" / "platform_support.yml"
RELEASES_PATH = ROOT / "_data" / "releases.json"
HISTORY_PATH = ROOT / "_data" / "previous_releases.json"
PROJECT_GENERATOR = ROOT / "ci" / "generate-projects-to-versions.py"
PROJECTS_OUTPUT_PATH = ROOT / "ci" / "customization" / "projects-to-versions.json"
REDIRECTS_OUTPUT_PATH = ROOT / "_redirects"

CALENDAR_HEADER = """# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# SPDX-License-Identifier: Apache-2.0
#
# Canonical RAPIDS release channels and schedules. Generated projections live in
# releases.json and previous_releases.json; edit this file instead of those files.

"""


class IndentDumper(yaml.SafeDumper):
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


def next_rapids_release(version):
    parsed = version_tuple(version, "next_nightly release")
    if len(parsed) != 2:
        raise DataError("RAPIDS release versions must use YY.MM")
    year, month = parsed
    if month not in {2, 4, 6, 8, 10, 12}:
        raise DataError(f"unsupported RAPIDS release month in {version}")
    month += 2
    if month == 14:
        year += 1
        month = 2
    return f"{year:02d}.{month:02d}"


def load_release_generator():
    path = ROOT / "ci" / "generate-release-data.py"
    spec = importlib.util.spec_from_file_location("generate_release_data", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def dump_calendar(calendar):
    body = yaml.dump(
        calendar,
        Dumper=IndentDumper,
        sort_keys=False,
        default_flow_style=False,
        width=1000,
    )
    return CALENDAR_HEADER + body


def target_channels(channels, new_next_nightly):
    expected = next_rapids_release(channels["next_nightly"])
    if new_next_nightly != expected:
        raise DataError(
            f"new next nightly must be {expected}, the release after "
            f"{channels['next_nightly']}"
        )
    return {
        "legacy": channels["stable"],
        "stable": channels["nightly"],
        "nightly": channels["next_nightly"],
        "next_nightly": new_next_nightly,
    }


def validate_prerequisites(calendar, platform_support, new_next_nightly):
    channels = calendar.get("channels", {})
    releases = calendar.get("releases", {})
    targets = target_channels(channels, new_next_nightly)
    missing = [version for version in targets.values() if version not in releases]
    if missing:
        raise DataError(
            "add complete release_calendar.yml records before rollover: "
            + ", ".join(missing)
        )

    platform_releases = platform_support.get("releases", [])
    platform_versions = {
        release.get("version")
        for release in platform_releases
        if isinstance(release, dict)
    }
    required_platform = {targets["stable"], targets["nightly"]}
    missing_platform = sorted(required_platform - platform_versions)
    if missing_platform:
        raise DataError(
            "add platform support policy before rollover for: "
            + ", ".join(missing_platform)
        )

    marked_nightly = [
        release.get("version")
        for release in platform_releases
        if isinstance(release, dict) and release.get("nightly") is True
    ]
    if marked_nightly != [targets["nightly"]]:
        raise DataError(
            "move nightly: true in platform_support.yml before rollover; "
            f"expected {[targets['nightly']]}, found {marked_nightly}"
        )
    return targets


def main():
    parser = argparse.ArgumentParser(
        description="Rotate release channels after source policy records are ready."
    )
    parser.add_argument(
        "--new-next-nightly",
        required=True,
        help="The already-authored release to assign to next_nightly (YY.MM).",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Validate and print without writing."
    )
    args = parser.parse_args()

    try:
        calendar = load_yaml(CALENDAR_PATH)
        platform_support = load_yaml(PLATFORM_PATH)
        targets = validate_prerequisites(
            calendar, platform_support, args.new_next_nightly
        )
        calendar["channels"] = targets
        generator = load_release_generator()
        active, history = generator.generate(calendar, platform_support)
    except (DataError, OSError, KeyError, TypeError) as error:
        print(f"Release rollover blocked: {error}", file=sys.stderr)
        return 1

    print("Channel rotation:")
    for channel, version in targets.items():
        print(f"- {channel}: {version}")
    if args.dry_run:
        print("Dry run complete; no files changed.")
        return 0

    managed_paths = (
        CALENDAR_PATH,
        RELEASES_PATH,
        HISTORY_PATH,
        PROJECTS_OUTPUT_PATH,
        REDIRECTS_OUTPUT_PATH,
    )
    original_contents = {
        path: path.read_text(encoding="utf-8") for path in managed_paths
    }
    try:
        CALENDAR_PATH.write_text(dump_calendar(calendar), encoding="utf-8")
        RELEASES_PATH.write_text(json_text(active), encoding="utf-8")
        HISTORY_PATH.write_text(json_text(history), encoding="utf-8")
        result = subprocess.run(
            [sys.executable, PROJECT_GENERATOR], cwd=ROOT, check=False
        )
    except OSError as error:
        for path, content in original_contents.items():
            path.write_text(content, encoding="utf-8")
        print(f"Release rollover failed and was restored: {error}", file=sys.stderr)
        return 1
    if result.returncode:
        for path, content in original_contents.items():
            path.write_text(content, encoding="utf-8")
        print(
            "Docs artifact generation failed; the rollover was restored.",
            file=sys.stderr,
        )
        return result.returncode

    print("Review these human policy decisions before opening the rollover PR:")
    print("- docs.yml channel availability and delayed project publication")
    print("- install_packages.yml lifecycle and standard-bundle membership")
    print("- platform support details for the new nightly release")
    print("- dates and cohort membership for the new next_nightly schedule")
    return 0


if __name__ == "__main__":
    sys.exit(main())
