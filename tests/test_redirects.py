# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import json

from scripts import generate_redirect_site


def test_redirects_route_migrated_docs_and_portal() -> None:
    redirects = generate_redirect_site.generate_redirects(status=302)
    releases = json.loads(generate_redirect_site.RELEASES_CONFIG.read_text())
    stable = releases["stable"]["version"]

    assert f"/api/cudf/stable/* https://docs.nvidia.com/cudf/{stable}/:splat 302!" in redirects
    assert f"/api/cudf/{stable} https://docs.nvidia.com/cudf/{stable}/ 302!" in redirects
    assert "/deployment/* https://docs.nvidia.com/datascience/deployment/:splat 302!" in redirects
    assert "/notices/* https://docs.nvidia.com/datascience/notices/:splat 302!" in redirects
    assert "/ https://docs.nvidia.com/datascience/ 302!" in redirects
    assert "\n/* " not in redirects


def test_redirects_route_external_unversioned_docs() -> None:
    redirects = generate_redirect_site.generate_redirects(status=301)

    assert "/api/cuvs/stable/* https://docs.nvidia.com/cuvs/:splat 301!" in redirects


def test_redirects_leave_unmigrated_api_docs_and_shared_assets_local() -> None:
    redirects = generate_redirect_site.generate_redirects(status=302)
    releases = json.loads(generate_redirect_site.RELEASES_CONFIG.read_text())
    legacy = releases["legacy"]["version"]

    assert "/api/dask-cudf/stable " not in redirects
    assert f"/api/dask-cudf/{legacy} " not in redirects
    assert "/api/cudf/legacy " not in redirects
    assert f"/api/cudf/{legacy} " not in redirects
    assert "/api/* " not in redirects
    assert "/assets/* " not in redirects
