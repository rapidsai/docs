#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTICES_DIR = ROOT / "_notices"
PARENTS = {
    "rdn": "RAPIDS Developer Notices",
    "rgn": "RAPIDS General Notices",
    "rsn": "RAPIDS Support Notices",
}


def next_id(notice_type):
    pattern = re.compile(rf"^{notice_type}(\d{{4}})\.md$")
    ids = [
        int(match.group(1))
        for path in NOTICES_DIR.glob(f"{notice_type}*.md")
        if (match := pattern.fullmatch(path.name))
    ]
    return max(ids, default=0) + 1


def main():
    parser = argparse.ArgumentParser(description="Create valid notice front matter.")
    parser.add_argument("--type", choices=sorted(PARENTS), required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--topic", required=True)
    parser.add_argument("--rapids-version", required=True)
    parser.add_argument("--author", default="RAPIDS Ops")
    args = parser.parse_args()

    notice_id = next_id(args.type)
    path = NOTICES_DIR / f"{args.type}{notice_id:04d}.md"
    today = date.today().isoformat()
    contents = f"""---
layout: notice
parent: {PARENTS[args.type]}
grand_parent: RAPIDS Notices
nav_exclude: true
notice_type: {args.type}
notice_id: {notice_id}
notice_pin: false
title: {json.dumps(args.title)}
notice_author: {json.dumps(args.author)}
notice_status: Proposal
notice_status_color: blue
notice_topic: {json.dumps(args.topic)}
notice_rapids_version: {json.dumps(args.rapids_version)}
notice_created: {today}
notice_updated: {today}
---

## Overview

TODO

## Impact

TODO
"""
    try:
        path.write_text(contents, encoding="utf-8")
    except OSError as error:
        print(f"Could not create notice: {error}", file=sys.stderr)
        return 1
    print(path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
