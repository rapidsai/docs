#!/bin/bash
#######################################
# Recursively customizes all docs in a specified folder relative
# to the project's root. Intended to be run from the project's
# root directory
#
# Usage:
# customization/customize_docs_in_folder.sh api/
#
# Positional Arguments:
#   1) FOLDER_TO_CUSTOMIZE: project root relative folder to customize (i.e. api/, api/rmm, etc.)
#######################################
set -e

display_usage() {
  echo "Usage:"
  echo " - customization/customize_docs_in_folder.sh api/       # update files in api/ folder"
  echo " - customization/customize_docs_in_folder.sh api/cudf   # update files in api/cudf folder"
}

FOLDER_TO_CUSTOMIZE=$1

if [[ $# -ne 1 ]]; then
  display_usage
  exit 1
fi

if [ ! -d "${FOLDER_TO_CUSTOMIZE}" ]; then
  echo "Couldn't find subfolder: ${FOLDER_TO_CUSTOMIZE}"
  exit 1
fi

SCRIPT_SRC_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )" # directory of where this script is located
JTD_SEARCH_TERM='class="wy-side-nav-search"'
DOXYGEN_SEARCH_TERM='id="titlearea"'
PYDATA_SEARCH_TERM='class="col-12 col-md-3 bd-sidebar"'

# IFS is changed due to cuxfilter docs having spaces in their filenames
OIFS="$IFS"
IFS=$'\n'
for FILE in $(grep "${JTD_SEARCH_TERM}\|${DOXYGEN_SEARCH_TERM}\|${PYDATA_SEARCH_TERM}" -rl \
  --include=\*.html \
  --exclude-dir=stable \
  --exclude-dir=nightly \
  --exclude-dir=latest \
  --exclude-dir=legacy \
  ${FOLDER_TO_CUSTOMIZE} ); do
  python ${SCRIPT_SRC_FOLDER}/customize_doc.py $(realpath ${FILE})
  echo "" # line break for readability
done
IFS="$OIFS"
