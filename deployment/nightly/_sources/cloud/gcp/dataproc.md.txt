# Dataproc

RAPIDS can be deployed on Google Cloud Dataproc using Dask. For more details, see our **[detailed instructions and helper scripts.](https://github.com/GoogleCloudDataproc/initialization-actions/tree/master/rapids)**

**0. Copy initialization actions to your own Cloud Storage bucket.** Don't create clusters that reference initialization actions located in `gs://goog-dataproc-initialization-actions-REGION` public buckets. These scripts are provided as reference implementations and are synchronized with ongoing [GitHub repository](https://github.com/GoogleCloudDataproc/initialization-actions) changes.

It is strongly recommended that you copy the initialization scripts into your own Storage bucket to prevent unintended upgrades from upstream in the cluster:

```console
$ REGION=<region>
$ GCS_BUCKET=<bucket_name>
$ gcloud storage buckets create gs://$GCS_BUCKET
$ gsutil cp gs://goog-dataproc-initialization-actions-${REGION}/gpu/install_gpu_driver.sh gs://$GCS_BUCKET
$ gsutil cp gs://goog-dataproc-initialization-actions-${REGION}/dask/dask.sh gs://$GCS_BUCKET
$ gsutil cp gs://goog-dataproc-initialization-actions-${REGION}/rapids/rapids.sh gs://$GCS_BUCKET

```

**1. Create Dataproc cluster with Dask RAPIDS.** Use the gcloud command to create a new cluster. Because of an Anaconda version conflict, script deployment on older images is slow, we recommend using Dask with Dataproc 2.0+.

```console
$ CLUSTER_NAME=<CLUSTER_NAME>
$ DASK_RUNTIME=yarn
$ gcloud dataproc clusters create $CLUSTER_NAME\
    --region $REGION\
    --image-version 2.0-ubuntu18\
    --master-machine-type n1-standard-32\
    --master-accelerator type=nvidia-tesla-t4,count=2\
    --worker-machine-type n1-standard-32\
    --worker-accelerator type=nvidia-tesla-t4,count=2\
    --initialization-actions=gs://$GCS_BUCKET/install_gpu_driver.sh,gs://$GCS_BUCKET/dask.sh,gs://$GCS_BUCKET/rapids.sh\
    --initialization-action-timeout 60m\
    --optional-components=JUPYTER\
    --metadata gpu-driver-provider=NVIDIA,dask-runtime=$DASK_RUNTIME,rapids-runtime=DASK\
    --enable-component-gateway

```

[GCS_BUCKET] = name of the bucket to use.\
[CLUSTER_NAME] = name of the cluster.\
[REGION] = name of region where cluster is to be created.\
[DASK_RUNTIME] = Dask runtime could be set to either yarn or standalone.

**2. Run Dask RAPIDS Workload.** Once the cluster has been created, the Dask scheduler listens for workers on `port 8786`, and its status dashboard is on `port 8787` on the Dataproc master node.

To connect to the Dask web interface, you will need to create an SSH tunnel as described in the [Dataproc web interfaces documentation.](https://cloud.google.com/dataproc/docs/concepts/accessing/cluster-web-interfaces) You can also connect using the Dask Client Python API from a Jupyter notebook, or from a Python script or interpreter session.

```{relatedexamples}

```
