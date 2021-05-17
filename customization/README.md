# Documentation Customization

The documentation below describes how the scripts work to customize the generated HTML files. The scripts should be run in the order they appear in the table of contents.

## Table of Contents

- [Dependencies](#dependencies)
- [Update Symlinks](#symlinks)
- [Generate Library Map](#generate-library-map)
- [Customize HTML File](#customize-html)
- [TL;DR](#TL;DR)

### Dependencies

- [jq](https://github.com/stedolan/jq)
- [BeautifulSoup4](https://github.com/waylan/beautifulsoup)

### Symlinks

For the doc customization to work correctly, all of the symlinks need to be up to date. The symlinks ultimately enable us to generate paths like `/cudf/stable/` that point to the latest RAPIDS release version folder (i.e. `/cudf/0.13/`).

[update_symlinks.sh](/update_symlinks.sh) is a shell script that updates each project's symlinks according to the versions in [releases.json](/_data/releases.json). It looks for the legacy, stable, and nightly version folders (i.e. `0.11`, `0.12`, etc.) and creates the corresponding symlinks if those folders exist.

**Usage:**

> **Note:** This script is intended to be run from the project's root.

```sh
update_symlinks.sh
```

### Generate Library Map

One of the ways we customize the documentation files is by adding dropdown selectors to each doc page that allows visitors to select and navigate between RAPIDS libraries and their versions. In order to know what page a user will be directed to upon selection, a map of available libraries and versions needs to be generated. [lib_map.sh](lib_map.sh) generates this map.

`lib_map.sh` creates a JSON file that is used by `customize_docs.py` to populate the available options for the _libray_ and _version_ selectors.

**Usage:**

> **Note:** This script is intended to be run from the project's root.

```sh
customization/lib_map.sh
```

An excerpt of the generated JSON file is shown below:

```json
{
  "clx": {
    "nightly": "/clx/en/nightly/api.html",
    "stable": "/clx/en/stable/api.html",
    "legacy": null
  },
  "cuml": {
    "nightly": "/cuml/en/nightly/api.html",
    "stable": "/cuml/en/stable/api.html",
    "legacy": "/cuml/en/legacy/api.html"
  },
  "cuxfilter": {
    "nightly": "/cuxfilter/en/nightly",
    "stable": null,
    "legacy": null
  },
  "libcudf": {
    "nightly": "/libcudf/nightly/namespacecudf.html",
    "stable": "/libcudf/stable/namespacecudf.html",
    "legacy": "/libcudf/legacy/namespacecudf.html"
  }
}
```

### Customize HTML

[customize_doc.py](customize_doc.py) is a Python script that uses [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to theme Doxygen and Sphinx HTML documentation files. It adds the following elements to each documentation page:

- A _Home_ button that links to https://docs.rapids.ai/api
- A _library_ selector that enables navigation to different RAPIDS libraries
- A _version_ selector that enables navigation to the different versions of each RAPIDS library
- A `link` tag that points to [custom.css](/assets/css/custom.css) in the file's `head`
- A `script` tag that points to [custom.js](/assets/js/custom.js) at the end the file's `body`
- A `link` tag enabling [FontAwesome](https://fontawesome.com/) in the file's `head` (only for Doxygen files)

`customize_doc.py` can be safely run multiple times on a single file without adding duplicate elements to the page.

**Usage:**

> Before running the script, it is important that [update_symlinks.sh](/update_symlinks.sh) and [lib_map.sh](lib_map.sh) have been run.

```sh
python customization/customize_docs.py ${ABS_PATH_TO_HTML_FILE} ${CURRENT_RAPIDS_VERSION}
```

#### Helper Script

[customize_docs_in_folder.sh](customize_docs_in_folder.sh) is a helper script that makes it easy to recursively customize all of the files in a specified folder.

**Usage:**

> **Note:** This script is intended to be run from the project's root.

```sh
NIGHTLY_VERSION=19

customization/customize_docs_in_folder.sh api/ ${NIGHTLY_VERSION}

# or

customization/customize_docs_in_folder.sh api/rmm ${NIGHTLY_VERSION}
```

### TL;DR

To customize the docs, run:

```sh
NIGHTLY_VERSION="19"

update_symlinks.sh # ensures symlink accuracy

customization/lib_map.sh # generates a JSON file needed by customize_docs.py

customization/customize_docs_in_folder.sh api/rmm ${NIGHTLY_VERSION}

```
