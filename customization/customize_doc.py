"""
Script to customize doxygen/sphinx generated HTML for RAPIDS
"""
import re
import sys
import json
import os
from bs4 import BeautifulSoup

FILEPATH = sys.argv[1]

LIB_MAP_PATH = os.path.join(os.path.dirname(__file__), "lib_map.json")

with open(LIB_MAP_PATH) as fp:
    LIB_PATH_DICT = json.load(fp)

SCRIPT_TAG_ID = "rapids-selector-js"
STYLE_TAG_ID = "rapids-selector-css"
FA_TAG_ID = "rapids-fa-tag"
RAW_TAG_OPEN = "{% raw %}"
RAW_TAG_CLOSE = "{% endraw %}"


def get_version_from_fp():
    """
    Gets the current RAPIDS version from the filepath
    """
    match = re.search(r"0.\d{1,3}", FILEPATH)

    if match:
        return match[0]

    raise Exception(f"Couldn't find valid RAPIDS version in {FILEPATH}.")


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
    doc_lib = get_lib_from_fp()

    # Creates a template string to be interpolated by Jekyll
    version_template_str = lambda x: "{{" + f" '{x}' | version_selector " + "}}"

    # Iterate over non-None keys library keys from LIB_PATH_DICT
    for version_name, version_path in [
        (_, path) for _, path in LIB_PATH_DICT[doc_lib].items() if path is not None
    ]:
        option_text = version_template_str(version_name)
        option_href = version_path
        extra_classes = ["{{ " + f"'{version_name}' | add_active_class" + " }}"]
        options.append(
            {"href": option_href, "text": option_text, "extra_classes": extra_classes}
        )

    return {"selected": version_template_str("doc"), "options": options}


def create_library_options():
    """
    Creates options for library selector
    """
    doc_lib = get_lib_from_fp()
    options = []

    for lib, lib_versions in LIB_PATH_DICT.items():
        extra_classes = []
        if lib_versions["stable"]:
            option_href = lib_versions["stable"]
        elif lib_versions["nightly"]:
            option_href = lib_versions["nightly"]
        elif lib_versions["legacy"]:
            option_href = lib_versions["legacy"]
        else:
            continue
        if lib == doc_lib:
            extra_classes.append("rapids-selector__menu-item--selected")
        options.append(
            {"href": option_href, "text": lib, "extra_classes": extra_classes}
        )

    return {"selected": doc_lib, "options": options}


def create_selector(soup, menu):
    """
    Creates a dropdown selector
    """
    container = soup.new_tag(
        "div",
        attrs={"class": ["rapids-selector__container", "rapids-selector--hidden"]},
    )
    selected = soup.new_tag("div", attrs={"class": "rapids-selector__selected"})
    selected.string = menu["selected"]
    container.append(selected)
    drop_down_menu = soup.new_tag("div", attrs={"class": ["rapids-selector__menu"]})
    options = menu["options"]

    for option in options:
        option_classes = ["rapids-selector__menu-item"]
        option_classes.extend(option["extra_classes"])
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

    raise Exception(
        f"Couldn't identify {FILEPATH} as either Doxygen or Sphinx document"
    )


def get_frontmatter():
    """
    Returns the frontmatter used in documentation files.
    """
    return (
        "---\n"
        "permalink: /:path/:basename\n"
        "nav_exclude: true\n"
        "doc_version: '" + get_version_from_fp() + "'\n"
        "---\n"
    )


def sanitize_html(html_str):
    """
    Removes any existing Jekyll/Liquid templating strings from the
    HTML file.
    """
    html_start_index = html_str.index("<!DOCTYPE html")

    # remove frontmatter
    html_str = html_str[html_start_index:]

    # remove raw tags
    html_str = html_str.replace(RAW_TAG_OPEN, "").replace(RAW_TAG_CLOSE, "")

    return html_str


def main():
    """
    Given the path to a documentation HTML file, this function will
    parse the file and add library/version selectors and a Home button
    """
    print(f"Processing {FILEPATH}...")
    with open(FILEPATH) as html_str:
        html = sanitize_html(html_str.read())
    soup = BeautifulSoup(html, "html.parser")

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

    # Add raw tag so no proceeding content is parsed by Jekyll
    container.append(RAW_TAG_OPEN)

    # Insert new elements
    reference_el.insert(0, container)
    soup.body.append(script_tag)
    soup.head.append(style_tab)

    with open(FILEPATH, "w") as output_file:
        output_file.write(get_frontmatter() + str(soup) + RAW_TAG_CLOSE)


if __name__ == "__main__":
    main()
