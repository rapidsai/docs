# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# SPDX-License-Identifier: Apache-2.0

"""Render current and historical release schedules."""

from .dates import _short_date


def _schedule_table(release: dict) -> str:
    rows = [
        ("Development", release["dev"]),
        (
            "[Burn Down](/releases/process/#burn-down) (cuDF/RMM/rapids-cmake/raft/dask-cuda/KvikIO/ucxx/rapidsmpf/nvForest)",
            release["cudf_burndown"],
        ),
        ("[Burn Down](/releases/process/#burn-down) (others)", release["other_burndown"]),
        (
            "[Code Freeze/Testing](/releases/process/#code-freeze) (cuDF/RMM/rapids-cmake/raft/dask-cuda/KvikIO/ucxx/rapidsmpf/nvForest)",
            release["cudf_codefreeze"],
        ),
        (
            "[Code Freeze/Testing](/releases/process/#code-freeze) (others)",
            release["other_codefreeze"],
        ),
        ("[Release](/releases/process/#releasing)", release["release"]),
    ]
    output = ["| Phase | Start | End | Duration |", "|:--|:--|:--|:--|"]
    output.extend(
        f"| {name} | {_short_date(values['start'])} | {_short_date(values['end'])} | {values['days']} days |"
        for name, values in rows
    )
    return "\n".join(output)


def _current_schedules(data: dict) -> str:
    releases = data["releases"]
    return "\n\n".join(
        [
            f"## Release v{releases['nightly']['version']} Schedule",
            "**NOTE:** *Dates are subject to change at any time. Completed release schedules are posted "
            "[here](/releases/schedule/).*",
            _schedule_table(releases["nightly"]),
            f"## *PROPOSED* Release v{releases['next_nightly']['version']} Schedule",
            _schedule_table(releases["next_nightly"]),
        ]
    )


def _old_project_group(version: str) -> str:
    group = "cuDF/RMM"
    if version >= "23.06":
        group += "/rapids-cmake/"
        if version <= "24.12":
            group += "cugraph-ops/"
        group += "raft"
    return group


def _previous_schedules(data: dict) -> str:
    sections = []
    for release in data["previous_releases"]:
        output = [f"### Release v{release['version']} Schedule", ""]
        if release.get("dev"):
            rows = [("Development", release["dev"])]
            group_suffix = (
                " (cuDF/RMM/rapids-cmake/raft/dask-cuda/KvikIO/ucxx/rapidsmpf)"
                if release.get("other_burndown")
                else ""
            )
            rows.append(
                (
                    f"[Burn Down](/releases/process/#burn-down){group_suffix}",
                    release.get("cudf_burndown") or release["burndown"],
                )
            )
            if release.get("other_burndown"):
                rows.append(
                    (
                        "[Burn Down](/releases/process/#burn-down) (others)",
                        release["other_burndown"],
                    )
                )
            if release.get("cudf_codefreeze"):
                rows.append(
                    (
                        f"[Code Freeze/Testing](/releases/process/#code-freeze){group_suffix}",
                        release["cudf_codefreeze"],
                    )
                )
                rows.append(
                    (
                        "[Code Freeze/Testing](/releases/process/#code-freeze) (others)",
                        release["other_codefreeze"],
                    )
                )
            else:
                rows.append(
                    ("[Code Freeze/Testing](/releases/process/#code-freeze)", release["codefreeze"])
                )
            rows.append(("[Release](/releases/process/#releasing)", release["release"]))
            output.extend(["| Phase | Start | End | Duration |", "|:--|:--|:--|:--|"])
            output.extend(
                f"| {name} | {_short_date(values['start'])} | {_short_date(values['end'])} | {values['days']} days |"
                for name, values in rows
            )
        elif release.get("date"):
            output.extend(
                ["| Phase | Date |", "|:--|:--|", f"| Release | {_short_date(release['date'])} |"]
            )
        else:
            group = _old_project_group(release["version"])
            rows = [
                (f"Development ({group})", release["cudf_dev"]),
                ("Development (others)", release["other_dev"]),
                (f"[Burn Down](/releases/process/#burn-down) ({group})", release["cudf_burndown"]),
                ("[Burn Down](/releases/process/#burn-down) (others)", release["other_burndown"]),
                (
                    f"[Code Freeze/Testing](/releases/process/#code-freeze) ({group})",
                    release["cudf_codefreeze"],
                ),
                (
                    "[Code Freeze/Testing](/releases/process/#code-freeze) (others)",
                    release["other_codefreeze"],
                ),
                ("[Release](/releases/process/#releasing)", release["release"]),
            ]
            output.extend(["| Phase | Start | End | Duration |", "|:--|:--|:--|:--|"])
            output.extend(
                f"| {name} | {_short_date(values['start'])} | {_short_date(values['end'])} | {values['days']} days |"
                for name, values in rows
            )
        sections.append("\n".join(output))
    return "\n\n".join(sections)
