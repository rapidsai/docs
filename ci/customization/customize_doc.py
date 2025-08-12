# SPDX-FileCopyrightText: Copyright (c) 2023-2025, NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Script to customize doxygen/sphinx generated HTML for RAPIDS
"""

import re
import sys
import json
import os
from bs4 import BeautifulSoup
from copy import deepcopy

SCRIPT_TAG_ID = "rapids-selector-js"
PIXEL_SRC_TAG_ID = "rapids-selector-pixel-src"
PIXEL_INVOCATION_TAG_ID = "rapids-selector-pixel-invocation"
STYLE_TAG_ID = "rapids-selector-css"
FA_TAG_ID = "rapids-fa-tag"


def get_version_from_fp(*, filepath: str, versions_dict: dict):
    """
    Determines if the current HTML document is for legacy, stable, or nightly versions
    based on the file path
    """
    match = re.search(r"/(\d?\d\.\d\d)/", filepath)
    version_number_from_filepath = match.group(1)

    # take a map of the form {"stable": "YY.MM", ...} and flip to {"YY.MM": "stable"}
    for version_name, version_number in versions_dict.items():
        if version_number == version_number_from_filepath:
            return {"name": version_name, "number": version_number_from_filepath}

    # if we get here, the version number wasn't found
    raise ValueError(
        f"Filepath implies version '{version_number_from_filepath}', no matching entry in versions_dict: {versions_dict}"
    )


def get_lib_from_fp(*, filepath: str, lib_path_dict: dict) -> str:
    """
    Determines the current RAPIDS library based on the file path
    """

    for lib in lib_path_dict.keys():
        if re.search(f"(^{lib}/|/{lib}/)", filepath):
            return lib
    raise ValueError(f"Couldn't find valid library name in '{filepath}'.")


def create_home_container(soup):
    """
    Creates and returns a div with a Home button and icon in it
    """
    container = soup.new_tag("div", attrs={"class": "rapids-home-container"})
    home_btn = soup.new_tag("a", attrs={"class": "rapids-home-container__home-btn"})
    home_btn["href"] = "/api"
    home_btn.string = "Home"
    container.append(home_btn)
    return container


def add_font_awesome(soup):
    """
    Adds a font-awesome to the head of the HTML
    """
    fa_tag = soup.new_tag(
        "link",
        attrs={
            "href": "https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
            "rel": "stylesheet",
            "id": FA_TAG_ID,
        },
    )
    soup.head.append(fa_tag)


def create_version_options(
    *, project_name: str, filepath: str, lib_path_dict: dict, versions_dict: dict
):
    """
    Creates options for legacy/stable/nightly selector
    """
    options = []
    doc_version = get_version_from_fp(filepath=filepath, versions_dict=versions_dict)
    doc_is_extra_legacy = (  # extra legacy means the doc version is older then current legacy
        doc_version["name"] == "legacy"
        and versions_dict["legacy"] != doc_version["number"]
    )
    doc_is_extra_nightly = (  # extra nightly means the doc version is newer then current nightly
        doc_version["name"] == "nightly"
        and versions_dict["nightly"] != doc_version["number"]
    )
    for version_name, version_path in [
        (_, path) for _, path in lib_path_dict[project_name].items() if path is not None
    ]:
        if (doc_is_extra_legacy and version_name == "legacy") or (
            doc_is_extra_nightly and version_name == "nightly"
        ):
            version_number_str = doc_version["number"]
        else:
            version_number_str = versions_dict[version_name]
        is_selected = False
        option_href = version_path
        version_text = f"{version_name} ({version_number_str})"
        if version_name == doc_version["name"]:
            print(f"default version: {version_name}")
            is_selected = True
        options.append(
            {"selected": is_selected, "href": option_href, "text": version_text}
        )

    return options


def create_library_options(*, project_name: str, lib_path_dict: dict):
    """
    Creates options for library selector
    """
    options = []

    for lib, lib_versions in lib_path_dict.items():
        if lib_versions["stable"]:
            option_href = lib_versions["stable"]
        elif lib_versions["nightly"]:
            option_href = lib_versions["nightly"]
        elif lib_versions["legacy"]:
            option_href = lib_versions["legacy"]
        else:
            continue
        is_selected = False
        if lib == project_name:
            print(f"default lib: {lib}")
            is_selected = True
        options.append({"selected": is_selected, "href": option_href, "text": lib})

    return options


def create_selector(soup, options):
    """
    Creates a dropdown selector
    """
    container = soup.new_tag(
        "div",
        attrs={"class": ["rapids-selector__container", "rapids-selector--hidden"]},
    )
    selected = soup.new_tag("div", attrs={"class": "rapids-selector__selected"})
    selected.string = next(option["text"] for option in options if option["selected"])
    container.append(selected)
    drop_down_menu = soup.new_tag("div", attrs={"class": ["rapids-selector__menu"]})

    for option in options:
        option_classes = ["rapids-selector__menu-item"]
        if option["selected"]:
            option_classes.append("rapids-selector__menu-item--selected")
        option_el = soup.new_tag(
            "a", href=option["href"], attrs={"class": option_classes}
        )
        option_el.string = option["text"]
        drop_down_menu.append(option_el)

    container.append(drop_down_menu)
    return container


def create_script_tag(soup):
    """
    Creates and returns a script tag that points to custom.js
    """
    script_tag = soup.new_tag(
        "script", defer=None, id=SCRIPT_TAG_ID, src="/assets/js/custom.js"
    )
    return script_tag


def create_pixel_tags(soup):
    """
    Creates and returns the pixel script tags
    """

    head_tag = soup.new_tag(
        "script",
        id=PIXEL_SRC_TAG_ID,
        src="https://assets.adobedtm.com/5d4962a43b79/814eb6e9b4e1/launch-4bc07f1e0b0b.min.js",
    )
    body_tag = soup.new_tag(
        "script",
        type="text/javascript",
        id=PIXEL_INVOCATION_TAG_ID,
    )
    body_tag.string = "_satellite.pageBottom();"
    return [head_tag, body_tag]


def create_css_link_tag(soup):
    """
    Creates and returns a link tag that points to custom.css
    """
    script_tag = soup.new_tag(
        "link", id=STYLE_TAG_ID, rel="stylesheet", href="/assets/css/custom.css"
    )
    return script_tag


def delete_element(soup, selector):
    """
    Deletes element from soup object if it already exists
    """
    try:
        soup.select(f"{selector}")[0].extract()
    except Exception:
        pass


def delete_existing_elements(soup):
    """
    Deletes any existing page elements to prevent duplicates on the page
    """
    doxygen_title_area = "#titlearea > table"
    sphinx_home_btn = ".wy-side-nav-search .icon.icon-home"
    sphinx_doc_version = ".wy-side-nav-search .version"
    existing_jtd_container = "#rapids-jtd-container"
    existing_pydata_container = "#rapids-pydata-container"
    existing_doxygen_container = "#rapids-doxygen-container"

    for element in [
        existing_jtd_container,
        existing_pydata_container,
        existing_doxygen_container,
        sphinx_doc_version,
        sphinx_home_btn,
        doxygen_title_area,
        f"#{SCRIPT_TAG_ID}",
        f"#{STYLE_TAG_ID}",
        f"#{FA_TAG_ID}",
        f"#{PIXEL_SRC_TAG_ID}",
        f"#{PIXEL_INVOCATION_TAG_ID}",
    ]:
        delete_element(soup, element)


class UnsupportedThemeError(ValueError):
    """
    Custom exception indicating that a document uses a Sphinx theme this script
    either cannot identify or does not know how to modify.
    """

    pass


def get_theme_info(soup, *, filepath: str):
    """
    Determines what theme a given HTML file is using or exits if it's
    not able to be determined. Returns a string identifier and reference element
    that is used for inserting the library/version selectors to the doc.
    """
    # Sphinx Themes
    jtd_identifier = ".wy-side-nav-search"  # Just-the-docs theme
    pydata_identifier = ".bd-sidebar"  # Pydata theme

    # Doxygen
    doxygen_identifier = "#titlearea"

    if soup.select(jtd_identifier):
        return "jtd", soup.select(jtd_identifier)[0]

    if soup.select(doxygen_identifier):
        return "doxygen", soup.select(doxygen_identifier)[0]

    if soup.select(pydata_identifier):
        return "pydata", soup.select(pydata_identifier)[0]

    raise UnsupportedThemeError(
        f"Couldn't identify {filepath} as a supported theme type. Skipping file."
    )


def main(
    *,
    filepath: str,
    lib_path_dict: dict,
    project_name: str,
    versions_dict: dict[str, str],
) -> None:
    """
    Given the path to a documentation HTML file, this function will
    parse the file and add library/version selectors and a Home button
    """

    print(f"--- {filepath} ---")

    with open(filepath) as fp:
        soup = BeautifulSoup(fp, "html5lib")

    try:
        doc_type, reference_el = get_theme_info(soup, filepath=filepath)
    except UnsupportedThemeError as err:
        print(f"{str(err)}", file=sys.stderr)
        return

    # Delete any existing added/unnecessary elements
    delete_existing_elements(soup)

    # Add Font Awesome to Doxygen for icons
    if doc_type == "doxygen":
        add_font_awesome(soup)

    # Create new elements
    home_btn_container = create_home_container(soup)
    library_selector = create_selector(
        soup,
        create_library_options(
            project_name=project_name,
            lib_path_dict=lib_path_dict,
        ),
    )
    version_selector = create_selector(
        soup,
        create_version_options(
            project_name=project_name,
            filepath=filepath,
            lib_path_dict=lib_path_dict,
            versions_dict=versions_dict,
        ),
    )
    container = soup.new_tag("div", id=f"rapids-{doc_type}-container")
    script_tag = create_script_tag(soup)
    [pix_head_tag, pix_body_tag] = create_pixel_tags(soup)
    style_tab = create_css_link_tag(soup)

    # Append elements to container
    container.append(home_btn_container)
    container.append(library_selector)
    container.append(version_selector)

    # Insert new elements
    reference_el.insert(0, container)
    soup.body.append(script_tag)
    soup.body.append(pix_body_tag)
    soup.head.append(pix_head_tag)
    soup.head.append(style_tab)

    with open(filepath, "w") as fp:
        fp.write(soup.decode(formatter="html5"))


if __name__ == "__main__":
    MANIFEST_FILEPATH = sys.argv[1]
    PROJECT_TO_VERSIONS_PATH = sys.argv[2]
    LIB_MAP_PATH = os.path.join(os.path.dirname(__file__), "lib_map.json")

    # read in config files (doing this here so it only happens once)
    with open(LIB_MAP_PATH) as fp:
        LIB_PATH_DICT = json.load(fp)

    with open(PROJECT_TO_VERSIONS_PATH) as fp:
        PROJECT_TO_VERSIONS_DICT = json.load(fp)

    with open(MANIFEST_FILEPATH) as manifest_file:
        for line in manifest_file:
            filepath = line.strip()

            lib_path_dict = deepcopy(LIB_PATH_DICT)

            # determine project name (e.g. 'cudf')
            project_name = get_lib_from_fp(
                lib_path_dict=lib_path_dict,
                filepath=filepath,
            )

            main(
                filepath=filepath,
                lib_path_dict=lib_path_dict,
                project_name=project_name,
                versions_dict=deepcopy(PROJECT_TO_VERSIONS_DICT[project_name]),
            )
