---
layout: default
title: gpuCI
nav_order: 7
has_children: false
has_toc: true
permalink: gpuci
---

# gpuCI Usage Docs
{:.no_toc}

Our gpuCI is responsible for testing each PR and commit with GPUs and building conda packages for all RAPIDS projects.
{: .fs-6 .fw-300 }

### Intended audience
{:.no_toc}

Community
{: .label .label-yellow}

Developers
{: .label .label-green}

Operations
{: .label .label-purple}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Overview

[gpuCI](http://gpuci.gpuopenanalytics.com) is the name for our GPU-backed CI service based on a [custom plugin](https://github.com/gpuopenanalytics/remote-docker-plugin) and Jenkins. This allows us to use Docker [containers](https://github.com/rapidsai/gpuci-build-environment) as the build environment for testing [RAPIDS](http://rapids.ai/) projects through the use of [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) for GPU pass-through to the containers.

## Process

New pull requests (PRs) and pushes to branches trigger jobs on the [gpuCI](http://gpuci.gpuopenanalytics.com) server to build from source and run the included tests. The results are available on the server itself, or if triggered by a PR they are embedded in the PR with the high level result and a link for detailed build information.

## Triggers

### Push to a branch

Any push to a branch triggers a gpuCI job that builds and tests the current code, linking and showing the results as a build status icon on the README:

[![Build Status](https://gpuci.gpuopenanalytics.com/buildStatus/icon?job=rapidsai%2Fgpuci%2Fcudf%2Fbranches%2Fcudf-branch-pipeline)](https://gpuci.gpuopenanalytics.com/job/rapidsai/job/gpuci/job/cudf/job/branches/job/cudf-branch-pipeline/)

### Open PR or Update PR

When a new PR is opened or an existing one has been updated, gpuCI will trigger a series of CI jobs to be run on the PR. The results of these jobs wil be embedded into the status of the PR.

> **IMPORTANT:** gpuCI will not run any builds until a valid changelog entry has been detected. If a changelog entry is missing, a comment will be posted on the PR instructing the author to add an entry. This is to ensure that no build resources are wasted on PRs that are expecting more commits.

> **BE AWARE:** gpuCI may request `Can one of the admins verify this patch?` in a comment on the PR. If this appears, one of the PICs for the RAPIDS library needs to respond to approve the PR. See the commands list [below](#admins---approving-pr-builds) for available commands.

### Comment on PR

Comments with the text `rerun tests` are used in a PR to manually trigger a retest when the code has not changed.

This is helpful when trying to troubleshoot issues with the build process and/or to see if the encountered error is persistent. Use gpuCI to examine the _Console Output_ to find more detail.

## Commands

### Admins - Approving PR builds

* To approve PR author for just the current PR, comment the command:
  * `ok to test`
* To approve PR author for all PRs in the future, comment the command:
  * `add to whitelist`

### Users

* To manually trigger tests in a PR, comment the command:
  * `rerun tests`
* To skip CI testing (for documentation changes) add the following to the title of the PR:
  * `[skip ci]`
  * **NOTE:** The changelog check will still run.
* To skip the changelog check (e.g. for manual auto-merger resolution) add the following to the title of the PR:
  * `[skip ci changelog]`

## Help

If you run into issues and need help with gpuCI, please file an issue in the repo that represents the code base with the issue and start the issue title with `[gpuCI]`
