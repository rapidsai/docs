---
layout: default
nav_order: 4
parent: RAPIDS Maintainer Docs
title: gpuCI
---

# gpuCI Technical Documentation

## Overview

Outlines how gpuCI is configured for RAPIDS and how to integrate other projects

gpuCI is accessible here: <https://gpuci.gpuopenanalytics.com/>

### Intended audience

Developers
{: .label .label-green}

Project Leads
{: .label .label-blue}

Operations
{: .label .label-purple}

## Infrastructure

This is an overview of the tools used in gpuCI

### Jenkins

Jenkins is an open source project for CI/CD and general automation that is very extensible and well adopted

### gpuCI

gpuCI is made of two pieces: definitions for standardized build and test scripts in all RAPIDS projects' repositories and code to generate the Jenkins build jobs which use those standardized scripts.

The build and scripts are used for
- CPU builds with conda
- GPU builds & unit tests
- Executing style & changelog checks

This standardization allows for scripts to create and config jobs. These generation scripts are planned to be open sourced soon.
- [https://gpuci.gpuopenanalytics.com/view/all/job/Rapids Seed Job/](https://gpuci.gpuopenanalytics.com/view/all/job/Rapids%20Seed%20Job/)
- Uses Jenkins job-dsl plugin
- Creates all the Jenkins jobs for every RAPIDS project
- Handles the bi-directional links between Jenkins & GitHub

### remote-docker-plugin

gpuCI uses a custom [plugin](https://github.com/gpuopenanalytics/remote-docker-plugin) written and open sourced by RAPIDS to better handle GPU testing on Jenkins using [nvidia-docker](https://github.com/NVIDIA/nvidia-docker).

### Docker containers

All jobs which use Docker run inside of the `gpuci/rapidsai-base` images.

[Docker Hub](https://hub.docker.com/r/gpuci/rapidsai-base)

[GitHub](https://github.com/rapidsai/gpuci-build-environment)

#### Conda environment

The images contain a common conda environment with basic tools such as `python`, `cmake`, `make`, `cython`, and `flake8`. See the full list [here](https://github.com/rapidsai/gpuci-build-environment/blob/main/Dockerfile#L66)

The conda environment can be used in the scripts with `source activate rapids`

## Jobs

### Pull requests

Pull requests trigger test builds using [GitHub pull request builder plugin](https://wiki.jenkins.io/display/JENKINS/GitHub+pull+request+builder+plugin).

Each PR is built with the following four types of jobs.

#### Changelog

Uses the `ci/checks/changelog.sh` script to determine success or failure

#### Style

Uses the `ci/checks/style.sh` script to determine success or failure

#### CPU builds

Each PR is built in a container with a matrix of parameters:
- CUDA 10.1, 10.2 & 11.0
- Python 3.7 & 3.8

This allows for testing compilation against multiple CUDA and Python versions.

#### GPU build

Each PR is built in a container using CUDA {{ site.data.versions.CUDA_VER }} and Python {{ site.data.versions.PYTHON_VER }}. the purpose of this job is primarily for testing with a GPU present.

Due to limited GPU resources and high volume of pull requests, it's not currently practical to matrix test GPUs. In the future, artifacts produced in the CPU steps will be reused in a matrix of GPU tests so GPU resources are used only to test instead of compiling and testing.

### Branch

Branch builds occur when a PR is merged and once per day. Currently, which branches to build is manually configured.

#### CPU builds

Each branch is built in a container with a matrix of parameters:
- CUDA 10.1, 10.2 & 11.0
- Python 3.7 & 3.8

These builds can publish nightly conda packages.

#### GPU build

Each branch is built in a container using CUDA {{ site.data.versions.CUDA_VER }} and Python {{ site.data.versions.PYTHON_VER }}. the purpose of this job is primarily for testing with a GPU present.

#### Auto-mergers

During the release process, the branch for the next release is created and set as default. Once this happens, the auto-merger branch jobs are activated. Auto-mergers automatically merge any commits made to the release branch to the latest default branch during burn down.

**When Auto Merging Fails**

It is important to note that the auto-merge jobs will sometimes fail due to merge conflicts, and will request a manual merge to be done. *Never* use the GitHub Web UI to fix the merge conflicts as it will cause changes in the default branch to be merged into the release branch. Please use the following steps to fix the merge conflicts manually:

Using the example of `branch-{{ site.data.releases.stable.version }}` release branch and a new default `branch-{{ site.data.releases.nightly.version }}`.

```
git checkout branch-{{ site.data.releases.stable.version }}
git pull <rapidsai remote>
git checkout branch-{{ site.data.releases.nightly.version }}
git pull <rapidsai remote>
git checkout -b branch-{{ site.data.releases.nightly.version }}-merge-{{ site.data.releases.stable.version }}
git merge branch-{{ site.data.releases.stable.version }}
# Fix any merge conflicts caused by this merge
git commit -am "Merge branch-{{ site.data.releases.stable.version }} into branch-{{ site.data.releases.nightly.version }}"
git push <personal fork> branch-{{ site.data.releases.nightly.version }}-merge-{{ site.data.releases.stable.version }}
```

Once this is done, open a PR that targets the new default branch (`branch-{{ site.data.releases.nightly.version }}` in this example) with your changes. 

**IMPORTANT**: Before merging and approving this PR, be sure to change the merging strategy to `Create a Merge Commit`. Otherwise, history will be lost and the branches become incompatible.

Once this PR is approved and merged, the auto-merger PR should automatically be merged since it will contain the same commit hashes.

## Scripts

These scripts are a standardized way for gpuCI to build projects. This allows for rapid integration and immediate feedback in pull requests on build changes.

All scripts are executed with the working directory as the project's root directory. For example, the prebuild script is run as `source ci/cpu/prebuid.sh`. Keep this in mind if the scripts need to access other files or scripts in the project.

### Directory structure

- ci
    - checks
        - `changelog.sh`
        - `style.sh`
    - cpu
        - `prebuild.sh`
        - `build.sh`
    - gpu
        - `prebuild.sh`
        - `build.sh`
    - releases
        - `update-version.sh`

### ci/checks/changelog.sh

- Required: No
- Job type: PR only
- Docker: `gpuci/rapidsai-base:cuda10.0-ubuntu16.04-gcc5-py3.6`

Executed as a check to see if the changelog was updated. It's up the scripts to determine if the changelog was updated and exit with 0 for success or non-zero for error.

If not provided, a simple check of whether `CHANGELOG.md` has been updated and if it contains the `PR_ID`.

### ci/checks/style.sh

- Required: Yes
- Job type: PR only
- Docker: `gpuci/rapidsai-base:cuda10.0-ubuntu16.04-gcc5-py3.6`
- Variables:
  - PR_ID
  - COMMIT_HASH
  - REPORT_HASH
  - DOCKER_IMAGE

Executed as a check to ensure code style is correct. `flake8` is available in the common conda environment.

### ci/cpu/prebuild.sh

- Required: No
- Job type: Both
- Docker: `gpuci/rapidsai-base:cuda${CUDA}-ubuntu${UBUNTU}-gcc5-py${PYTHON}`

If provided, gpuCI will source this file before building. This allows for setting any environment variables required for the build script. For example,  translating `CUDA` or `PYTHON`, or setting a variable to enable additional tests for some combinations of `CUDA` and `PYTHON`.

Many RAPIDS projects have two components: python and C/C++. For these projects, this script sets variables to prevent duplicate builds which speeds up testing.

### ci/cpu/build.sh

- Required: Yes
- Job type: Both
- Docker: `gpuci/rapidsai-base:cuda${CUDA}-ubuntu${UBUNTU}-gcc5-py${PYTHON}`

This script actually builds the code inside of a container. For most RAPIDS projects this means building the conda package. There is no GPU available, so testing in this script is limited to CPU only code.

Additionally, this script should upload packages to Anaconda if necessary. The `GIT_BRANCH` variable can be used to determine what type of build:
- `COMMIT_HASH` for PRs
- `branch-x.y` for development branch builds
- `main` for release builds

### ci/gpu/prebuild.sh

- Required: No
- Job type: Both
- Docker: `gpuci/rapidsai-base:cuda10.0-ubuntu16.04-gcc5-py$3.6`

If provided, gpuCI will source this file before building. This allows for setting any environment variables required for the build script.

### ci/gpu/build.sh

- Required: Yes
- Job type: Both
- Docker: `gpuci/rapidsai-base:cuda10.0-ubuntu16.04-gcc5-py$3.6`

This script actually builds the code inside of a container. A GPU is available so this script should execute any tests requiring a GPU.

If the tests output in in XML format in `test-results/*.xml` or a file named `junit*.xml`, the results will be published on Jenkins.

### ci/releases/update-version.sh

- Required: Only if auto-releasing is enabled
- Job type: Main Branch only
- Docker: No

This script is run with a parameter of `major`, `minor`, or `patch` to indicate what to release. gpuCI determines this based on where the commit is coming from. Merge commits from `branch-*` are minor releases whereas commits directly to main are patch releases. Major releases must be manually triggered.

The script should calculate the next version and update the source code, build scripts, and documentation with the new version.

**Note:** The script must export `NEXT_FULL_TAG` as the full `x.y.z` version.

After this, gpuCI will commit the changes and tag the commit with `v${NEXT_FULL_TAG}` before pushing to the repository.

## Environment variables

gpuCI exposes various environment variables that the CI scripts can utilize.

`BUILD_MODE` is either `pull-request` or `branch` for PR builds and branch builds respectively.

`BUILD_TYPE` is one of:
1. `cpu` - For CPU jobs using the `ci/cpu/` scripts
2. `gpu` - For GPU jobs using the `ci/gpu/` scripts
3. `style` - For the style checker job using the `ci/checks/style.sh` script
4. `changelog` - For the changelog checker job using the `ci/checks/changelog.sh` script
5. `gpu-matrix` - For full GPU matrix test job using the `ci/gpu` scripts

Other variables:
- `SOURCE_BRANCH` - The name of the branch being built. For pull requests, this is the head (or compare) branch.
- `COMMIT_HASH` - The current commit being built. For pull requests, this is `pull/${PR_ID}/merge` (for GitHub builds). For branch builds, this is the tip of the branch.
- `CUDA` - The current version of CUDA being used for the build formatted as `major.minor` (`10.1` or `11.0`)
- `PYTHON` - The current version of Python being used for the build formatted as `major.minor` (`3.7` or `3.8`)

During a pull request build, the following environment variables are exposed:
- `PR_ID` - The numeric ID of the pull request
- `PR_AUTHOR` - The username of who opened pull request
- `TARGET_BRANCH` - The base branch of the pull request
- `REPORT_HASH` - The git hash for reporting GitHub status. This is typically equivalent to `pull/${PR_ID}/head`.

### Project flash

- `PROJECT_FLASH` - Set to `1` when Project Flash is enabled for the build
- `FLASH_ID` - Unique identifier used to mark artifacts passed between Project Flash builds
