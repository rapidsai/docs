#!/bin/bash
#######################################
# Updates or removes all symlinked folders based on the given positional parameter
#######################################
set -e

display_usage() {
  echo "Usage:"
  echo " - update_symlinks 19 ## updates symlinks to use 19 as nightly version"
  echo " - update_symlinks rm ## removes all current symlinks"
}

if [[ $# -eq 0 ]]; then
  display_usage
  exit 1
fi

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
