---
layout: default
nav_order: 3
parent: Resources
grand_parent: RAPIDS Maintainer Docs
title: Reproducing CI
---

# {{ page.title }}
{:.no_toc}

## Overview
{:.no_toc}

This page outlines some helpful information about reproducing CI builds and tests locally.

At this time, this information only applies to `conda` related builds and tests.

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

## Reproducing CI Jobs

The GitHub Action jobs that power RAPIDS' CI are simply a collection of shell scripts that are run inside of our [CI containers](https://github.com/rapidsai/ci-imgs).

This makes it easy to reproduce build and test issues from CI on local machines.

To get started, you should first identify the image that's being used in a particular GitHub Action job.

This can be done by inspecting the _Intialize Containers_ step as seen in the screenshot below.

![](/assets/images/reproducing-ci/container.png)

After the container image has been identified, you can volume mount your local repository into the container with the command below:

```sh
docker run \
  --rm \
  -it \
  --gpus all \
  --network=host \
  --volume $PWD:/repo \
  --workdir /repo \
  rapidsai/ci:cuda11.8.0-ubuntu22.04-py3.10
```

This command makes the following assumptions:

- Your current directory is the repository that you wish you troubleshoot
- Your current directory has the same commit checked out as the pull-request whose jobs you are trying to debug

A few notes about the flags above:

- Most of the RAPIDS conda builds occur on machines without GPUs. Only the tests require GPUs. Therefore, you can omit the `--gpus` flag when running local conda builds
- The `--network` flag ensures that the container has access to the VPN connection on your host machine. VPN connectivity is required for test jobs since they need access to [downloads.rapids.ai](https://downloads.rapids.ai) for downloading build artifacts from a particular pull-request. This flag can be ommitted for build jobs

After you run the command above, you will be able to run commands inside the container.

From here you can run any of the CI scripts:

```sh
# to build cpp...
./ci/build_cpp.sh

# to test cpp...
./ci/test_cpp.sh

# to build python...
./ci/build_python.sh

# to test python...
./ci/test_python.sh

# to test notebooks...
./ci/test_notebooks.sh

# to build docs...
./ci/build_docs.sh
```

## Additional Considerations

There are a few additional considerations for running CI jobs locally.

### GPU Driver Versions

RAPIDS' CI test jobs may run on one of many GPU driver versions. When you're trying reproduce CI test failures locally, it's important to pay attention to both the driver version used in CI and the driver version on your local machine.

Discrepancies in these versions could lead to inconsistent test results.

You can typically find the driver version of a CI machine in its job output.

### Downloading Build Artifacts for Tests

In RAPIDS' CI workflows, the builds and tests occur on different machines.

Machines without GPUs are used for builds, while the tests occur on machines with GPUs.

Due to this process, the artifacts from the build jobs must be downloaded in order for the test jobs to run.

In CI, this process happens transparently.

Local builds lack the context provided by the CI environment and therefore will require input from the user in order to ensure that the correct artifacts are downloaded.

Anytime the `rapids-download-conda-from-s3` command (e.g. [here](https://github.com/rapidsai/cugraph/blob/b50850f0498e163e56b0374c1c64e551a5898f26/ci/test_python.sh#L22-L23)) is encountered in a local test run, the user will be prompted for any necessary environment variables that are missing.

The screenshot below shows an example.

![](/assets/images/reproducing-ci/prompts.png)

You can enter these values preemptively to suppress the prompts. For example:

```sh
export RAPIDS_BUILD_TYPE=pull-request
export RAPIDS_REPOSITORY=rapidsai/cugraph
export RAPIDS_REF_NAME=pull-request/3258

./ci/test_python.sh
```

## Limitations

There are a few limitations to keep in mind when running CI scripts locally.

### Can't Upload Local Artifacts

Build artifacts from locally run jobs cannot be uploaded to [downloads.rapids.ai](https://downloads.rapids.ai).

It is assumed that once a build successfully completes locally, the changes will be pushed to a pull-request where the artifacts can be properly uploaded.

To attempt a complete build and test workflow locally, you could manually update any instances of `CPP_CHANNEL` and `PYTHON_CHANNEL` that use `rapids-download-conda-from-s3` (e.g. [1](https://github.com/rapidsai/cuml/blob/dc38afc584154ebe7332d43f69e3913492f7a273/ci/build_python.sh#L14),[2](https://github.com/rapidsai/cuml/blob/dc38afc584154ebe7332d43f69e3913492f7a273/ci/test_python_common.sh#L22-L23)) with the value of the `RAPIDS_CONDA_BLD_OUTPUT_DIR` environment variable that is [set in our CI images](https://github.com/rapidsai/ci-imgs/blob/d048ffa6bfd672fa72f31aeb7cc5cf2363aff6d9/Dockerfile#L105).

This value is used to set the `output_folder` of the `.condarc` file used in our CI images (see [docs](https://conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html#specify-conda-build-build-folder-conda-build-3-16-3-output-folder)). Therefore, any locally built packages will end up in this directory.

For example:

```sh
sed -ri '/rapids-download-conda-from-s3/ s/_CHANNEL=.*/_CHANNEL=${RAPIDS_CONDA_BLD_OUTPUT_DIR}/' ci/*.sh

./ci/build_cpp.sh
./ci/build_python.sh
./ci/test_cpp.sh
./ci/test_python.sh
./ci/test_notebooks.sh
./ci/build_docs.sh
```

### VPN Access

Currently, [downloads.rapids.ai](https://downloads.rapids.ai) is only available via the NVIDIA VPN.

Therefore, if you want to run any test jobs locally, you'll need to be connected to the VPN for the build artifacts to properly download.
