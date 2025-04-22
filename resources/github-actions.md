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

- `pr.yaml` - [rmm workflow example](https://github.com/rapidsai/rmm/blob/branch-23.12/.github/workflows/pr.yaml), [rmm workflow run history](https://github.com/rapidsai/rmm/actions/workflows/pr.yaml)
- `build.yaml` - [rmm workflow example](https://github.com/rapidsai/rmm/blob/branch-23.12/.github/workflows/build.yaml), [rmm workflow run history](https://github.com/rapidsai/rmm/actions/workflows/build.yaml)
- `test.yaml` - [rmm workflow example](https://github.com/rapidsai/rmm/blob/branch-23.12/.github/workflows/test.yaml), [rmm workflow run history](https://github.com/rapidsai/rmm/actions/workflows/test.yaml)

These GitHub Actions workflow files contain a description of all the automated jobs that run as a part of the workflow.

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

The `GPUtester` account is a system account used to trigger nightly workflow runs from an upstream workflow.

## Reusable Workflows

RAPIDS uses a collection of reusable GitHub Actions workflows in order to single-source common build configuration settings.
These reusable workflows can be found in the [rapidsai/shared-workflows](https://github.com/rapidsai/shared-workflows) repository.

An example of one of the reusable workflows used by RAPIDS is the [`conda-cpp-build.yaml` workflow](https://github.com/rapidsai/shared-workflows/blob/b5de46f0bb78115af9a4c80645faad3bb72b12be/.github/workflows/conda-cpp-build.yaml), which is the source of truth for which architectures and CUDA versions build RAPIDS C++ packages.

Similarly, the [`conda-cpp-tests.yaml` workflow](https://github.com/rapidsai/shared-workflows/blob/b5de46f0bb78115af9a4c80645faad3bb72b12be/.github/workflows/conda-cpp-tests.yaml) specifies configurations for testing RAPIDS C++ packages.

The majority of these reusable workflows leverage the CI images from the [rapidsai/ci-imgs](https://github.com/rapidsai/ci-imgs/) repository.

## Reusable Shell Scripts

In addition to the reusable GitHub Actions workflows, RAPIDS projects also leverage reusable shell scripts from the [rapidsai/gha-tools](https://github.com/rapidsai/gha-tools/) repository.

All of these shell scripts are prefixed with the string `rapids-`.

As an example, `rapids-print-env` is used to print common environment information.

`rapids-mamba-retry` is another tool that wraps the `mamba` executable to retry commands that fail due to transient issues like network problems.

## Downloading CI Artifacts

Artifacts from both pull-requests and branch builds can be accessed on the GitHub UI for the specific workflow run, found in the Actions tab of the repository.

![](/assets/images/workflow-ui.png)

There is also a link provided in the `Run actions/upload-artifact@v4` step of every C++ and Python build job where the build artifacts for that particular job can be accessed.

![](/assets/images/downloads-github.png)

This link downloads the required artifact as a zip file.

This can also be done using the following `gh` CLI command to download the artifact. This command also unzips the artifact to the destination location:

```sh
gh run download <workflow-run-id> --repo <repo-name> --name <artifact-name> --dir <destination-directory>
```

For example, to download the artifact `rmm_conda_python_cuda11_py311_x86_64` from the workflow run ID `14437867406` on the `rmm` repository into the `/artifacts` directory, you can use this command:

```sh
gh run download 14437867406 --repo rapidsai/rmm --name rmm_conda_python_cuda11_py311_x86_64 --dir /artifacts
```

## Using Conda CI Artifacts Locally

The artifacts that result from running `conda build` are conda channels. RAPIDS' CI system uploads these conda channels to GitHub Artifacts as zip files.

The packages in the conda channel can be used by downloading the artifact to your local filesystem using `gh` CLI and using the resulting path in your conda commands.

For example, the following snippet will download an artifact for `librmm` from workflow run ID `14437867406` and install it into the active conda environment:

```sh
# Download and extract the artifact
gh run download 14437867406 --repo rapidsai/rmm -name rmm_conda_cpp_cuda11_x86_64 --dir local_channel
mamba install --channel file://local_channel --channel rapidsai-nightly --channel conda-forge --channel nvidia librmm
```

Note: Make sure you have the GitHub CLI (`gh`) installed and authenticated on your host machine to download artifacts from GitHub Artifacts. To download artifacts made for a specific PR, replace the workflow run ID with the ID of the run triggered by the PR branch.

## Using Wheel CI Artifacts Locally

RAPIDS' CI system compresses the wheels that it builds into zip files and uploads them to GitHub Artifacts.

The wheels can be used by downloading the artifact to your local filesystem using `gh` CLI and using the resulting path in your pip commands.

For example, the following snippet will download an artifact for `librmm` and install it into the active conda environment:

```sh
# Download and extract the artifact
gh run download 14437867406 --repo rapidsai/rmm --name rmm_wheel_python_rmm_cu12_py312_x86_64 --dir wheels
pip install wheels/rmm_cu12-25.6.0a23-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl
```

Note: Make sure you have the GitHub CLI (`gh`) installed and authenticated on your host machine to download artifacts from GitHub Artifacts. To download artifacts made for a specific PR, replace the workflow run ID with the ID of the run triggered by the PR branch.

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

**Example 1:** Building `libcuml` (C++) using `librmm` and `libraft` PR artifacts.

Add a new file called `ci/use_conda_packages_from_prs.sh`.

```shell
# ci/use_conda_packages_from_prs.sh

# download CI artifacts
LIBRAFT_CHANNEL=$(rapids-get-pr-conda-artifact-github raft 1388 cpp)
LIBRMM_CHANNEL=$(rapids-get-pr-conda-artifact-github rmm 1095 cpp)

# make sure they can be found locally
conda config --system --add channels "${LIBRAFT_CHANNEL}"
conda config --system --add channels "${LIBRMM_CHANNEL}"
```

Then copy the following into every script in the `ci/` directory that is doing `conda` installs.

```shell
source ./ci/use_conda_packages_from_prs.sh
```

**Example 2:** Testing `cudf` (Python) using `librmm`, `rmm`, and `libkvikio` PR artifacts.

It's important to include all of the recursive dependencies.
So, for example, Python testing jobs that use the `rmm` Python package also need the `librmm` C++ package.

```shell
# ci/use_conda_packages_from_prs.sh

# download CI artifacts
LIBKVIKIO_CHANNEL=$(rapids-get-pr-conda-artifact-github kvikio 224 cpp)
LIBRMM_CHANNEL=$(rapids-get-pr-conda-artifact-github rmm 1223 cpp)
RMM_CHANNEL=$(rapids-get-pr-conda-artifact-github rmm 1223 python)

# make sure they can be found locally
conda config --system --add channels "${LIBKVIKIO_CHANNEL}"
conda config --system --add channels "${LIBRMM_CHANNEL}"
conda config --system --add channels "${RMM_CHANNEL}"
```

Then copy the following into every script in the `ci/` directory that is doing `conda` installs.

```shell
source ./ci/use_conda_packages_from_prs.sh
```

**Note:** By default `rapids-get-pr-conda-artifact-github` uses the most recent commit from the specified PR.
A commit hash from the dependent PR can be added as an optional 4th argument to pin testing to a specific commit.

## Using Wheel CI Artifacts in Other PRs

To use wheels produced by other PRs' CI:

* download the wheels at the beginning of CI jobs
* constrain `pip` to always use them

Consider the following examples.

**Example:** Building `libcuml` (C++) using `librmm` and `libraft` PR artifacts.

Add a new file called `ci/use_wheels_from_prs.sh`.

```shell
# ci/use_wheels_from_prs.sh

RAPIDS_PY_CUDA_SUFFIX=$(rapids-wheel-ctk-name-gen "${RAPIDS_CUDA_VERSION}")

# download wheels, store the directories holding them in variables
LIBRMM_WHEELHOUSE=$(
  RAPIDS_PY_WHEEL_NAME="librmm_${RAPIDS_PY_CUDA_SUFFIX}" rapids-get-pr-wheel-artifact-github rmm 1678 cpp
)
LIBRAFT_WHEELHOUSE=$(
  RAPIDS_PY_WHEEL_NAME="libraft_${RAPIDS_PY_CUDA_SUFFIX}" rapids-get-pr-wheel-artifact-github raft 2433 cpp
)

# write a pip constraints file saying e.g. "whenever you encounter a requirement for 'librmm-cu12', use this wheel"
cat > /tmp/constraints.txt <<EOF
librmm-${RAPIDS_PY_CUDA_SUFFIX} @ file://$(echo ${LIBRMM_WHEELHOUSE}/librmm_*.whl)
libraft-${RAPIDS_PY_CUDA_SUFFIX} @ file://$(echo ${LIBRAFT_WHEELHOUSE}/libraft_*.whl)
EOF

export PIP_CONSTRAINT=/tmp/constraints.txt
```

Then copy the following into every script in the `ci/` directory that is doing `pip` installs or wheel builds with e.g. `pip wheel`.

```shell
source ./ci/use_wheels_from_prs.sh
```

This should generally be enough.
If any of the other CI scripts are already setting the environment variable `PIP_CONSTRAINT`, you may need to
modify them slightly to ensure they **append to**, instead of **overwriting**, the constraints set up by `use_wheels_from_prs.sh`.

**Example 2:** Testing `cudf` (Python) using `librmm`, `rmm`, and `libkvikio` PR artifacts.

It's important to include all of the recursive dependencies.
So, for example, Python testing jobs that use the `rmm` Python package also need the `librmm` C++ package.

```shell
# ci/use_wheels_from_prs.sh

RAPIDS_PY_CUDA_SUFFIX=$(rapids-wheel-ctk-name-gen "${RAPIDS_CUDA_VERSION}")

# download wheels, store the directories holding them in variables
LIBKVIKIO_WHEELHOUSE=$(
  RAPIDS_PY_WHEEL_NAME="libkvikio_${RAPIDS_PY_CUDA_SUFFIX}" rapids-get-pr-wheel-artifact-github kvikio 510 cpp
)
LIBRMM_WHEELHOUSE=$(
  RAPIDS_PY_WHEEL_NAME="librmm_${RAPIDS_PY_CUDA_SUFFIX}" rapids-get-pr-wheel-artifact-github rmm 1678 cpp
)
RMM_WHEELHOUSE=$(
  RAPIDS_PY_WHEEL_NAME="rmm_${RAPIDS_PY_CUDA_SUFFIX}" rapids-get-pr-wheel-artifact-github rmm 1678 python
)

# write a pip constraints file saying e.g. "whenever you encounter a requirement for 'librmm-cu12', use this wheel"
cat > /tmp/constraints.txt <<EOF
libkvikio-${RAPIDS_PY_CUDA_SUFFIX} @ file://$(echo ${LIBKVIKIO_WHEELHOUSE}/libkvikio_*.whl)
librmm-${RAPIDS_PY_CUDA_SUFFIX} @ file://$(echo ${LIBRMM_WHEELHOUSE}/librmm_*.whl)
rmm-${RAPIDS_PY_CUDA_SUFFIX} @ file://$(echo ${RMM_WHEELHOUSE}/rmm_*.whl)
EOF

export PIP_CONSTRAINT=/tmp/constraints.txt
```

Then copy the following into every script in the `ci/` directory that is doing `pip` installs or wheel builds with e.g. `pip wheel`.

```shell
source ./ci/use_wheels_from_prs.sh
```

As above, if any of the other CI scripts are already setting the environment variable `PIP_CONSTRAINT`, you may need to
modify them slightly to ensure they **append to**, instead of **overwriting**, the constraints set up by `use_wheels_from_prs.sh`.

**Note:** By default `rapids-get-pr-wheel-artifact-github` uses the most recent commit from the specified PR.
A commit hash from the dependent PR can be added as an optional 4th argument to pin testing to a specific commit.

## Skipping CI for Commits

See the GitHub Actions documentation page below on how to prevent GitHub Actions from running on certain commits. This is useful for preventing GitHub Actions from running on pull requests that are not fully complete. This also helps preserve the finite GPU resources provided by the RAPIDS Ops team.

With GitHub Actions, it is not possible to configure all commits for a pull request to be skipped. It must be specified at the commit level.

**Link**: [https://docs.github.com/en/actions/managing-workflow-runs/skipping-workflow-runs](https://docs.github.com/en/actions/managing-workflow-runs/skipping-workflow-runs)

## Rerunning Failed GitHub Actions

See the GitHub Actions documentation page below on how to rerun failed workflows. In addition to rerunning an entire workflow, GitHub Actions also provides the ability to rerun only the failed jobs in a workflow.

At this time there are no alternative ways to rerun tests with GitHub Actions beyond what is described in the documentation (e.g. there is no `rerun tests` comment for GitHub Actions).

**Link**: [https://docs.github.com/en/actions/managing-workflow-runs/re-running-workflows-and-jobs](https://docs.github.com/en/actions/managing-workflow-runs/re-running-workflows-and-jobs)
