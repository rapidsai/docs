---
layout: default
nav_order: 3
parent: Contributing
title: Pull Requests
---

# Pull Requests

## Overview

...

### Intended audience

Community
{: .label .label-yellow}

Developers
{: .label .label-green}

Managers
{: .label .label-blue}

## ...

## Pull request formatting

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
