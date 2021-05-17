#!/bin/bash
#######################################
# Updates or removes all symlinked folders based on the given positional parameter
#######################################
set -eEo pipefail

display_usage() {
  echo "Usage:"
  echo " - update_symlinks ## updates symlinks to match versions in _data/releases.json"
  echo " - update_symlinks rm ## removes all current symlinks"
}

# If there is more than one argument, or if there is one argument that's not "rm"
# then show usage info and exit.
if [[ $# -eq "1" && "$1" != "rm" ]] || [[ $# -gt 1 ]]; then
  display_usage
  exit 1
fi

PROJ_ROOT=$(dirname $(realpath $0))

echo "Removing existing symlinks..."
find ${PROJ_ROOT} -type l -ls -delete > /dev/null

if [[ "$1" == "rm" ]]; then
  exit 0
fi

STABLE_FOLDER=$( cat "${PROJ_ROOT}/_data/releases.json" | jq -r '.stable.version')
LEGACY_FOLDER=$( cat "${PROJ_ROOT}/_data/releases.json" | jq -r '.legacy.version')
NIGHTLY_FOLDER=$( cat "${PROJ_ROOT}/_data/releases.json" | jq -r '.nightly.version')

echo "Updating symlinks..."
echo ""
for FOLDER in api/*/ ; do

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
