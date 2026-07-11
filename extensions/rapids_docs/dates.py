# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# SPDX-License-Identifier: Apache-2.0

"""Shared date parsing and formatting helpers."""

from datetime import datetime

from dateutil import parser as date_parser


def _date(value) -> datetime:
    if isinstance(value, datetime):
        return value
    if hasattr(value, "year") and hasattr(value, "month") and hasattr(value, "day"):
        return datetime(value.year, value.month, value.day)
    return date_parser.parse(str(value))


def _long_date(value) -> str:
    parsed = _date(value)
    return f"{parsed.strftime('%B')} {parsed.day}, {parsed.year}"


def _short_date(value) -> str:
    parsed = _date(value)
    return f"{parsed.strftime('%a, %b')} {parsed.day}, {parsed.year}"
