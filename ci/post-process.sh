#!/bin/bash
# SPDX-FileCopyrightText: Copyright (c) 2025, NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: Apache-2.0

set -euo pipefail

CURRENT_DIR=$(dirname $(realpath $0))

pip install -r "${CURRENT_DIR}/customization/requirements.txt"

"${CURRENT_DIR}"/update_symlinks.sh

"${CURRENT_DIR}"/customization/lib_map.sh

"${CURRENT_DIR}"/get-projects-to-versions.sh > "${CURRENT_DIR}"/customization/projects-to-versions.json

"${CURRENT_DIR}"/customization/customize_docs_in_folder.sh "_site/api"
