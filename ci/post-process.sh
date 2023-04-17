#!/bin/bash
set -euo pipefail

CURRENT_DIR=$(dirname $(realpath $0))

pip install -r "${CURRENT_DIR}/customization/requirements.txt"

"${CURRENT_DIR}"/update_symlinks.sh

"${CURRENT_DIR}"/customization/lib_map.sh

# TODO: change "_site/api/rmm" to "_site/api" after everything is confirmed
# working
"${CURRENT_DIR}"/customization/customize_docs_in_folder.sh "_site/api/rmm"
