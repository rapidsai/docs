---
layout: default
nav_order: 4
parent: Resources
title: Style Guide
---

# Style Guide

## Overview

Summary of style formats for various aspects of RAPIDS projects.

### Intended audience

Community
{: .label .label-yellow}

Developers
{: .label .label-green}

## Code style

### Python

All Python code in RAPIDS projects is style checked using [`flake8`](https://github.com/PyCQA/flake8)

Individual project should configure `flake8` to suit their needs, for example to exclude specific directories or files.

## Git commits

Git commit messages should convey the change succinctly, but with enough detail to be understood without extra context.

- First line should be a short description
- Limit the first line to 72 characters or less
- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Second line should be empty
- After second line, detail the changes and implementation details
- Reference issues and pull requests liberally after the second line

Consider starting the first line with a tag (e.g. `DOC Update documentation`):

| Tag  | Description                          |
|:-----|:-------------------------------------|
| ENH  | Enhancement, new functionality       |
| BUG  | Bug Fix                              |
| DOC  | Additions/updates to documentation   |
| TST  | Additions/updates to tests           |
| BLD  | Updates to the build process/scripts |
| PERF | Performance improvement              |
| CLN  | Code cleanup                         |

## Pull requests

### Title

Pull request titles should be succinct and state how the PR addresses the issue.

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Must start with `[WIP]` or `[REVIEW]`

`[WIP]` denotes a PR which is still being worked on and should never be merged. This is used to solicit feedback from the community.

`[REVIEW]` denotes a PR which the author believes fully addresses the issue and is ready to be reviewed and merged.

### Description

The description must start with `Addresses #[issue number]`. If the PR addresses multiple issues, use an unordered list.

The description should also detail the implementations, challenges, and solutions so reviewers can understand the approach.

The description should NOT reword the issue description.

### Comments

All comments and reviews to pull requests must follow the [Code of Conduct]({{ site.baseurl }}docs/resources/conduct/)
