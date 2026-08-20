# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import json

import pytest
import yaml

from scripts import generate_redirect_site


def test_redirects_route_migrated_docs_and_portal() -> None:
    redirects = generate_redirect_site.generate_redirects(status=302)
    releases = json.loads(generate_redirect_site.RELEASES_CONFIG.read_text())
    stable = releases["stable"]["version"]

    assert f"/api/cudf/stable/* https://docs.nvidia.com/cudf/{stable}/:splat 302!" in redirects
    assert f"/api/cudf/{stable} https://docs.nvidia.com/cudf/{stable}/ 302!" in redirects
    assert "/deployment/* https://docs.nvidia.com/datascience/deployment/:splat 302!" in redirects
    assert redirects.rstrip().endswith("/* https://docs.nvidia.com/datascience/:splat 302!")


def test_redirects_route_external_unversioned_docs() -> None:
    redirects = generate_redirect_site.generate_redirects(status=301)

    assert "/api/cuvs/stable/* https://docs.nvidia.com/cuvs/:splat 301!" in redirects


def test_redirect_cutover_requires_complete_migration_metadata() -> None:
    docs = yaml.safe_load(generate_redirect_site.DOCS_CONFIG.read_text())
    assert docs["apis"]["dask-cudf"]["first_docs_nvidia_com_release"] is None

    with pytest.raises(SystemExit, match="dask-cudf:stable"):
        generate_redirect_site.generate_redirects(status=302, require_complete=True)
