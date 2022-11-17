# Compute Engine Instance

The easiest way to deploy RAPIDS on a single instance is to use the `rapidsai/rapidsai` Docker image.

**1. Create a VM instance.** In the GCP console, nagivate to `Compute Engine` -> `VM instances` -> `CREATE INSTANCE`.

Under the `Machine configuration` setting, select `GPU` and choose your NVIDIA GPU type and number.

Next under the `Container` setting, select `Deploy Container` and specify your preferred registry location of the `rapidsai/rapidsai` as your container image and check `Allocate a buffer for STDIN` and `Allocate a pseudo-TTY` to enable interactivty with the container.

After customizing other aspects of your VM, click `CREATE` to initialize the VM.

For the `gcloud` CLI, you can use the `gcloud compute instances create-with-container` command with at _minimum_ flags:

```shell
$ gcloud compute instances create-with-container $INSTANCE_NAME --container-image=$IMAGE_PATH --accelerator=count=$GPU_NUMBER,type=$GPU_TYPE --container-stdin --container-tty
```

**2. Test RAPIDS.**

Once the VM is running, you can SSH into the VM from the GCP console or using the `gcloud` CLI using `gcloud compute ssh` and `docker attach` to the container enter a shell to start using RAPIDS.

```shell
USER@VM-NAME ~ $ docker attach $CONTAINER_ID
(rapids) root@VM-NAME:/rapids/notebooks# conda list cudf
# packages in environment at /opt/conda/envs/rapids:
#
# Name                    Version                   Build  Channel
cudf                      22.08.00        cuda_11_py39_gb71873c701_0    rapidsai
cudf_kafka                22.08.00        py39_gb71873c701_0    rapidsai
dask-cudf                 22.08.00        cuda_11_py39_gb71873c701_0    rapidsai
libcudf                   22.08.00        cuda11_gb71873c701_0    rapidsai
libcudf_kafka             22.08.00          gb71873c701_0    rapidsai
```
