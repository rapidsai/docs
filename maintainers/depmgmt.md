---
layout: default
nav_order: 4
parent: RAPIDS Maintainer Docs
title: Dependency Management
---

# Dependency Management Documentation

## Overview

Outlines how to test and change dependencies of the RAPIDS projects

### Intended audience

Developers
{: .label .label-green}

Project Leads
{: .label .label-blue}

Operations
{: .label .label-purple}

## Testing a Dependency

The build scripts located in the `ci/gpu` folder of the project can be easily modified to test a dependency. For example, the build script for cuDF may contain these lines to install packages required to build from source and test notebooks:


```
conda install "rmm=$MINOR_VERSION.*" "rapids-build-env=$MINOR_VERSION.*" \
              "rapids-notebook-env=$MINOR_VERSION.*"
```

`rapids-build-env` and `rapids-notebook-env` are meta-packages that are used to keep dependencies across the projects consistent. These packages have various packages with specific versions listed as its dependencies. To change these dependencies as a test on a PR, the meta-package should be removed. Removing it allows the installation of different versions of dependencies without causing conda conflicts. Here is what to add to the script to allow this:

```
conda install "rmm=$MINOR_VERSION.*" "rapids-build-env=$MINOR_VERSION.*" \
              "rapids-notebook-env=$MINOR_VERSION.*"

conda remove -f rapids-build-env rapids-notebook-env
conda install "your-pkg=1.0.0"
```

With this method, dependencies changes can be tested inside a PR. However, this should only be used as a temporary test, and not a permanent change. Once it is confirmed that the change works, the new dependency should be updated or added to the `integration` repository.

## Adding a Dependency

The (RAPIDS Integration repository)[https://github.com/rapidsai/integration] contains all the information needed for adding a dependency to the RAPIDS projects. The `meta.yaml` you change should be based on the purpose of the package you are installing. The purpose of each meta-package is listed below:

Package Name | Purpose
--- | ---
`rapids-build-env` | Installs all `conda` build dependencies to build & test RAPIDS libraries from source
`rapids-doc-env` | Installs all tools needed to build RAPIDS documentation
`rapids-notebook-env` | Installs a Jupyter Notebook server and other dependencies to run RAPIDS example notebooks; used in the `runtime` [stable](https://hub.docker.com/r/rapidsai/rapidsai/tags?page=1&name=runtime) and [nightly](https://hub.docker.com/r/rapidsai/rapidsai-nightly/tags?page=1&name=runtime) RAPIDS containers.

### Adding Versions

For new packages or those that do not have defined versions they need to be
added.

#### Modifying Recipes

To add a package with versioning to the recipe we need the `PACKAGE_NAME` and
the `VERSIONING_NAME` added to the file.

- `PACKAGE_NAME` - is the conda package name
- `VERSIONING_NAME` - is the conda package name with `-` replaced with `_` and a suffix of `_version` added
  - For example 
    - `cupy` would become `cupy_version`
    - `scikit-learn` would become `scikit_learn_version`

Once the `PACKAGE_NAME` and `VERSIONING_NAME` are ready, we can add them to
the `meta.yml` as follows:

```
PACKAGE_NAME {{ VERSIONING_NAME }}
```

- **NOTE:** The `VERSIONING_NAME` must be surrounded by the `{{ }}` for the substitution to work.

Using our examples of `cupy` and `scikit-learn` we would have these entries in
the `meta.yaml`:

```
cupy {{ cupy_version }}
```
```
scikit-learn {{ scikit_learn_version }}
```

#### Modifying Versions Files

There are two versions files that are in `conda/recipes`:
 - `release-versions.yaml` - These are versions used by the `ci/axis/release.yaml` for RELEASE builds
 - `nightly-versions.yaml` - These are versions used by the `ci/axis/nightly.yaml` for NIGHTLY builds

Both of these files will need a config added to specify the version for the
newly created `VERSIONING_NAME`.

For each `VERSIONING_NAME` we need a `VERSION_SPEC`. This can be any of the
standard `conda` version specifiers:
```
>=1.8.0
>=0.48,<0.49
>=7.0,<8.0.0a0,!=7.1.0
=2.5.*
```

Combined together each of the versions files would add the following for each
`VERSIONING_NAME`:
```
VERSIONING_NAME:
  - 'VERSION_SPEC'
```

Using our examples of `cupy` and `scikit-learn` we would have these entries in
the `meta.yaml`:

```
cupy_version:
  - '>=7,<8.0.0a0,!=7.1.0'
```
```
scikit_learn_version:
  - '=0.21.3'
```

### Updating Versions

There are two versions files that are in `conda/recipes`:
 - `release-versions.yaml` - These are versions used by the `ci/axis/release.yaml` for RELEASE builds
 - `nightly-versions.yaml` - These are versions used by the `ci/axis/nightly.yaml` for NIGHTLY builds

 Edit the files above and update the `VERSION_SPEC` as desired.
 
 For more information see the [Modifying Versions Files](#modifying-versions-files)

Once done, submit a PR to the `integration` repository. The changes will be built and tested on a development docker image to confirm that it doesn't conflict with other RAPIDS libraries.

