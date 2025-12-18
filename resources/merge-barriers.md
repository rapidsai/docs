---
layout: default
nav_order: 6
parent: Resources
grand_parent: Maintainer Docs
title: Merge Barriers
---

# _Merge Barriers_ Check

## Overview

A GitHub action that checks whether a pull-request is up-to-date with the any merge barrier commits from the source repository.

### Intended audience

Community
{: .label .label-yellow}

Developers
{: .label .label-green}

Project Leads
{: .label .label-blue}

Operations
{: .label .label-purple}

## Summary

Pull requests can be explicitly marked as "merge barriers" to be required to be merged into a pull request before it can be merged. This is used for pull requests that have wide-reaching implications, such as broad reformatting or linting, which are highly likely to cause logical merge conflicts with many other pull requests.

The _Merge Barriers_ check is configurable by editing the following value in the `.github/ops-bot.yaml` file:

```yaml
# enables/disables the Merge Barriers Check
merge_barriers: true
```

A pull request can be marked as a merge barrier by adding the following line to the description:

```
Ops-Bot-Merge-Barrier: true
```

If a pull request with this line is merged, no pull requests can be merged after it unless they merge in the merge barrier commit. If a pull request cannot be merged due to missing a merge barrier, the easiest fix is to simply merge in the latest commit from the target branch.

For more generic requirements to keep a pull request reasonably up-to-date with the origin, see the [recently updated check](./recently-updated.md).
