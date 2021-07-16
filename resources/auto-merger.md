---
layout: default
nav_order: 3
parent: Resources
grand_parent: RAPIDS Maintainer Docs
title: Auto-Merger
---

# Auto-Merger

## Overview

Summary of the automated merge process used for pull requests.

### Intended audience

Community
{: .label .label-yellow}

Developers
{: .label .label-green}

## Summary

Some RAPIDS repositories use an auto-merger to merge pull requests. The auto-merger serves two purposes:

1. Ensures all merged pull requests have consistent and useful commit messages
2. Allows pull request merges to be scheduled to occur when all merge criteria (below) are satisfied

To use the auto-merger, simply type `@gpucibot merge` as a comment on a given pull request. The auto-merger will not run if the comment includes any other text besides `@gpucibot merge`.

If the merge criteria below are satisfied when the comment is left on the pull request, the pull request will merge immediately.

If the merge criteria below are **not satisfied** when the comment is left on the pull request, the pull request will merge when the criteria become satisfied.

### Merge criteria

- All **required** (not optional) CI checks must be passing
- Must not have merge conflicts
- Must not be merging to the `main` branch
- No changes have been requested from users who have `write`, `admin`, or `owner` permissions
- Any user who left the `@gpucibot merge` comment must have `write` or `admin` privileges on the repo

The pull request will be squash merged and the commit title will be formatted like `<PR_Title> (#<PR_Number>)` . Any square brackets `[]` in the title will be automatically removed. The commit message will be formatted like:

```
This PR adds some extra line breaks to the commit messages.

Authors:
  - AJ Schmidt (https://github.com/ajschmidt8)

Approvers:
  - Ray Douglass (https://github.com/raydouglass)

URL: https://github.com/rapidsai/cudf/pull/8638/

```

> **PRO TIP!** - Use GitHub's [saved replies](https://docs.github.com/en/free-pro-team@latest/github/writing-on-github/using-saved-replies) feature to avoid having to type out the `@gpucibot merge` comment by hand every time.
