---
layout: default
title: Deploying RAPIDS
nav_order: 5
permalink: deployment
---

# Deploying RAPIDS
{: .no_toc}

RAPIDS libraries are deployable across multiple environments types:
1. Single Node Single GPU
2. Single Node Multiple GPUs
3. Multiple Nodes, Multiple GPUs
4. Multiple or Single Node managed by a scheduling service:
    a. Kubernetes
    b. SLURM

Included below are guides for deploying to some of these environments.
{: .fs-6 .fw-300}

### Single Node Single GPU
In Single Node, Single GPU environments simply [install](https://rapids.ai/start.html#get-rapids) and import the libraries:
```
>>> import cudf, cuml, cugraph, cuspatial # Good to go!
```
<!--
Modify the codeblock if needed
-->
{: .mb-7 }

### Single Node Multi GPU
RAPIDS libraries also scale up to multiple GPUs on a single node. This is most easily setup using [Dask-CUDA](https://github.com/rapidsai/dask-cuda)'s `LocalCUDACluster` API to detect and start one worker process per available GPU.
```
>>> from dask_cuda import LocalCUDACluster
>>> from dask.distributed import Client
>>> import dask_cudf

>>> IPADDR = "0.0.0.0" # Change to more specific node IP if desired
>>> cluster = LocalCUDACluster(ip= IPADDR)
>>> client = Client(clsuter)
```
{: .mb-7 }
<!--
Include output of client maybe?
Choose a beginner example instead of intermediate?
-->
### Multi Node Multi GPU

#### **Manual Setup**
This is the most basic means of deploying RAPIDS to multiple hosts. Most more advanced deployments use the same commands with environment configuration & parameter variations.
- Run the `dask-scheduler` on one node
    ```
    $ dask-scheduler
    ```
- Run `dask-cuda-worker` on each worker node, providing the scheduler node's address. `dask-cuda-worker` will detect available GPUs and fork, starting one dask worker process per GPU.

    ```
    $ dask-cuda-worker 127.0.0.1:8786
    Start worker at:   tcp://127.0.0.1:36124
    Registered to: tcp://127.0.0.1:8786
    ```
- Connect to the cluster from a Python script
    ```
    >>> from dask.distributed import Client
    >>> # wrap Dask client API use in a main check
    >>> if __name__ == "__main__":
    ...     client = Client(address="127.0.0.1:8786")
    ...     # use_dask_APIs()
    ```
    Notes:
    - For more information on Dask CLI options use `dask-scheduler --help` and `dask-cuda-worker --help`

    More information on deploying manually can be found [here](https://docs.dask.org/en/latest/setup/cli.html).

    Dask also supports other options like [SSH](https://docs.dask.org/en/latest/setup/ssh.html) and [NFS](https://docs.dask.org/en/latest/setup/hpc.html#using-a-shared-network-file-system-and-a-job-scheduler).

    `dask-cuda-worker` is a convenient and optional extension of the normal `dask-worker` CLI command. You can also use `dask-worker` directly, manually configuring which GPUs are accessible to which workers:
    ```
    $ CUDA_VISIBLE_DEVICES=0 dask-worker localhost:8786 --nprocs 1 --nthreads 1 --memory-limit 0
    $ CUDA_VISIBLE_DEVICES=1 dask-worker localhost:8786 --nprocs 1 --nthreads 1 --memory-limit 0
    ```
{: .mb-5}

#### **Kubernetes and Helm**
RAPIDS libraries can also be deployed using [Kubernetes](https://kubernetes.io) and [Helm](https://helm.sh). This is useful for deploying RAPIDS on existing Kubernetes clusters, or to managed cloud Kubernetes services.
- [Install Helm](https://helm.sh/docs/using_helm/#installing-helm)
- [Link-to-k8-script-and-charts]
- ```
    $ helm install [link-to-chart] --name rapids-dask --namespace rapids
  ```
- Check the status of the running pods
  ```
  $ kubectl get pods -w --namespace rapids
  ```
  Additional Information:
GPU scheduling in Kubernetes](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/) 
[Dask Kubernetes](https://kubernetes.dask.org/en/latest/)
{: .mb-5}

#### **Docker**

##### **Docker Compose**
- Get the docker yml file [link-to-repo]
- ```
  $ docker compose ...
  ```

##### **Docker Swarm**


#### **Cloud deployments**

You can use a single type of configuration to deploy RAPIDS across multiple cloud providers with Kubernetes and Helm. You can also deploy RAPIDS through other managed service offerings where available.

##### **Google Dataproc**

<!--
RAPIDS general instead of cudf specific
-->

