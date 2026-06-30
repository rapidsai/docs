#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import json
import sys
from pathlib import Path

from data_utils import DataError, load_yaml, version_tuple


ROOT = Path(__file__).resolve().parents[1]
PACKAGES_PATH = ROOT / "_data" / "install_packages.yml"
DOCS_PATH = ROOT / "_data" / "docs.yml"
RELEASES_PATH = ROOT / "_data" / "releases.json"
PLATFORM_PATH = ROOT / "_data" / "platform_support.yml"
METHODS = {"conda", "pip"}
BUNDLE_METHODS = {"conda", "pip", "docker"}


def package_names(value, field, errors):
    if not isinstance(value, list) or not value:
        errors.append(f"{field} must be a non-empty list")
        return
    if not all(isinstance(item, str) and item for item in value):
        errors.append(f"{field} entries must be non-empty strings")


def is_available(package, version):
    try:
        parsed = version_tuple(version)
        added = package.get("added_in_release")
        removed = package.get("removed_after_release")
        return (added is None or parsed >= version_tuple(added)) and (
            removed is None or parsed <= version_tuple(removed)
        )
    except DataError:
        return False


def main():
    try:
        catalog = load_yaml(PACKAGES_PATH)
        docs = load_yaml(DOCS_PATH)
        platform = load_yaml(PLATFORM_PATH)
        with RELEASES_PATH.open(encoding="utf-8") as file:
            releases = json.load(file)
    except (OSError, DataError, json.JSONDecodeError) as error:
        print(error, file=sys.stderr)
        return 1

    errors = []
    packages = catalog.get("packages") if isinstance(catalog, dict) else None
    third_party = (
        catalog.get("third_party_packages") if isinstance(catalog, dict) else None
    )
    if not isinstance(packages, dict) or not packages:
        errors.append("install_packages.yml packages must be a non-empty mapping")
        packages = {}
    if not isinstance(third_party, dict):
        errors.append("install_packages.yml third_party_packages must be a mapping")
        third_party = {}

    docs_projects = {
        project
        for group in ("apis", "libs", "inactive-projects")
        for project in docs.get(group, {})
    }
    for package_id, package in packages.items():
        field = f"packages.{package_id}"
        if not isinstance(package, dict):
            errors.append(f"{field} must be a mapping")
            continue
        if not isinstance(package.get("display_name"), str):
            errors.append(f"{field}.display_name must be a string")
        bundle_display_names = package.get("bundle_display_names")
        if bundle_display_names is not None and (
            not isinstance(bundle_display_names, list)
            or not bundle_display_names
            or not all(isinstance(name, str) and name for name in bundle_display_names)
        ):
            errors.append(
                f"{field}.bundle_display_names must be a non-empty string list"
            )
        docs_project = package.get("docs_project")
        if docs_project not in docs_projects:
            errors.append(
                f"{field}.docs_project references unknown project {docs_project}"
            )

        parsed_bounds = {}
        for bound in ("added_in_release", "removed_after_release"):
            if bound in package:
                try:
                    parsed_bounds[bound] = version_tuple(
                        package[bound], f"{field}.{bound}"
                    )
                except DataError as error:
                    errors.append(str(error))
        if (
            parsed_bounds.get("added_in_release")
            and parsed_bounds.get("removed_after_release")
            and parsed_bounds["added_in_release"]
            > parsed_bounds["removed_after_release"]
        ):
            errors.append(
                f"{field}.added_in_release must not exceed removed_after_release"
            )

        configured_methods = METHODS.intersection(package)
        if not configured_methods:
            errors.append(f"{field} must define conda or pip metadata")
        for method in configured_methods:
            method_data = package[method]
            if not isinstance(method_data, dict):
                errors.append(f"{field}.{method} must be a mapping")
                continue
            package_names(
                method_data.get("packages"), f"{field}.{method}.packages", errors
            )
            for optional_names in ("nightly_packages", "nightly_dependencies"):
                if optional_names in method_data:
                    package_names(
                        method_data[optional_names],
                        f"{field}.{method}.{optional_names}",
                        errors,
                    )
            if "display_name" in method_data and not isinstance(
                method_data["display_name"], str
            ):
                errors.append(f"{field}.{method}.display_name must be a string")
            if "pypi" in method_data and not isinstance(method_data["pypi"], bool):
                errors.append(f"{field}.{method}.pypi must be a boolean")
            if method != "pip" and any(
                key in method_data
                for key in ("pypi", "nightly_packages", "nightly_dependencies")
            ):
                errors.append(f"{field}.{method} contains metadata reserved for pip")

        bundle = package.get("standard_bundle")
        if (
            not isinstance(bundle, list)
            or len(bundle) != len(set(bundle))
            or not set(bundle).issubset(BUNDLE_METHODS)
        ):
            errors.append(
                f"{field}.standard_bundle must be a list containing only "
                f"{sorted(BUNDLE_METHODS)}"
            )
        for method in set(bundle or []).intersection(METHODS):
            if method not in package:
                errors.append(
                    f"{field}.standard_bundle includes {method} without {method} metadata"
                )

    for channel in ("stable", "nightly"):
        version = releases[channel]["version"]
        for method in METHODS:
            labels = []
            for package in packages.values():
                if method in package and is_available(package, version):
                    labels.append(
                        package[method].get("display_name", package["display_name"])
                    )
            if len(labels) != len(set(labels)):
                errors.append(
                    f"{channel} {method} selector package labels must be unique"
                )

    supported_cuda_majors = {
        cuda["major"]
        for release in platform.get("releases", [])
        if release.get("version")
        in {releases["stable"]["version"], releases["nightly"]["version"]}
        for cuda in release.get("cuda", [])
    }
    third_party_labels = []
    for package_id, package in third_party.items():
        field = f"third_party_packages.{package_id}"
        if not isinstance(package, dict):
            errors.append(f"{field} must be a mapping")
            continue
        display_name = package.get("display_name")
        if not isinstance(display_name, str) or not display_name:
            errors.append(f"{field}.display_name must be a non-empty string")
        third_party_labels.append(display_name)
        package_names(package.get("conda_packages"), f"{field}.conda_packages", errors)
        cuda_majors = package.get("cuda_majors", [])
        if not isinstance(cuda_majors, list) or not all(
            isinstance(major, int) for major in cuda_majors
        ):
            errors.append(f"{field}.cuda_majors must be a list of integers")
        elif not set(cuda_majors).issubset(supported_cuda_majors):
            errors.append(f"{field}.cuda_majors includes an unsupported CUDA major")
    if len(third_party_labels) != len(set(third_party_labels)):
        errors.append("third-party package display names must be unique")

    if errors:
        print("Install package validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Install package data is valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
