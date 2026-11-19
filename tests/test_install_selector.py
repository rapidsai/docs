# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import shutil
import subprocess
from pathlib import Path

import pytest


@pytest.mark.skipif(
    shutil.which("node") is None, reason="Node.js is required to exercise the install selector"
)
def test_nx_cugraph_release_boundary() -> None:
    root = Path(__file__).resolve().parents[1]
    subprocess.run(["node", str(root / "tests/install_selector.cjs")], check=True, cwd=root)
