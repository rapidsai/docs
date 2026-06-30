#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import argparse
import sys
from datetime import date, timedelta
from pathlib import Path

from data_utils import DataError, json_text, load_yaml, version_tuple, write_or_check


ROOT = Path(__file__).resolve().parents[1]
CALENDAR_PATH = ROOT / "_data" / "release_calendar.yml"
PLATFORM_PATH = ROOT / "_data" / "platform_support.yml"
RELEASES_PATH = ROOT / "_data" / "releases.json"
HISTORY_PATH = ROOT / "_data" / "previous_releases.json"

CHANNELS = ("legacy", "stable", "nightly", "next_nightly")
PHASES = {
    "development": ("Development", None),
    "burn_down": ("Burn Down", "burn-down"),
    "code_freeze": ("Code Freeze/Testing", "code-freeze"),
    "release": ("Release", "releasing"),
}
COHORTS = {"all", "early", "remaining"}
PHASE_ORDER = {name: index for index, name in enumerate(PHASES)}
COHORT_ORDER = {"all": 0, "early": 1, "remaining": 2}


def parse_iso_date(value, field, errors):
    if not isinstance(value, str):
        errors.append(f"{field} must be a quoted ISO date")
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        errors.append(f"{field} must use YYYY-MM-DD: {value!r}")
        return None


def validate_schedule(version, release, cohort_sets, errors):
    phases = release.get("phases")
    if phases is None:
        return parse_iso_date(
            release.get("released_on"), f"release {version}.released_on", errors
        )
    if "released_on" in release:
        errors.append(
            f"release {version}.released_on is derived from its release phase"
        )
    if not isinstance(phases, list) or not phases:
        errors.append(f"release {version}.phases must be a non-empty list")
        return None

    parsed_phases = []
    phase_keys = []
    uses_split_cohorts = False
    for index, phase in enumerate(phases):
        field = f"release {version}.phases[{index}]"
        if not isinstance(phase, dict):
            errors.append(f"{field} must be a mapping")
            continue
        kind = phase.get("phase")
        cohort = phase.get("cohort")
        if kind not in PHASES:
            errors.append(f"{field}.phase must be one of {sorted(PHASES)}")
        if cohort not in COHORTS:
            errors.append(f"{field}.cohort must be one of {sorted(COHORTS)}")
        if kind in PHASES and cohort in COHORTS:
            phase_keys.append((kind, cohort))
        uses_split_cohorts |= cohort in {"early", "remaining"}
        start = parse_iso_date(phase.get("start"), f"{field}.start", errors)
        end = parse_iso_date(phase.get("end"), f"{field}.end", errors)
        if start is not None and end is not None:
            if start > end:
                errors.append(f"{field}.start must not be after its end")
            parsed_phases.append((kind, cohort, start, end))

    expected_order = sorted(
        phase_keys, key=lambda item: (PHASE_ORDER[item[0]], COHORT_ORDER[item[1]])
    )
    if phase_keys != expected_order:
        errors.append(f"release {version}.phases must be ordered by phase and cohort")
    if len(phase_keys) != len(set(phase_keys)):
        errors.append(f"release {version}.phases contains a duplicate phase/cohort")

    cohort_set = release.get("cohort_set")
    if uses_split_cohorts:
        if cohort_set not in cohort_sets:
            errors.append(
                f"release {version}.cohort_set must reference a defined cohort set"
            )
    elif cohort_set is not None:
        errors.append(
            f"release {version}.cohort_set is only valid for split-cohort schedules"
        )

    release_phases = [phase for phase in parsed_phases if phase[0] == "release"]
    if len(release_phases) != 1 or release_phases[0][1] != "all":
        errors.append(f"release {version} must have one all-cohort release phase")
        return None

    if release.get("schedule_exception"):
        return release_phases[0][3]

    non_release = [phase for phase in parsed_phases if phase[0] != "release"]
    tracks = ("early", "remaining") if uses_split_cohorts else ("all",)
    for track in tracks:
        track_phases = sorted(
            (phase for phase in non_release if phase[1] in {"all", track}),
            key=lambda phase: phase[2],
        )
        if [phase[0] for phase in track_phases] != [
            "development",
            "burn_down",
            "code_freeze",
        ]:
            errors.append(
                f"release {version} {track} schedule must contain development, "
                "burn_down, and code_freeze exactly once"
            )
        for previous, current in zip(track_phases, track_phases[1:]):
            if current[2] != previous[3] + timedelta(days=1):
                errors.append(
                    f"release {version} {track} schedule is not contiguous between "
                    f"{previous[0]} and {current[0]}"
                )

    if non_release:
        latest_end = max(phase[3] for phase in non_release)
        if release_phases[0][2] != latest_end + timedelta(days=1):
            errors.append(
                f"release {version} release phase must start after the prior phases"
            )
    return release_phases[0][3]


