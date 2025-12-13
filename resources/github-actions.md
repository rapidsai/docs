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

Every RAPIDS repository using GitHub Actions has, at a minimum, the following three GitHub Action workflow files:

- `pr.yaml` - [rmm workflow example](https://github.com/rapidsai/rmm/blob/main/.github/workflows/pr.yaml), [rmm workflow run history](https://github.com/rapidsai/rmm/actions/workflows/pr.yaml)
- `build.yaml` - [rmm workflow example](https://github.com/rapidsai/rmm/blob/main/.github/workflows/build.yaml), [rmm workflow run history](https://github.com/rapidsai/rmm/actions/workflows/build.yaml)
- `test.yaml` - [rmm workflow example](https://github.com/rapidsai/rmm/blob/main/.github/workflows/test.yaml), [rmm workflow run history](https://github.com/rapidsai/rmm/actions/workflows/test.yaml)

These GitHub Actions workflow files contain a description of all the automated jobs that run as a part of the workflow.

These jobs contain things like C++/Python builds, C++/Python tests, notebook tests, etc.

The chart below provides an overview of how each workflow file is used.

| Event:                             | Runs workflows:                 | Performs Builds? | Performs Tests? | Uploads to Anaconda.org/Wheel Registry? |
| ---------------------------------- | ------------------------------- | :--------------: | :-------------: | :-------------------------------------: |
| - PRs                              | - `pr.yaml`                     | ✅               | ✅              | ❌                                      |
| - `release/*` Merges<br>- Releases | - `build.yaml`                  | ✅               | ❌              | ✅                                      |
| - Nightlies                        | - `build.yaml`<br>- `test.yaml` | ✅               | ✅              | ✅                                      |

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

The `GPUtester` account is a system account used to trigger nightly workflow runs from an upstream workflow.

## Reusable Workflows

RAPIDS uses a collection of reusable GitHub Actions workflows in order to single-source common build configuration settings.
These reusable workflows can be found in the [rapidsai/shared-workflows](https://github.com/rapidsai/shared-workflows) repository.

An example of one of the reusable workflows used by RAPIDS is the [`conda-cpp-build.yaml` workflow](https://github.com/rapidsai/shared-workflows/blob/main/.github/workflows/conda-cpp-build.yaml), which is the source of truth for which architectures and CUDA versions build RAPIDS C++ packages.

Similarly, the [`conda-cpp-tests.yaml` workflow](https://github.com/rapidsai/shared-workflows/blob/main/.github/workflows/conda-cpp-tests.yaml) specifies configurations for testing RAPIDS C++ packages.

The majority of these reusable workflows leverage the CI images from the [rapidsai/ci-imgs](https://github.com/rapidsai/ci-imgs/) repository.

## Reusable Shell Scripts

In addition to the reusable GitHub Actions workflows, RAPIDS projects also leverage reusable shell scripts from the [rapidsai/gha-tools](https://github.com/rapidsai/gha-tools/) repository.

All of these shell scripts are prefixed with the string `rapids-`.

As an example, `rapids-print-env` is used to print common environment information.

`rapids-mamba-retry` is another tool that wraps the `mamba` executable to retry commands that fail due to transient issues like network problems.

## Downloading CI Artifacts

CI artifacts are uploaded to the GitHub Actions artifact store.

Artifacts produced in public repositories can generally be accessed by anyone, using the methods described below.[^1]

### Finding Artifacts in the GitHub UI

Those artifacts are visible in the GitHub Actions UI.
Navigate to the `Actions` tab, then select a specific workflow run.
Scroll down to the "Artifacts" section of the run summary.

![](/assets/images/workflow-ui.png)

There is also a link provided in the `Run actions/upload-artifact` step of every build job where the build artifacts for that particular job can be accessed.

![](/assets/images/downloads-github.png)

That link returns the corresponding artifact as a zip file.

### Downloading Artifacts Programmatically

Artifacts can also be downloaded programmatically using the `gh` CLI ([docs](https://cli.github.com/manual/)).

To download artifacts, you must authenticate with GitHub, using a personal access token that has the `repo` scope.
Do one of the following to authenticate:

* set environment variable `GH_TOKEN` to a GitHub personal access token with at least the `repo` scope
* log in interactively by running `gh auth login`

For more details, see the `gh` CLI authentication docs ([link](https://cli.github.com/manual/gh_auth_login)).

After authenticating, artifacts can be downloaded with the following command:

```shell
gh run download \
  {workflow-run-id} \
  --repo {org}/{repo} \
  --name {artifact-name} \
  --dir {destination-directory}
```

Where those inputs are defined as follows:

* `{workflow-run-id}` = the unique identifier for a GitHub Actions workflow run
* `{org}/{repo}` = the repository the workflow run occurred in (e.g. `rapidsai/rmm`)
* `{artifact-name}` = unique identifier for an artifact within one workflow run (e.g. `rmm_conda_python_cuda12_py312_x86_64`)
* `{destination-directory}` = local directory the artifact's contents should be decompressed to

The `{org}`, `{repo}`, and `{workflow-run-id}` can be found in the URL for CI jobs.
Those URLs are of the form `https://github.com/{org}/{repo}/actions/runs/{workflow-run-id}`

Valid values for `{artifact-name}` can be found on the "Actions" tab in the GitHub Actions UI, as described in "Finding Artifacts in the GitHub UI" above.
The run IDs can also be identified programmatically.

For example, the following sequence of commands accomplishes the task *"download the latest `rmm` Python 3.12, CUDA 12 conda packages built from `main`"*.

```shell
# get the most recent successful main nightly or branch build
RUN_ID=$(
  gh run list \
    --repo "rapidsai/rmm" \
    --branch "main" \
    --workflow "build.yaml" \
    --status "success" \
    --json "createdAt,databaseId" \
    --jq 'sort_by(.createdAt) | reverse | .[0] | .databaseId'
)

# create a temporary directory to store files
RMM_CHANNEL="$(mktemp -d)"

# download files
gh run download \
  "${RUN_ID}" \
  --repo "rapidsai/rmm" \
  --name "rmm_conda_python_cuda12_py312_x86_64" \
  --dir "${RMM_CHANNEL}"

# inspect the files that were downloaded
ls "${RMM_CHANNEL}"
```

### Using Conda CI Artifacts Locally

The artifacts that result from running `conda build` are conda channels.
RAPIDS' CI system uploads these conda channels to the GitHub Actions artifact store as zip files.

To use these:

* identify the GitHub Actions workflow run ID that produced the artifacts you want
* download them to local directories using the `gh` CLI
* pass the paths to those directories as channels via `--channel` to `conda` / `mamba` commands

For example, to create a conda environment that uses the latest `librmm` and `rmm` conda packages built from `main` on an x86_64, CUDA 12 system:

```shell
# get the most recent successful nightly or branch build
RUN_ID=$(
  gh run list \
    --repo "rapidsai/rmm" \
    --branch "main" \
    --workflow "build.yaml" \
    --status 'success' \
    --json 'createdAt,databaseId' \
    --jq 'sort_by(.createdAt) | reverse | .[0] | .databaseId'
)

# create temporary directories to store packages
LIBRMM_CHANNEL="$(mktemp -d)"
RMM_CHANNEL="$(mktemp -d)"

# download packages
gh run download \
  "${RUN_ID}" \
  --repo "rapidsai/rmm" \
  --name "rmm_conda_cpp_cuda12_x86_64" \
  --dir "${LIBRMM_CHANNEL}"

gh run download \
  "${RUN_ID}" \
  --repo "rapidsai/rmm" \
  --name "rmm_conda_python_cuda12_py312_x86_64" \
  --dir "${RMM_CHANNEL}"

# create conda environment
conda create \
  --yes \
  --name rmm-test-env \
  --channel "${LIBRMM_CHANNEL}" \
  --channel "${RMM_CHANNEL}" \
  --channel rapidsai-nightly \
  --channel conda-forge \
    librmm \
    rmm
```

Because those build artifacts contain conda *channels* and not just packages, you can also use `conda search` to inspect them.

Like this:

```shell
conda search \
  --override-channels \
  --channel "${RMM_CHANNEL}" \
  --info \
      rmm
```

That produces a summary like this:

```text
rmm 25.08.00a32 cuda12_py312_250509_dbd8cc7a
--------------------------------------------
file name   : rmm-25.08.00a32-cuda12_py312_250509_dbd8cc7a.conda
name        : rmm
version     : 25.08.00a32
build       : cuda12_py312_250509_dbd8cc7a
build number: 0
size        : 430 KB
license     : Apache-2.0
subdir      : linux-64
url         : file:///tmp/tmp.LfkdLFvzzj/linux-64/rmm-25.08.00a32-cuda12_py312_250509_dbd8cc7a.conda
md5         : fd3ceea32ef3aee44cb207602668cf8d
timestamp   : 2025-05-09 05:10:10 UTC
dependencies:
  - cuda-cudart
  - cuda-python >=12.6.2,<13.0a0
  - cuda-version >=12,<13.0a0
  - numpy >=1.23,<3.0a0
  - python
  - libstdcxx >=13
  - libgcc >=13
  - __glibc >=2.28,<3.0.a0
  - librmm >=25.6.0a32,<25.7.0a0
  - python_abi 3.12.* *_cp312
```

### Using Wheel CI Artifacts Locally

RAPIDS' CI system uploads wheels that it builds to the GitHub Actions artifact store as zip files.

To use these:

* identify the GitHub Actions workflow run ID that produced the artifacts you want
* download them to local directories using the `gh` CLI
* pass the paths to wheels in those directories to installers like `pip` or `uv`

For example, to create a virtual environment with `librmm` and `rmm` packages built from `main` on an x86_64, CUDA 12 system:

```shell
# create virtualenv
python -m venv ./rmm-test-env
source ./rmm-test-env/bin/activate

# get the most recent successful nightly or branch build
RUN_ID=$(
  gh run list \
    --repo "rapidsai/rmm" \
    --branch "main" \
    --workflow "build.yaml" \
    --status 'success' \
    --json 'createdAt,databaseId' \
    --jq 'sort_by(.createdAt) | reverse | .[0] | .databaseId'
)

# create temporary directories to store wheels
LIBRMM_WHEELHOUSE="$(mktemp -d)"
RMM_WHEELHOUSE="$(mktemp -d)"

# figure out Python version in the venv
PY_VERSION=$(python -c 'from sys import version_info as vi; print(f"{vi.major}{vi.minor}")')

# download packages
gh run download \
  "${RUN_ID}" \
  --repo "rapidsai/rmm" \
  --name "rmm_wheel_cpp_librmm_cu12_x86_64" \
  --dir "${LIBRMM_WHEELHOUSE}"

gh run download \
  "${RUN_ID}" \
  --repo "rapidsai/rmm" \
  --name "rmm_wheel_python_rmm_cu12_py${PY_VERSION}_x86_64" \
  --dir "${RMM_WHEELHOUSE}"

# install into the environment
python -m pip install \
  "${LIBRMM_WHEELHOUSE}"/librmm_*.whl \
  "${RMM_WHEELHOUSE}"/rmm_*.whl
```

### Using Conda CI Artifacts in Other PRs

For changes that cross library boundaries, it may be necessary to test a pull request to one library with changes from a pull request to another library.
Consider the overall RAPIDS dependency graph when testing.
For example, if you are testing artifacts from an RMM PR `rmm#A` in cuML, you probably also need to create a cuDF PR `cudf#B` that uses the artifacts from `rmm#A`, and then your cuML test PR will need to include the artifact channels for both `rmm#A` and `cudf#B`.

To do this, it is necessary to download CI artifacts (described in the above section) from one library during the CI workflow of another library.
First, determine the pull request number(s) to be tested from the other library.
Then, fetch the CI artifacts from the other library's pull request and use them when building and testing.
The example code below demonstrates building and testing with conda packages from other library PRs.
Replace the pull request numbers and library names as needed.

Remember that changes to use CI artifacts should be _temporary_ and should be reverted prior to merging any required changes in that PR.

**Example 1:** Building `libcuml` (C++) using `librmm` and `libraft` PR artifacts.

Add a new file called `ci/use_conda_packages_from_prs.sh`.

```shell
#!/bin/bash
# Copyright (c) 2025, NVIDIA CORPORATION.

# download CI artifacts
LIBRAFT_CHANNEL=$(rapids-get-pr-artifact raft 789 python conda)
LIBRMM_CHANNEL=$(rapids-get-pr-artifact rmm 1909 cpp conda)

# For `rattler` builds:
#
# Add these channels to the array checked by 'rapids-rattler-channel-string'.
# This ensures that when conda packages are built with strict channel priority enabled,
# the locally-downloaded packages will be preferred to remote packages (e.g. nightlies).
#
RAPIDS_PREPENDED_CONDA_CHANNELS=(
    "${LIBRAFT_CHANNEL}"
    "${LIBRMM_CHANNEL}"
)
export RAPIDS_PREPENDED_CONDA_CHANNELS

# For tests and `conda-build` builds:
#
# Add these channels to the system-wide conda configuration.
# This results in PREPENDING them to conda's channel list, so
# these packages should be found first if strict channel priority is enabled.
#
for _channel in "${RAPIDS_PREPENDED_CONDA_CHANNELS[@]}"
do
   conda config --system --add channels "${_channel}"
done
```

Then copy the following into every script in the `ci/` directory that is doing `conda` installs.

```shell
source ./ci/use_conda_packages_from_prs.sh
```

**Example 2:** Testing `cudf` (Python) using `librmm`, `rmm`, and `libkvikio` PR artifacts.

It's important to include all of the recursive dependencies.
So, for example, Python testing jobs that use the `rmm` Python package also need the `librmm` C++ package.

```shell
#!/bin/bash
# Copyright (c) 2025, NVIDIA CORPORATION.

# download CI artifacts
LIBKVIKIO_CHANNEL=$(rapids-get-pr-artifact kvikio 224 cpp conda)
LIBRMM_CHANNEL=$(rapids-get-pr-artifact rmm 1223 cpp conda)
RMM_CHANNEL=$(rapids-get-pr-artifact rmm 1223 python conda)

# For `rattler` builds:
#
# Add these channels to the array checked by 'rapids-rattler-channel-string'.
# This ensures that when conda packages are built with strict channel priority enabled,
# the locally-downloaded packages will be preferred to remote packages (e.g. nightlies).
#
RAPIDS_PREPENDED_CONDA_CHANNELS=(
    "${LIBKVIKIO_CHANNEL}"
    "${LIBRMM_CHANNEL}"
    "${RMM_CHANNEL}"
)
export RAPIDS_PREPENDED_CONDA_CHANNELS

# For tests and `conda-build` builds:
#
# Add these channels to the system-wide conda configuration.
# This results in PREPENDING them to conda's channel list, so
# these packages should be found first if strict channel priority is enabled.
#
for _channel in "${RAPIDS_PREPENDED_CONDA_CHANNELS[@]}"
do
   conda config --system --add channels "${_channel}"
done
```

Then copy the following into every script in the `ci/` directory that is doing `conda` installs.

```shell
source ./ci/use_conda_packages_from_prs.sh
```

**Note:** By default `rapids-get-pr-artifact` uses the most recent commit from the specified PR.
A commit hash from the dependent PR can be added as an optional 4th argument to pin testing to a specific commit.

### Using Wheel CI Artifacts in Other PRs

To use wheels produced by other PRs' CI:

* download the wheels at the beginning of CI jobs
* constrain `pip` to always use them

Consider the following examples.

**Example:** Building `libcuml` (C++) using `librmm` and `libraft` PR artifacts.

Add a new file called `ci/use_wheels_from_prs.sh`.

```shell
#!/bin/bash
# Copyright (c) 2025, NVIDIA CORPORATION.

# initialize PIP_CONSTRAINT
source rapids-init-pip

RAPIDS_PY_CUDA_SUFFIX=$(rapids-wheel-ctk-name-gen "${RAPIDS_CUDA_VERSION}")

# download wheels, store the directories holding them in variables
LIBRAFT_WHEELHOUSE=$(
  RAPIDS_PY_WHEEL_NAME="libraft_${RAPIDS_PY_CUDA_SUFFIX}" rapids-get-pr-artifact raft 2433 cpp wheel
)
LIBRMM_WHEELHOUSE=$(
  RAPIDS_PY_WHEEL_NAME="librmm_${RAPIDS_PY_CUDA_SUFFIX}" rapids-get-pr-artifact rmm 1909 cpp wheel
)

# write a pip constraints file saying e.g. "whenever you encounter a requirement for 'librmm-cu12', use this wheel"
cat > "${PIP_CONSTRAINT}" <<EOF
libraft-${RAPIDS_PY_CUDA_SUFFIX} @ file://$(echo ${LIBRAFT_WHEELHOUSE}/libraft_*.whl)
librmm-${RAPIDS_PY_CUDA_SUFFIX} @ file://$(echo ${LIBRMM_WHEELHOUSE}/librmm_*.whl)
EOF
```

Then copy the following into every script in the `ci/` directory that is doing `pip` installs or wheel builds with e.g. `pip wheel`.

```shell
source ./ci/use_wheels_from_prs.sh
```

This should generally be enough.

**Example 2:** Testing `cudf` (Python) using `librmm`, `rmm`, and `libkvikio` PR artifacts.

It's important to include all of the recursive dependencies.
So, for example, Python testing jobs that use the `rmm` Python package also need the `librmm` C++ package.

```shell
#!/bin/bash
# Copyright (c) 2025, NVIDIA CORPORATION.

# initialize PIP_CONSTRAINT
source rapids-init-pip

RAPIDS_PY_CUDA_SUFFIX=$(rapids-wheel-ctk-name-gen "${RAPIDS_CUDA_VERSION}")

# download wheels, store the directories holding them in variables
LIBKVIKIO_WHEELHOUSE=$(
  RAPIDS_PY_WHEEL_NAME="libkvikio_${RAPIDS_PY_CUDA_SUFFIX}" rapids-get-pr-artifact kvikio 510 cpp wheel
)
LIBRMM_WHEELHOUSE=$(
  RAPIDS_PY_WHEEL_NAME="librmm_${RAPIDS_PY_CUDA_SUFFIX}" rapids-get-pr-artifact rmm 1678 cpp wheel
)
RMM_WHEELHOUSE=$(
  RAPIDS_PY_WHEEL_NAME="rmm_${RAPIDS_PY_CUDA_SUFFIX}" rapids-get-pr-artifact rmm 1678 python wheel
)

# write a pip constraints file saying e.g. "whenever you encounter a requirement for 'librmm-cu12', use this wheel"
cat > "${PIP_CONSTRAINT}" <<EOF
libkvikio-${RAPIDS_PY_CUDA_SUFFIX} @ file://$(echo ${LIBKVIKIO_WHEELHOUSE}/libkvikio_*.whl)
librmm-${RAPIDS_PY_CUDA_SUFFIX} @ file://$(echo ${LIBRMM_WHEELHOUSE}/librmm_*.whl)
rmm-${RAPIDS_PY_CUDA_SUFFIX} @ file://$(echo ${RMM_WHEELHOUSE}/rmm_*.whl)
EOF
```

Then copy the following into every script in the `ci/` directory that is doing `pip` installs or wheel builds with e.g. `pip wheel`.

```shell
source ./ci/use_wheels_from_prs.sh
```

**Note:** By default `rapids-get-pr-artifact` uses the most recent commit from the specified PR.
A commit hash from the dependent PR can be added as an optional 4th argument to pin testing to a specific commit.

## Skipping CI for Commits

See the GitHub Actions documentation page below on how to prevent GitHub Actions from running on certain commits. This is useful for preventing GitHub Actions from running on pull requests that are not fully complete. This also helps preserve the finite GPU resources provided by the RAPIDS Ops team.

With GitHub Actions, it is not possible to configure all commits for a pull request to be skipped. It must be specified at the commit level.

**Link**: [https://docs.github.com/en/actions/managing-workflow-runs/skipping-workflow-runs](https://docs.github.com/en/actions/managing-workflow-runs/skipping-workflow-runs)

## Rerunning Failed GitHub Actions

See the GitHub Actions documentation page below on how to rerun failed workflows. In addition to rerunning an entire workflow, GitHub Actions also provides the ability to rerun only the failed jobs in a workflow.

At this time there are no alternative ways to rerun tests with GitHub Actions beyond what is described in the documentation (e.g. there is no `rerun tests` comment for GitHub Actions).

**Link**: [https://docs.github.com/en/actions/managing-workflow-runs/re-running-workflows-and-jobs](https://docs.github.com/en/actions/managing-workflow-runs/re-running-workflows-and-jobs)

<hr>

[^1]: Using CI artifacts from private repositories requires some additional configuration. `rapidsai` organization members, see [https://github.com/rapidsai/kb/issues/54](https://github.com/rapidsai/kb/issues/54).
