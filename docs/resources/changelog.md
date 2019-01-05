---
layout: default
nav_order: 2
parent: Resources
title: Changelog Format
---

# Changelog Format

## Overview

Summary of the format for changelogs used by RAPIDS projects.

### Intended audience

Community
{: .label .label-yellow}

Developers
{: .label .label-green}

Managers
{: .label .label-blue}

## Format

The changelog is ordered reverse chronologically, which mean the next release is first and previous releases follow.

The changelog is formatted in Markdown.

### Title

The title should be at 'Heading level 1'

Each release should be titled as: `[project name] [version] ([release date])`

- The version is the SemVer outlined [here](docs/releases/versions#versioning-method)
- The release date is formatted as `(DD MMM YYYY)`, e.g. `(05 Jan 2019)`
- The release date should be `TDB` for the next release

### Body

The body of each release consists of three sections in order:

- New Features
- Improvements
- Bug Fixes

If a section has no items, it can be ommitted.

Each section should be 'Header level 2'. Each section contains an unordered list of the pull requests that are merged into the release.

The format of each item is: `PR #[pull request number] [component name]: [description]`

- The component name is optional, but should be used as often as possible
- The description should follow similiarly to git commit and PR description messages. Often the PR description can be used.


### Example

#### rapidsProject 0.2.0 (TDB)

##### New Features

- PR #10 DataComponent: Adds new data reader

##### Improvements

- PR #11 Improves processing speed

##### Bug Fixes

-  PR #11 OtherComponent: Fixes endianness

#### rapidsProject 0.1.0 (05 Jan 2019)

##### New Features

- PR #1 DataComponent: Creates data component for processing data

