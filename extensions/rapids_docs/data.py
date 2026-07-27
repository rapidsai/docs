# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# SPDX-License-Identifier: Apache-2.0

"""Load the portal's structured source data."""

import json
from pathlib import Path

import frontmatter
import yaml


def _source_dir(app) -> Path:
    return Path(app.srcdir)


def _load_data(app) -> dict:
    data_dir = _source_dir(app) / "_data"
    with (data_dir / "docs.yml").open() as file:
        docs = yaml.safe_load(file)
    with (data_dir / "platform_support.yml").open() as file:
        platform_support = yaml.safe_load(file)
    with (data_dir / "releases.json").open() as file:
        releases = json.load(file)
    with (data_dir / "previous_releases.json").open() as file:
        previous_releases = json.load(file)

    notices = []
    for path in sorted((_source_dir(app) / "notices").glob("r[dgs]n[0-9][0-9][0-9][0-9].md")):
        post = frontmatter.load(path)
        metadata = dict(post.metadata)
        metadata["docname"] = f"notices/{path.stem}"
        metadata["body"] = post.content
        notices.append(metadata)

    return {
        "docs": docs,
        "notices": notices,
        "platform_support": platform_support,
        "previous_releases": previous_releases,
        "releases": releases,
    }
