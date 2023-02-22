# Elastic Container Service (ECS)

```{warning}
This is a legacy page and may contain outdated information. We are working hard to update our documentation with the latest and greatest information, thank you for bearing with us.
```

RAPIDS can be deployed on a multi-node ECS cluster using Dask’s
dask-cloudprovider management tools. For more details, see our **[blog post on
deploying on
ECS.](https://medium.com/rapids-ai/getting-started-with-rapids-on-aws-ecs-using-dask-cloud-provider-b1adfdbc9c6e)**

**0. Run from within AWS.** The following steps assume you are running them from
within the same AWS VPC. One way to ensure this is to run through the [AWS
Single Instance (EC2)](#aws-single-instance-ec2) instructions and then run these steps from
there.

**1. Setup AWS credentials.** First, you will need AWS credentials to allow us
to interact with the AWS CLI. If someone else manages your AWS account, you will
need to get these keys from them. You can provide these credentials to
dask-cloudprovider in a number of ways, but the easiest is to setup your local
environment using the AWS command line tools:

```shell
$ pip install awscli
$ aws configure
```

**2. Install dask-cloudprovider.** To install, you will need to run the following:

```shell
$ pip install dask-cloudprovider[aws]
```

**3. Create an EC2 cluster:** In the AWS console, visit the ECS dashboard. From
the “Clusters” section on the left hand side, click “Create Cluster”.

Make sure to select an EC 2 Linux + Networking cluster so that we can specify
our networking options.

Give the cluster a name EX. `rapids-cluster`.

Change the instance type to one that supports RAPIDS-supported GPUs (see
introduction section for list of supported instance types). For this example, we
will use `p3.2xlarge`, each of which comes with one NVIDIA V100 GPU.

In the networking section, select the default VPC and all the subnets available
in that VPC.

All other options can be left at defaults. You can now click “create” and wait
for the cluster creation to complete.

**4. Create a Dask cluster:**

Get the Amazon Resource Name (ARN) for the cluster you just created.

Set `AWS_DEFAULT_REGION` environment variable to your **[default region](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions)**:

```shell
$ export AWS_DEFAULT_REGION=[REGION]
```

[REGION] = code fo the region being used.

Create the ECSCluster object in your Python session:

```python
from dask_cloudprovider.aws import ECSCluster

cluster = ECSCluster(
    cluster_arn=[CLUSTER_ARN], n_workers=[NUM_WORKERS], worker_gpu=[NUM_GPUS]
)
```

[CLUSTER_ARN] = The ARN of an existing ECS cluster to use for launching tasks <br />
[NUM_WORKERS] = Number of workers to start on cluster creation. <br />
[NUM_GPUS] = The number of GPUs to expose to the worker, this must be less than or equal to the number of GPUs in the instance type you selected for the ECS cluster (e.g `1` for `p3.2xlarge`).

**5. Test RAPIDS.** Create a distributed client for our cluster:

```python
from dask.distributed import Client

client = Client(cluster)
```

Load sample data and test the cluster!

```python
import dask, cudf, dask_cudf

ddf = dask.datasets.timeseries()
gdf = ddf.map_partitions(cudf.from_pandas)
gdf.groupby("name").id.count().compute().head()
```

```shell
Out[34]:
Xavier 99495
Oliver 100251
Charlie 99354
Zelda 99709
Alice 100106
Name: id, dtype: int64
```

**6. Cleanup.** Your cluster will continue to run (and incur charges!) until you
shut it down. You can either scale the number of nodes down to zero instances,
or shut it down altogether. If you are planning to use the cluster again soon,
it is probably preferable to reduce the nodes to zero.

```{relatedexamples}

```
