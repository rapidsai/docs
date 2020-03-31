#!/bin/bash
#######################################
# Updates all symlink folders based on a given nightly version number
#
# Usage:
# update_symlinks.sh 13
#
# Positional Arguments:
#   1) NIGHTLY_VERSION: current RAPIDS nightly version (i.e. 13, 14, 15, etc.)
#######################################
set -e

PROJ_ROOT=$(pwd)
NIGHTLY_VERSION=$1

STABLE_FOLDER=$(echo "0.$((${NIGHTLY_VERSION} - 1))")
LEGACY_FOLDER=$(echo "0.$((${NIGHTLY_VERSION} - 2))")
NIGHTLY_FOLDER=$(echo "0.$((${NIGHTLY_VERSION}))")

for FOLDER in api/*/ ; do

  cd ${FOLDER}
  echo ""
  echo "${FOLDER}--------"

  if [ -d "${STABLE_FOLDER}" ]; then
    rm -rf stable latest
    ln -s ${STABLE_FOLDER} stable
    ln -s ${STABLE_FOLDER} latest
    echo "stable & latest point to ${STABLE_FOLDER}"
  fi

  if [ -d "${LEGACY_FOLDER}" ]; then
    rm -rf legacy
    ln -s ${LEGACY_FOLDER} legacy
    echo "legacy points to ${LEGACY_FOLDER}"
  fi

  if [ -d "${NIGHTLY_FOLDER}" ]; then
    rm -rf nightly
    ln -s ${NIGHTLY_FOLDER} nightly
    echo "nightly points to ${NIGHTLY_FOLDER}"
  fi

  echo "---------------"
  echo ""
  cd ${PROJ_ROOT}
done
