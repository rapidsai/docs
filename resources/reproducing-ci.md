---
layout: default
nav_order: 3
parent: Resources
grand_parent: Maintainer Docs
title: Reproducing CI Locally
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

The GitHub Actions jobs that power RAPIDS CI are simply a collection of shell scripts that are run inside of our [CI containers](https://github.com/rapidsai/ci-imgs).

This makes it easy to reproduce build and test issues from CI on local machines.

To get started, you should first identify the image that's being used in a particular GitHub Actions job.

This can be done by inspecting the _Initialize Containers_ step as seen in the screenshot below.

![](/assets/images/reproducing-ci/container.png)

After the container image has been identified, you can volume mount your local repository into the container with the command below:

```sh
docker run \
  --rm \
  --gpus all \
  --pull=always \
  --volume $PWD:/repo \
  --workdir /repo \
  -it rapidsai/ci-conda:latest
```

Once the container has started, you can run any of the CI scripts inside of it:

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

The `docker` command above makes the follow assumptions:

- Your current directory is the repository that you wish to troubleshoot
- Your current directory has the same commit checked out as the pull-request whose jobs you are trying to debug

A few notes about the `docker` command flags:

- Most of the RAPIDS conda builds occur on machines without GPUs. Only the tests require GPUs. Therefore, you can omit the `--gpus` flag when running local conda builds

## Additional Considerations

There are a few additional considerations for running CI jobs locally.

### GPU Driver Versions

RAPIDS CI test jobs may run on one of many GPU driver versions. When reproducing CI test failures locally, it's important to pay attention to both the driver version used in CI and the driver version on your local machine.

Discrepancies in these versions could lead to inconsistent test results.

You can typically find the driver version of a CI machine in its job output.

### GitHub Authentication

RAPIDS projects use the GitHub Actions artifact store to pass packages between build and test jobs.
To use CI scripts locally which expect to download those artifacts, you must be authenticated with the GitHub API.

If you run any RAPIDS CI scripts which require GitHub Authentication and are not yet authenticated,
you'll encounter an interactive prompt to log in via a browser session.

Those credentials will be stored in local storage in the container... when you delete the container, they'll be deleted too.

To avoid that interactive prompt, or to more tightly control the permissions granted to CI scripts,
set the environment variable `GH_TOKEN` to a GitHub personal access token ([docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)).
That token only needs to have the `repo` scope.

For example, you might generate a local `.env` file:

```text
GH_TOKEN=<redacted>
```

Then mount that into the container at runtime:

```shell
docker run \
  ...
  --env-file "$(pwd)/.env" \
  ...
```

Or pull authenticate locally with the `gh` CLI and pass that token through `docker run`.

```shell
gh auth login

 docker run \
  ...
  --env "GH_TOKEN=$(gh auth token)" \
  ...
```

NOTE: On shared machines, this method might expose your GitHub token in the output of `ps`. In those settings,
consider just relying on the interactive prompts inside the container or using the `--env-file` approach.

For more details, see "GitHub Actions" ([link](./github-actions)).

### Downloading Build Artifacts for Tests

In RAPIDS CI workflows, the builds and tests occur on different machines.

Machines without GPUs are used for builds, while the tests occur on machines with GPUs.

Artifacts from the build jobs must be downloaded from the GitHub Actions artifact store in order for the test jobs to run.

In CI, this process happens transparently.

Local builds lack the context provided by the CI environment and therefore require some user-supplied input in order to ensure that the correct artifacts are downloaded.

Any time the `rapids-download-{conda,wheels}-from-github` command (e.g.
[here](https://github.com/rapidsai/cugraph/blob/6200e99714113ea08fef6c8ae05d93c5516e9a13/ci/test_cpp.sh#L11))
or the `rapids-download-from-github "$(rapids-package-name ...)"` command (e.g.
[here](https://github.com/rapidsai/cuxfilter/blob/b9964b157db60a647421bba719a661afb9994a83/ci/test_python.sh#L13))
is encountered in a local test run, the user will be prompted for any necessary
environment variables that are missing.

The screenshot below shows an example.

![](/assets/images/reproducing-ci/prompts.png)

You can enter these values preemptively to suppress the prompts. For example:

```sh
export RAPIDS_BUILD_TYPE=pull-request # or "branch" or "nightly"
export RAPIDS_REPOSITORY=rapidsai/cugraph

export RAPIDS_REF_NAME=pull-request/3258 # use this type of value for "pull-request" builds
export RAPIDS_REF_NAME=branch-{{ site.data.releases.nightly.version }} # use this type of value for "branch"/"nightly" builds

export RAPIDS_NIGHTLY_DATE=2023-06-20 # this variable is only necessary for "nightly" builds

./ci/test_python.sh
```

## Limitations

There are a few limitations to keep in mind when running CI scripts locally.

### Local Artifacts Cannot Be Uploaded

Build artifacts from local jobs cannot be uploaded to the same artifact storage used by CI.

If builds are failing in CI, developers should fix the problem locally and then push their changes to a pull request.

Then CI jobs will run and the fixed build artifacts will be made available for the test job(s) to download and use.

To attempt a complete build and test workflow locally, you can manually update any instances of `CPP_CHANNEL` and `PYTHON_CHANNEL` that use `rapids-download-conda-from-github` (e.g. [1](https://github.com/rapidsai/cuml/blob/47aad39a3f71564976b4f5179201530bafe73f69/ci/test_python_common.sh#L9-L10)) with the value of the `RAPIDS_CONDA_BLD_OUTPUT_DIR` environment variable that is [set in the RAPIDS CI images](https://github.com/rapidsai/ci-imgs/blob/b7ef0f3932da7b8ce958baadc7597c1d7f1f2ab0/ci-conda.Dockerfile#L224).

This value is used to set the `output_folder` of the `.condarc` file used in the RAPIDS CI images (see [docs](https://conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html#specify-conda-build-build-folder-conda-build-3-16-3-output-folder)).
Therefore, any locally built packages will end up in this directory.

For example:

```sh
# Replace all local uses of `rapids-download-conda-from-github`
sed -ri '/rapids-download-conda-from-github/ s/_CHANNEL=.*/_CHANNEL=${RAPIDS_CONDA_BLD_OUTPUT_DIR}/' ci/*.sh

# Run the sequence of build/test scripts
./ci/build_cpp.sh
./ci/build_python.sh
./ci/test_cpp.sh
./ci/test_python.sh
./ci/test_notebooks.sh
./ci/build_docs.sh
```

### Some Builds Rely on Versioning Information in Git Tags

Some RAPIDS projects rely on versioning information stored in `git` tags.

For example, some use `conda` recipes that rely on the mechanisms described in ["Git environment variables" in the `conda-build` docs](https://docs.conda.io/projects/conda-build/en/stable/user-guide/environment-variables.html#git-environment-variables).

When those tags are unavailable, builds might fail with errors similar to this:

> Error: Failed to render jinja template in /repo/conda/recipes/libcudf/meta.yaml:
> 'GIT_DESCRIBE_NUMBER' is undefined
> conda returned exit code: 1

To fix that, pull the latest set of tags from the upstream repo.

For example, for `cudf`:

```sh
git fetch \
  git@github.com:rapidsai/cudf.git \
  --tags
```
