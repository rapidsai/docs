#!/bin/bash
# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ $# -ne 2 ]]; then
  echo "Usage: $0 <registered-project> <YY.MM or YY.MM.P>" >&2
  exit 1
fi
PROJECT=$1
VERSION=$2
[[ ${PROJECT} =~ ^[a-z][a-z0-9-]+$ ]] || { echo "Invalid docs project" >&2; exit 1; }
[[ ${VERSION} =~ ^[0-9]{2}\.[0-9]{2}(\.[0-9]+)?$ ]] || { echo "Invalid release version" >&2; exit 1; }
IFS='.' read -r major minor patch <<< "${VERSION}"
patch=${patch:-0}
patch=$(printf '%s' "${patch}" | sed 's/^0*//')
patch=${patch:-0}
VERSION="${major}.${minor}.${patch}"

GROUP_ID=$(jq -er --arg project "${PROJECT}" '.[$project]["group-id"]' "${SCRIPT_DIR}/java-docs-projects.json")
ARTIFACT_ID=$(jq -er --arg project "${PROJECT}" '.[$project]["artifact-id"]' "${SCRIPT_DIR}/java-docs-projects.json")
GROUP_PATH=${GROUP_ID//./\/}
URL="https://repo1.maven.org/maven2/${GROUP_PATH}/${ARTIFACT_ID}/${VERSION}/${ARTIFACT_ID}-${VERSION}-javadoc.jar"
WORK_DIR=$(mktemp -d)
trap 'rm -rf "${WORK_DIR}"' EXIT

# Publication can precede availability from the Maven Central download endpoint.
# Retry propagation failures for at most 15 minutes; stop on other HTTP errors.
deadline=$((SECONDS + 900))
attempt=0
status=000
while (( SECONDS < deadline )); do
  attempt=$((attempt + 1))
  status=$(curl --silent --show-error --location --connect-timeout 15 --max-time 60 \
    --output "${WORK_DIR}/javadoc.jar" --write-out '%{http_code}' "${URL}") || status=000
  case "${status}" in
    200) break ;;
    000|404|429|5??)
      echo "Waiting for Maven Central javadoc (${status}, attempt ${attempt})"
      sleep 15
      ;;
    *) echo "Javadoc download failed: HTTP ${status}" >&2; exit 1 ;;
  esac
done
[[ ${status} == 200 ]] || { echo "Timed out waiting for ${URL}" >&2; exit 1; }
unzip -tq "${WORK_DIR}/javadoc.jar" >/dev/null
mkdir "${WORK_DIR}/html"
unzip -q "${WORK_DIR}/javadoc.jar" -d "${WORK_DIR}/html"
[[ -f ${WORK_DIR}/html/index.html ]] || { echo "Javadoc index.html is missing" >&2; exit 1; }
aws s3 sync --delete "${WORK_DIR}/html/" "s3://rapidsai-docs/${PROJECT}/html/${VERSION}/"
echo "Uploaded ${PROJECT} docs for ${VERSION}"
