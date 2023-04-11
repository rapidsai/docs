# LocalCUDACluster

Create a cluster of one or more GPUs on your local machine. You can launch a Dask scheduler on LocalCUDACluster to parallelize and distribute your RAPIDS workflows across multiple GPUs on a single node.

In addition to enabling multi-GPU computation, `LocalCUDACluster` also provides a simple interface for managing the cluster, such as starting and stopping the cluster, querying the status of the nodes, and monitoring the workload distribution.

## Pre-requisites

Before running these instructions, ensure you have installed the [`dask`](https://docs.dask.org/en/stable/install.html) and [`dask_cuda`](https://docs.rapids.ai/api/dask-cuda/nightly/install.html) packages in your local environment

## Cluster setup

### Instantiate a LocalCUDACluster object

In this example, we create a cluster with two workers, each of which is responsible for executing tasks on a separate GPU.

```console
cluster = LocalCUDACluster(n_workers=2)
```

### Connecting a Dask client

Dask scheduler coordinates the execution of tasks, whereas Dask client is the user-facing interface that submits tasks to the scheduler and monitors their progress.

```console
client = Client(cluster)
```

## Test RAPIDS

To test RAPIDS, create a distributed client for the cluster and query for the GPU model.

```Python
from dask_cuda import LocalCUDACluster
from dask.distributed import Client

cluster = LocalCUDACluster()
client = Client(cluster)

def get_gpu_model():
    import pynvml

    pynvml.nvmlInit()
    return pynvml.nvmlDeviceGetName(pynvml.nvmlDeviceGetHandleByIndex(0))


client.submit(get_gpu_model).result()
```

## 3.Clean up

Be sure to shut down and clean LocalCUDACluster when you are done:

```console
client.close()
cluster.close()
```