def validate_calendar(calendar, platform_support):
    errors = []
    if not isinstance(calendar, dict):
        raise DataError("release_calendar.yml must contain a mapping")

    channels = calendar.get("channels")
    releases = calendar.get("releases")
    cohort_sets = calendar.get("cohort_sets")
    labels = calendar.get("project_labels")
    if not isinstance(channels, dict) or tuple(channels) != CHANNELS:
        errors.append(f"channels must appear in this order: {', '.join(CHANNELS)}")
        channels = {}
    if not isinstance(releases, dict) or not releases:
        errors.append("releases must be a non-empty mapping")
        releases = {}
    if not isinstance(cohort_sets, dict):
        errors.append("cohort_sets must be a mapping")
        cohort_sets = {}
    if not isinstance(labels, dict):
        errors.append("project_labels must be a mapping")
        labels = {}

    channel_versions = []
    for channel in CHANNELS:
        version = channels.get(channel)
        try:
            parsed = version_tuple(version, f"channels.{channel}")
            channel_versions.append(parsed)
        except DataError as error:
            errors.append(str(error))
        if version not in releases:
            errors.append(f"channels.{channel} references missing release {version!r}")
    if len(channel_versions) == len(CHANNELS):
        if channel_versions != sorted(set(channel_versions)):
            errors.append("channel releases must be distinct and oldest-to-newest")

    for set_name, cohort_set in cohort_sets.items():
        if not isinstance(cohort_set, dict) or not cohort_set.get("early"):
            errors.append(f"cohort set {set_name} must define a non-empty early list")
            continue
        for project in cohort_set["early"]:
            if project not in labels:
                errors.append(
                    f"cohort set {set_name} references project without a label: {project}"
                )

    parsed_release_versions = []
    release_dates = []
    ucxx_versions = []
    for version, release in releases.items():
        try:
            parsed_version = version_tuple(version, f"release {version}")
            parsed_release_versions.append(parsed_version)
        except DataError as error:
            errors.append(str(error))
            parsed_version = None
        if not isinstance(release, dict):
            errors.append(f"release {version} must be a mapping")
            continue
        released_on = validate_schedule(version, release, cohort_sets, errors)
        if parsed_version is not None and released_on is not None:
            release_dates.append((parsed_version, released_on))
        if "ucxx_version" in release:
            try:
                ucxx_versions.append(
                    (version_tuple(version), version_tuple(release["ucxx_version"]))
                )
            except DataError as error:
                errors.append(str(error))

    if parsed_release_versions != sorted(parsed_release_versions, reverse=True):
        errors.append("release records must be ordered newest-to-oldest")
    ordered_dates = [released_on for _, released_on in sorted(release_dates)]
    if ordered_dates != sorted(set(ordered_dates)):
        errors.append("release dates must be unique and increase with release versions")
    ordered_ucxx = [value for _, value in sorted(ucxx_versions)]
    if len(ordered_ucxx) != len(set(ordered_ucxx)):
        errors.append("UCXX release versions must be unique")
    if ordered_ucxx != sorted(ordered_ucxx):
        errors.append("UCXX release versions must increase with RAPIDS releases")

    platform_releases = platform_support.get("releases", [])
    platform_by_version = {
        item.get("version"): item
        for item in platform_releases
        if isinstance(item, dict) and isinstance(item.get("version"), str)
    }
    for channel in ("stable", "nightly"):
        version = channels.get(channel)
        if version not in platform_by_version:
            errors.append(
                f"{channel} release {version} is missing from platform_support.yml"
            )
    nightly_version = channels.get("nightly")
    marked_nightly = [
        item.get("version")
        for item in platform_releases
        if isinstance(item, dict) and item.get("nightly") is True
    ]
    if marked_nightly != [nightly_version]:
        errors.append(
            "exactly the nightly channel must have nightly: true in "
            f"platform_support.yml; expected {[nightly_version]}, found {marked_nightly}"
        )

    if errors:
        raise DataError("Release data validation failed:\n- " + "\n- ".join(errors))
    return channels, releases, cohort_sets, labels


def projected_phases(release, cohort_sets, labels):
    cohort_set = cohort_sets.get(release.get("cohort_set"), {})
    early_label = "/".join(labels[project] for project in cohort_set.get("early", []))
    projected = []
    for phase in release.get("phases", []):
        name, anchor = PHASES[phase["phase"]]
        cohort = phase["cohort"]
        cohort_label = ""
        if cohort == "early":
            cohort_label = early_label
        elif cohort == "remaining":
            cohort_label = "others"
        item = {
            "name": name,
            "cohort": cohort,
            "cohort_label": cohort_label,
            "start": phase["start"],
            "end": phase["end"],
        }
        if anchor:
            item["process_anchor"] = anchor
        projected.append(item)
    return projected


def canonical_release_date(release):
    if release.get("phases"):
        return next(
            phase["end"] for phase in release["phases"] if phase["phase"] == "release"
        )
    return release["released_on"]


def project_release(version, release, cohort_sets, labels):
    result = {"version": version}
    if "ucxx_version" in release:
        result["ucxx_version"] = release["ucxx_version"]
    if release.get("phases"):
        result["phases"] = projected_phases(release, cohort_sets, labels)
    else:
        result["date"] = release["released_on"]
    return result


def generate(calendar, platform_support):
    channels, releases, cohort_sets, labels = validate_calendar(
        calendar, platform_support
    )
    active = {}
    for channel in CHANNELS:
        version = channels[channel]
        release = releases[version]
        if channel in {"legacy", "stable"}:
            item = {"version": version}
            if "ucxx_version" in release:
                item["ucxx_version"] = release["ucxx_version"]
            item["date"] = canonical_release_date(release)
        else:
            item = project_release(version, release, cohort_sets, labels)
        active[channel] = item

    stable_version = version_tuple(channels["stable"])
    history = [
        project_release(version, release, cohort_sets, labels)
        for version, release in releases.items()
        if version_tuple(version) <= stable_version
    ]
    return active, history


def main():
    parser = argparse.ArgumentParser(
        description="Generate release channel and history projections."
    )
    parser.add_argument(
        "--check", action="store_true", help="Fail instead of updating stale outputs."
    )
    args = parser.parse_args()

    try:
        active, history = generate(load_yaml(CALENDAR_PATH), load_yaml(PLATFORM_PATH))
        write_or_check(RELEASES_PATH, json_text(active), args.check)
        write_or_check(HISTORY_PATH, json_text(history), args.check)
    except (DataError, OSError) as error:
        print(error, file=sys.stderr)
        return 1

    action = "validated" if args.check else "generated"
    print(f"Release data {action} successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
