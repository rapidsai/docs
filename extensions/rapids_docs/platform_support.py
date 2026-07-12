# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# SPDX-License-Identifier: Apache-2.0

"""Render the platform support page."""


def _compute_capability(cuda: dict) -> str:
    capabilities = []
    for capability in cuda["compute_capability"]:
        sms = capability["sm"]
        if not isinstance(sms, list):
            sms = [sms]
        capabilities.append(f"{capability['name']} ({', '.join(map(str, sms))})")
    return ", ".join(capabilities) + " or newer"


def _platform_support(data: dict) -> str:
    releases = data["platform_support"]["releases"]
    links = ", ".join(
        f"[{release['version']}{' (nightly)' if release.get('nightly') else ''}]"
        f"(#rapids-{str(release['version']).replace('.', '')})"
        for release in releases
    )
    sections = [f"**Releases:** {links}"]
    for release in releases:
        title = f"## RAPIDS {release['version']}"
        if release.get("nightly"):
            title += " (nightly)"
        cuda_headers = [f"CUDA {cuda['major']}" for cuda in release["cuda"]]
        cuda_rows = [
            (
                "Toolkit",
                [
                    f"{cuda['toolkit_min']}"
                    + (
                        f" - {cuda['toolkit_max']}"
                        if cuda["toolkit_min"] != cuda["toolkit_max"]
                        else ""
                    )
                    for cuda in release["cuda"]
                ],
            ),
            ("Driver", [f"{cuda['driver_min']}+" for cuda in release["cuda"]]),
            ("Compute Capability", [_compute_capability(cuda) for cuda in release["cuda"]]),
        ]
        table = [
            "| | " + " | ".join(cuda_headers) + " |",
            "|:--|" + "|".join(":--" for _ in cuda_headers) + "|",
        ]
        table.extend(f"| **{name}** | " + " | ".join(values) + " |" for name, values in cuda_rows)
        sections.append(
            "\n".join(
                [
                    "---",
                    "",
                    title,
                    "",
                    '### <i class="fas fa-desktop" aria-hidden="true"></i> Operating Systems',
                    "",
                    f'- <i class="fab fa-linux" aria-hidden="true"></i> '
                    f"**Linux (glibc {release['glibc_min']}+):** {', '.join(release['cpu_arch'])} "
                    f"(tested on {', '.join(release['os_support'])})",
                    '- <i class="fab fa-windows" aria-hidden="true"></i> '
                    "**Windows:** Supported via [WSL](/install/#wsl2) with a compatible Linux distribution",
                    "",
                    '### <i class="fab fa-python" aria-hidden="true"></i> Python',
                    "",
                    f"**{', '.join(release['python'])}**",
                    "",
                    '### <i class="fas fa-microchip" aria-hidden="true"></i> CUDA',
                    "",
                    *table,
                    "",
                    '### <i class="fas fa-hammer" aria-hidden="true"></i> Source Builds',
                    "",
                    "| Dependency | Version |",
                    "|:--|:--|",
                    f"| **GCC** | {release['source_build']['gcc']} |",
                    f"| **CCCL** | {release['source_build']['cccl']} |",
                    f"| **nvCOMP** | {release['source_build']['nvcomp']} |",
                ]
            )
        )
    return "\n\n".join(sections)
