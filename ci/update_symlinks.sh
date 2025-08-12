#!/bin/bash
# SPDX-FileCopyrightText: Copyright (c) 2025, NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: Apache-2.0

#######################################
# Updates or removes all symlinked folders based on the given positional parameter
#######################################
set -euEo pipefail

PROJECTS_TO_VERSIONS_PATH="${1}"

# expect paths to be relative to the project root
PROJ_ROOT=$(realpath "$(dirname $(realpath $0))/../")
pushd "${PROJ_ROOT}"

PROJECTS_TO_VERSIONS_JSON=$(cat "${PROJECTS_TO_VERSIONS_PATH}")

echo "Updating symlinks..."
echo ""
for PROJECT in $(jq -r 'keys | .[]' <<< "${PROJECTS_TO_VERSIONS_JSON}"); do
  VERSIONS_FOR_THIS_PROJECT=$(
    jq \
      -r \
      --arg pr "${PROJECT}" \
      '.[$pr]' \
    <<< "${PROJECTS_TO_VERSIONS_JSON}"
  )

  if [[ "${VERSIONS_FOR_THIS_PROJECT}" == "{}" ]]; then
    echo "skipping '${PROJECT}'... no API docs hosted for this project"
    continue
  fi

  # expect to find a local folder, relative to the root of the repo,
  # named e.g. '_site/api/cudf'
  PROJECT_FOLDER="_site/api/${PROJECT}"
  pushd "${PROJECT_FOLDER}"
  echo ""
  echo "${PROJECT_FOLDER}/--------"

  # loop over 'stable', 'nightly', etc.
  for VERSION_NAME in $(jq -r 'keys | .[]' <<< "${VERSIONS_FOR_THIS_PROJECT}"); do
    # expect to find a directory matching the version number, e.g. '_site/api/cudf/25.10'
    VERSION_NUMBER=$(
      jq \
        -r \
        --arg version_name "${VERSION_NAME}" \
        '.[$version_name]' \
      <<< "${VERSIONS_FOR_THIS_PROJECT}"
    )
    FOLDER_FOR_THIS_VERSION="${VERSION_NUMBER}"

    # map /latest to the same version as /stable
    if [[ "${VERSION_NAME}" == "stable" ]]; then
      ln -s "${FOLDER_FOR_THIS_VERSION}" stable
      ln -s "${FOLDER_FOR_THIS_VERSION}" latest
      echo "  - 'stable' and 'latest' point to '${FOLDER_FOR_THIS_VERSION}'"
    else
      ln -s "${FOLDER_FOR_THIS_VERSION}" "${VERSION_NAME}"
      echo "  - '${VERSION_NAME}' points to '${FOLDER_FOR_THIS_VERSION}'"
    fi
  done # for VERSION

  popd
  echo "---------------"
  echo ""
done # for PROJECT
