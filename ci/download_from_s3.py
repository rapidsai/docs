#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# SPDX-License-Identifier: Apache-2.0

"""Download the versioned RAPIDS documentation tree from S3."""

from __future__ import annotations

import json
import os
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import boto3

BUCKET = "rapidsai-docs"
ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = ROOT / os.environ.get("SITE_DIR", "_site")
API_DIR = SITE_DIR / "api"
DEPLOYMENT_DIR = SITE_DIR / "deployment"
PROJECT_VERSIONS = ROOT / "ci" / "customization" / "projects-to-versions.json"
WORKERS = int(os.environ.get("S3_DOWNLOAD_WORKERS", "16"))


def validate_output() -> None:
    if not SITE_DIR.is_dir():
        raise SystemExit(f'"{SITE_DIR}" does not exist. Build the Sphinx portal first.')
    api_entries = sorted(path.name for path in API_DIR.iterdir())
    if api_entries != ["index.html"]:
        raise SystemExit(f'"{API_DIR}" must contain only index.html before importing API docs.')
    if DEPLOYMENT_DIR.exists():
        raise SystemExit(f'"{DEPLOYMENT_DIR}" is populated only during full-site assembly.')


def object_keys(client, prefix: str) -> list[str]:
    paginator = client.get_paginator("list_objects_v2")
    keys = [
        item["Key"]
        for page in paginator.paginate(Bucket=BUCKET, Prefix=prefix)
        for item in page.get("Contents", [])
        if not item["Key"].endswith("/")
    ]
    if not keys:
        raise SystemExit(f"No files found in s3://{BUCKET}/{prefix}")
    return keys


def download_prefix(client, prefix: str, destination: Path) -> None:
    keys = object_keys(client, prefix)
    print(f"Copying s3://{BUCKET}/{prefix} to {destination} ({len(keys)} files)")

    def download(key: str) -> None:
        relative = key.removeprefix(prefix)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        client.download_file(BUCKET, key, str(target))

    with ThreadPoolExecutor(max_workers=WORKERS) as executor:
        list(executor.map(download, keys))


def main() -> None:
    validate_output()
    profile = os.environ.get("AWS_PROFILE")
    session = boto3.Session(profile_name=profile) if profile else boto3.Session()
    client = session.client("s3")

    projects = json.loads(PROJECT_VERSIONS.read_text())
    for project, versions in projects.items():
        for version_number in versions.values():
            prefix = f"{project}/html/{version_number}/"
            download_prefix(client, prefix, API_DIR / project / str(version_number))

    for version in ("nightly", "stable"):
        download_prefix(
            client,
            f"deployment/html/{version}/",
            DEPLOYMENT_DIR / version,
        )


if __name__ == "__main__":
    main()
