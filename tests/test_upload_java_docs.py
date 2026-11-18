# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import os
import subprocess
import zipfile
from pathlib import Path

import pytest


@pytest.fixture
def upload_env(tmp_path):
    mock_bin = tmp_path / "bin"
    mock_bin.mkdir()
    scripts = {
        "curl": """#!/bin/bash
set -euo pipefail
echo "$*" >> "$MOCK_ROOT/curl.log"
output=""
while [[ $# -gt 0 ]]; do
  if [[ $1 == --output ]]; then output=$2; shift 2; else shift; fi
done
if [[ ! -f $MOCK_ROOT/seen ]]; then
  touch "$MOCK_ROOT/seen"
  echo 404
else
  cp "$MOCK_ROOT/javadoc.jar" "$output"
  echo 200
fi
""",
        "aws": '#!/bin/bash\necho "$*" >> "$MOCK_ROOT/aws.log"\n',
        "sleep": "#!/bin/bash\nexit 0\n",
    }
    for name, script in scripts.items():
        executable = mock_bin / name
        executable.write_text(script)
        executable.chmod(0o755)
    with zipfile.ZipFile(tmp_path / "javadoc.jar", "w") as archive:
        archive.writestr("index.html", "<html>Released documentation</html>")
    return tmp_path, {
        **os.environ,
        "MOCK_ROOT": str(tmp_path),
        "PATH": f"{mock_bin}:{os.environ['PATH']}",
    }


def run_upload(env):
    script = Path(__file__).resolve().parents[1] / "ci/upload_java_docs.sh"
    return subprocess.run(
        ["bash", str(script), "cuvs-lucene", "26.12.01"],
        env=env,
        capture_output=True,
        text=True,
    )


def test_lucene_download_retries_and_uploads_to_the_exact_version(upload_env):
    root, env = upload_env

    result = run_upload(env)

    assert result.returncode == 0, result.stderr
    urls = (root / "curl.log").read_text().splitlines()
    assert len(urls) == 2
    maven_path = (
        "/com/nvidia/cuvs/lucene/cuvs-lucene-10.2/26.12.1/cuvs-lucene-10.2-26.12.1-javadoc.jar"
    )
    assert all(url.endswith(maven_path) for url in urls)
    upload = (root / "aws.log").read_text().strip()
    assert upload.endswith("s3://rapidsai-docs/cuvs-lucene/html/26.12.1/")


def test_missing_javadoc_index_blocks_upload(upload_env):
    root, env = upload_env
    with zipfile.ZipFile(root / "javadoc.jar", "w") as archive:
        archive.writestr("other.html", "Incomplete javadoc")

    result = run_upload(env)

    assert result.returncode != 0
    assert "Javadoc index.html is missing" in result.stderr
    assert not (root / "aws.log").exists()
