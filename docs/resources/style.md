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

Individual projects should configure `flake8` to suit their needs, for example to exclude specific directories or files.

## Git commits

Git commit messages should convey the change succinctly, but with enough detail to be understood without extra context.

### Commit tags

Consider starting the first line with a tag (e.g. `DOC Update conda install process`):

| Tag | Description                          |
|:----|:-------------------------------------|
| ENH | Enhancement, new functionality       |
| BUG | Bug Fix                              |
| DOC | Additions/updates to documentation   |
| TST | Additions/updates to tests           |
| BLD | Updates to the build process/scripts |
| PRF | Performance improvement              |
| CLN | Code cleanup                         |

These help communicate the actions that are being taken, and help others when trying to review changes in a PR.

### First line

The *first line* should be a short description of the changes made, keeping the following in mind:
- Limit the *first line* to 72 characters or less; use a *third line* for a detailed description
- Begin the *first line* with a commit tag from the table above
- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")

### Multi-line git messages

The *second line* should **always be empty**, if you need to add addtional details start on the *third line*.

For the third and successive lines, keep the following in mind:
- Detail the changes and implementation details
- Reference issues and pull requests by their number, for example `#47`
- Use `- ` to show elements of a list, starting a new line for each new list item

### Sample git commits

Single-line git commit message:
```
DOC Update conda install process
```

Multi-line git commit message:
```
DOC Update conda install process

- This corrects bug #47 that prevents users from installing X because of Y...
- Also fixed spelling mistakes and an incorrect version number
```

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
