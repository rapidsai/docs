# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# SPDX-License-Identifier: Apache-2.0

"""Copy additional files into the built portal."""

import shutil
from pathlib import Path

from .data import _source_dir


def _copy_portal_files(app, exception) -> None:
    """Copy trees whose root paths are part of the published site interface."""
    if exception is not None or app.builder.name not in {"html", "dirhtml"}:
        return
    source_dir = _source_dir(app)
    output_dir = Path(app.outdir)
    for directory in ("assets", "licenses"):
        shutil.copytree(
            source_dir / directory,
            output_dir / directory,
            dirs_exist_ok=True,
        )
    for filename in ("LICENSE", "SECURITY.md"):
        shutil.copy2(source_dir / filename, output_dir / filename)

    # ``dirhtml`` correctly creates pretty URLs everywhere except the hosting
    # platform's required top-level error document. sphinx-notfound-page has
    # already rewritten this page's resource and navigation links as absolute.
    shutil.copy2(output_dir / "404" / "index.html", output_dir / "404.html")
