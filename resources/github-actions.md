---
layout: default
nav_order: 3
parent: Resources
grand_parent: Maintainer Docs
title: GitHub Actions
---

# {{ page.title }}
{:.no_toc}

## Overview
{:.no_toc}

The RAPIDS team uses GitHub Actions for CI/CD. The official documentation for GitHub Actions can be viewed [here](https://docs.github.com/en/actions).

### Intended audience
{: .no_toc }

Operations
{: .label .label-purple}

Developers
{: .label .label-green}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

RAPIDS uses self-hosted runners provided by NVIDIA for GPU-enabled testing. More information about these self-hosted runners can be found on the official documentation site [here](https://docs.gha-runners.nvidia.com/).

Additionally, the section [here](https://docs.gha-runners.nvidia.com/pull-request-testing) about pull request testing may be useful for users who are not already familiar with the process.

Finally, the page [here](https://docs.gha-runners.nvidia.com/runners/) outlines the list of runner labels that are available for use.

## Downloading CI Artifacts

For NVIDIA employees with VPN access, artifacts from both pull-requests and branch builds can be accessed on [https://downloads.rapids.ai/](https://downloads.rapids.ai/).

There is a link provided at the end of every C++ and Python build job where the build artifacts for that particular workflow run can be accessed.

![](/assets/images/downloads.png)

## Using CI Artifacts in Other PRs

For changes that cross library boundaries, it may be necessary to test a pull request to one library with changes from a pull request to another library.
To do this, it is necessary to download CI artifacts (described in the above section) from one library during the CI workflow of another library.
First, determine the pull request number and commit hash that need to be tested from the other library.
Then, fetch the CI artifacts from the other library's pull request and use them when building and testing.
The example code below demonstrates building and testing with conda packages from other library PRs.
Replace the pull request numbers, commit hashes, and library names as needed.

**Example 1:** Building `libcuml` (C++) using `librmm`, `libraft`, `libcumlprims_mg` PR artifacts. Adapted from [cuML PR 5318](https://github.com/rapidsai/cuml/pull/5318).

```sh
# ci/build_cpp.sh

RAPIDS_CUDA_MAJOR="${RAPIDS_CUDA_VERSION%%.*}"
LIBRMM_CHANNEL=$(rapids-get-artifact ci/rmm/pull-request/1223/72e0c74/rmm_conda_cpp_cuda${RAPIDS_CUDA_MAJOR}_$(arch).tar.gz)
LIBRAFT_CHANNEL=$(rapids-get-artifact ci/raft/pull-request/1388/7bddaee/raft_conda_cpp_cuda${RAPIDS_CUDA_MAJOR}_$(arch).tar.gz)
LIBCUMLPRIMS_CHANNEL=$(rapids-get-artifact ci/cumlprims_mg/pull-request/129/85effb7/cumlprims_mg_conda_cpp_cuda${RAPIDS_CUDA_MAJOR}_$(arch).tar.gz)

# Build library packages with the CI artifact channels providing the updated dependencies

rapids-mamba-retry mambabuild \
    --channel "${LIBRMM_CHANNEL}" \
    --channel "${LIBRAFT_CHANNEL}" \
    --channel "${LIBCUMLPRIMS_CHANNEL}" \
    conda/recipes/libcuml
```

**Example 2:** Testing `cudf` (Python) using `librmm`, `rmm`, and `libkvikio` PR artifacts. Adapted from [cuDF PR 12922](https://github.com/rapidsai/cudf/pull/12922).

```sh
# ci/test_python_common.sh

RAPIDS_CUDA_MAJOR="${RAPIDS_CUDA_VERSION%%.*}"
PYTHON_MINOR_VERSION=$(python --version | sed -E 's/Python [0-9]+\.([0-9]+)\.[0-9]+/\1/g')
LIBRMM_CHANNEL=$(rapids-get-artifact ci/rmm/pull-request/1223/8704a75/rmm_conda_cpp_cuda${RAPIDS_CUDA_MAJOR}_$(arch).tar.gz)
RMM_CHANNEL=$(rapids-get-artifact ci/rmm/pull-request/1223/b8d1c12/rmm_conda_python_cuda${RAPIDS_CUDA_MAJOR}_3${PYTHON_MINOR_VERSION}_$(arch).tar.gz)
LIBKVIKIO_CHANNEL=$(rapids-get-artifact ci/kvikio/pull-request/224/68febbb/kvikio_conda_cpp_cuda${RAPIDS_CUDA_MAJOR}_$(arch).tar.gz)

# Install library packages with the CI artifact channels providing the updated dependencies for testing

rapids-mamba-retry install \
  --channel "${CPP_CHANNEL}" \
  --channel "${PYTHON_CHANNEL}" \
  --channel "${LIBRMM_CHANNEL}" \
  --channel "${LIBKVIKIO_CHANNEL}" \
  --channel "${RMM_CHANNEL}" \
  cudf libcudf
```

Note that the custom channel for PR artifacts is needed in the build scripts _and_ the test scripts.
If building/testing a Python package that depends on a C++ library, it is also necessary to use PR artifacts from that C++ library (e.g. if testing `rmm` artifacts, use the corresponding `librmm` CI artifacts as well).

## Skipping CI for Commits

See the GitHub Actions documentation page below on how to prevent GitHub Actions from running on certain commits. This is useful for preventing GitHub Actions from running on pull requests that are not fully complete. This also helps preserve the finite GPU resources provided by the RAPIDS Ops team.

With GitHub Actions, it is not possible to configure all commits for a pull request to be skipped. It must be specified at the commit level.

**Link**: [https://docs.github.com/en/actions/managing-workflow-runs/skipping-workflow-runs](https://docs.github.com/en/actions/managing-workflow-runs/skipping-workflow-runs)

## Rerunning Failed GitHub Actions

See the GitHub Actions documentation page below on how to rerun failed workflows. In addition to rerunning an entire workflow, GitHub Actions also provides the ability to rerun only the failed jobs in a workflow.

At this time there are no alternative ways to rerun tests with GitHub Actions beyond what is described in the documentation (e.g. there is no `rerun tests` comment for GitHub Actions).

**Link**: [https://docs.github.com/en/actions/managing-workflow-runs/re-running-workflows-and-jobs](https://docs.github.com/en/actions/managing-workflow-runs/re-running-workflows-and-jobs)
