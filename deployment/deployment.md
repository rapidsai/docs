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

## Single Node Single GPU

In Single Node, Single GPU environments simply [install](https://rapids.ai/start.html#get-rapids) and import the libraries.

```python
>>> import cudf, cuml, cugraph, cuspatial # Good to go!
```
{: .mb-7 }

## Single Node Multi GPU

RAPIDS libraries also scale up to multiple GPUs on a single node. This is most easily setup using [Dask-CUDA](https://github.com/rapidsai/dask-cuda)'s `LocalCUDACluster` API to detect and start one worker process per available GPU.

```python
>>> from dask_cuda import LocalCUDACluster
>>> from dask.distributed import Client
>>> import dask_cudf

>>> IPADDR = "0.0.0.0" # Change to more specific node IP if desired
>>> cluster = LocalCUDACluster(ip= IPADDR)
>>> client = Client(cluster)
```
{: .mb-7 }
<!--
Include output of client maybe?
-->
## Multi Node Multi GPU

### Manual Setup
This is the most basic means of deploying RAPIDS to multiple hosts. Most more advanced deployments use the same commands with environment configuration & parameter variations.

- Run the `dask-scheduler` on one node
```sh
$ dask-scheduler
```
{: .mb-5}

- Run `dask-cuda-worker` on each worker node, providing the scheduler node's address. `dask-cuda-worker` will detect available GPUs and fork, starting one dask worker process per GPU.
```sh
$ dask-cuda-worker 127.0.0.1:8786
Start worker at:   tcp://127.0.0.1:36124
Registered to: tcp://127.0.0.1:8786
```
{: .mb-5}

- Connect to the cluster from a Python script
```python
>>> from dask.distributed import Client
>>> # wrap Dask client API use in a main check
>>> if __name__ == "__main__":
...     client = Client(address="127.0.0.1:8786")
...     # use_dask_APIs()
```
{: .mb-7}

#### **Notes**

- For more information on Dask CLI options use `dask-scheduler --help` and `dask-cuda-worker --help`

- More information on deploying manually can be found [here](https://docs.dask.org/en/latest/setup/cli.html).

- `dask-cuda-worker` is a convenient and optional extension of the normal `dask-worker` CLI command. You can also use `dask-worker` directly, manually configuring which GPUs are accessible to which workers:
```sh
$ CUDA_VISIBLE_DEVICES=0 dask-worker localhost:8786 --nprocs 1 --nthreads 1 --memory-limit 0
$ CUDA_VISIBLE_DEVICES=1 dask-worker localhost:8786 --nprocs 1 --nthreads 1 --memory-limit 0
```
{: .mb-5}

##### **Additional options**

  - [SSH](https://docs.dask.org/en/latest/setup/ssh.html)
```sh
$ dask-ssh 10.0.0.1 10.0.0.2 --remote-dask-worker dask_cuda.dask_cuda_worker
```

  - [NFS](https://docs.dask.org/en/latest/setup/hpc.html#using-a-shared-network-file-system-and-a-job-scheduler)
```sh
$ dask-scheduler --scheduler-file /path/to/file.json
$ dask-cuda-worker --scheduler-file /path/to/file.json
```
{: .mb-5}

### Kubernetes and Helm

RAPIDS libraries can also be deployed using [Kubernetes](https://kubernetes.io) and [Helm](https://helm.sh). This is useful for deploying RAPIDS on existing Kubernetes clusters, or to managed cloud Kubernetes services.

- [Install Helm](https://helm.sh/docs/using_helm/#installing-helm)
- [Link-to-k8-script-and-charts]

```sh
$ helm install [link-to-chart] --name rapids-dask --namespace rapids
```

- Check the status of the running pods

```sh
$ kubectl get pods -w --namespace rapids
```

- Additional Information:
GPU scheduling in [Kubernetes](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/)
[Dask Kubernetes](https://kubernetes.dask.org/en/latest/)
{: .mb-5}

### Docker Swarm

- Start a [swarm](https://docs.docker.com/engine/swarm), on a scheduler host.
```sh
$ docker swarm init
Swarm initialized: current node (xyz) is now a manager.
To add a worker to this swarm, run the following command:
    docker swarm join --token TOKEN_TO_JOIN 10.0.0.1:2377
```

- Executing the command provided above on the worker nodes.
```sh
$ docker swarm join --token TOKEN_TO_JOIN 10.0.0.1:2377
```

- Deploy services to the swarm using a [docker compose file](https://docs.docker.com/compose/compose-file/). A [RAPIDS docker compose](https://github.com/ayushdg/rapids-deployment/blob/master/docker-compose.yml) file is available to help you get started.
```sh
$ docker stack deploy -c docker-compose.yml test
```

- To stop the cluster
```sh
$ docker stack rm test
```
{: .mb-7}

#### **Notes**

- Generally the dask-scheduler should have access to the same data volume as the workers since it will often try to perform metadata operations on the files being processed.

### Cloud deployments

You can use a single type of configuration to deploy RAPIDS across multiple cloud providers with Kubernetes and Helm. You can also deploy RAPIDS through other managed service offerings where available.
