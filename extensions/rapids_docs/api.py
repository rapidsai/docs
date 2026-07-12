# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# SPDX-License-Identifier: Apache-2.0

"""Render the API documentation listings."""


def _version_label(project: dict, version_name: str, releases: dict) -> str:
    override = project.get("version-overrides", {}).get(version_name)
    if override:
        return str(override)
    version_key = "ucxx_version" if "ucxx" in project["path"].lower() else "version"
    return str(releases[version_name][version_key])


def _api_docs(data: dict, section: str) -> str:
    cards = []
    for project in data["docs"][section].values():
        if project.get("hidden", False):
            continue
        versions = []
        for name in ("nightly", "stable", "legacy"):
            if project["versions"].get(name) == 1:
                label = _version_label(project, name, data["releases"])
                versions.append(f"[{name.title()} ({label})](/api/{project['path']}/{name}/)")
        links = []
        if project.get("cllink"):
            links.append(f"[Changelog]({project['cllink']})")
        links.append(f"[GitHub]({project['ghlink']})")
        footer = []
        if versions:
            footer.extend(["**Documentation:** " + " · ".join(versions), ""])
        footer.append("**Resources:** " + " · ".join(links))
        cards.append(
            "\n".join(
                [
                    f":::{{grid-item-card}} {project['name']}",
                    ":class-card: rapids-api-card",
                    ":class-title: rapids-api-card-title",
                    ":class-footer: rapids-api-card-footer",
                    "",
                    project["desc"],
                    "",
                    "+++",
                    *footer,
                    ":::",
                ]
            )
        )
    return "\n".join(
        [
            "::::{grid} 1 1 1 1",
            ":gutter: 2",
            ":class-container: rapids-api-grid",
            "",
            "\n\n".join(cards),
            "::::",
        ]
    )
