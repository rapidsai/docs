---
layout: default
nav_order: 2
parent: RAPIDS Resources
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

Project Leads
{: .label .label-blue}

## Format

The changelog is ordered reverse chronologically, which mean the next release is first and previous releases follow.

The changelog is formatted in [Markdown](https://help.github.com/articles/basic-writing-and-formatting-syntax/) and in the root of the project repository named `CHANGELOG.md`.

### Title

Each release should be titled as: 
```
# [project name] [version] ([release date])
```
- `#` - sets the header level to 1
- `[project name]` - is the name of the project
- `[version]` - is the SemVer outlined [here]({{ site.baseurl }}docs/resources/versions/#versioning-method)
- `[release date]` - is formatted as `(DD MMM YYYY)`, e.g. `(05 Jan 2019)` for a known release date; otherwise, use `TBD` as a placeholder

### Body

The body of each release consists of three sections in order:

- New Features
- Improvements
- Bug Fixes

Each of these three sections should start as 'Header level 2' using `## [section title]` as the format. If a section has no items, it can be omitted.

For each section there is an unordered list of the pull requests that are merged into the release and their descriptions. The format of each list item is: 
```
PR #[pull request number] [description]
```
- `[pull request number]` - is the number for the given PR
- `[description]` - should follow similarly to git commit and PR description messages. Ensure these are concise, but "human readable." Often the PR description can be used.


### Example `CHANGELOG.md` file

```
# rapidsProject 0.2.0 (TDB)

## New Features

- PR #10 DataComponent: Adds new data reader

## Improvements

- PR #11 Improves processing speed

## Bug Fixes

-  PR #12 OtherComponent: Fixes endianness

# rapidsProject 0.1.0 (05 Jan 2019)

## New Features

- PR #1 DataComponent: Creates data component for processing data
- PR #2 Adds parser for CSV
```
