# Documentation Customization

The documentation below describes how the scripts work to customize the generated HTML files.
The scripts should be run in the order they appear in the table of contents.

Unless otherwise stated, all scripts should be run from the root of this repository.

## Table of Contents

- [Dependencies](#dependencies)
- [Quickstart](#quckstart)
- [Project Versions](#project-versions)
- [Update Symlinks](#symlinks)
- [Generate Library Map](#generate-library-map)
- [Customize HTML File](#customize-html)
- [TL;DR](#TL;DR)

### Dependencies

- `aws` CLI ([docs](https://aws.amazon.com/cli/))
- `jq` ([docs](https://jqlang.org/manual/))
- Python / `pip`
- `yq` ([docs](https://mikefarah.gitbook.io/yq))

### Quickstart

If you just want to try running all of the customization locally, download all of the API docs ([as described in `ci/README.md`](../README.md)), then invoke the following script:

```shell
./ci/post-process.sh
```

To learn more about each step, keep reading.

### Project Versions

Building the API docs requires answering these questions:

* which RAPIDS projects?
* what version types? (stable? legacy? nightly?)
* what version numbers correspond to those version types?

Logic for all of that is centralized in a script.

Invoke it to see what will be built.

```shell
./ci/get-projects-to-versions.sh > ./ci/customization/projects-to-versions.json
```

### Symlinks

Initially, the downloaded API docs are in directories named with version numbers, like this:

```console
$ tree -L 2 ./_site/api
_site/api/
├── cudf
│   ├── 25.06
│   ├── 25.08
│   ├── 25.10
```

Those directory paths become links on the docs site, like https://docs.rapids.ai/api/cudf/25.10/.

To be more bookmark-friendly, the docs site also has links with version _types_ like `/legacy`, `/nightly`, and `/stable`.

To avoid fully copying files, that's done via creating symlinks, similar to this:

```shell
pushd ./_site/api/cudf
ln -s 25.10 stable
```

To avoid hard-coding all those versions and paths, that logic is automated in a script.
Try running it to generate the symlinks.

```shell
./ci/update_symlinks.sh ./ci/customization/projects-to-versions.json
```

After that is run, you'll see links like the following have been created.

```console
$ tree -L 2 ./_site/api
./_site/api/
├── cudf
│   ├── 25.06
│   ├── 25.08
│   ├── 25.10
│   ├── latest -> 25.08
│   ├── legacy -> 25.06
│   ├── nightly -> 25.10
│   └── stable -> 25.08
```

### Generate Library Map

One of the ways we customize the documentation files is by adding dropdown selectors to each doc page that allows visitors to select and navigate between RAPIDS libraries and their versions.

In order to know what page a user will be directed to upon selection, a map of available libraries and versions needs to be generated.
[lib_map.sh](lib_map.sh) generates this map.

`lib_map.sh` creates a JSON file that is used by `customize_docs.py` to populate the available options for the _library_ and _version_ selectors.

```sh
./ci/customization/lib_map.sh
```

An excerpt of the generated JSON file is shown below:

```json
{
  "cuml": {
    "nightly": "/cuml/en/nightly",
    "stable": "/cuml/en/stable",
    "legacy": "/cuml/en/legacy"
  },
  "libcudf": {
    "nightly": "/libcudf/nightly/namespacecudf/",
    "stable": "/libcudf/stable/namespacecudf/",
    "legacy": "/libcudf/legacy/namespacecudf/"
  },
  "rapidsmpf": {
    "nightly": "/api/rapidsmpf/nightly",
    "stable": null,
    "legacy": null
  },
}
```

### Customize HTML

[customize_doc.py](customize_doc.py) is a Python script that uses [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to theme Doxygen and Sphinx HTML documentation files.

It adds the following elements to each documentation page:

- A _Home_ button that links to https://docs.rapids.ai/api
- A _library_ selector that enables navigation to different RAPIDS libraries
- A _version_ selector that enables navigation to the different versions of each RAPIDS library
- A `link` tag that points to [custom.css](/assets/css/custom.css) in the file's `head`
- A `script` tag that points to [custom.js](/assets/js/custom.js) at the end the file's `body`
- A `link` tag enabling [FontAwesome](https://fontawesome.com/) in the file's `head` (only for Doxygen files)

`customize_doc.py` can be safely run multiple times on a single file without adding duplicate elements to the page.

That's invoked by a wrapper script that determines HTML files to pass in.

```sh
PROJECTS_TO_JSON_PATH="./ci/customization/projects-to-versions.json"

# all API docs
./ci/customization/customize_docs_in_folder.sh \
  ./_site/api \
  "${PROJECTS_TO_JSON_PATH}"

# just cudf
./ci/customization/customize_docs_in_folder.sh \
  ./site/api/cudf \
  ./ci/customization/projects-to-versions.json
```
