---
layout: default
nav_order: 1
parent: Containers
grand_parent: Demos
title: RAPIDS Demo Container
permalink: containers/rapids-demo
---

# RAPIDS Demo Container

Get started with our preconfigured RAPIDS demo container, featuring several demo notebooks using cuDF, cuML, cuGraph, Dask, and XGBoost
{: .fs-6 .fw-300 }

1. TOC
{:toc}

### Current Version

#### RAPIDS 0.10 - 17 October 2019

Versions of libraries included in the `0.10` [images](#rapids-10-images):
- `cuDF` [v0.10.0](https://github.com/rapidsai/cudf/tree/v0.10.0), `cuML` [v0.10.0](https://github.com/rapidsai/cuml/tree/v0.10.0), `cuGraph` [v0.10.0](https://github.com/rapidsai/cugraph/tree/v0.10.0), `RMM` [v0.10.0](https://github.com/rapidsai/RMM/tree/v0.10.0), `cuSpatial` [v0.10.0](https://github.com/rapidsai/cuspatial/tree/v0.10.0)
- `xgboost` [branch](https://github.com/rapidsai/xgboost/tree/rapids-0.10-release), `dask-xgboost` [branch](https://github.com/rapidsai/dask-xgboost/tree/dask-cudf) `dask-cuda` [branch](https://github.com/rapidsai/dask-cuda/tree/branch-0.10)

Updates & changes
- Added cuSpatial, the GPU-accelerated spatial and trajectory data management and analytics library.
- Added support for CUDA 10.1.
- Updated containers with `v0.10.0` release of cuDF, cuML, cuGraph, cuStrings, and RMM, as well as updated versions of xgboost, dask-xgboost, and dask-cuda.

### Former Versions

#### RAPIDS 0.9 - 21 August 2019

Versions of libraries included in the `0.9` [images](#rapids-09-images):
- `cuDF` [v0.9.0](https://github.com/rapidsai/cudf/tree/v0.9.0), `cuML` [v0.9.0](https://github.com/rapidsai/cuml/tree/v0.9.0), `cuGraph` [v0.9.0](https://github.com/rapidsai/cugraph/tree/v0.9.0), `RMM` [v0.9.0](https://github.com/rapidsai/RMM/tree/v0.9.0)
- `xgboost` [branch](https://github.com/rapidsai/xgboost/tree/cudf-interop), `dask-xgboost` [branch](https://github.com/rapidsai/dask-xgboost/tree/dask-cudf) `dask-cuda` [branch](https://github.com/rapidsai/dask-cuda/tree/branch-0.8)

Updates & changes
- Updated containers with `v0.9.0` release of cuDF, cuML, cuGraph, cuStrings, RMM, and dask-cuda.

#### RAPIDS 0.8 - 27 June 2019

Versions of libraries included in the `0.8` [images](#rapids-08-images):
- `cuDF` [v0.8.0](https://github.com/rapidsai/cudf/tree/v0.8.0), `cuML` [v0.8.0](https://github.com/rapidsai/cuml/tree/v0.8.0), `cuGraph` [v0.8.0](https://github.com/rapidsai/cugraph/tree/v0.8.0), `RMM` [v0.8.0](https://github.com/rapidsai/RMM/tree/v0.8.0)
- `xgboost` [branch](https://github.com/rapidsai/xgboost/tree/cudf-interop), `dask-xgboost` [branch](https://github.com/rapidsai/dask-xgboost/tree/dask-cudf), `dask-cudf` [branch](https://github.com/rapidsai/dask-cudf/tree/branch-0.8), `dask-cuda` [branch](https://github.com/rapidsai/dask-cuda/tree/branch-0.8)

Updates & changes
- Updated containers with `v0.8.0` release of cuDF, cuML, cuGraph, cuStrings, RMM, dask-cuda, dask-cudf, and dask-cuml.

#### RAPIDS 0.7 - 16 May 2019

Versions of libraries included in the `0.7` [images](#rapids-07-images):
- `cuDF` [v0.7.2](https://github.com/rapidsai/cudf/tree/v0.7.2), `cuML` [v0.7.0](https://github.com/rapidsai/cuml/tree/v0.7.0), `cuGraph` [v0.7.0](https://github.com/rapidsai/cugraph/tree/v0.7.0), `RMM` [v0.7.0](https://github.com/rapidsai/RMM/tree/v0.7.0)
- `xgboost` [branch](https://github.com/rapidsai/xgboost/tree/cudf-interop), `dask-xgboost` [branch](https://github.com/rapidsai/dask-xgboost/tree/dask-cudf), `dask-cudf` [branch](https://github.com/rapidsai/dask-cudf/tree/branch-0.7), `dask-cuda` [branch](https://github.com/rapidsai/dask-cuda/tree/branch-0.7)

Updates & changes
- Updated containers with `v0.7.2` release of cuDf and `v0.7.0` release of cuML, cuGraph, cuStrings, RMM, dask-cuda, dask-cudf, and dask-cuml.
- Added example notebooks for cuGraph and additional cuML example notebooks in the `runtime` & `devel` containers

#### RAPIDS 0.6 - 28 Mar 2019

Versions of libraries included in the `0.6` [images](#rapids-06-images):
- `cuDF` [v0.6.1](https://github.com/rapidsai/cudf/tree/v0.6.1), `cuML` [v0.6.0](https://github.com/rapidsai/cuml/tree/v0.6.0), `cuGraph` [v0.6.0](https://github.com/rapidsai/cugraph/tree/v0.6.0), `RMM` [v0.6.0](https://github.com/rapidsai/RMM/tree/v0.6.0)
- `xgboost` [branch](https://github.com/rapidsai/xgboost/tree/cudf-interop), `dask-xgboost` [branch](https://github.com/rapidsai/dask-xgboost/tree/dask-cudf), `dask-cudf` [branch](https://github.com/rapidsai/dask-cudf), `dask-cuda` [branch](https://github.com/rapidsai/dask-cuda)

#### RAPIDS 0.5.1 - 26 Feb 2019

`0.5` [image list](#rapids-05-images)

Versions of libraries included in the `0.5` [images](#rapids-05-images):
- `cuDF` [v0.5.1](https://github.com/rapidsai/cudf/tree/v0.5.1), `cuML` [v0.5.1](https://github.com/rapidsai/cuml/tree/v0.5.1), `RMM` [v0.5.0](https://github.com/rapidsai/RMM/tree/v0.5.0)
- `xgboost` [branch](https://github.com/rapidsai/xgboost/tree/cudf-mnmg-abi), `dask-xgboost` [branch](https://github.com/rapidsai/dask-xgboost/tree/dask-cudf), `dask-cudf` [branch](https://github.com/rapidsai/dask-cudf), `dask-cuda` [branch](https://github.com/rapidsai/dask-cuda)

Updates & changes
- Added [CentOS 7 images](#centos-7)
- Reduced the number of example notebooks in the `runtime/devel` containers
- Updated containers with `v0.5.1` release of cuDf & cuML

#### RAPIDS 0.4 - 05 Dec 2018

`0.4` [image list](#rapids-04-images)

Versions of libraries included in the `0.4` [images](#rapids-04-images):
- `cuDF` [v0.4.0](https://github.com/rapidsai/cudf/tree/v0.4.0), `cuML` [v0.4.0](https://github.com/rapidsai/cuml/tree/v0.4.0)
- `xgboost`, `dask-xgboost`, `dask-cudf`

### Tags

The RAPIDS image is based on the `runtime` [nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) image. This means it is a drop-in replacement, making it easy to gain the RAPIDS libraries while maintaining support for existing CUDA applications.

RAPIDS images come in three types:

- `base` - contains a RAPIDS environment ready for use.<br/>Use this image if you want to use RAPIDS as a part of your pipeline.
- `runtime` - extends the `base` image by adding a notebook server and example notebooks.<br/>Use this image if you want to explore RAPIDS through notebooks and examples.
- `devel` - contains the compiler toolchain, the debugging tools, the headers and the libraries for RAPIDS development, as well as the RAPIDS source code and all build artifacts in place.<br/>Use this image to develop RAPIDS from source.

#### Common Tags

For most users the `runtime` image will be sufficient to get started with RAPIDS,
you can use the following tags to pull the latest stable image:
- `latest` or `cuda9.2-runtime-ubuntu16.04` <br/>with `gcc 5.4` and `Python 3.6`
- `cuda10.0-runtime-ubuntu18.04`<br/>with `gcc 7.3` and `Python 3.6`

#### Other Tags

View the full [tag list](#full-tag-list) for all available images.

## Prerequisites

* NVIDIA Pascal™ GPU architecture or better
* CUDA [9.2](https://developer.nvidia.com/cuda-92-download-archive) or [10.0](https://developer.nvidia.com/cuda-downloads) compatible NVIDIA driver
* Ubuntu 16.04/18.04 or CentOS 7
* Docker CE v18+
* [nvidia-docker](https://github.com/nvidia/nvidia-docker/wiki/Installation-(version-2.0)) v2+

## Usage

### Start Container and Notebook Server

```bash
$ docker pull rapidsai/rapidsai:cuda9.2-runtime-ubuntu16.04
$ docker run --runtime=nvidia \
--rm -it \
-p 8888:8888 \
-p 8787:8787 \
-p 8786:8786 \
rapidsai/rapidsai:cuda9.2-runtime-ubuntu16.04
```
**NOTE:** This will open a shell with [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) running in the background on port 8888 on your host machine.

### Use JupyterLab to Explore the Notebooks

Notebooks can be found in the following directories within the container:

* `/rapids/notebooks/xgboost` - XGBoost demo notebooks
* `/rapids/notebooks/cudf` - cuDF demo notebooks
* `/rapids/notebooks/cuml` - cuML demo notebooks
* `/rapids/notebooks/cugraph` - cuGraph demo notebooks
* `/rapids/notebooks/tutorials` - Tutorials with end-to-end workflows

For a full description of each notebook, see the [README](https://github.com/rapidsai/notebooks/blob/branch-0.7/README.md) in the notebooks repository.

### Custom Data and Advanced Usage

You are free to modify the above steps. For example, you can launch an interactive session with your own data:

```bash
docker run --runtime=nvidia \
--rm -it \
-p 8888:8888 \
-p 8787:8787 \
-p 8786:8786 \
-v /path/to/host/data:/rapids/my_data
rapidsai/rapidsai:cuda9.2-runtime-ubuntu16.04
```

This will map data from your host operating system to the container OS in the `/rapids/my_data` directory. You may need to modify the provided notebooks for the new data paths.

### Access Documentation within Notebooks

You can check the documentation for RAPIDS APIs inside the JupyterLab notebook using a `?` command, like this:
```
[1] ?cudf.read_csv
```
This prints the function signature and its usage documentation. If this is not enough, you can see the full code for the function using `??`:
```
[1] ??pygdf.read_csv
```
Check out the RAPIDS [documentation](http://rapids.ai/start.html) for more detailed information and a RAPIDS [cheat sheet](https://rapids.ai/files/cheatsheet.pdf).

## More Information

Check out the [RAPIDS](https://docs.rapids.ai/api) and [XGBoost](https://xgboost.readthedocs.io/en/latest/) API docs.

Learn how to setup a mult-node cuDF and XGBoost data preparation and distributed training environment by following the [mortgage data example notebook and scripts](https://github.com/rapidsai/notebooks).

## Where can I get help or file bugs/requests?

Please submit issues with the container to this GitHub repository: [https://github.com/rapidsai/docs](https://github.com/rapidsai/docs/issues/new)

For issues with RAPIDS libraries like cuDF, cuML, RMM, or others file an issue in the related GitHub project.

Additional help can be found on [Stack Overflow](https://stackoverflow.com/tags/rapids) or [Google Groups](https://groups.google.com/forum/#!forum/rapidsai).

## Full Tag List

Using the image types [above](#tags) `base`, `runtime`, or `devel` we use the following
tag naming scheme for RAPIDS images:

```
0.10-cuda9.2-devel-ubuntu16.04-py3.6
^       ^    ^        ^         ^
|       |    type     |         python version
|       |             |
|       cuda version  |
|                     |
RAPIDS version        linux version
```

The `base` and `runtime` image types can be found in the `rapidsai/rapidsai` DockerHub repo, and the `devel` image types can be found in the `rapidsai/rapidsai-dev` DockerHub repo.

### RAPIDS 0.10 Images

#### Ubuntu 16.04

All `ubuntu16.04` images use `gcc 5.4`

**CUDA 9.2**

| Short Tags | Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `cuda9.2-base-ubuntu16.04` | `0.10-cuda9.2-base-ubuntu16.04` | base | 3.6 |
| `latest`<br>or<br>`cuda9.2-runtime-ubuntu16.04` | `0.10-cuda9.2-runtime-ubuntu16.04` | runtime | 3.6 |
| --- | `0.10-cuda9.2-devel-ubuntu16.04-py3.6` | devel | 3.6 |
| --- | `0.10-cuda9.2-devel-ubuntu16.04-py3.7` | devel | 3.7 |

**CUDA 10.0**

| Short Tags | Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `cuda10.0-base-ubuntu16.04` | `0.10-cuda10.0-base-ubuntu16.04` | base | 3.6 |
| `cuda10.0-runtime-ubuntu16.04` | `0.10-cuda10.0-runtime-ubuntu16.04` | runtime | 3.6 |
| --- | `0.10-cuda10.0-devel-ubuntu16.04-py3.6` | devel | 3.6 |
| --- | `0.10-cuda10.0-devel-ubuntu16.04-py3.7` | devel | 3.7 |

**CUDA 10.1**

| Short Tags | Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `cuda10.1-base-ubuntu16.04` | `0.10-cuda10.1-base-ubuntu16.04` | base | 3.6 |
| `cuda10.1-runtime-ubuntu16.04` | `0.10-cuda10.1-runtime-ubuntu16.04` | runtime | 3.6 |
| --- | `0.10-cuda10.1-devel-ubuntu16.04-py3.6` | devel | 3.6 |
| --- | `0.10-cuda10.1-devel-ubuntu16.04-py3.7` | devel | 3.7 |

#### Ubuntu 18.04

All `ubuntu18.04` images use `gcc 7.3`

**CUDA 9.2**

| Short Tags | Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `cuda9.2-base-ubuntu18.04` | `0.10-cuda9.2-base-ubuntu18.04` | base | 3.6 |
| `cuda9.2-runtime-ubuntu18.04` | `0.10-cuda9.2-runtime-ubuntu18.04` | runtime | 3.6 |
| --- | `0.10-cuda9.2-devel-ubuntu18.04-py3.6` | devel | 3.6 |
| --- | `0.10-cuda9.2-devel-ubuntu18.04-py3.7` | devel | 3.7 |

**CUDA 10.0**

| Short Tags | Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `cuda10.0-base-ubuntu18.04` | `0.10-cuda10.0-base-ubuntu18.04` | base | 3.6 |
| `cuda10.0-runtime-ubuntu18.04` | `0.10-cuda10.0-runtime-ubuntu18.04` | runtime | 3.6 |
| --- | `0.10-cuda10.0-devel-ubuntu18.04-py3.6` | devel | 3.6 |
| --- | `0.10-cuda10.0-devel-ubuntu18.04-py3.7` | devel | 3.7 |

**CUDA 10.1**

| Short Tags | Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `cuda10.1-base-ubuntu18.04` | `0.10-cuda10.1-base-ubuntu18.04` | base | 3.6 |
| `cuda10.1-runtime-ubuntu18.04` | `0.10-cuda10.1-runtime-ubuntu18.04` | runtime | 3.6 |
| --- | `0.10-cuda10.1-devel-ubuntu18.04-py3.6` | devel | 3.6 |
| --- | `0.10-cuda10.1-devel-ubuntu18.04-py3.7` | devel | 3.7 |

#### CentOS 7

All `centos7` images use `gcc 7.3`

**CUDA 9.2**

| Short Tags | Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `cuda9.2-base-centos7` | `0.10-cuda9.2-base-centos7` | base | 3.6 |
| `cuda9.2-runtime-centos7` | `0.10-cuda9.2-runtime-centos7` | runtime | 3.6 |
| --- | `0.10-cuda9.2-devel-centos7-py3.6` | devel | 3.6 |
| --- | `0.10-cuda9.2-devel-centos7-py3.7` | devel | 3.7 |

**CUDA 10.0**

| Short Tags | Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `cuda10.0-base-centos7` | `0.10-cuda10.0-base-centos7` | base | 3.6 |
| `cuda10.0-runtime-centos7` | `0.10-cuda10.0-runtime-centos7` | runtime | 3.6 |
| --- | `0.10-cuda10.0-devel-centos7-py3.6` | devel | 3.6 |
| --- | `0.10-cuda10.0-devel-centos7-py3.7` | devel | 3.7 |

**CUDA 10.1**

| Short Tags | Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `cuda10.1-base-centos7` | `0.10-cuda10.1-base-centos7` | base | 3.6 |
| `cuda10.1-runtime-centos7` | `0.10-cuda10.1-runtime-centos7` | runtime | 3.6 |
| --- | `0.10-cuda10.1-devel-centos7-py3.6` | devel | 3.6 |
| --- | `0.10-cuda10.1-devel-centos7-py3.7` | devel | 3.7 |

### RAPIDS 0.9 Images

#### Ubuntu 16.04

All `ubuntu16.04` images use `gcc 5.4`

**CUDA 9.2**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.9-cuda9.2-base-ubuntu16.04` | base | 3.6 |
| `0.9-cuda9.2-runtime-ubuntu16.04` | runtime | 3.6 |
| `0.9-cuda9.2-devel-ubuntu16.04-py3.6` | devel | 3.6 |
| `0.9-cuda9.2-devel-ubuntu16.04-py3.7` | devel | 3.7 |

**CUDA 10.0**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.9-cuda10.0-base-ubuntu16.04` | base | 3.6 |
| `0.9-cuda10.0-runtime-ubuntu16.04` | runtime | 3.6 |
| `0.9-cuda10.0-devel-ubuntu16.04-py3.6` | devel | 3.6 |
| `0.9-cuda10.0-devel-ubuntu16.04-py3.7` | devel | 3.7 |

#### Ubuntu 18.04

All `ubuntu18.04` images use `gcc 7.3`

**CUDA 9.2**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.9-cuda9.2-base-ubuntu18.04` | base | 3.6 |
| `0.9-cuda9.2-runtime-ubuntu18.04` | runtime | 3.6 |
| `0.9-cuda9.2-devel-ubuntu18.04-py3.6` | devel | 3.6 |
| `0.9-cuda9.2-devel-ubuntu18.04-py3.7` | devel | 3.7 |

**CUDA 10.0**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.9-cuda10.0-base-ubuntu18.04` | base | 3.6 |
| `0.9-cuda10.0-runtime-ubuntu18.04` | runtime | 3.6 |
| `0.9-cuda10.0-devel-ubuntu18.04-py3.6` | devel | 3.6 |
| `0.9-cuda10.0-devel-ubuntu18.04-py3.7` | devel | 3.7 |

#### CentOS 7

All `centos7` images use `gcc 7.3`

**CUDA 9.2**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.9-cuda9.2-base-centos7` | base | 3.6 |
| `0.9-cuda9.2-runtime-centos7` | runtime | 3.6 |
| `0.9-cuda9.2-devel-centos7-py3.6` | devel | 3.6 |
| `0.9-cuda9.2-devel-centos7-py3.7` | devel | 3.7 |

**CUDA 10.0**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.9-cuda10.0-base-centos7` | base | 3.6 |
| `0.9-cuda10.0-runtime-centos7` | runtime | 3.6 |
| `0.9-cuda10.0-devel-centos7-py3.6` | devel | 3.6 |
| `0.9-cuda10.0-devel-centos7-py3.7` | devel | 3.7 |

### RAPIDS 0.8 Images

#### Ubuntu 16.04

All `ubuntu16.04` images use `gcc 5.4`

**CUDA 9.2**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.8-cuda9.2-base-ubuntu16.04-gcc5-py3.6` | base | 3.6 |
| `0.8-cuda9.2-base-ubuntu16.04-gcc5-py3.7` | base | 3.7 |
| `0.8-cuda9.2-runtime-ubuntu16.04-gcc5-py3.6` | runtime | 3.6 |
| `0.8-cuda9.2-runtime-ubuntu16.04-gcc5-py3.7` | runtime | 3.7 |
| `0.8-cuda9.2-devel-ubuntu16.04-gcc5-py3.6` | devel | 3.6 |
| `0.8-cuda9.2-devel-ubuntu16.04-gcc5-py3.7` | devel | 3.7 |

**CUDA 10.0**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.8-cuda10.0-base-ubuntu16.04-gcc5-py3.6` | base | 3.6 |
| `0.8-cuda10.0-base-ubuntu16.04-gcc5-py3.7` | base | 3.7 |
| `0.8-cuda10.0-runtime-ubuntu16.04-gcc5-py3.6` | runtime | 3.6 |
| `0.8-cuda10.0-runtime-ubuntu16.04-gcc5-py3.7` | runtime | 3.7 |
| `0.8-cuda10.0-devel-ubuntu16.04-gcc5-py3.6` | devel | 3.6 |
| `0.8-cuda10.0-devel-ubuntu16.04-gcc5-py3.7` | devel | 3.7 |

#### Ubuntu 18.04

All `ubuntu18.04` images use `gcc 7.3`

**CUDA 9.2**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.8-cuda9.2-base-ubuntu18.04-gcc7-py3.6` | base | 3.6 |
| `0.8-cuda9.2-base-ubuntu18.04-gcc7-py3.7` | base | 3.7 |
| `0.8-cuda9.2-runtime-ubuntu18.04-gcc7-py3.6` | runtime | 3.6 |
| `0.8-cuda9.2-runtime-ubuntu18.04-gcc7-py3.7` | runtime | 3.7 |
| `0.8-cuda9.2-devel-ubuntu18.04-gcc7-py3.6` | devel | 3.6 |
| `0.8-cuda9.2-devel-ubuntu18.04-gcc7-py3.7` | devel | 3.7 |

**CUDA 10.0**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.8-cuda10.0-base-ubuntu18.04-gcc7-py3.6` | base | 3.6 |
| `0.8-cuda10.0-base-ubuntu18.04-gcc7-py3.7` | base | 3.7 |
| `0.8-cuda10.0-runtime-ubuntu18.04-gcc7-py3.6` | runtime | 3.6 |
| `0.8-cuda10.0-runtime-ubuntu18.04-gcc7-py3.7` | runtime | 3.7 |
| `0.8-cuda10.0-devel-ubuntu18.04-gcc7-py3.6` | devel | 3.6 |
| `0.8-cuda10.0-devel-ubuntu18.04-gcc7-py3.7` | devel | 3.7 |

#### CentOS 7

All `centos7` images use `gcc 7.3`

**CUDA 9.2**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.8-cuda9.2-base-centos7-gcc7-py3.6` | base | 3.6 |
| `0.8-cuda9.2-base-centos7-gcc7-py3.7` | base | 3.7 |
| `0.8-cuda9.2-runtime-centos7-gcc7-py3.6` | runtime | 3.6 |
| `0.8-cuda9.2-runtime-centos7-gcc7-py3.7` | runtime | 3.7 |
| `0.8-cuda9.2-devel-centos7-gcc7-py3.6` | devel | 3.6 |
| `0.8-cuda9.2-devel-centos7-gcc7-py3.7` | devel | 3.7 |

**CUDA 10.0**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.8-cuda10.0-base-centos7-gcc7-py3.6` | base | 3.6 |
| `0.8-cuda10.0-base-centos7-gcc7-py3.7` | base | 3.7 |
| `0.8-cuda10.0-runtime-centos7-gcc7-py3.6` | runtime | 3.6 |
| `0.8-cuda10.0-runtime-centos7-gcc7-py3.7` | runtime | 3.7 |
| `0.8-cuda10.0-devel-centos7-gcc7-py3.6` | devel | 3.6 |
| `0.8-cuda10.0-devel-centos7-gcc7-py3.7` | devel | 3.7 |

### RAPIDS 0.7 Images

#### Ubuntu 16.04

All `ubuntu16.04` images use `gcc 5.4`

**CUDA 9.2**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.7-cuda9.2-base-ubuntu16.04-gcc5-py3.6` | base | 3.6 |
| `0.7-cuda9.2-base-ubuntu16.04-gcc5-py3.7` | base | 3.7 |
| `0.7-cuda9.2-runtime-ubuntu16.04-gcc5-py3.6` | runtime | 3.6 |
| `0.7-cuda9.2-runtime-ubuntu16.04-gcc5-py3.7` | runtime | 3.7 |
| `0.7-cuda9.2-devel-ubuntu16.04-gcc5-py3.6` | devel | 3.6 |
| `0.7-cuda9.2-devel-ubuntu16.04-gcc5-py3.7` | devel | 3.7 |

**CUDA 10.0**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.7-cuda10.0-base-ubuntu16.04-gcc5-py3.6` | base | 3.6 |
| `0.7-cuda10.0-base-ubuntu16.04-gcc5-py3.7` | base | 3.7 |
| `0.7-cuda10.0-runtime-ubuntu16.04-gcc5-py3.6` | runtime | 3.6 |
| `0.7-cuda10.0-runtime-ubuntu16.04-gcc5-py3.7` | runtime | 3.7 |
| `0.7-cuda10.0-devel-ubuntu16.04-gcc5-py3.6` | devel | 3.6 |
| `0.7-cuda10.0-devel-ubuntu16.04-gcc5-py3.7` | devel | 3.7 |

#### Ubuntu 18.04

All `ubuntu18.04` images use `gcc 7.3`

**CUDA 9.2**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.7-cuda9.2-base-ubuntu18.04-gcc7-py3.6` | base | 3.6 |
| `0.7-cuda9.2-base-ubuntu18.04-gcc7-py3.7` | base | 3.7 |
| `0.7-cuda9.2-runtime-ubuntu18.04-gcc7-py3.6` | runtime | 3.6 |
| `0.7-cuda9.2-runtime-ubuntu18.04-gcc7-py3.7` | runtime | 3.7 |
| `0.7-cuda9.2-devel-ubuntu18.04-gcc7-py3.6` | devel | 3.6 |
| `0.7-cuda9.2-devel-ubuntu18.04-gcc7-py3.7` | devel | 3.7 |

**CUDA 10.0**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.7-cuda10.0-base-ubuntu18.04-gcc7-py3.6` | base | 3.6 |
| `0.7-cuda10.0-base-ubuntu18.04-gcc7-py3.7` | base | 3.7 |
| `0.7-cuda10.0-runtime-ubuntu18.04-gcc7-py3.6` | runtime | 3.6 |
| `0.7-cuda10.0-runtime-ubuntu18.04-gcc7-py3.7` | runtime | 3.7 |
| `0.7-cuda10.0-devel-ubuntu18.04-gcc7-py3.6` | devel | 3.6 |
| `0.7-cuda10.0-devel-ubuntu18.04-gcc7-py3.7` | devel | 3.7 |

#### CentOS 7

All `centos7` images use `gcc 7.3`

**CUDA 9.2**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.7-cuda9.2-base-centos7-gcc7-py3.6` | base | 3.6 |
| `0.7-cuda9.2-base-centos7-gcc7-py3.7` | base | 3.7 |
| `0.7-cuda9.2-runtime-centos7-gcc7-py3.6` | runtime | 3.6 |
| `0.7-cuda9.2-runtime-centos7-gcc7-py3.7` | runtime | 3.7 |
| `0.7-cuda9.2-devel-centos7-gcc7-py3.6` | devel | 3.6 |
| `0.7-cuda9.2-devel-centos7-gcc7-py3.7` | devel | 3.7 |

**CUDA 10.0**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.7-cuda10.0-base-centos7-gcc7-py3.6` | base | 3.6 |
| `0.7-cuda10.0-base-centos7-gcc7-py3.7` | base | 3.7 |
| `0.7-cuda10.0-runtime-centos7-gcc7-py3.6` | runtime | 3.6 |
| `0.7-cuda10.0-runtime-centos7-gcc7-py3.7` | runtime | 3.7 |
| `0.7-cuda10.0-devel-centos7-gcc7-py3.6` | devel | 3.6 |
| `0.7-cuda10.0-devel-centos7-gcc7-py3.7` | devel | 3.7 |

### RAPIDS 0.6 Images

#### Ubuntu 16.04

All `ubuntu16.04` images use `gcc 5.4`

**CUDA 9.2**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.6-cuda9.2-base-ubuntu16.04-gcc5-py3.6` | base | 3.6 |
| `0.6-cuda9.2-base-ubuntu16.04-gcc5-py3.7` | base | 3.7 |
| `0.6-cuda9.2-runtime-ubuntu16.04-gcc5-py3.6` | runtime | 3.6 |
| `0.6-cuda9.2-runtime-ubuntu16.04-gcc5-py3.7` | runtime | 3.7 |
| `0.6-cuda9.2-devel-ubuntu16.04-gcc5-py3.6` | devel | 3.6 |
| `0.6-cuda9.2-devel-ubuntu16.04-gcc5-py3.7` | devel | 3.7 |

**CUDA 10.0**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.6-cuda10.0-base-ubuntu16.04-gcc5-py3.6` | base | 3.6 |
| `0.6-cuda10.0-base-ubuntu16.04-gcc5-py3.7` | base | 3.7 |
| `0.6-cuda10.0-runtime-ubuntu16.04-gcc5-py3.6` | runtime | 3.6 |
| `0.6-cuda10.0-runtime-ubuntu16.04-gcc5-py3.7` | runtime | 3.7 |
| `0.6-cuda10.0-devel-ubuntu16.04-gcc5-py3.6` | devel | 3.6 |
| `0.6-cuda10.0-devel-ubuntu16.04-gcc5-py3.7` | devel | 3.7 |

#### Ubuntu 18.04

All `ubuntu18.04` images use `gcc 7.3`

**CUDA 9.2**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.6-cuda9.2-base-ubuntu18.04-gcc7-py3.6` | base | 3.6 |
| `0.6-cuda9.2-base-ubuntu18.04-gcc7-py3.7` | base | 3.7 |
| `0.6-cuda9.2-runtime-ubuntu18.04-gcc7-py3.6` | runtime | 3.6 |
| `0.6-cuda9.2-runtime-ubuntu18.04-gcc7-py3.7` | runtime | 3.7 |
| `0.6-cuda9.2-devel-ubuntu18.04-gcc7-py3.6` | devel | 3.6 |
| `0.6-cuda9.2-devel-ubuntu18.04-gcc7-py3.7` | devel | 3.7 |

**CUDA 10.0**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.6-cuda10.0-base-ubuntu18.04-gcc7-py3.6` | base | 3.6 |
| `0.6-cuda10.0-base-ubuntu18.04-gcc7-py3.7` | base | 3.7 |
| `0.6-cuda10.0-runtime-ubuntu18.04-gcc7-py3.6` | runtime | 3.6 |
| `0.6-cuda10.0-runtime-ubuntu18.04-gcc7-py3.7` | runtime | 3.7 |
| `0.6-cuda10.0-devel-ubuntu18.04-gcc7-py3.6` | devel | 3.6 |
| `0.6-cuda10.0-devel-ubuntu18.04-gcc7-py3.7` | devel | 3.7 |

#### CentOS 7

All `centos7` images use `gcc 7.3`

**CUDA 9.2**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.6-cuda9.2-base-centos7-gcc7-py3.6` | base | 3.6 |
| `0.6-cuda9.2-base-centos7-gcc7-py3.7` | base | 3.7 |
| `0.6-cuda9.2-runtime-centos7-gcc7-py3.6` | runtime | 3.6 |
| `0.6-cuda9.2-runtime-centos7-gcc7-py3.7` | runtime | 3.7 |
| `0.6-cuda9.2-devel-centos7-gcc7-py3.6` | devel | 3.6 |
| `0.6-cuda9.2-devel-centos7-gcc7-py3.7` | devel | 3.7 |

**CUDA 10.0**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.6-cuda10.0-base-centos7-gcc7-py3.6` | base | 3.6 |
| `0.6-cuda10.0-base-centos7-gcc7-py3.7` | base | 3.7 |
| `0.6-cuda10.0-runtime-centos7-gcc7-py3.6` | runtime | 3.6 |
| `0.6-cuda10.0-runtime-centos7-gcc7-py3.7` | runtime | 3.7 |
| `0.6-cuda10.0-devel-centos7-gcc7-py3.6` | devel | 3.6 |
| `0.6-cuda10.0-devel-centos7-gcc7-py3.7` | devel | 3.7 |

### RAPIDS 0.5 Images

#### Ubuntu 16.04

All `ubuntu16.04` images use `gcc 5.4`

**CUDA 9.2**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.5-cuda9.2-base-ubuntu16.04-gcc5-py3.6` | base | 3.6 |
| `0.5-cuda9.2-base-ubuntu16.04-gcc5-py3.7` | base | 3.7 |
| `0.5-cuda9.2-runtime-ubuntu16.04-gcc5-py3.6` | runtime | 3.6 |
| `0.5-cuda9.2-runtime-ubuntu16.04-gcc5-py3.7` | runtime | 3.7 |
| `0.5-cuda9.2-devel-ubuntu16.04-gcc5-py3.6` | devel | 3.6 |
| `0.5-cuda9.2-devel-ubuntu16.04-gcc5-py3.7` | devel | 3.7 |

**CUDA 10.0**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.5-cuda10.0-base-ubuntu16.04-gcc5-py3.6` | base | 3.6 |
| `0.5-cuda10.0-base-ubuntu16.04-gcc5-py3.7` | base | 3.7 |
| `0.5-cuda10.0-runtime-ubuntu16.04-gcc5-py3.6` | runtime | 3.6 |
| `0.5-cuda10.0-runtime-ubuntu16.04-gcc5-py3.7` | runtime | 3.7 |
| `0.5-cuda10.0-devel-ubuntu16.04-gcc5-py3.6` | devel | 3.6 |
| `0.5-cuda10.0-devel-ubuntu16.04-gcc5-py3.7` | devel | 3.7 |

#### Ubuntu 18.04

All `ubuntu18.04` images use `gcc 7.3`

**CUDA 9.2**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.5-cuda9.2-base-ubuntu18.04-gcc7-py3.6` | base | 3.6 |
| `0.5-cuda9.2-base-ubuntu18.04-gcc7-py3.7` | base | 3.7 |
| `0.5-cuda9.2-runtime-ubuntu18.04-gcc7-py3.6` | runtime | 3.6 |
| `0.5-cuda9.2-runtime-ubuntu18.04-gcc7-py3.7` | runtime | 3.7 |
| `0.5-cuda9.2-devel-ubuntu18.04-gcc7-py3.6` | devel | 3.6 |
| `0.5-cuda9.2-devel-ubuntu18.04-gcc7-py3.7` | devel | 3.7 |

**CUDA 10.0**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.5-cuda10.0-base-ubuntu18.04-gcc7-py3.6` | base | 3.6 |
| `0.5-cuda10.0-base-ubuntu18.04-gcc7-py3.7` | base | 3.7 |
| `0.5-cuda10.0-runtime-ubuntu18.04-gcc7-py3.6` | runtime | 3.6 |
| `0.5-cuda10.0-runtime-ubuntu18.04-gcc7-py3.7` | runtime | 3.7 |
| `0.5-cuda10.0-devel-ubuntu18.04-gcc7-py3.6` | devel | 3.6 |
| `0.5-cuda10.0-devel-ubuntu18.04-gcc7-py3.7` | devel | 3.7 |

#### CentOS 7

All `centos7` images use `gcc 7.3`

**CUDA 9.2**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.5-cuda9.2-base-centos7-gcc7-py3.6` | base | 3.6 |
| `0.5-cuda9.2-base-centos7-gcc7-py3.7` | base | 3.7 |
| `0.5-cuda9.2-runtime-centos7-gcc7-py3.6` | runtime | 3.6 |
| `0.5-cuda9.2-runtime-centos7-gcc7-py3.7` | runtime | 3.7 |
| `0.5-cuda9.2-devel-centos7-gcc7-py3.6` | devel | 3.6 |
| `0.5-cuda9.2-devel-centos7-gcc7-py3.7` | devel | 3.7 |

**CUDA 10.0**

| Full Tag | Image Type | Python Version |
| --- | --- | --- |
| `0.5-cuda10.0-base-centos7-gcc7-py3.6` | base | 3.6 |
| `0.5-cuda10.0-base-centos7-gcc7-py3.7` | base | 3.7 |
| `0.5-cuda10.0-runtime-centos7-gcc7-py3.6` | runtime | 3.6 |
| `0.5-cuda10.0-runtime-centos7-gcc7-py3.7` | runtime | 3.7 |
| `0.5-cuda10.0-devel-centos7-gcc7-py3.6` | devel | 3.6 |
| `0.5-cuda10.0-devel-centos7-gcc7-py3.7` | devel | 3.7 |

### RAPIDS 0.4 Images

**NOTE:** This release uses *non-standard* lables but have been kept for legacy users.

#### Ubuntu 16.04

All `ubuntu16.04` images use `gcc 5.4`

**CUDA 9.2**

| Full Tag | Image Type | Python Version | Notes |
| --- | --- | --- | --- |
| `cuda9.2_ubuntu16.04` | runtime | 3.5 | `jupyter` user by default |
| `cuda9.2_ubuntu16.04_root` | runtime | 3.5 | `root` user by default |

**CUDA 10.0**

| Full Tag | Image Type | Python Version | Notes |
| --- | --- | --- | --- |
| `cuda10.0_ubuntu16.04` | runtime | 3.5 | `jupyter` user by default |
| `cuda10.0_ubuntu16.04_root` | runtime | 3.5 | `root` user by default |
