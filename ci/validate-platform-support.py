#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import json
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PLATFORM_SUPPORT_PATH = ROOT / "_data" / "platform_support.yml"
RELEASES_PATH = ROOT / "_data" / "releases.json"


def dotted_version(value, field, errors):
    if not isinstance(value, str):
        errors.append(f"{field} must be a quoted dotted version string")
        return None

    try:
        return tuple(int(part) for part in value.split("."))
    except ValueError:
        errors.append(f"{field} must contain only dot-separated integers: {value!r}")
        return None


def validate_python_versions(release, errors):
    version = release.get("version", "<unknown>")
    field = f"release {version} python"
    python_versions = release.get("python")
    if not isinstance(python_versions, list) or not python_versions:
        errors.append(f"{field} must be a non-empty list")
        return

    parsed_versions = [
        dotted_version(item, f"{field}[{index}]", errors)
        for index, item in enumerate(python_versions)
    ]
    if None in parsed_versions:
        return
    if len(set(parsed_versions)) != len(parsed_versions):
        errors.append(f"{field} contains duplicate versions")
    if parsed_versions != sorted(parsed_versions):
        errors.append(f"{field} must be sorted from oldest to newest")


def validate_cuda_versions(release, errors):
    version = release.get("version", "<unknown>")
    field = f"release {version} cuda"
    cuda_versions = release.get("cuda")
    if not isinstance(cuda_versions, list) or not cuda_versions:
        errors.append(f"{field} must be a non-empty list")
        return

    majors = []
    for index, cuda in enumerate(cuda_versions):
        item_field = f"{field}[{index}]"
        if not isinstance(cuda, dict):
            errors.append(f"{item_field} must be a mapping")
            continue

        major = cuda.get("major")
        if not isinstance(major, int) or isinstance(major, bool):
            errors.append(f"{item_field}.major must be an integer")
            continue
        majors.append(major)

        minimum = dotted_version(
            cuda.get("toolkit_min"), f"{item_field}.toolkit_min", errors
        )
        maximum = dotted_version(
            cuda.get("toolkit_max"), f"{item_field}.toolkit_max", errors
        )
        if minimum is None or maximum is None:
            continue
        if minimum[0] != major or maximum[0] != major:
            errors.append(f"{item_field} toolkit bounds must match CUDA major {major}")
        if minimum > maximum:
            errors.append(f"{item_field}.toolkit_min must not exceed toolkit_max")

    if len(set(majors)) != len(majors):
        errors.append(f"{field} contains duplicate major versions")
    if majors != sorted(majors):
        errors.append(f"{field} must be sorted from oldest to newest")


def main():
    with PLATFORM_SUPPORT_PATH.open() as f:
        platform_support = yaml.safe_load(f)
    with RELEASES_PATH.open() as f:
        releases = json.load(f)

    errors = []
    if not isinstance(platform_support, dict):
        errors.append("platform_support.yml must contain a mapping")
        platform_support = {}

    platform_releases = platform_support.get("releases")
    if not isinstance(platform_releases, list) or not platform_releases:
        errors.append("platform_support.yml releases must be a non-empty list")
        platform_releases = []

    releases_by_version = {}
    for index, release in enumerate(platform_releases):
        if not isinstance(release, dict):
            errors.append(f"releases[{index}] must be a mapping")
            continue
        version = release.get("version")
        if not isinstance(version, str):
            errors.append(f"releases[{index}].version must be a quoted string")
            continue
        if version in releases_by_version:
            errors.append(f"platform support contains duplicate release {version}")
        releases_by_version[version] = release
        validate_python_versions(release, errors)
        validate_cuda_versions(release, errors)

    for channel in ("stable", "nightly"):
        version = releases[channel]["version"]
        if version not in releases_by_version:
            errors.append(
                f"{channel} release {version} is missing from platform_support.yml"
            )

    nightly_version = releases["nightly"]["version"]
    marked_nightly = [
        release.get("version")
        for release in platform_releases
        if isinstance(release, dict) and release.get("nightly") is True
    ]
    if marked_nightly != [nightly_version]:
        errors.append(
            "exactly the current nightly release must have nightly: true; "
            f"expected {[nightly_version]}, found {marked_nightly}"
        )

    if errors:
        print("Platform support validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Platform support data is valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
