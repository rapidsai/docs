# Google Kubernetes Engine

RAPIDS can be deployed on Google Cloud via the [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine) (GKE).

To run RAPIDS you'll need a Kubernetes cluster with GPUs available.

## Prerequisites

First you'll need to have the [`gcloud` CLI tool](https://cloud.google.com/sdk/gcloud) installed along with [`kubectl`](https://kubernetes.io/docs/tasks/tools/), [`helm`](https://helm.sh/docs/intro/install/), etc for managing Kubernetes.

Ensure you are logged into the `gcloud` CLI.

```console
$ gcloud init
```

## Create the Kubernetes cluster

Now we can launch a GPU enabled GKE cluster.

```console
$ gcloud container clusters create rapids \
  --accelerator type=nvidia-tesla-a100,count=2 --machine-type a2-highgpu-2g \
  --zone us-central1-c --release-channel stable
```

With this command, you’ve launched a GKE cluster called rapids-gpu-kubeflow. You’ve specified that it should use nodes of type a2-highgpu-2g, each with two A100 GPUs.

## Install drivers

Next, [install the NVIDIA drivers](https://cloud.google.com/kubernetes-engine/docs/how-to/gpus#installing_drivers) onto each node.

```console
$ kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/nvidia-driver-installer/cos/daemonset-preloaded-latest.yaml
daemonset.apps/nvidia-driver-installer created
```

Verify that the NVIDIA drivers are successfully installed.

```console
$ kubectl get po -A --watch | grep nvidia
kube-system   nvidia-driver-installer-6zwcn                                 1/1     Running   0         8m47s
kube-system   nvidia-driver-installer-8zmmn                                 1/1     Running   0         8m47s
kube-system   nvidia-driver-installer-mjkb8                                 1/1     Running   0         8m47s
kube-system   nvidia-gpu-device-plugin-5ffkm                                1/1     Running   0         13m
kube-system   nvidia-gpu-device-plugin-d599s                                1/1     Running   0         13m
kube-system   nvidia-gpu-device-plugin-jrgjh                                1/1     Running   0         13m
```

After your drivers are installed, create a quick sample pod that uses some GPU compute to make sure that everything is working as expected.

```console
$ cat << EOF | kubectl create -f -
apiVersion: v1
kind: Pod
metadata:
  name: cuda-vectoradd
spec:
  restartPolicy: OnFailure
  containers:
  - name: cuda-vectoradd
    image: "nvidia/samples:vectoradd-cuda11.2.1"
    resources:
       limits:
         nvidia.com/gpu: 1
EOF
```

```console
$ kubectl logs pod/cuda-vectoradd
[Vector addition of 50000 elements]
Copy input data from the host memory to the CUDA device
CUDA kernel launch with 196 blocks of 256 threads
Copy output data from the CUDA device to the host memory
Test PASSED
Done
```

If you see `Test PASSED` in the output, you can be confident that your Kubernetes cluster has GPU compute set up correctly.

Next, clean up that pod.

```console
$ kubectl delete po cuda-vectoradd
pod "cuda-vectoradd" deleted
```

## Install RAPIDS

Now that you have a GPU enables Kubernetes cluster on GKE you can install RAPIDS with [any of the supported methods](../../platforms/kubernetes).

## Clean up

You can also delete the GKE cluster to stop billing with the following command.

```console
$ gcloud container clusters delete rapids --zone us-central1-c
Deleting cluster rapids...⠼
```
