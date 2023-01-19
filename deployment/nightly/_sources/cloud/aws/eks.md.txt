# AWS Elastic Kubernetes Service (EKS)

RAPIDS can be deployed on AWS via the [Elastic Kubernetes Service](https://aws.amazon.com/eks/) (EKS).

To run RAPIDS you'll need a Kubernetes cluster with GPUs available.

## Prerequisites

First you'll need to have the [`aws` CLI tool](https://aws.amazon.com/cli/) and [`eksctl` CLI tool](https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html) installed along with [`kubectl`](https://kubernetes.io/docs/tasks/tools/), [`helm`](https://helm.sh/docs/intro/install/), etc for managing Kubernetes.

Ensure you are logged into the `aws` CLI.

```console
$ aws configure
```

## Create the Kubernetes cluster

Now we can launch a GPU enabled EKS cluster. First launch an EKS cluster with `eksctl`.

```console
$ eksctl create cluster rapids \
                      --version 1.24 \
                      --nodes 3 \
                      --node-type=p3.8xlarge \
                      --timeout=40m \
                      --ssh-access \
                      --ssh-public-key <public key ID> \  # Be sure to set your public key ID here
                      --region us-east-1 \
                      --zones=us-east-1c,us-east-1b,us-east-1d \
                      --auto-kubeconfig \
                      --install-nvidia-plugin=false
```

With this command, you’ve launched an EKS cluster called `rapids`. You’ve specified that it should use nodes of type `p3.8xlarge`. We also specified that we don't want to install the NVIDIA drivers as we will do that with the NVIDIA operator.

To access the cluster we need to pull down the credentials.

```console
$ aws eks --region us-east-1 update-kubeconfig --name rapids
```

## Install drivers

Next, [install the NVIDIA drivers](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/getting-started.html) onto each node.

```console
$ helm install --repo https://helm.ngc.nvidia.com/nvidia --wait --generate-name -n gpu-operator --create-namespace gpu-operator
NAME: gpu-operator-1670843572
NAMESPACE: gpu-operator
STATUS: deployed
REVISION: 1
TEST SUITE: None
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

After your drivers are installed, you are ready to test your cluster.

```{include} ../../_includes/check-gpu-pod-works.md

```

## Install RAPIDS

Now that you have a GPU enabled Kubernetes cluster on EKS you can install RAPIDS with [any of the supported methods](../../platforms/kubernetes).

## Clean up

You can also delete the EKS cluster to stop billing with the following command.

```console
$ eksctl delete cluster --region=us-east-1 --name=rapids
Deleting cluster rapids...⠼
```
