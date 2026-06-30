#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import re
import sys
from datetime import date
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
NOTICES_DIR = ROOT / "_notices"
FILENAME = re.compile(r"^(rdn|rgn|rsn)(\d{4})\.md$")
STATUS_COLORS = {
    "Proposal": "blue",
    "Completed": "green",
    "Review": "purple",
    "In Progress": "yellow",
    "Closed": "red",
}


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        raise ValueError("must start with YAML front matter")
    value = yaml.safe_load(parts[1])
    if not isinstance(value, dict):
        raise ValueError("front matter must be a mapping")
    return value


def notice_date(value, field):
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError:
            match = re.fullmatch(r"(\d{4})-(\d{1,2})-(\d{1,2})", value)
            if match:
                return date(*(int(part) for part in match.groups()))
    raise ValueError(f"{field} must be a valid calendar date")


def main():
    errors = []
    identifiers = {notice_type: [] for notice_type in ("rdn", "rgn", "rsn")}
    for path in sorted(NOTICES_DIR.glob("*.md")):
        match = FILENAME.fullmatch(path.name)
        if not match:
            errors.append(f"{path.name}: filename must use TYPE0000.md")
            continue
        filename_type, filename_id = match.groups()
        expected_id = int(filename_id)
        identifiers[filename_type].append(expected_id)
        try:
            notice = front_matter(path)
            if notice.get("layout") != "notice":
                raise ValueError("layout must be notice")
            if notice.get("notice_type") != filename_type:
                raise ValueError("notice_type must match the filename")
            if notice.get("notice_id") != expected_id:
                raise ValueError("notice_id must match the filename number")
            if not isinstance(notice.get("notice_pin"), bool):
                raise ValueError("notice_pin must be a boolean")
            status = notice.get("notice_status")
            expected_color = STATUS_COLORS.get(status)
            if expected_color is None:
                raise ValueError(f"unknown notice_status {status!r}")
            if notice.get("notice_status_color") != expected_color:
                raise ValueError(
                    f"{status} notices must use status color {expected_color}"
                )
            created = notice_date(notice.get("notice_created"), "notice_created")
            updated = notice_date(notice.get("notice_updated"), "notice_updated")
            if updated < created:
                raise ValueError("notice_updated must not precede notice_created")
            for field in (
                "parent",
                "grand_parent",
                "title",
                "notice_author",
                "notice_topic",
                "notice_rapids_version",
            ):
                if not isinstance(notice.get(field), str) or not notice[field].strip():
                    raise ValueError(f"{field} must be a non-empty string")
        except (OSError, yaml.YAMLError, ValueError) as error:
            errors.append(f"{path.name}: {error}")

    for notice_type, ids in identifiers.items():
        expected = list(range(1, max(ids, default=0) + 1))
        if ids != expected:
            errors.append(f"{notice_type} notice IDs must be contiguous and unique")

    if errors:
        print("Notice validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {sum(map(len, identifiers.values()))} notices.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
