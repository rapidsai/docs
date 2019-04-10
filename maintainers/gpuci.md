---
layout: default
nav_order: 4
parent: RAPIDS Maintainer Docs
title: gpuCI
---

# gpuCI Technical Documentation

## Overview

Outlines how gpuCI is configured for RAPIDS and how to integrate other projects

gpuCI is accessible here: https://gpuci.gpuopenanalytics.com/

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

- Open source project for CI/CD and general automation that is very extensible and well adopted
- gpuCI
  - Build scripts are standardized across RAPIDS projects
    - CPU builds with conda & pip
    - GPU builds & unit tests
    - Executing style & changelog checks
    - Planned to be open sourced soon
  - Standardization allows for scripts to create and config jobs
    - [https://gpuci.gpuopenanalytics.com/view/gpuCIv2/job/gpuCIv2/job/Rapids%20Seed%20Job/](https://gpuci.gpuopenanalytics.com/view/gpuCIv2/job/gpuCIv2/job/Rapids%20Seed%20Job/)
    - Uses Jenkins job-dsl plugin
    - Creates 125+ Jenkins jobs to perform everything listed in this document
    - Handles the links between Jenkins & GitHub
  - Custom [plugin](https://github.com/gpuopenanalytics/remote-docker-plugin) written & open sourced by RAPIDS to better handle GPU testing with nvidia-docker

### Docker containers

All jobs which use Docker use the `gpuci/rapidsai-base` images.

[Docker Hub](https://hub.docker.com/r/gpuci/rapidsai-base)

[GitHub](https://github.com/rapidsai/gpuci-build-environment)

#### Conda environment

The images contain a common conda environment with basic tools such as `python`, `cmake`, `make`, `cython`, and `flake8`. See the full list [here](https://github.com/rapidsai/gpuci-build-environment/blob/master/Dockerfile#L66)

The conda environment can be used in the scripts with `source activate gdf`

## Jobs

### Pull requests

TODO

### Branch

TODO

## Scripts

These scripts are a standardized way for gpuCI to build projects. This allows for rapid integration and immediate feedback in pull requests on build changes.

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

Required: No
Job type: PR only
Docker: No
Variables:
- PR_ID
- COMMIT_HASH
- REPORT_HASH

Executed as a check to see if the changelog was updated. It's up the script to determine if the changelog was updated and exit with 0 for success or non-zero for error.

If not provided, a simple check of whether `CHANGELOG.md` has been updated and if it contains the `PR_ID`.

### ci/checks/style.sh

Required: Yes
Job type: PR only
Docker: `gpuci/rapidsai-base:cuda9.2-ubuntu16.04-gcc5-py3.6`
Variables:
- PR_ID
- COMMIT_HASH
- REPORT_HASH
- DOCKER_IMAGE

Executed as a check to ensure code style is correct. `flake8` is available in the common conda environment.

### ci/cpu/prebuild.sh

Required: No
Job type: Both
Docker: No
Variables:
    - DOCKER_IMAGE
    - PR_ID
    - COMMIT_HASH
    - REPORT_HASH
    - CUDA
    - PYTHON
    - UBUNTU
    - ghprbPullAuthorLogin
    - ghprbSourceBranch
    - CONDA_USERNAME

If provided, gpuCI will source this file before building. This allows for setting any environment variables required for the build script. For example,  translating `CUDA` or `PYTHON`, or setting a variable to enable additional tests for some combinations of `CUDA` and `PYTHON`.

Many RAPIDS projects have two components: python and C/C++. For these projects, this script sets variables to prevent duplicate builds which speeds up testing.

### ci/cpu/build.sh

Required: Yes
Job type: Both
Docker: `gpuci/rapidsai-base:cuda${CUDA}-ubuntu${UBUNTU}-gcc5-py${PYTHON}`
Variables:
    - DOCKER_IMAGE
    - PR_ID
    - COMMIT_HASH
    - REPORT_HASH
    - CUDA
    - PYTHON
    - UBUNTU
    - ghprbPullAuthorLogin
    - ghprbSourceBranch
    - CONDA_USERNAME
    - GIT_BRANCH

This script actually builds the code inside of a container. For most RAPIDS projects this means building the conda package. There is no GPU available, so testing in this script is limited to CPU only code.

Additionally, this script should upload packages to Anaconda if necessary. The `GIT_BRANCH` variable can be used to determine what type of build:
- `COMMIT_HASH` for PRs
- `branch-x.y` for development branch builds
- `master` for release builds

### ci/gpu/prebuild.sh

Required: No
Job type: Both
Docker: `gpuci/rapidsai-base:cuda10.0-ubuntu16.04-gcc5-py$3.6`
Variables:
    - DOCKER_IMAGE
    - PR_ID
    - COMMIT_HASH
    - REPORT_HASH

If provided, gpuCI will source this file before building. This allows for setting any environment variables required for the build script.

### ci/gpu/build.sh

Required: Yes
Job type: Both
Docker: `gpuci/rapidsai-base:cuda10.0-ubuntu16.04-gcc5-py$3.6`
Variables:
    - DOCKER_IMAGE
    - PR_ID
    - COMMIT_HASH
    - REPORT_HASH

This script actually builds the code inside of a container. A GPU is available so this script should execute any tests requiring a GPU.

If the tests output in in XML format in `test-results/*.xml` or a file named `junit*.xml`, the results will be published on Jenkins.

### ci/releases/update-version.sh

Required: Only if auto-releasing is enabled
Job type: Master Branch only
Docker: No
Variables:
    - BRANCH

This script is run with a parameter of `major`, `minor`, or `patch` to indicate what to release. The script should calculate the next version and update the source code, build scripts, and documentation with the new version.

**Note:** The script must export `NEXT_FULL_TAG` as the full `x.y.z` version.

After this, gpuCI will commit the changes and tag the commit with `v${NEXT_FULL_TAG}` before pushing to the repository.