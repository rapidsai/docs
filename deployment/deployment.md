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

This [notebook](https://github.com/rapidsai/notebooks-contrib/blob/master/intermediate_notebooks/examples/weather.ipynb) demonstrates the approach discussed above.
{: .mb-7 }
<!--
Include output of client maybe?
Choose a beginner example instead of intermediate?
-->
### Multi Node Multi GPU
There are multiple methods of deploying RAPIDS in a Multi-Node setting.

#### **Manual Setup**
This is the most fundamental way to deploy RAPIDS on multiple machines.
- Launch the `dask-scheduler` on one node
    ```
    $ dask-scheduler
    ```
- Launch `dask-cuda-worker` on the rest of the nodes providing the address to the node hosting the scheduler
    ```
    $ dask-cuda-worker 127.0.0.1:8786
    Start worker at:   tcp://127.0.0.1:36124
    Registered to: tcp://127.0.0.1:8786
    ```
- Connect to the cluster in python
    ```
    from dask.distributed import Client
    client = Client(address="127.0.0.1:8786")
    ```
    Notes:
    - If the node has access to multiple GPUs the `dask-cuda-worker` CLI will start one worker per GPU on the node.
    - For more information on the CLI options use `dask-scheduler --help` and `dask-cuda-worker --help`

    More information on deploying manually can be found [here](https://docs.dask.org/en/latest/setup/cli.html).
{: .mb-5}

#### **Kubernetes and Helm**
RAPIDS libraries can also be deployed using [Kubernetes](https://kubernetes.io) and [Helm](https://helm.sh). This is useful for deploying RAPIDS on Cloud services like [AWS](https://aws.amazon.com), [GCP](https://cloud.google.com) or [Azure](https://azure.microsoft.com/en-us/).
- Install Helm based on the [docs](https://helm.sh/docs/using_helm/#installing-helm)
- Setup a cluster in Google Kubernetes Engines (optional)
- [Link-to-k8-script-and-charts]
- ```
    $ helm install [link-to-chart] --name rapids-dask --namespace rapids
  ```
- Check the status of the running pods
  ```
  kubectl get pods -w --namespace rapids
  ```
For more information on installing with Kubernetes and Helm visit [link-to-k8-repo]
{: .mb-5}

#### **Docker**

##### **Docker Compose**
- Get the docker yml file [link-to-repo]
- ```
  $ docker compose ...
  ```

##### **Docker Swarm**


#### **Cloud deployments**

For deploying RAPIDS on common cloud providers we recommend using Kuberentes and Helm. You can also deploy RAPIDS in other environments.

##### **Google Dataproc**

<!--
RAPIDS general instead of cudf specific
-->

