# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import json

from scripts import generate_redirect_site


def test_redirects_route_migrated_docs_and_portal() -> None:
    redirects = generate_redirect_site.generate_redirects()
    releases = json.loads(generate_redirect_site.RELEASES_CONFIG.read_text())
    stable = releases["stable"]["version"]

    assert f"/api/cudf/stable/* https://docs.nvidia.com/cudf/{stable}/:splat 301!" in redirects
    assert f"/api/cudf/{stable} https://docs.nvidia.com/cudf/{stable}/ 301!" in redirects
    # Deployment redirects are hand-maintained in _redirects and target latest/.
    assert (
        "/deployment/stable/* https://docs.nvidia.com/datascience/deployment/latest/:splat 301!"
        in redirects
    )
    assert "/deployment/*" not in redirects
    assert "/notices/* https://docs.nvidia.com/datascience/notices/:splat 301!" in redirects
    assert "/ https://docs.nvidia.com/datascience/ 301!" in redirects
    assert " 302!" not in redirects
    assert "\n/* " not in redirects


def test_nightly_redirects_use_latest() -> None:
    releases = json.loads(generate_redirect_site.RELEASES_CONFIG.read_text())
    nightly = releases["nightly"]["version"]
    project = {
        "path": "cudf",
        "first_docs_nvidia_com_release": "26.08",
        "versions": {"nightly": 1},
    }

    assert generate_redirect_site._project_rules(project, releases) == [
        "/api/cudf/nightly https://docs.nvidia.com/cudf/latest/ 301!",
        "/api/cudf/nightly/* https://docs.nvidia.com/cudf/latest/:splat 301!",
        f"/api/cudf/{nightly} https://docs.nvidia.com/cudf/latest/ 301!",
        f"/api/cudf/{nightly}/* https://docs.nvidia.com/cudf/latest/:splat 301!",
    ]


def test_redirects_route_external_unversioned_docs() -> None:
    redirects = generate_redirect_site.generate_redirects()

    assert "/api/cuvs/stable/* https://docs.nvidia.com/cuvs/:splat 301!" in redirects


def test_redirects_leave_unmigrated_api_docs_and_shared_assets_local() -> None:
    redirects = generate_redirect_site.generate_redirects()
    releases = json.loads(generate_redirect_site.RELEASES_CONFIG.read_text())
    legacy = releases["legacy"]["version"]

    assert "/api/ucxx/stable " not in redirects
    assert "/api/ucxx/nightly " not in redirects
    assert f"/api/ucxx/{releases['stable']['ucxx_version']} " not in redirects
    assert "/api/dask-cudf/legacy " not in redirects
    assert f"/api/dask-cudf/{legacy} " not in redirects
    assert "/api/cudf/legacy " not in redirects
    assert f"/api/cudf/{legacy} " not in redirects
    assert "/api/* " not in redirects
    assert "/assets/* " not in redirects
