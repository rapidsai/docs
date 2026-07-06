#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
# SPDX-License-Identifier: Apache-2.0

"""Compare Sphinx routes, headings, and normalized content with Jekyll."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

from bs4 import BeautifulSoup

SOURCE_COMMIT = "b6afa0cbf4ddfc4c0a21f7c79b18631f214fd759"
MINIMUM_CONTENT_COVERAGE = 0.90
HEADING_RENAMES = {
    "/install/": {"jupyterlab.": "jupyterlab"},
}
HEADING_OMISSIONS = {
    "/visualization/": {"note: web hosted vs local hosted chart interaction"},
}


def routes(root: Path) -> set[str]:
    output = set()
    for path in root.rglob("index.html"):
        relative = path.relative_to(root)
        if relative.parts[0] == "assets":
            continue
        route = "/" + "/".join(relative.parts[:-1])
        output.add(route.rstrip("/") + "/")
    return output


def _page_path(root: Path, route: str) -> Path:
    if route == "/":
        return root / "index.html"
    return root / route.strip("/") / "index.html"


def _normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).lower()
    value = value.replace("`", "").replace("\u2019", "'").replace("\u2018", "'")
    value = re.sub(r"\s+#$", "", value)
    return re.sub(r"\s+", " ", value).strip()


def _page_data(path: Path, *, jekyll: bool) -> dict:
    soup = BeautifulSoup(path.read_text(errors="ignore"), "html.parser")
    main = soup.select_one("#main-content" if jekyll else "article.bd-article") or soup

    if jekyll:
        # just-the-docs appends child navigation after the authored content.
        for heading in list(main.select("h1,h2,h3,h4,h5,h6")):
            if _normalize(heading.get_text(" ", strip=True)) == "table of contents":
                for following in list(heading.find_all_next()):
                    following.decompose()
                heading.decompose()

    headings = [
        _normalize(heading.get_text(" ", strip=True))
        for heading in main.select("h1,h2,h3,h4,h5,h6")
    ]
    for element in main.select("script,style,nav,.toc,.headerlink"):
        element.decompose()
    text = main.get_text(" ", strip=True)
    # The Jekyll visualization includes contain malformed en-dash HTML comment
    # delimiters. Browsers display those license comments as text, while MyST
    # correctly preserves them as non-visible HTML comments.
    text = re.sub(
        r"<![–-]\s*SPDX-FileCopyrightText:.*?SPDX-License-Identifier:\s*Apache-2\.0\s*[–-]>",
        " ",
        text,
        flags=re.IGNORECASE,
    )
    text = _normalize(text)
    words = Counter(re.findall(r"[a-z0-9]+", text))
    return {"headings": headings, "words": dict(sorted(words.items()))}


def _write_manifest(jekyll_site: Path, output: Path) -> None:
    pages = {
        route: _page_data(_page_path(jekyll_site, route), jekyll=True)
        for route in sorted(routes(jekyll_site))
    }
    manifest = {"source_commit": SOURCE_COMMIT, "pages": pages}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(f"Recorded {len(pages)} Jekyll pages from {SOURCE_COMMIT}")


def _compare(manifest_path: Path, sphinx_site: Path) -> None:
    manifest = json.loads(manifest_path.read_text())
    if manifest["source_commit"] != SOURCE_COMMIT:
        raise SystemExit("Baseline manifest has an unexpected source commit")

    failures = []
    coverages = []
    for route, expected in manifest["pages"].items():
        path = _page_path(sphinx_site, route)
        if not path.exists():
            failures.append(f"{route}: route is missing")
            continue

        actual = _page_data(path, jekyll=False)
        missing_headings = [
            heading
            for heading in expected["headings"]
            if heading not in HEADING_OMISSIONS.get(route, set())
            if HEADING_RENAMES.get(route, {}).get(heading, heading) not in actual["headings"]
        ]
        if missing_headings:
            failures.append(f"{route}: missing headings: {', '.join(missing_headings)}")

        expected_words = Counter(expected["words"])
        actual_words = Counter(actual["words"])
        coverage = sum((expected_words & actual_words).values()) / sum(expected_words.values())
        coverages.append((coverage, route))
        if coverage < MINIMUM_CONTENT_COVERAGE:
            failures.append(
                f"{route}: normalized content coverage is {coverage:.1%}, "
                f"below {MINIMUM_CONTENT_COVERAGE:.0%}"
            )

    if failures:
        raise SystemExit("Jekyll parity validation failed:\n- " + "\n- ".join(failures))

    minimum, minimum_route = min(coverages)
    print(
        f"Validated {len(manifest['pages'])} Jekyll routes and headings; "
        f"minimum normalized content coverage is {minimum:.1%} ({minimum_route})"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("baseline", type=Path)
    parser.add_argument("sphinx", type=Path)
    parser.add_argument(
        "--write",
        action="store_true",
        help="write a baseline manifest from a Jekyll site instead of comparing",
    )
    args = parser.parse_args()

    if args.write:
        _write_manifest(args.baseline, args.sphinx)
    else:
        _compare(args.baseline, args.sphinx)


if __name__ == "__main__":
    main()
