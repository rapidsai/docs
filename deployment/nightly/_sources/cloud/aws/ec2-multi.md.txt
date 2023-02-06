# EC2 Cluster (via Dask)

To launch a multi-node cluster on AWS EC2 we recommend you use [Dask Cloud Provider](https://cloudprovider.dask.org/en/latest/), a native cloud integration for Dask. It helps manage Dask clusters on different cloud platforms.

## Local Environment Setup

Before running these instructions, ensure you have installed RAPIDS.

```{note}
This method of deploying RAPIDS effectively allows you to burst beyond the node you are on into a cluster of EC2 VMs. This does come with the caveat that you are on a RAPIDS capable environment with GPUs.
```

If you are using a machine with an NVIDIA GPU then follow the [local install instructions](../../local). Alternatively if you do not have a GPU locally consider using s remote environment like a [SageMaker Notebook Instance](./sagemaker).

### Install the AWS CLI

Install the AWS CLI tools following the [official instructions](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

### Install Dask Cloud Provider

Also install `dask-cloudprovider` and ensure you select the `aws` optional extras.

```console
$ pip install "dask-cloudprovider[aws]"
```

## Cluster setup

We'll now setup the [EC2Cluster](https://cloudprovider.dask.org/en/latest/aws.html#elastic-compute-cloud-ec2) from Dask Cloud Provider.

To do this, you'll first need to run `aws configure` and ensure the credentials are updated. [Learn more about the setup](https://cloudprovider.dask.org/en/latest/aws.html#authentication). The API also expects a security group that allows access to ports 8786-8787 and all traffic between instances in the security group. If you do not pass a group here, `dask-cloudprovider` will create one for you.

```python
from dask_cloudprovider.aws import EC2Cluster

cluster = EC2Cluster(
    instance_type="g4dn.12xlarge",  # 4 T4 GPUs
    docker_image="rapidsai/rapidsai-core:22.12-cuda11.5-runtime-ubuntu20.04-py3.9",
    worker_class="dask_cuda.CUDAWorker",
    worker_options={"rmm-managed-memory": True},
    security_groups=["<SECURITY GROUP ID>"],
    docker_args="--shm-size=256m -e DISABLE_JUPYTER=true",
    n_workers=3,
    security=False,
    availability_zone="us-east-1a",
    region="us-east-1",
)
```

```{warning}
Instantiating this class can take upwards of 30 minutes. See the [Dask docs](https://cloudprovider.dask.org/en/latest/packer.html) on prebuilding AMIs to speed this up.
```

````{dropdown} If you have non-default credentials you may need to pass your credentials manually.
:color: info
:icon: info

Here's a small utility for parsing credential profiles.

```python
import os
import configparser
import contextlib


def get_aws_credentials(*, aws_profile="default"):
    parser = configparser.RawConfigParser()
    parser.read(os.path.expanduser("~/.aws/config"))
    config = parser.items(
        f"profile {aws_profile}" if aws_profile != "default" else "default"
    )
    parser.read(os.path.expanduser("~/.aws/credentials"))
    credentials = parser.items(aws_profile)
    all_credentials = {key.upper(): value for key, value in [*config, *credentials]}
    with contextlib.suppress(KeyError):
        all_credentials["AWS_REGION"] = all_credentials.pop("REGION")
    return all_credentials
```

```python
cluster = EC2Cluster(..., env_vars=get_aws_credentials(aws_profile="foo"))
```

````

## Connecting a client

Once your cluster has started you can connect a Dask client to submit work.

```python
from dask.distributed import Client

client = Client(cluster)
```

```python
import cudf
import dask_cudf

df = dask_cudf.from_cudf(cudf.datasets.timeseries(), npartitions=2)
df.x.mean().compute()
```

## Clean up

When you create your cluster Dask Cloud Provider will register a finalizer to shutdown the cluster. So when your Python process exits the cluster will be cleaned up.

You can also explicitly shutdown the cluster with:

```python
client.close()
cluster.close()
```

```{relatedexamples}

```
