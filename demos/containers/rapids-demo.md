---
layout: default
nav_order: 1
parent: Containers
grand_parent: Demos
title: RAPIDS Demo Container
permalink: containers/rapids-demo
---

# RAPIDS Demo Container

Get started with our preconfigured RAPIDS demo container, featuring several demo notebooks using cuDF, cuML, Dask, and XGBoost
{: .fs-6 .fw-300 }

1. TOC
{:toc}

### Current Version

#### RAPIDS 0.7 - 11 May 2019

Versions of libraries included in the `0.7` [images](#rapids-07-images):
- `cuDF` [v0.7.1](https://github.com/rapidsai/cudf/tree/v0.7.1), `cuML` [v0.7.0](https://github.com/rapidsai/cuml/tree/v0.7.0), `cuGraph` [v0.7.0](https://github.com/rapidsai/cugraph/tree/v0.7.0), `RMM` [v0.7.0](https://github.com/rapidsai/RMM/tree/v0.7.0)
- `xgboost` [branch](https://github.com/rapidsai/xgboost/tree/cudf-interop), `dask-xgboost` [branch](https://github.com/rapidsai/dask-xgboost/tree/dask-cudf), `dask-cudf` [branch](https://github.com/rapidsai/dask-cudf/tree/branch-0.7), `dask-cuda` [branch](https://github.com/rapidsai/dask-cuda/tree/branch-0.7)

Updates & changes
- Updated containers with `v0.7.1` release of cuDf and `v0.7.0` release of cuML, cuGraph, cuStrings, RMM, dask-cuda, dask-cudf, and dask-cuml.
- Added example notebooks for cuGraph and additional cuML example notebooks in the `runtime` & `devel` containers

### Former Versions

#### RAPIDS 0.6 - 28 Mar 2019

Versions of libraries included in the `0.6` [images](#rapids-06-images):
- `cuDF` [v0.6.1](https://github.com/rapidsai/cudf/tree/v0.6.1), `cuML` [v0.6.0](https://github.com/rapidsai/cuml/tree/v0.6.0), `RMM` [v0.6.0](https://github.com/rapidsai/RMM/tree/v0.6.0)
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

The RAPIDS image is based on the `devel` [nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) image. This means it is a drop-in replacement, making it easy to gain the RAPIDS
libraries while maintaining support for existing CUDA applications.

RAPIDS images come in three types:

- `base` - contains a RAPIDS environment ready for use.<br/>Use this image if you want to use RAPIDS as a part of your pipeline.
- `runtime` - extends the `base` image by adding a notebook server and example notebooks.<br/>Use this image if you want to explore RAPIDS through notebooks and examples.
- `devel` - extends the `runtime` image by adding the compiler toolchain, the debugging tools, the headers and the static libraries for RAPIDS development.<br/>Use this image to develop RAPIDS from source.

#### Common Tags

For most users the `runtime` image will be sufficient to get started with RAPIDS,
you can use the following tags to pull the latest stable image:
- `latest` or `cuda9.2-runtime-ubuntu16.04` <br/>with `gcc 5.4` and `Python 3.6`
- `cuda10.0-runtime-ubuntu16.04`<br/>with `gcc 7.3` and `Python 3.6`

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
(rapids) root@container:/rapids/notebooks# bash utils/start-jupyter.sh
```
**NOTE:** This will run [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) on port 8888 on your host machine.

### Use JupyterLab to Explore the Notebooks

Notebooks can be found in two directories within the container:

* `/rapids/notebooks/cuml` - cuML demo notebooks
  * These notebooks have data pre-loaded in the container image and will be decompressed by the notebooks
* `/rapids/notebooks/mortgage` - cuDF, Dask, XGBoost demo notebook
  * This notebook requires download of [Mortgage Data](https://docs.rapids.ai/datasets/mortgage-data), see notebook `E2E.ipynb` for more details

### Custom Data and Advanced Usage

You are free to modify the above steps. For example, you can launch an interactive session with your own data:

    docker run --runtime=nvidia \
               --rm -it \
               -p 8888:8888 \
               -p 8787:8787 \
               -p 8786:8786 \
               -v /path/to/host/data:/rapids/my_data
               rapidsai/rapidsai:cuda9.2-runtime-ubuntu16.04

This will map data from your host operating system to the container OS in the `/rapids/my_data` directory. You may need to modify the provided notebooks for the new data paths. 

### Access Documentation within Notebooks

You can check the documentation for RAPIDS APIs inside the JupyterLab notebook using a `?` command, like this:

    [1] ?cudf.read_csv

This prints the function signature and its usage documentation. If this is not enough, you can see the full code for the function using `??`:

    [1] ??pygdf.read_csv

Check out the RAPIDS [documentation](http://rapids.ai/start.html) for more detailed information and a RAPIDS [cheat sheet](https://rapids.ai/files/cheatsheet.pdf).

## More Information

Check out the [cuDF](https://rapidsai.github.io/projects/cudf/en/latest), [cuML](https://rapidsai.github.io/projects/cuml/en/latest), and [XGBoost](https://xgboost.readthedocs.io/en/latest/) API docs.

Learn how to setup a mult-node cuDF and XGBoost data preparation and distributed training environment by following the [mortgage data example notebook and scripts](https://github.com/rapidsai/notebooks).

## Where can I get help or file bugs/requests?

Please submit issues with the container to this GitHub repository: [https://github.com/rapidsai/docs](https://github.com/rapidsai/docs/issues/new)

For issues with RAPIDS libraries like cuDF, cuML, RMM, or others file an issue in the related GitHub project.

Additional help can be found on [Stack Overflow](https://stackoverflow.com/tags/rapids) or [Google Groups](https://groups.google.com/forum/#!forum/rapidsai).

## Useful Tips and Tools for Monitoring and Debugging

### Changing How Many GPUs are Used

In the notebook,  you should see a cell like this:

```cmd = "../utils/dask-setup.sh rapids GPU 8 8786 8787 8790 " + str(IPADDR) + " MASTER INFO"```

Change the "GPU 8" to be "GPU X" where X = number of GPUs in your system (e.g. 4 for DGX Station, 8 for DGX-1, 16 for DGX-2).

### Changing How Much Data is Used

In the notebook, you should see a cell like this:

```python
acq_data_path = "/rapids/data/mortgage/acq"
perf_data_path = "/rapids/data/mortgage/perf"
col_names_path = "/rapids/data/mortgage/names.csv"
start_year = 2000
end_year = 2002 # end_year is inclusive
part_count = 11 # the number of data files to train against
```

These are the paths to data, the number of years on which to perform ETL, and the number of parts to use for training.

Note: the entire mortgage dataset is 68 quarters, broken into 112 parts so that each part is (on average) 1.7GB. Reducing the number of parts, `part_count`, reduces how much data is input to XGBoost training. Adjusting the `start_year` and`end_year` changes how many years on which to perform ETL.

### The Dask Dashboard. 

This cell from the notebook

```python
import subprocess

cmd = "hostname --all-ip-addresses"
process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
IPADDR = str(output.decode()).split()[0]
_client = IPADDR + str(":8786")

client = dask.distributed.Client(_client)
client
```

initializes the Dask client. Once done, you should see output like

```
Client

Scheduler: tcp://172.17.0.3:8786
Dashboard: http://172.17.0.3:8787/status
Cluster

Workers: 8
Cores: 8
Memory: 0 B
```

Note: clicking `Dashboard: http://172.17.0.3:8787/status`  may not work. The IP address in the link may be the networking device in the container. You have to use the IP address of the primary networking device, which should be the one you used to access the Jupyter notebook server. `http://your.ip.address:8787/status`

Once there, you can look at active processes, view the (delayed) task graph, and read through individual worker logs.

### Individual Worker Logs

When you hit an unusual error, there are often traces of the error in the individual worker logs accessible from the Dashboard status page (see above). CUDA out-of-memory errors will show up here.

## Common Errors

### Running out of device memory

ETL processes may involve creating many copies of data in device memory, resulting in sporadic spikes of memory utilization. Memory utilization which exceeds available device resources will cause the worker to crash.

Because we have disabled experimental features that would enable the worker to recover, restart its work, or share its work with other workers, the error is silently propagated forward in the Dask's delayed task graph. This can manifest itself in the form of unusually short ETL times (sub-millisecond timescale).

An error may be raised by another routine referring to `NoneType` in `data` or similar

Training processes need a certain amount of available memory to expand throughout processing. With XGBoost, the overhead is typically 25% of available device memory. This means that we cannot exceed 24GB of memory utilization on a 32GB GPU, or 12GB of memory utilization on a 16GB GPU.

### Running out of system memory

The final step of the ETL process migrates all computed results back to system memory before training, and if you do not have sufficient system memory, your program will crash. The step before training migrates a portion of the data back into device memory for XGBoost to train against.

## Full Tag List

Using the image types [above](#tags) `base`, `runtime`, or `devel` we use the following
tag naming scheme for RAPIDS images:

```
0.5-cuda9.2-devel-ubuntu16.04-gcc5-py3.6
 ^       ^    ^        ^         ^    ^
 |       |    type     |         |    python version
 |       |             |         |
 |       cuda version  |         gcc version
 |                     |
 RAPIDS version        linux version
 ```
### RAPIDS 0.7 Images

#### Ubuntu 16.04

All `ubuntu16.04` images use `gcc 5.4`

**CUDA 9.2**

| Short Tags | Full Tag | Image Type | Python Version |
| --- | --- | --- | --- |
| `cuda9.2-base-ubuntu16.04` | `0.7-cuda9.2-base-ubuntu16.04-gcc5-py3.6` | base | 3.6 |
| - | `0.7-cuda9.2-base-ubuntu16.04-gcc5-py3.7` | base | 3.7 |
| `latest`<br>or<br>`cuda9.2-runtime-ubuntu16.04` | `0.7-cuda9.2-runtime-ubuntu16.04-gcc5-py3.6` | runtime | 3.6 |
| - | `0.7-cuda9.2-runtime-ubuntu16.04-gcc5-py3.7` | runtime | 3.7 |
| `cuda9.2-devel-ubuntu16.04` | `0.7-cuda9.2-devel-ubuntu16.04-gcc5-py3.6` | devel | 3.6 |
| - | `0.7-cuda9.2-devel-ubuntu16.04-gcc5-py3.7` | devel | 3.7 |

**CUDA 10.0**

| Short Tags | Full Tag | Image Type | Python Version |
| --- | --- | --- | --- |
| `cuda10.0-base-ubuntu16.04` | `0.7-cuda10.0-base-ubuntu16.04-gcc5-py3.6` | base | 3.6 |
| - | `0.7-cuda10.0-base-ubuntu16.04-gcc5-py3.7` | base | 3.7 |
| `cuda10.0-runtime-ubuntu16.04` | `0.7-cuda10.0-runtime-ubuntu16.04-gcc5-py3.6` | runtime | 3.6 |
| - | `0.7-cuda10.0-runtime-ubuntu16.04-gcc5-py3.7` | runtime | 3.7 |
| `cuda10.0-devel-ubuntu16.04` | `0.7-cuda10.0-devel-ubuntu16.04-gcc5-py3.6` | devel | 3.6 |
| - | `0.7-cuda10.0-devel-ubuntu16.04-gcc5-py3.7` | devel | 3.7 |

#### Ubuntu 18.04

All `ubuntu18.04` images use `gcc 7.3`

**CUDA 9.2**

| Short Tags | Full Tag | Image Type | Python Version |
| --- | --- | --- | --- |
| `cuda9.2-base-ubuntu18.04` | `0.7-cuda9.2-base-ubuntu18.04-gcc7-py3.6` | base | 3.6 |
| - | `0.7-cuda9.2-base-ubuntu18.04-gcc7-py3.7` | base | 3.7 |
| `cuda9.2-runtime-ubuntu18.04` | `0.7-cuda9.2-runtime-ubuntu18.04-gcc7-py3.6` | runtime | 3.6 |
| - | `0.7-cuda9.2-runtime-ubuntu18.04-gcc7-py3.7` | runtime | 3.7 |
| `cuda9.2-devel-ubuntu18.04` | `0.7-cuda9.2-devel-ubuntu18.04-gcc7-py3.6` | devel | 3.6 |
| - | `0.7-cuda9.2-devel-ubuntu18.04-gcc7-py3.7` | devel | 3.7 |

**CUDA 10.0**

| Short Tags | Full Tag | Image Type | Python Version |
| --- | --- | --- | --- |
| `cuda10.0-base-ubuntu18.04` | `0.7-cuda10.0-base-ubuntu18.04-gcc7-py3.6` | base | 3.6 |
| - | `0.7-cuda10.0-base-ubuntu18.04-gcc7-py3.7` | base | 3.7 |
| `cuda10.0-runtime-ubuntu18.04` | `0.7-cuda10.0-runtime-ubuntu18.04-gcc7-py3.6` | runtime | 3.6 |
| - | `0.7-cuda10.0-runtime-ubuntu18.04-gcc7-py3.7` | runtime | 3.7 |
| `cuda10.0-devel-ubuntu18.04` | `0.7-cuda10.0-devel-ubuntu18.04-gcc7-py3.6` | devel | 3.6 |
| - | `0.7-cuda10.0-devel-ubuntu18.04-gcc7-py3.7` | devel | 3.7 |

#### CentOS 7

All `centos7` images use `gcc 7.3`

**CUDA 9.2**

| Short Tags | Full Tag | Image Type | Python Version |
| --- | --- | --- | --- |
| `cuda9.2-base-centos7` | `0.7-cuda9.2-base-centos7-gcc7-py3.6` | base | 3.6 |
| - | `0.7-cuda9.2-base-centos7-gcc7-py3.7` | base | 3.7 |
| `cuda9.2-runtime-centos7` | `0.7-cuda9.2-runtime-centos7-gcc7-py3.6` | runtime | 3.6 |
| - | `0.7-cuda9.2-runtime-centos7-gcc7-py3.7` | runtime | 3.7 |
| `cuda9.2-devel-centos7` | `0.7-cuda9.2-devel-centos7-gcc7-py3.6` | devel | 3.6 |
| - | `0.7-cuda9.2-devel-centos7-gcc7-py3.7` | devel | 3.7 |

**CUDA 10.0**

| Short Tags | Full Tag | Image Type | Python Version |
| --- | --- | --- | --- |
| `cuda10.0-base-centos7` | `0.7-cuda10.0-base-centos7-gcc7-py3.6` | base | 3.6 |
| - | `0.7-cuda10.0-base-centos7-gcc7-py3.7` | base | 3.7 |
| `cuda10.0-runtime-centos7` | `0.7-cuda10.0-runtime-centos7-gcc7-py3.6` | runtime | 3.6 |
| - | `0.7-cuda10.0-runtime-centos7-gcc7-py3.7` | runtime | 3.7 |
| `cuda10.0-devel-centos7` | `0.7-cuda10.0-devel-centos7-gcc7-py3.6` | devel | 3.6 |
| - | `0.7-cuda10.0-devel-centos7-gcc7-py3.7` | devel | 3.7 |

### RAPIDS 0.6 Images

#### Ubuntu 16.04

All `ubuntu16.04` images use `gcc 5.4`

**CUDA 9.2**

| Short Tags | Full Tag | Image Type | Python Version |
| --- | --- | --- | --- |
| `cuda9.2-base-ubuntu16.04` | `0.6-cuda9.2-base-ubuntu16.04-gcc5-py3.6` | base | 3.6 |
| - | `0.6-cuda9.2-base-ubuntu16.04-gcc5-py3.7` | base | 3.7 |
| `latest`<br>or<br>`cuda9.2-runtime-ubuntu16.04` | `0.6-cuda9.2-runtime-ubuntu16.04-gcc5-py3.6` | runtime | 3.6 |
| - | `0.6-cuda9.2-runtime-ubuntu16.04-gcc5-py3.7` | runtime | 3.7 |
| `cuda9.2-devel-ubuntu16.04` | `0.6-cuda9.2-devel-ubuntu16.04-gcc5-py3.6` | devel | 3.6 |
| - | `0.6-cuda9.2-devel-ubuntu16.04-gcc5-py3.7` | devel | 3.7 |

**CUDA 10.0**

| Short Tags | Full Tag | Image Type | Python Version |
| --- | --- | --- | --- |
| `cuda10.0-base-ubuntu16.04` | `0.6-cuda10.0-base-ubuntu16.04-gcc5-py3.6` | base | 3.6 |
| - | `0.6-cuda10.0-base-ubuntu16.04-gcc5-py3.7` | base | 3.7 |
| `cuda10.0-runtime-ubuntu16.04` | `0.6-cuda10.0-runtime-ubuntu16.04-gcc5-py3.6` | runtime | 3.6 |
| - | `0.6-cuda10.0-runtime-ubuntu16.04-gcc5-py3.7` | runtime | 3.7 |
| `cuda10.0-devel-ubuntu16.04` | `0.6-cuda10.0-devel-ubuntu16.04-gcc5-py3.6` | devel | 3.6 |
| - | `0.6-cuda10.0-devel-ubuntu16.04-gcc5-py3.7` | devel | 3.7 |

#### Ubuntu 18.04

All `ubuntu18.04` images use `gcc 7.3`

**CUDA 9.2**

| Short Tags | Full Tag | Image Type | Python Version |
| --- | --- | --- | --- |
| `cuda9.2-base-ubuntu18.04` | `0.6-cuda9.2-base-ubuntu18.04-gcc7-py3.6` | base | 3.6 |
| - | `0.6-cuda9.2-base-ubuntu18.04-gcc7-py3.7` | base | 3.7 |
| `cuda9.2-runtime-ubuntu18.04` | `0.6-cuda9.2-runtime-ubuntu18.04-gcc7-py3.6` | runtime | 3.6 |
| - | `0.6-cuda9.2-runtime-ubuntu18.04-gcc7-py3.7` | runtime | 3.7 |
| `cuda9.2-devel-ubuntu18.04` | `0.6-cuda9.2-devel-ubuntu18.04-gcc7-py3.6` | devel | 3.6 |
| - | `0.6-cuda9.2-devel-ubuntu18.04-gcc7-py3.7` | devel | 3.7 |

**CUDA 10.0**

| Short Tags | Full Tag | Image Type | Python Version |
| --- | --- | --- | --- |
| `cuda10.0-base-ubuntu18.04` | `0.6-cuda10.0-base-ubuntu18.04-gcc7-py3.6` | base | 3.6 |
| - | `0.6-cuda10.0-base-ubuntu18.04-gcc7-py3.7` | base | 3.7 |
| `cuda10.0-runtime-ubuntu18.04` | `0.6-cuda10.0-runtime-ubuntu18.04-gcc7-py3.6` | runtime | 3.6 |
| - | `0.6-cuda10.0-runtime-ubuntu18.04-gcc7-py3.7` | runtime | 3.7 |
| `cuda10.0-devel-ubuntu18.04` | `0.6-cuda10.0-devel-ubuntu18.04-gcc7-py3.6` | devel | 3.6 |
| - | `0.6-cuda10.0-devel-ubuntu18.04-gcc7-py3.7` | devel | 3.7 |

#### CentOS 7

All `centos7` images use `gcc 7.3`

**CUDA 9.2**

| Short Tags | Full Tag | Image Type | Python Version |
| --- | --- | --- | --- |
| `cuda9.2-base-centos7` | `0.6-cuda9.2-base-centos7-gcc7-py3.6` | base | 3.6 |
| - | `0.6-cuda9.2-base-centos7-gcc7-py3.7` | base | 3.7 |
| `cuda9.2-runtime-centos7` | `0.6-cuda9.2-runtime-centos7-gcc7-py3.6` | runtime | 3.6 |
| - | `0.6-cuda9.2-runtime-centos7-gcc7-py3.7` | runtime | 3.7 |
| `cuda9.2-devel-centos7` | `0.6-cuda9.2-devel-centos7-gcc7-py3.6` | devel | 3.6 |
| - | `0.6-cuda9.2-devel-centos7-gcc7-py3.7` | devel | 3.7 |

**CUDA 10.0**

| Short Tags | Full Tag | Image Type | Python Version |
| --- | --- | --- | --- |
| `cuda10.0-base-centos7` | `0.6-cuda10.0-base-centos7-gcc7-py3.6` | base | 3.6 |
| - | `0.6-cuda10.0-base-centos7-gcc7-py3.7` | base | 3.7 |
| `cuda10.0-runtime-centos7` | `0.6-cuda10.0-runtime-centos7-gcc7-py3.6` | runtime | 3.6 |
| - | `0.6-cuda10.0-runtime-centos7-gcc7-py3.7` | runtime | 3.7 |
| `cuda10.0-devel-centos7` | `0.6-cuda10.0-devel-centos7-gcc7-py3.6` | devel | 3.6 |
| - | `0.6-cuda10.0-devel-centos7-gcc7-py3.7` | devel | 3.7 |

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
