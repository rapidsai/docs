---
layout: default
nav_order: 3
parent: RAPIDS Maintainer Docs
title: Testing Practices
---

# Testing Practices

## Overview

Summary of the testing practices used by RAPIDS projects.

### Intended audience

Developers
{: .label .label-green}

Project Leads
{: .label .label-blue}

Operations
{: .label .label-purple}

## Infrastructure

Overall goal, follow the open source ecosystem for infrastructure choices

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
  - Custom plugin written & open sourced by RAPIDS to better handle GPU testing with nvidia-docker

### GitHub

- All projects are hosted on GitHub for open source visibility

### Docker

- Industry standard for containerized software
- Allows for isolating all builds

## Code Style / Formatting

- Run style checks and/or auto-formatters per commit to ensure code is uniformly formatted in a clean and consistent way before it is ever merged to the repository
  - Handles things like maximum line length, trailing whitespace, linebreak semantics, etc.

### Follow open source ecosystem in use of code formatters

- C++
  - Clang-Format (Planned)
- Python
  - Flake8
  - Auto-formatting with Black (Planned)

## Unit Testing

- Runs per commit to ensure code is never pushed in a broken state
  - Reports back to github to give end user feedback of exactly what the issue(s) is
- Matrix of tests across supported Operating System / CUDA / Python versions along with running through CUDA-memcheck (planned)
- Tests that project builds successfully both with and without GPUs, and then ensures that the suite of unit tests run successfully with GPUs
  - Tests building of packages for conda and pip
- Tests are designed as black box tests for both external user facing functions and internal functions
  - Tests are written to compare against Pandas / Numpy / Scikit-Learn / NetworkX / etc. to ensure the results are completely in line with expectations of end users

### Follow open source ecosystem in use of testing frameworks

- C++
  - GTest
    - [https://github.com/google/googletest/blob/master/googletest/docs/primer.md](https://github.com/google/googletest/blob/master/googletest/docs/primer.md)
    - I.E. cuDF GTests:
      - [https://github.com/rapidsai/cudf/tree/branch-0.7/cpp/tests](https://github.com/rapidsai/cudf/tree/branch-0.7/cpp/tests)
- Python
  - Pytest
    - [https://docs.pytest.org/en/latest/getting-started.html](https://docs.pytest.org/en/latest/getting-started.html)
    - I.E. cuDF PyTests:
      - [https://github.com/rapidsai/cudf/tree/branch-0.7/python/cudf/tests](https://github.com/rapidsai/cudf/tree/branch-0.7/python/cudf/tests)

## Datasets

- Many tests depend on the presence of specific datasets in order to properly verify code correctness.
- Some datasets are small enough that they can be included with the source code, but others are relatively large and cannot practically coexist with the source. In both cases, the test executable should not assume datasets are located in a particular place (either with a relative path, since the executable could be moved, or an absolute path, since different machines will likely use different absolute paths), so the location of the datasets must be provided at test runtime.
- There are three mechanisms that allow tests to locate datasets on disk:
  - Users can set the environment variable `RAPIDS_DATASET_ROOT_DIR` to the path of the directory containing the datasets needed by tests.
  - Users can pass the flag `-DRAPIDS_DATASET_ROOT_DIR=<root dir>` to the `cmake` command when building from source. If the environment variable described above is not set, this setting will be used.
  - Finally, test developers can specify a default directory to use in the event that both the environment variable and the build option are not set. Since this is essentially hardcoding a path in the test executable, users should be made aware of what the location is as well as the options they have (the `RAPIDS_DATASET_ROOT_DIR` env var and the `-DRAPIDS_DATASET_ROOT_DIR=<root dir>` build option) for overriding it.

### Test developer API

- `const std::string& get_rapids_dataset_root_dir(const std::string& defaultRdrd)`
  - Tests that need to access the dataset directory should use this function for properly retrieving the dataset root directory defined by the user at build-time or runtime, or a specific default hardcoded in the test passed in as `defaultRdrd`.
  - An example is shown below:
```
    const std::string& rapidsDatasetRootDir = get_rapids_dataset_root_dir("/datasets");
    readDataset(rapidsDatasetRootDir + "/golden_data/web-BerkStan.pagerank_val_0.85.bin");
```
In the above example, if the tests are built with `-DRAPIDS_DATASET_ROOT_DIR=/bar` and the environment variable `RAPIDS_DATASET_ROOT_DIR` is set to `/foo`, the `readDataset()` call will get `/foo/golden_data/web-BerkStan.pagerank_val_0.85.bin`. If the environment variable is not set, the call will get `/bar/golden_data/web-BerkStan.pagerank_val_0.85.bin`. Finally, if the user didn't set the environment var and didn't use the build flag, the call will get `/datasets/golden_data/web-BerkStan.pagerank_val_0.85.bin`.

*NOTE: At the moment, only the `cugraph` library has adopted the `get_rapids_dataset_root_dir()` functionality.*

## Integration / Workflow Testing and Benchmarking

- Runs nightly to ensure the different libraries integrate as expected similar to how other Python libraries integrate (i.e. cuDF with cuML vs Pandas with SKLearn)
- In addition to checking the runs succeed without error and checking correctness, measures performance regressions in the workflows
- Pipe output of Google Benchmark into ASV dashboards for easy consumption
- Run with profiling and dump an nvprof / nsight profile per workflow for easy analysis by developers (planned)
- Allows for naturally using example / workflow notebooks for integration / workflow / performance testing as well
- Matrix of tests across supported Operating System / CUDA / Python versions

### Follow open source ecosystem in use of testing frameworks

- C++
  - GTest
  - Google Benchmark (Planned)
    - [https://github.com/google/benchmark#example-usage](https://github.com/google/benchmark#example-usage)
- Python
  - Pytest
  - Airspeed Velocity (ASV)
    - [https://asv.readthedocs.io/en/stable/using.html](https://asv.readthedocs.io/en/stable/using.html)

## Packaging and Release

- Follow open source ecosystem in packaging and delivery mechanisms:
  - Conda
  - Pip
  - Docker
- Releases
  - Release every ~6 weeks with no known critical bugs
  - Allows users to have a stable release that won't introduce performance regressions / bugs during the development process
  - Full set of unit / integration / workflow tests are performed before publish packages / containers
- "Nightlies"
  - Allows cutting edge users to install the latest conda package to test new functionality coming in the next release
  - Conda packages are created for each project on a per merge basis
  - Docker containers are built nightly and have integration tests run and must pass before publishing containers

## Examples of Testing in Action

- DLPack support for cuDF
  - [https://github.com/rapidsai/cudf/pull/913](https://github.com/rapidsai/cudf/pull/913)
    - C++ implementation with GTest unit tests
  - [https://github.com/rapidsai/cudf/pull/1159](https://github.com/rapidsai/cudf/pull/1159)
    - Python bindings implementation with PyTest unit tests and integration correctness tests with CuPy/Chainer
    - Found some additional issues in other libraries implementations that required some fixes in the C++ implementation
- String support for cuDF
  - [https://github.com/rapidsai/cudf/pull/1032](https://github.com/rapidsai/cudf/pull/1032)
    - C++ implementation and Python bindings
    - Originally depended on an unreleased version of a different library so CI builds failed and prevented merging into the main repository until it was resolved
    - GTests and PyTest unit tests where results of each incrementally drove development across both C++ and Python
    - Heavily uses unit test parameterization to effectively test different function parameters for sufficient test coverage
