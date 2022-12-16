# Dataproc

```{warning}
This is a legacy page and may contain outdated information. We are working hard to update our documentation with the latest and greatest information, thank you for bearing with us.
```

RAPIDS can be deployed on Google Cloud Dataproc using Dask. We have **[helper scripts and detailed instructions](https://github.com/GoogleCloudDataproc/initialization-actions/tree/master/rapids)** to help.

**1. Create Dataproc cluster with Dask RAPIDS.** Use the gcloud command to create a new cluster with the below initialization action. Because of an Anaconda version conflict, script deployment on older images is slow, we recommend using Dask with Dataproc 2.0+.

```console
$ export GCS_BUCKET=[BUCKET_NAME]
$ export CLUSTER_NAME=[CLUSTER_NAME]
$ export REGION=[REGION]
$ export DASK_RUNTIME=[DASK_RUNTIME]
$ gcloud dataproc clusters create $CLUSTER_NAME\
    --region $REGION\
    --image-version preview-ubuntu18\
    --master-machine-type [MACHINE_TYPE]\
    --master-accelerator type=[GPU_TYPE],count=[NUM_GPU]\
    --worker-machine-type [MACHINE_TYPE]\
    --worker-accelerator type=[GPU_TYPE],count=[NUM_GPU]\
    --optional-components=ANACONDA\
    --initialization-actions gs://goog-dataproc-initialization-actions-${REGION}/gpu/install_gpu_driver.sh,gs://goog-dataproc-initialization-actions-${REGION}/dask/dask.sh,gs://goog-dataproc-initialization-actions-${REGION}/rapids/rapids.sh\
    --initialization-action-timeout=60m\
    --metadata gpu-driver-provider=NVIDIA,dask-runtime=${DASK_RUNTIME},rapids-runtime=DASK\
    --enable-component-gateway

```

[BUCKET_NAME] = name of the bucket to use.\
[CLUSTER_NAME] = name of the cluster.\
[REGION] = name of region where cluster is to be created.\
[DASK_RUNTIME] = Dask runtime could be set to either yarn or standalone.

**2. Run Dask RAPIDS Workload.** Once the cluster has been created, the Dask scheduler listens for workers on port 8786, and its status dashboard is on port 8787 on the Dataproc master node. To connect to the Dask web interface, you will need to create an SSH tunnel as described in the **[Dataproc web interfaces documentation.](https://cloud.google.com/dataproc/docs/concepts/accessing/cluster-web-interfaces)** You can also connect using the Dask Client Python API from a Jupyter notebook, or from a Python script or interpreter session.

For more, see our **[detailed instructions and helper scripts.](https://github.com/GoogleCloudDataproc/initialization-actions/tree/master/rapids)**
