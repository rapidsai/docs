---
layout: default
title: Deploying RAPIDS
nav_order: 5
permalink: deployment
---

# Deploying RAPIDS
{: .no_toc}

The RAPIDS collections of libraries can be deployed across multiple environments ranging from local nodes with a single GPU to complex HPC and cloud clusters. Highlighted below are some methods to deploy rapids libraries in different environments.
{: .fs-6 .fw-300}

### Single Node Single GPU
Running RAPIDS libraries in a Single Node Single GPU environment does not involve any additional setup. [Install](https://rapids.ai/start.html#get-rapids) the libraries you need and run in your preferred environment.
```
import cudf, cuml, cugraph, cuspatial # Good to go!
```
<!--
Modify the codeblock if needed
-->
{: .mb-7 }

### Single Node Multi GPU
RAPIDS libraries have the ability to scale up and take advantage of multiple GPUs on a single node. The [Dask-CUDA](https://github.com/rapidsai/dask-cuda) library makes it simple to set up workers on a single node with the `LocalCUDACluster` method.
```
from dask_cuda import LocalCUDACluster
from dask.distributed import Client
import dask_cudf

IPADDR = "0.0.0.0" # Update to use IP of the node
cluster = LocalCUDACluster(ip= IPADDR)
client = Client(clsuter)
```

This [notebook](https://github.com/rapidsai/notebooks-contrib/blob/master/intermediate_notebooks/examples/weather.ipynb) demonstrates the approach in an example.
{: .mb-7 }
<!--
Include output of client maybe?
Choose a beginner example instead of intermediate?
-->
### Multi Node Multi GPU


<!--
RAPIDS general instead of cudf specific
-->

