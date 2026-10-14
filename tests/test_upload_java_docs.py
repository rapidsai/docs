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
echo "$output" > "$MOCK_ROOT/download-path"
if [[ ${MOCK_HTTP:-} != "" ]]; then
  echo "$MOCK_HTTP"
elif [[ ! -f $MOCK_ROOT/seen ]]; then
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


def run_upload(env, project="cudf-java", version="26.12.00"):
    script = Path(__file__).resolve().parents[1] / "ci/upload_java_docs.sh"
    return subprocess.run(
        ["bash", str(script), project, version], env=env, capture_output=True, text=True
    )


def test_propagation_retry_uploads_normalized_version_and_cleans_up(upload_env):
    root, env = upload_env
    result = run_upload(env)
    assert result.returncode == 0, result.stderr
    curl_log = (root / "curl.log").read_text()
    assert len(curl_log.splitlines()) == 2
    assert "/ai/rapids/cudf/26.12.0/cudf-26.12.0-javadoc.jar" in curl_log
    assert "s3://rapidsai-docs/cudf-java/html/26.12.0/" in (root / "aws.log").read_text()
    assert not Path((root / "download-path").read_text().strip()).parent.exists()


@pytest.mark.parametrize(
    ("project", "version"),
    [("unknown", "26.12.0"), ("../cudf-java", "26.12.0"), ("cudf-java", "26.12.0-SNAPSHOT")],
)
def test_invalid_input_never_downloads_or_uploads(upload_env, project, version):
    root, env = upload_env
    assert run_upload(env, project, version).returncode != 0
    assert not (root / "curl.log").exists()
    assert not (root / "aws.log").exists()


def test_permanent_http_error_does_not_upload(upload_env):
    root, env = upload_env
    result = run_upload({**env, "MOCK_HTTP": "401"})
    assert result.returncode != 0
    assert len((root / "curl.log").read_text().splitlines()) == 1
    assert not (root / "aws.log").exists()


@pytest.mark.parametrize("valid_zip", [False, True])
def test_missing_or_invalid_javadoc_does_not_upload(upload_env, valid_zip):
    root, env = upload_env
    if valid_zip:
        with zipfile.ZipFile(root / "javadoc.jar", "w") as archive:
            archive.writestr("other.html", "Incomplete javadoc")
    else:
        (root / "javadoc.jar").write_text("invalid ZIP")
    assert run_upload(env).returncode != 0
    assert not (root / "aws.log").exists()
