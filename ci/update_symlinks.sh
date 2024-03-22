#!/bin/bash
#######################################
# Updates or removes all symlinked folders based on the given positional parameter
#######################################
set -euEo pipefail

PROJ_ROOT=$(realpath "$(dirname $(realpath $0))/../")

STABLE_FOLDER=$( cat "${PROJ_ROOT}/_data/releases.json" | jq -r '.stable.version')
LEGACY_FOLDER=$( cat "${PROJ_ROOT}/_data/releases.json" | jq -r '.legacy.version')
NIGHTLY_FOLDER=$( cat "${PROJ_ROOT}/_data/releases.json" | jq -r '.nightly.version')

echo "Updating symlinks..."
echo ""
for FOLDER in _site/api/*/ ; do
  if [[ "${FOLDER}" == *"libucxx"* ]]; then
    STABLE_FOLDER=$( cat "${PROJ_ROOT}/_data/releases.json" | jq -r '.stable.ucxx_version')
    LEGACY_FOLDER=$( cat "${PROJ_ROOT}/_data/releases.json" | jq -r '.legacy.ucxx_version')
    NIGHTLY_FOLDER=$( cat "${PROJ_ROOT}/_data/releases.json" | jq -r '.nightly.ucxx_version')
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
