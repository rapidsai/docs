#!/bin/bash
# SPDX-FileCopyrightText: Copyright (c) 2025, NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: Apache-2.0

set -euo pipefail

CURRENT_DIR=$(dirname $(realpath $0))

pip install -r "${CURRENT_DIR}/customization/requirements.txt"

PROJECTS_TO_VERSIONS_PATH="${CURRENT_DIR}"/customization/projects-to-versions.json

"${CURRENT_DIR}"/update_symlinks.sh "${PROJECTS_TO_VERSIONS_PATH}"

"${CURRENT_DIR}"/customization/lib_map.sh

"${CURRENT_DIR}"/customization/customize_docs_in_folder.sh "_site/api" "${PROJECTS_TO_VERSIONS_PATH}"
