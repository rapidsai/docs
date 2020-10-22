#!/bin/bash
#######################################
# Updates or removes all symlinked folders based on the given positional parameter
#
# Usage:
# update_symlinks.sh 17 # used to update symlink folders
#
# or
#
# update_symlinks.sh rm # used to remove existing symlink folders
#
# Positional Arguments:
#   1) Either of the following:
#      - NIGHTLY_VERSION: current RAPIDS nightly version (i.e. 16, 17, 18, etc.)
#      - "rm"
#######################################
set -e

PROJ_ROOT=$(pwd)

if [ "${1}" = "rm" ]; then
  RM_SYMLINKS="true"
  echo "Removing symlinks..."
else
  RM_SYMLINKS="false"
  NIGHTLY_VERSION="${1}"
  STABLE_FOLDER=$(echo "0.$((${NIGHTLY_VERSION} - 1))")
  LEGACY_FOLDER=$(echo "0.$((${NIGHTLY_VERSION} - 2))")
  NIGHTLY_FOLDER=$(echo "0.$((${NIGHTLY_VERSION}))")
fi

for FOLDER in api/*/ ; do

  cd ${FOLDER}
  echo ""
  echo "${FOLDER}--------"

  # Remove existing symlinks
  rm -rf legacy stable latest nightly

  if [ "${RM_SYMLINKS}" == "true" ]; then
    echo "  - symlinks removed"

  elif [ "${RM_SYMLINKS}" == "false" ]; then

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
  fi

  echo "---------------"
  echo ""
  cd ${PROJ_ROOT}
done
