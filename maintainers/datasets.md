---
layout: default
nav_order: 3
parent: RAPIDS Maintainer Docs
title: Datasets
---

# Datasets

## Overview

Many tests depend on the presence of specific datasets in order to properly verify code correctness. Some datasets are small enough that they can be included with the source code, but others are relatively large and cannot practically coexist with the source. In both cases, a test author should not write a test to assume datasets are located in a particular place (either with a relative path, since the executable could be moved, or an absolute path, since different machines will likely use different absolute paths), and should instead allow for the location of the datasets to be provided by a user.

### Intended audience

Developers
{: .label .label-green}

Project Leads
{: .label .label-blue}

Operations
{: .label .label-purple}

## Running Tests That Use Datasets

Tests using the RAPIDS dataset locating utilities (see below) allow a user to specify the location of datasets using one of the following mechanisms:

### The `RAPIDS_DATASET_ROOT_DIR` option to `cmake`

The `cmake` command responsible for building the test executables supports the option `RAPIDS_DATASET_ROOT_DIR`, which can be used as shown below:
```
cmake -DRAPIDS_DATASET_ROOT_DIR=/location/to/datasets
```
This mechanism allows a user building tests from source to create test executables that will find their datasets in the directory specified.

### The `RAPIDS_DATASET_ROOT_DIR` environment variable

If a user needs to override the `RAPIDS_DATASET_ROOT_DIR` build option, or if the build option was not used, the `RAPIDS_DATASET_ROOT_DIR` environment variable can be set to the location of the datasets.

This environment variable takes precedence over the build option, meaning both options can be used. This can be useful for experimenting on different datasets without requiring a rebuild, or for running the test binaries on a different system that has the datasets installed to an alternate location. The environment variable can be set as shown below prior to running the tests (showing a bash shell):
```
export RAPIDS_DATASET_ROOT_DIR=/location/to/datasets
```

### The built-in `/datasets` default

Finally, if neither the build option nor the environment variable are set, tests using the RAPIDS dataset locating utilities will default to `/datasets` as the location where datasets will be accessed.

## Writing Tests That Use Datasets

Test developers can use the RAPIDS dataset locating utilities by calling the following function:
```
const std::string& get_rapids_dataset_root_dir()
```
`get_rapids_dataset_root_dir()` will return a `std::string` reference to the root directory containing the datasets, as determined by the user-accessible options described above, or a default value of `/datasets` if the user did not use the options.

### Example API usage
```
const std::string& rapidsDatasetRootDir = get_rapids_dataset_root_dir();
readDataset(rapidsDatasetRootDir + "/golden_data/web-BerkStan.pagerank_val_0.85.bin");
```

### Best Practices
- Test authors should document the relative paths under the datasets root dir that tests require in a README or similar document.
- Instructions on how to obtain the datasets (if they are not included with the source) should also be included in a README or similar document. Optionally, a description of each dataset should be included as well if it's useful.
- Test authors should consider using test fixtures that have a `Setup()` method that ensures the datasets exist prior to accessing them. The `Setup()` method should throw an exception with the path to the dataset the test is using so users know to set or check one of the dataset location override mechanisms if necessary.

*NOTE: At the moment, only the `cugraph` library has adopted the `get_rapids_dataset_root_dir()` functionality.*

## Datasets for benchmarks

Developers and end users alike may need to run benchmarks to evaluate the performance of RAPIDS libraries. Benchmarks currently vary from RAPIDS repo to repo in how they're written, how they need to be run, and if and how they use datasets. At the moment, only the `cugraph` library has standardized on a convention for benchmark datasets, as described below:
- Datasets for both tests and benchmarks are located in \<repo root\>/datasets. This allows benchmark developers to use the same dataset locating APIs (`get_rapids_dataset_root_dir()`, etc.) with the same settings described above for running tests.
- A script is provided for downloading and installing different datasets for different use cases. The `-h` option to the script will describe the options available. For cugraph benchmarks, run the script with the `--benchmark` option from the `datasets` dir:
```
cd <repo root>/datasets
./get_test_data.sh --benchmark
```
