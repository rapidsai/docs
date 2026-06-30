#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import json
from pathlib import Path

import yaml


class DataError(ValueError):
    pass


def load_yaml(path):
    with path.open(encoding="utf-8") as file:
        return yaml.safe_load(file)


def version_tuple(value, field="version"):
    if not isinstance(value, str):
        raise DataError(f"{field} must be a quoted dotted version string")

    try:
        parsed = tuple(int(part) for part in value.split("."))
    except ValueError as error:
        raise DataError(
            f"{field} must contain only dot-separated integers: {value!r}"
        ) from error

    if len(parsed) < 2:
        raise DataError(f"{field} must contain at least two numeric components")
    return parsed


def json_text(value):
    return json.dumps(value, indent=2) + "\n"


def write_or_check(path, content, check):
    path = Path(path)
    if check:
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != content:
            raise DataError(f"{path} is stale; run its generator and commit the result")
        return

    path.write_text(content, encoding="utf-8")
