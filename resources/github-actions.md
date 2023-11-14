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

## GitHub Action Workflows

Every GitHub Actions supported RAPIDS repository has, at a minimum, the following three GitHub Action workflow files:

- `pr.yaml` - [rmm workflow example](https://github.com/rapidsai/rmm/blob/branch-23.12/.github/workflows/pr.yaml), [rmm workflow run history](https://github.com/rapidsai/rmm/actions/workflows/pr.yaml)
- `build.yaml` - [rmm workflow example](https://github.com/rapidsai/rmm/blob/branch-23.12/.github/workflows/build.yaml), [rmm workflow run history](https://github.com/rapidsai/rmm/actions/workflows/build.yaml)
- `test.yaml` - [rmm workflow example](https://github.com/rapidsai/rmm/blob/branch-23.12/.github/workflows/test.yaml), [rmm workflow run history](https://github.com/rapidsai/rmm/actions/workflows/test.yaml)

These GitHub Action workflow files contain a description of all the automated jobs that run as a part of the workflow.

These jobs contain things like C++/Python builds, C++/Python tests, notebook tests, etc.

The chart below provides an overview of how each workflow file is used.

| Event:                            | Runs workflows:                 | Performs Builds? | Performs Tests? | Uploads to Anaconda.org/Wheel Registry? |
| --------------------------------- | ------------------------------- | :--------------: | :-------------: | :-------------------------------------: |
| - PRs                             | - `pr.yaml`                     | ✅               | ✅              | ❌                                      |
| - `branch-*` Merges<br>- Releases | - `build.yaml`                  | ✅               | ❌              | ✅                                      |
| - Nightlies                       | - `build.yaml`<br>- `test.yaml` | ✅               | ✅              | ✅                                      |

Although release workflows don't run tests, they do go through a week of nightly testing to ensure everything works as expected. See [this page]({% link releases/process.md %}) for more details about the release process.

## How Nightlies Are Triggered

Since RAPIDS consists of a collection of libraries that depend on each other, it's important that nightly builds and tests run in the correct order.

The [rapidsai/workflows](https://github.com/rapidsai/workflows) repository has a [nightly pipeline job](https://github.com/rapidsai/workflows/actions/workflows/nightly-pipeline.yaml) that is responsible for triggering jobs in the correct order.

An example workflow run can be seen in the screenshot below.

![](/assets/images/nightly_pipeline.png)

## Subscribing to Nightlies

A [recent blog post by GitHub](https://github.blog/changelog/2022-12-06-github-actions-workflow-notifications-in-slack-and-microsoft-teams/) explains how workflows can be subscribed to via Slack.

The gist of the article is that the following command can be run in any Slack channel to subscribe that channel to a particular workflow:

```sh
/github subscribe owner/repo workflows:{name: "workflow_name"}
```

Multiple workflow names can also be passed to the command in order to subscribe to multiple workflows (shown in example below).

For RAPIDS libraries, it is recommended to use the following commands to subscribe a particular Slack channel to branch build, nightly build, and nightly test workflow runs:

```sh
/github subscribe rapidsai/<repo> workflows:{name: "test","build"}
/github unsubscribe rapidsai/<repo> issues pulls commits releases deployments
```

The second step is necessary because the `/github subscribe`` command will also subscribe the channel to a lot of other GitHub events, which will contribute a lot of noise.

The `name` field in the `workflows` object corresponds to the name of a particular workflow (e.g. [this field](https://github.com/rapidsai/cudf/blob/66b846a01d418c51fb01126218d6b5e3fd83d405/.github/workflows/test.yaml#L1)).

To only subscribe to nightly builds and nightly tests (and not branch builds), the actor filter can be used:

```sh
/github subscribe rapidsai/<repo> workflows:{name: "test","build", actor:"GPUtester"}
```

The `GPUtester` account is a system account that’s used to trigger nightly workflow runs from an upstream workflow.

## Reusable Workflows

RAPIDS uses a collection of reusable GitHub Action workflows in order to single-source common build configuration settings. These reusable workflows can be found in the [rapidsai/shared-workflows](https://github.com/rapidsai/shared-workflows) repository.

An example of one of the reusable workflows used by RAPIDS is the [`conda-cpp-build.yaml` workflow](https://github.com/rapidsai/shared-workflows/blob/b5de46f0bb78115af9a4c80645faad3bb72b12be/.github/workflows/conda-cpp-build.yaml), which is the source of truth for which architectures and CUDA versions that RAPIDS C++ packages build for.

Similarly, the [`conda-cpp-tests.yaml` workflow](https://github.com/rapidsai/shared-workflows/blob/b5de46f0bb78115af9a4c80645faad3bb72b12be/.github/workflows/conda-cpp-tests.yaml) exists and specifies which configurations that RAPIDS tests it's C++ packages against.

The majority of these reusable workflows leverage the CI images from the [rapidsai/ci-imgs](https://github.com/rapidsai/ci-imgs/) repository.

## Reusable Shell Scripts

In addition to the reusable GitHub Action workflows, RAPIDS projects also leverage reusable shell scripts from the [rapidsai/gha-tools](https://github.com/rapidsai/gha-tools/) repository.

All of these shell scripts are prefixed with the string `rapids-`.

As an example, `rapids-print-env` is used to print common environment information.

`rapids-mamba-retry` is another tool that wraps the `mamba` executable to retry commands that fail due to transient issues like network problems.

## Downloading CI Artifacts

For NVIDIA employees with VPN access, artifacts from both pull-requests and branch builds can be accessed on [https://downloads.rapids.ai/](https://downloads.rapids.ai/).

There is a link provided at the end of every C++ and Python build job where the build artifacts for that particular workflow run can be accessed.

![](/assets/images/downloads.png)

## Using Conda CI Artifacts Locally

The artifacts that result from running `conda build` are conda channels. RAPIDS' CI system then compresses these conda channels into tarballs and uploads them to [https://downloads.rapids.ai/](https://downloads.rapids.ai/).

The packages in the conda channel can be used by extracting the tarball to your local filesystem and using the resulting path in your conda commands.

For example, the following snippet will download a pull request artifact for `librmm` and install it into the active conda environment:

```sh
wget https://downloads.rapids.ai/ci/rmm/pull-request/1376/5124d43/rmm_conda_cpp_cuda11_x86_64.tar.gz
mkdir local_channel
tar xzf rmm_conda_cpp_cuda11_x86_64.tar.gz -C local_channel/
mamba install --channel file://local_channel --channel rapidsai-nightly --channel conda-forge --channel nvidia librmm
```

## Using Wheel CI Artifacts Locally

RAPIDS' CI system compresses the wheels that it builds into tarballs and uploads them to [https://downloads.rapids.ai/](https://downloads.rapids.ai/).

The wheels can be used by extracting the tarball to your local filesystem and using the resulting path in your pip commands.

For example, the following snippet will download a pull request artifact for `librmm` and install it into the active conda environment:

```sh
wget https://downloads.rapids.ai/ci/rmm/pull-request/1376/5124d43/rmm_wheel_python_rmm_cu12_39_x86_64.tar.gz
mkdir wheels
tar xzf rmm_wheel_python_rmm_cu12_39_x86_64.tar.gz -C wheels/
pip install wheels/rmm_cu12-24.2.0a1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
```

## Using Conda CI Artifacts in Other PRs

For changes that cross library boundaries, it may be necessary to test a pull request to one library with changes from a pull request to another library.
Consider the overall RAPIDS dependency graph when testing.
For example, if you are testing artifacts from an RMM PR `rmm#A` in cuML, you probably also need to create a cuDF PR `cudf#B` that uses the artifacts from `rmm#A`, and then your cuML test PR will need to include the artifact channels for both `rmm#A` and `cudf#B`.

To do this, it is necessary to download CI artifacts (described in the above section) from one library during the CI workflow of another library.
First, determine the pull request number(s) to be tested from the other library.
Then, fetch the CI artifacts from the other library's pull request and use them when building and testing.
The example code below demonstrates building and testing with conda packages from other library PRs.
Replace the pull request numbers and library names as needed.
Remember that changes to use CI artifacts should be _temporary_ and should be reverted prior to merging any required changes in that PR.

**Example 1:** Building `libcuml` (C++) using `librmm`, `libraft`, `libcumlprims_mg` PR artifacts.

```sh
# ci/build_cpp.sh

LIBRMM_CHANNEL=$(rapids-get-pr-conda-artifact rmm 1095 cpp)
LIBRAFT_CHANNEL=$(rapids-get-pr-conda-artifact raft 1388 cpp)
LIBCUMLPRIMS_CHANNEL=$(rapids-get-pr-conda-artifact cumlprims_mg 129 cpp)

# Build library packages with the CI artifact channels providing the updated dependencies

rapids-mamba-retry mambabuild \
    --channel "${LIBRMM_CHANNEL}" \
    --channel "${LIBRAFT_CHANNEL}" \
    --channel "${LIBCUMLPRIMS_CHANNEL}" \
    conda/recipes/libcuml
```

**Example 2:** Testing `cudf` (Python) using `librmm`, `rmm`, and `libkvikio` PR artifacts.

```sh
# ci/test_python_common.sh

LIBRMM_CHANNEL=$(rapids-get-pr-conda-artifact rmm 1223 cpp)
RMM_CHANNEL=$(rapids-get-pr-conda-artifact rmm 1223 python)
LIBKVIKIO_CHANNEL=$(rapids-get-pr-conda-artifact kvikio 224 cpp)

# Install library packages with the CI artifact channels providing the updated dependencies for testing

rapids-mamba-retry install \
  --channel "${CPP_CHANNEL}" \
  --channel "${PYTHON_CHANNEL}" \
  --channel "${LIBRMM_CHANNEL}" \
  --channel "${LIBKVIKIO_CHANNEL}" \
  --channel "${RMM_CHANNEL}" \
  cudf libcudf
```

Note that the custom channel for PR artifacts is needed in the build scripts _and_ the test scripts, for C++ _and_ Python.
If building/testing a Python package that depends on a C++ library, it is necessary to use PR artifacts from that C++ library and not just Python (e.g. if testing `rmm` artifacts, you must use the corresponding `librmm` CI artifacts as well as `rmm`).
In some repos, the `test_python.sh` is quite complicated with multiple calls to conda/mamba.
We recommend that the Python and C++ artifact channels should be added to every call of `rapids-mamba-retry` / `rapids-conda-retry` "just in case."

Note: By default `rapids-get-pr-conda-artifact` uses the most recent commit from the specified PR.
A commit hash from the dependent PR can be added as an optional 4th argument to test with an earlier commit or to pin testing to a commit even if the dependent PR is updated.
## Skipping CI for Commits

See the GitHub Actions documentation page below on how to prevent GitHub Actions from running on certain commits. This is useful for preventing GitHub Actions from running on pull requests that are not fully complete. This also helps preserve the finite GPU resources provided by the RAPIDS Ops team.

With GitHub Actions, it is not possible to configure all commits for a pull request to be skipped. It must be specified at the commit level.

**Link**: [https://docs.github.com/en/actions/managing-workflow-runs/skipping-workflow-runs](https://docs.github.com/en/actions/managing-workflow-runs/skipping-workflow-runs)

## Rerunning Failed GitHub Actions

See the GitHub Actions documentation page below on how to rerun failed workflows. In addition to rerunning an entire workflow, GitHub Actions also provides the ability to rerun only the failed jobs in a workflow.

At this time there are no alternative ways to rerun tests with GitHub Actions beyond what is described in the documentation (e.g. there is no `rerun tests` comment for GitHub Actions).

**Link**: [https://docs.github.com/en/actions/managing-workflow-runs/re-running-workflows-and-jobs](https://docs.github.com/en/actions/managing-workflow-runs/re-running-workflows-and-jobs)
