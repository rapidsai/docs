#!/bin/bash
# SPDX-FileCopyrightText: Copyright (c) 2025, NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: Apache-2.0

#######################################
# Updates or removes all symlinked folders based on the given positional parameter
#######################################
set -euEo pipefail

PROJ_ROOT=$(realpath "$(dirname $(realpath $0))/../")
RELEASES="${PROJ_ROOT}/_data/releases.json"

STABLE_VERSION=$(jq -r '.stable.version' < "${RELEASES}")
LEGACY_VERSION=$(jq -r '.legacy.version' < "${RELEASES}")
NIGHTLY_VERSION=$(jq -r '.nightly.version' < "${RELEASES}")

STABLE_UCXX_VERSION=$(jq -r '.stable.ucxx_version' < "${RELEASES}")
LEGACY_UCXX_VERSION=$(jq -r '.legacy.ucxx_version' < "${RELEASES}")
NIGHTLY_UCXX_VERSION=$(jq -r '.nightly.ucxx_version' < "${RELEASES}")

echo "Updating symlinks..."
echo ""
for FOLDER in _site/api/*/ ; do
  if [[ "${FOLDER}" == *"ucxx"* ]]; then
    STABLE_FOLDER=$STABLE_UCXX_VERSION
    LEGACY_FOLDER=$LEGACY_UCXX_VERSION
    NIGHTLY_FOLDER=$NIGHTLY_UCXX_VERSION
  else
    STABLE_FOLDER=$STABLE_VERSION
    LEGACY_FOLDER=$LEGACY_VERSION
    NIGHTLY_FOLDER=$NIGHTLY_VERSION
  fi

  cd ${FOLDER}
  echo ""
  echo "${FOLDER}--------"

  if [ -d "${STABLE_FOLDER}" ]; then
    ln -s ${STABLE_FOLDER} stable
    ln -s ${STABLE_FOLDER} latest
    echo "  - stable & latest point to ${STABLE_FOLDER}"
  fi

  if [ -d "${LEGACY_FOLDER}" ]; then
    ln -s ${LEGACY_FOLDER} legacy
    echo "  - legacy points to ${LEGACY_FOLDER}"
  fi

  if [ -d "${NIGHTLY_FOLDER}" ]; then
    ln -s ${NIGHTLY_FOLDER} nightly
    echo "  - nightly points to ${NIGHTLY_FOLDER}"
  fi

  echo "---------------"
  echo ""
  cd ${PROJ_ROOT}
done
