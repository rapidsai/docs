#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2025-2026, NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import argparse
import json
import sys
from pathlib import Path

from data_utils import DataError, json_text, load_yaml, version_tuple, write_or_check


ROOT = Path(__file__).resolve().parents[1]
DOCS_PATH = ROOT / "_data" / "docs.yml"
RELEASES_PATH = ROOT / "_data" / "releases.json"
CUSTOM_REDIRECTS_PATH = ROOT / "_data" / "redirects.yml"
PROJECTS_OUTPUT_PATH = ROOT / "ci" / "customization" / "projects-to-versions.json"
REDIRECTS_OUTPUT_PATH = ROOT / "_redirects"

DOC_GROUPS = ("apis", "libs", "inactive-projects")
CHANNELS = ("legacy", "stable", "nightly")


def enabled(value):
    return value is True or value == 1


def add_redirect(redirects, source, target, owner):
    if not isinstance(source, str) or not source.startswith("/"):
        raise DataError(f"{owner} redirect source must start with '/'")
    if not isinstance(target, str) or not target.startswith("/"):
        raise DataError(f"{owner} redirect target must start with '/'")

    sources = [source] if source.endswith("/") else [source, f"{source}/"]
    for variant in sources:
        previous = redirects.get(variant)
        if previous is not None and previous != target:
            raise DataError(
                f"redirect {variant} has conflicting targets: {previous}, {target}"
            )
        redirects[variant] = target


def project_versions_and_redirects(docs, releases):
    projects_to_versions = {}
    redirects = {}
    seen_paths = {}

    for group in DOC_GROUPS:
        projects = docs.get(group)
        if not isinstance(projects, dict):
            raise DataError(f"docs.yml {group} must be a mapping")

        for project_name, details in projects.items():
            field = f"docs.yml {group}.{project_name}"
            if project_name in projects_to_versions:
                raise DataError(f"duplicate docs project ID: {project_name}")
            if not isinstance(details, dict):
                raise DataError(f"{field} must be a mapping")
            path = details.get("path")
            if not isinstance(path, str) or not path:
                raise DataError(f"{field}.path must be a non-empty string")
            if path in seen_paths:
                raise DataError(f"{field}.path duplicates {seen_paths[path]}: {path}")
            seen_paths[path] = field
            versions = details.get("versions")
            if not isinstance(versions, dict):
                raise DataError(f"{field}.versions must be a mapping")

            version_field = details.get("release_version_field", "version")
            if not isinstance(version_field, str):
                raise DataError(f"{field}.release_version_field must be a string")
            overrides = details.get("version-overrides", {})
            if not isinstance(overrides, dict):
                raise DataError(f"{field}.version-overrides must be a mapping")
            unknown_overrides = set(overrides) - set(CHANNELS)
            if unknown_overrides:
                raise DataError(
                    f"{field}.version-overrides has unknown channels: "
                    f"{sorted(unknown_overrides)}"
                )

            selected_versions = {}
            for channel in CHANNELS:
                if channel not in versions:
                    raise DataError(f"{field}.versions is missing {channel}")
                if not isinstance(versions[channel], (bool, int)) or versions[
                    channel
                ] not in {0, 1}:
                    raise DataError(f"{field}.versions.{channel} must be 0 or 1")
                if not enabled(versions[channel]):
                    continue
                if channel in overrides:
                    if not isinstance(overrides[channel], str):
                        raise DataError(
                            f"{field}.version-overrides.{channel} must be quoted"
                        )
                    selected_versions[channel] = overrides[channel]
                    continue
                release = releases.get(channel)
                if not isinstance(release, dict) or version_field not in release:
                    raise DataError(f"{field} cannot resolve {channel}.{version_field}")
                selected_versions[channel] = release[version_field]
            projects_to_versions[project_name] = selected_versions

            redirect = details.get("redirect")
            if enabled(versions.get("stable")) and redirect is None:
                raise DataError(
                    f"{field} must declare redirect: stable, a custom target, or false"
                )
            if redirect is False or redirect is None:
                continue
            source = f"/api/{path}"
            if redirect == "stable":
                target = f"/api/{path}/stable/"
            elif isinstance(redirect, str) and redirect.startswith("/"):
                target = redirect
            else:
                raise DataError(
                    f"{field}.redirect must be stable, an absolute target, or false"
                )
            add_redirect(redirects, source, target, field)

    return projects_to_versions, redirects


def add_custom_redirects(redirects, custom_redirects, stable_version):
    entries = custom_redirects.get("redirects")
    if not isinstance(entries, list):
        raise DataError("redirects.yml redirects must be a list")

    for index, entry in enumerate(entries):
        field = f"redirects.yml redirects[{index}]"
        if not isinstance(entry, dict):
            raise DataError(f"{field} must be a mapping")
        if not entry.get("reason"):
            raise DataError(f"{field}.reason is required")
        expires_after = entry.get("expires_after")
        if expires_after is not None:
            if version_tuple(stable_version) > version_tuple(
                expires_after, f"{field}.expires_after"
            ):
                raise DataError(
                    f"{field} expired after {expires_after}; remove or extend it"
                )
        add_redirect(redirects, entry.get("source"), entry.get("target"), field)


def redirects_text(redirects):
    lines = [
        "# Generated by ci/generate-projects-to-versions.py. Do not edit directly.",
        "# Sources: _data/docs.yml and _data/redirects.yml.",
    ]
    lines.extend(f"{source} {redirects[source]}" for source in sorted(redirects))
    return "\n".join(lines) + "\n"


def generate():
    docs = load_yaml(DOCS_PATH)
    with RELEASES_PATH.open(encoding="utf-8") as file:
        releases = json.load(file)
    custom_redirects = load_yaml(CUSTOM_REDIRECTS_PATH)

    projects, redirects = project_versions_and_redirects(docs, releases)
    add_custom_redirects(redirects, custom_redirects, releases["stable"]["version"])
    return json_text(projects), redirects_text(redirects)


def main():
    parser = argparse.ArgumentParser(
        description="Generate API project versions and root redirects."
    )
    parser.add_argument(
        "--check", action="store_true", help="Fail instead of updating stale outputs."
    )
    args = parser.parse_args()

    try:
        projects_text, generated_redirects = generate()
        write_or_check(PROJECTS_OUTPUT_PATH, projects_text, args.check)
        write_or_check(REDIRECTS_OUTPUT_PATH, generated_redirects, args.check)
    except (DataError, OSError, json.JSONDecodeError) as error:
        print(error, file=sys.stderr)
        return 1

    action = "validated" if args.check else "generated"
    print(f"Docs artifacts {action} successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
