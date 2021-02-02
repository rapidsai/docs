---
layout: default
nav_order: 2
parent: Resources
grand_parent: RAPIDS Maintainer Docs
title: Changelog Format
---

# Changelog Format

## Overview

Summary of the changelog process used by RAPIDS projects.

### Intended audience

Community
{: .label .label-yellow}

Developers
{: .label .label-green}

Project Leads
{: .label .label-blue}

### Process

During the development cycle of each RAPIDS release, merged pull requests will be automatically recorded in a GitHub pre-release. The pre-releases can be found in a repository's _Release_ section on GitHub. (i.e. https://github.com/rapidsai/cudf/releases). At release time, the contents of the pre-release's body will be copied into the `CHANGELOG.md` file found in each repository's root directory.

### Body

The body of each pre-release contains a list of pull requests categorized into the following sections:

- Breaking Changes
- Bug Fixes
- Documentation
- New Features
- Improvements

### Pull Request Labels

In order to correctly categorize pull requests, the following labels must be applied to each:

#### `category` Label (choose one):

Categorizes the PR in the pre-release

- `bug`
- `doc`
- `feature request`
- `improvement`

#### `breaking` Label (choose one):

Determines if there is a "breaking" change to user functionality

**NOTE:** Developers should consult with their PICs for a repo specific set of guidelines for determining a "breaking" change

- `breaking`
- `non-breaking`
