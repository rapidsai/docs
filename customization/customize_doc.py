"""
Script to customize doxygen/sphinx generated HTML for RAPIDS
"""
import re
import sys
import json
import os
from bs4 import BeautifulSoup

FILEPATH = sys.argv[1]
NIGHTLY_VERSION = int(sys.argv[2])

LIB_MAP_PATH = os.path.join(os.path.dirname(__file__), "lib_map.json")

VERSIONS_DICT = {
    "nightly": NIGHTLY_VERSION,
    "stable": NIGHTLY_VERSION - 1,
    "legacy": NIGHTLY_VERSION - 2,
}
with open(LIB_MAP_PATH) as fp:
    LIB_PATH_DICT = json.load(fp)

SCRIPT_TAG_ID = "rapids-selector-js"
STYLE_TAG_ID = "rapids-selector-css"
FA_TAG_ID = "rapids-fa-tag"


def get_version_from_fp():
    """
    Determines if the current HTML document is for legacy, stable, or nightly versions
    based on the file path
    """
    match = re.search(r"0.\d{1,3}", FILEPATH)
    version_number = int(match[0].split(".")[1])
    version_name = "stable"
    if version_number > VERSIONS_DICT["stable"]:
        version_name = "nightly"
    if version_number < VERSIONS_DICT["stable"]:
        version_name = "legacy"
    return {"name": version_name, "number": version_number}


def get_lib_from_fp():
    """
    Determines the current RAPIDS library based on the file path
    """

    for lib in LIB_PATH_DICT.keys():
        if re.search(f"(^{lib}/|/{lib}/)", FILEPATH):
            return lib
    raise Exception(f"Couldn't find valid library name in {FILEPATH}.")


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


def create_version_options():
    """
    Creates options for legacy/stable/nightly selector
    """
    options = []
    doc_version = get_version_from_fp()
    doc_lib = get_lib_from_fp()
    doc_is_extra_legacy = (  # extra legacy means the doc version is older then current legacy
        doc_version["name"] == "legacy"
        and VERSIONS_DICT["legacy"] != doc_version["number"]
    )
    for version_name, version_path in [
        (_, path) for _, path in LIB_PATH_DICT[doc_lib].items() if path is not None
    ]:
        if doc_is_extra_legacy and version_name == "legacy":
            version_number = doc_version["number"]
        else:
            version_number = VERSIONS_DICT[version_name]
        is_selected = False
        option_href = version_path
        version_text = f"{version_name} (0.{str(version_number)})"
        if version_name == doc_version["name"]:
            print(f"default version: {version_name}")
            is_selected = True
        options.append(
            {"selected": is_selected, "href": option_href, "text": version_text}
        )

    return options


def create_library_options():
    """
    Creates options for library selector
    """
    doc_lib = get_lib_from_fp()
    options = []

    for lib, lib_versions in LIB_PATH_DICT.items():
        if lib_versions["stable"]:
            option_href = lib_versions["stable"]
        elif lib_versions["nightly"]:
            option_href = lib_versions["nightly"]
        elif lib_versions["legacy"]:
            option_href = lib_versions["legacy"]
        else:
            continue
        is_selected = False
        if lib == doc_lib:
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
    except:
        pass


def delete_existing_elements(soup):
    """
    Deletes any existing page elements to prevent duplicates on the page
    """
    doxygen_title_area = "#titlearea > table"
    sphinx_home_btn = ".wy-side-nav-search .icon.icon-home"
    sphinx_doc_version = ".wy-side-nav-search .version"
    existing_sphinx_container = "#rapids-sphinx-container"
    existing_doxygen_container = "#rapids-doxygen-container"

    for element in [
        existing_sphinx_container,
        existing_doxygen_container,
        sphinx_doc_version,
        sphinx_home_btn,
        doxygen_title_area,
        f"#{SCRIPT_TAG_ID}",
        f"#{STYLE_TAG_ID}",
        f"#{FA_TAG_ID}",
    ]:
        delete_element(soup, element)


def is_sphinx_or_doxygen(soup):
    """
    Identifies whether a given document is a Sphinx or Doxygen document
    by parsing the HTML. Returns a string identifier and reference element
    that is used for inserting the library/version selectors to the doc.
    """
    sphinx_identifier = ".wy-side-nav-search"
    doxygen_identifier = "#titlearea"

    if soup.select(sphinx_identifier):
        return "sphinx", soup.select(sphinx_identifier)[0]

    if soup.select(doxygen_identifier):
        return "doxygen", soup.select(doxygen_identifier)[0]

    raise Exception(f"Couldn't identify {FILEPATH} as either Doxygen or Sphinx")


def main():
    """
    Given the path to a documentation HTML file, this function will
    parse the file and add library/version selectors and a Home button
    """
    print(f"--- {FILEPATH} ---")
    with open(FILEPATH) as fp:
        soup = BeautifulSoup(fp, "html.parser")

    doc_type, reference_el = is_sphinx_or_doxygen(soup)

    # Delete any existing added/unnecessary elements
    delete_existing_elements(soup)

    # Add Font Awesome to Doxygen for icons
    if doc_type == "doxygen":
        add_font_awesome(soup)

    # Create new elements
    home_btn_container = create_home_container(soup)
    library_selector = create_selector(soup, create_library_options())
    version_selector = create_selector(soup, create_version_options())
    container = soup.new_tag("div", id=f"rapids-{doc_type}-container")
    script_tag = create_script_tag(soup)
    style_tab = create_css_link_tag(soup)

    # Append elements to container
    container.append(home_btn_container)
    container.append(library_selector)
    container.append(version_selector)

    # Insert new elements
    reference_el.insert(0, container)
    soup.body.append(script_tag)
    soup.head.append(style_tab)

    with open(FILEPATH, "w") as fp:
        fp.write(str(soup))


if __name__ == "__main__":
    main()
