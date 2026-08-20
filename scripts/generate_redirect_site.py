#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Generate redirects for the hybrid docs.rapids.ai compatibility site."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from extensions.rapids_docs.routes import _documentation_url, _version_label  # noqa: E402

DOCS_CONFIG = ROOT / "_data" / "docs.yml"
RELEASES_CONFIG = ROOT / "_data" / "releases.json"
MANUAL_REDIRECTS = ROOT / "_redirects"
SECTIONS = ("apis", "libs", "inactive-projects")
VERSION_NAMES = ("legacy", "stable", "nightly")
PORTAL_PREFIXES = (
    "_static",
    "contributing",
    "install",
    "licenses",
    "maintainers",
    "notices",
    "platform-support",
    "releases",
    "resources",
    "user-guide",
    "visualization",
)
PORTAL_FILES = ("404", "404.html", "LICENSE", "SECURITY.md", "genindex", "search")


def _rule(source: str, destination: str, status: int) -> str:
    return f"{source} {destination} {status}!"


def _project_rules(project: dict, releases: dict, status: int) -> list[str]:
    rules = []
    emitted_sources = set()
    project_path = project["path"]

    for version_name in VERSION_NAMES:
        if not project["versions"].get(version_name):
            continue
        version = _version_label(project, version_name, releases)
        destination = _documentation_url(project, version_name, version)
        if not project.get("external_docs_url") and destination.startswith(
            "https://docs.rapids.ai/"
        ):
            continue

        for source_version in (version_name, version):
            source = f"/api/{project_path}/{source_version}"
            if source in emitted_sources:
                continue
            emitted_sources.add(source)
            rules.extend(
                [
                    _rule(source, destination, status),
                    _rule(
                        f"{source}/*",
                        _documentation_url(project, version_name, version, ":splat"),
                        status,
                    ),
                ]
            )

    return rules


def generate_redirects(*, status: int) -> str:
    docs = yaml.safe_load(DOCS_CONFIG.read_text())
    releases = json.loads(RELEASES_CONFIG.read_text())
    rules = [
        "# Generated redirects for the hybrid docs.rapids.ai compatibility site.",
        "# Unmatched API routes continue to serve assembled documentation files.",
        "# Manual compatibility redirects run first and may intentionally chain.",
        MANUAL_REDIRECTS.read_text().rstrip(),
        "",
        "# API documentation aliases and numeric versions.",
    ]
    for section in SECTIONS:
        for project in docs[section].values():
            rules.extend(_project_rules(project, releases, status))

    rules.extend(
        [
            "",
            "# Deployment docs are independently published below the datascience prefix.",
            _rule(
                "/deployment/*",
                "https://docs.nvidia.com/datascience/deployment/:splat",
                status,
            ),
            "",
            "# Portal routes move beneath docs.nvidia.com/datascience.",
            _rule("/", "https://docs.nvidia.com/datascience/", status),
            _rule("/api", "https://docs.nvidia.com/datascience/api/", status),
            _rule("/api/", "https://docs.nvidia.com/datascience/api/", status),
        ]
    )
    for prefix in PORTAL_PREFIXES:
        rules.extend(
            [
                _rule(
                    f"/{prefix}",
                    f"https://docs.nvidia.com/datascience/{prefix}/",
                    status,
                ),
                _rule(
                    f"/{prefix}/*",
                    f"https://docs.nvidia.com/datascience/{prefix}/:splat",
                    status,
                ),
            ]
        )
    for filename in PORTAL_FILES:
        rules.append(
            _rule(
                f"/{filename}",
                f"https://docs.nvidia.com/datascience/{filename}",
                status,
            )
        )
    rules.extend(
        [
            "",
            "# Do not add a /* fallback: /api and /assets contain real site content.",
            "",
        ]
    )
    return "\n".join(rules)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--status", choices=(301, 302), default=302, type=int)
    args = parser.parse_args()

    output = generate_redirects(status=args.status)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
