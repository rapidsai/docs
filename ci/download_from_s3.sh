#!/bin/bash
# SPDX-FileCopyrightText: Copyright (c) 2025-2026, NVIDIA CORPORATION & AFFILIATES.
# SPDX-License-Identifier: Apache-2.0

set -euo pipefail

CURRENT_DIR=$(dirname "$(realpath "$0")")
python "${CURRENT_DIR}/download_from_s3.py"
