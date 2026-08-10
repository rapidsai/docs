# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Render the API documentation listings."""


def _version_label(project: dict, version_name: str, releases: dict) -> str:
    override = project.get("version-overrides", {}).get(version_name)
    if override:
        return str(override)
    version_key = "ucxx_version" if "ucxx" in project["path"].lower() else "version"
    return str(releases[version_name][version_key])


def _documentation_url(project: dict, version_name: str, version: str) -> str:
    first_docs_nvidia_com_release = project["first_docs_nvidia_com_release"]
    if first_docs_nvidia_com_release and tuple(map(int, version.split("."))) >= tuple(
        map(int, first_docs_nvidia_com_release.split("."))
    ):
        return f"https://docs.nvidia.com/{project['path']}/{version}/"
    return f"https://docs.rapids.ai/api/{project['path']}/{version_name}/"


def _api_docs(data: dict, section: str) -> str:
    cards = []
    for project in data["docs"][section].values():
        if project.get("hidden", False):
            continue
        versions = []
        external_docs_url = project.get("external_docs_url")
        if not external_docs_url:
            for name in ("nightly", "stable", "legacy"):
                if project["versions"].get(name) == 1:
                    label = _version_label(project, name, data["releases"])
                    url = _documentation_url(project, name, label)
                    versions.append(f"[{name.title()} ({label})]({url})")
        links = []
        if project.get("cllink"):
            links.append(f"[Changelog]({project['cllink']})")
        links.append(f"[GitHub]({project['ghlink']})")
        footer = []
        if external_docs_url:
            footer.extend([f"[Documentation]({external_docs_url})", ""])
        elif versions:
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
