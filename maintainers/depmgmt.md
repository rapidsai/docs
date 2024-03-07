---
layout: default
nav_order: 2
parent: Maintainer Docs
title: Dependency Management
---

# Dependency Management Documentation

## Overview

Outlines RAPIDS shared recipes and metapackages like `rapids`

### Intended audience

Developers
{: .label .label-green}

Project Leads
{: .label .label-blue}

Operations
{: .label .label-purple}

## Adding a Dependency

The [RAPIDS Integration repository](https://github.com/rapidsai/integration) defines shared recipes and metapackages used to deploy RAPIDS.

Most importantly, this repository defines `rapids`, the metapackage containing all RAPIDS libraries.

### Recipes and Versions

The files in `conda/recipes/` define recipes for packages like `rapids`.

To modify a recipe, edit its `meta.yaml`.

The file `conda/recipes/versions.yaml` defines some common versions that are used by the recipes.

All version specifiers follow [conda's package match specifications](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/pkg-specs.html#package-match-specifications).

To test changes, submit a PR to the `integration` repository. The changes will be built and tested on a development docker image to confirm that it doesn't conflict with RAPIDS libraries.
