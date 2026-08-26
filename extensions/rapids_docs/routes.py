# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Resolve portal and API documentation URLs for each hosting target."""

from urllib.parse import urljoin, urlsplit, urlunsplit


def _version_label(project: dict, version_name: str, releases: dict) -> str:
    override = project.get("version-overrides", {}).get(version_name)
    if override:
        return str(override)
    version_key = "ucxx_version" if "ucxx" in project["path"].lower() else "version"
    return str(releases[version_name][version_key])


def _version_tuple(version: str) -> tuple[int, ...]:
    return tuple(map(int, version.split(".")))


def _with_suffix(base_url: str, suffix: str) -> str:
    return urljoin(base_url.rstrip("/") + "/", suffix.lstrip("/"))


def _documentation_url(
    project: dict,
    version_name: str,
    version: str,
    suffix: str = "",
) -> str:
    if external_docs_url := project.get("external_docs_url"):
        return _with_suffix(external_docs_url, suffix)

    first_nvidia_release = project["first_docs_nvidia_com_release"]
    if first_nvidia_release and _version_tuple(version) >= _version_tuple(first_nvidia_release):
        base_url = f"https://docs.nvidia.com/{project['path']}/{version}/"
    else:
        base_url = f"https://docs.rapids.ai/api/{project['path']}/{version_name}/"
    return _with_suffix(base_url, suffix)


def _project_for_path(data: dict, project_path: str) -> dict | None:
    for section in ("apis", "libs", "inactive-projects"):
        for project in data["docs"][section].values():
            if project["path"].lower() == project_path.lower():
                return project
    return None


def _api_documentation_url(url: str, data: dict | None) -> str | None:
    if data is None:
        return None

    parsed = urlsplit(url)
    parts = parsed.path.strip("/").split("/")
    if len(parts) < 3 or parts[0] != "api" or parts[2] not in {"legacy", "stable", "nightly"}:
        return None

    project = _project_for_path(data, parts[1])
    if project is None or not project["versions"].get(parts[2]):
        return None

    version_name = parts[2]
    version = _version_label(project, version_name, data["releases"])
    suffix = "/".join(parts[3:])
    if suffix and parsed.path.endswith("/"):
        suffix += "/"
    destination = urlsplit(_documentation_url(project, version_name, version, suffix))
    return urlunsplit(
        (
            destination.scheme,
            destination.netloc,
            destination.path,
            parsed.query,
            parsed.fragment,
        )
    )


def _site_url(base_url: str, url: str, data: dict | None = None) -> str:
    if not url.startswith("/") or url.startswith("//"):
        return url
    return _api_documentation_url(url, data) or _with_suffix(base_url, url)
