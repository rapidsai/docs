---
layout: default
nav_order: 3
parent: Resources
grand_parent: Maintainer Docs
title: Git Methodology
---

# Git Methodology

## Overview

Details on our git branching method used for RAPIDS and our style conventions for git commits.

### Intended audience

Community
{: .label .label-yellow}

Developers
{: .label .label-green}

### See also

* [Versioning and Tagging]({% link resources/versions.md %})
* [Hotfix releases]({% link releases/hotfix.md %})
* [Releases]({% link releases/process.md %})

## Git branching

### Approach

Our development approach involves using the `main` branch as the main development branch. When a release occurs it will use the [Versioning and Tagging]({% link resources/versions.md %}) and [Release]({% link releases/process.md %}) proceedures.

### Development workflow

All PRs are merged into `main`. Release branches are created from `main` when the decision has been made to start the the **burndown** process for the release.

To **burndown** a release branch is to stop new development for the release, and focus on completing outstanding features and any bugs discovered from testing. Once this **burndown** happens, the dependencies in the `main` branch are updated to `YY.MB` so development can continue on any features not going into `YY.MA`. Updates to `release/YY.MA` will be [forward-merged]({% link resources/auto-merger.md %}) into `main`, and any merge conflicts are handled as part of this forward merge process. This means any fixes found during ***burndown*** make it to `main`, which contains the latest and greatest code.

Hotfixes (patch releases) related to the current release `YY.MA` are directly merged to `main` from a PR and then those changes are also merged to the current release branches in progress through an automated process. All merges to `main` trigger an automated CI job that will produce a new release and tag incrementing the patch version off of the previous highest tag in the repo. Once the tag is set, the automated CI build for conda packages creates and pushes new packages for users. This includes the version change enabling known good builds and the ability to rollback.

PRs can be edited on GitHub to set the target base branch for merging the PR. It is the reviewer's responsibility to ensure the PR is targeted for the correct and planned release branch. Once PRs have passed all tests, they are merged to their release branch, which triggers an automated CI build for conda packages that will be marked as development and pushed to the [rapidsai-nightly](https://anaconda.org/rapidsai-nightly/) channel hosted on anaconda. These can be inspected by the team to ensure the build works as intended and perform larger testing.

Once a release has been reviewed and signoff has been given, the automated tagging process tags and kicks off the conda builds for the public release.

### Summary

- Development stays on `main` branch (not moving to `release/YY.MX`)
- Releases happen on `release/YY.MX` branches (not on `main`)
- Forward merger automatically merges changes from release branches to main
- Alpha tags distinguish development versions (e.g., `v26.02.00a`) from release versions (e.g., `v25.12.00`)
- `RAPIDS_BRANCH` file replaces alpha suffixes for dependency resolution

## Large files and git

Any file larger than 5MB must be stored using either [Git LFS](https://git-lfs.github.com/) or S3.

| Size | Required | Not Required |
| ---- | -------- | ------------ |
| <5MB | Git | Git |
| >5MB | Git LFS | S3 |
| >2GB | Avoid | S3 |

A `required` file is a file that the average developer requires in order to build and/or test the project. This may include small datasets for running unit tests or large source files.

Files that are `not required` should be stored in S3 so the limited number of developers who need it can "opt-in" to downloading these larger files. This helps keep the repository smaller for the majority of users.

It is important to choose the appropriate storage mechanism from the beginning because transitioning from git to git LFS or S3 requires rewriting git history.

If you need data uploaded to S3, simply file an Ops issue.
