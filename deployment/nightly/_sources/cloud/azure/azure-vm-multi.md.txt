# Azure VM Cluster (via Dask)

## Create a Cluster using Dask Cloud Provider

The easiest way to setup a multi-node, multi-GPU cluster on Azure is to use [Dask Cloud Provider](https://cloudprovider.dask.org/en/latest/azure.html).

### 1. Install Dask Cloud Provider

Dask Cloud Provider can be installed via `conda` or `pip`. The Azure-specific capabilities will need to be installed via the `[azure]` pip extra.

```shell
$ pip install dask-cloudprovider[azure]
```

### 2. Configure your Azure Resources

Set up your [Azure Resouce Group](https://cloudprovider.dask.org/en/latest/azure.html#resource-groups), [Virtual Network](https://cloudprovider.dask.org/en/latest/azure.html#virtual-networks), and [Security Group](https://cloudprovider.dask.org/en/latest/azure.html#security-groups) according to [Dask Cloud Provider instructions](https://cloudprovider.dask.org/en/latest/azure.html#authentication).

### 3. Create a Cluster

In Python terminal, a cluster can be created using the `dask_cloudprovider` package. The below example creates a cluster with 2 workers in `westus2` with `Standard_NC12s_v3` VMs. The VMs should have at least 100GB of disk space in order to accommodate the RAPIDS container image and related dependencies.

```python
from dask_cloudprovider.azure import AzureVMCluster

resource_group = "<RESOURCE_GROUP>"
vnet = "<VNET>"
security_group = "<SECURITY_GROUP>"
subscription_id = "<SUBSCRIPTION_ID>"
cluster = AzureVMCluster(
    resource_group=resource_group,
    vnet=vnet,
    security_group=security_group,
    subscription_id=security_group,
    location="westus2",
    vm_size="Standard_NC12s_v3",
    public_ingress=True,
    disk_size=100,
    n_workers=2,
    worker_class="dask_cuda.CUDAWorker",
    docker_image="rapidsai/rapidsai-core:22.12-cuda11.5-runtime-ubuntu20.04-py3.9",
    docker_args="-e DISABLE_JUPYTER=true -p 8787:8787 -p 8786:8786",
)
```

### 4. Test RAPIDS

To test RAPIDS, create a distributed client for the cluster and query for the GPU model.

```python
from dask.distributed import Client

client = Client(cluster)


def get_gpu_model():
    import pynvml

    pynvml.nvmlInit()
    return pynvml.nvmlDeviceGetName(pynvml.nvmlDeviceGetHandleByIndex(0))


client.submit(get_gpu_model).result()
```

```shell
Out[5]: b'Tesla V100-PCIE-16GB'
```

### 5. Cleanup

Once done with the cluster, ensure the `cluster` and `client` are closed:

```python
client.close()
cluster.close()
```

```{relatedexamples}

```
