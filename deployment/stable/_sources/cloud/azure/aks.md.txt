# Azure Kubernetes Service

RAPIDS can be deployed on Azure via the [Azure Kubernetes Service](https://azure.microsoft.com/en-us/products/kubernetes-service/) (AKS).

To run RAPIDS you'll need a Kubernetes cluster with GPUs available.

## Prerequisites

First you'll need to have the [`az` CLI tool](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) installed along with [`kubectl`](https://kubernetes.io/docs/tasks/tools/), [`helm`](https://helm.sh/docs/intro/install/), etc for managing Kubernetes.

Ensure you are logged into the `az` CLI.

```console
$ az login
```

## Create the Kubernetes cluster

Now we can launch a GPU enabled AKS cluster. First launch an AKS cluster.

```console
$ az aks create -g <resource group> -n rapids \
        --enable-managed-identity \
        --node-count 1 \
        --enable-addons monitoring \
        --enable-msi-auth-for-monitoring  \
        --generate-ssh-keys
```

Once the cluster has created we need to pull the credentials into our local config.

```console
$ az aks get-credentials -g <resource group> --name rapids
Merged "rapids" as current context in ~/.kube/config
```

Next we need to add an additional node group with GPUs which you can [learn more about in the Azure docs](https://learn.microsoft.com/en-us/azure/aks/gpu-cluster).

`````{note}
You will need the `GPUDedicatedVHDPreview` feature enabled so that NVIDIA drivers are installed automatically.

You can check if this is enabled with:

````console
$ az feature list -o table --query "[?contains(name, 'Microsoft.ContainerService/GPUDedicatedVHDPreview')].{Name:name,State:properties.state}"
Name                                               State
-------------------------------------------------  -------------
Microsoft.ContainerService/GPUDedicatedVHDPreview  NotRegistered
````

````{dropdown} If you see NotRegistered follow these instructions
:color: info
:icon: info

If it is not registered for you you'll need to register it which can take a few minutes.

```console
$ az feature register --name GPUDedicatedVHDPreview --namespace Microsoft.ContainerService
Once the feature 'GPUDedicatedVHDPreview' is registered, invoking 'az provider register -n Microsoft.ContainerService' is required to get the change propagated
Name
-------------------------------------------------
Microsoft.ContainerService/GPUDedicatedVHDPreview
```

Keep checking until it does into a registered state.

```console
$ az feature list -o table --query "[?contains(name, 'Microsoft.ContainerService/GPUDedicatedVHDPreview')].{Name:name,State:properties.state}"
Name                                               State
-------------------------------------------------  -----------
Microsoft.ContainerService/GPUDedicatedVHDPreview  Registered
```

When the status shows as registered, refresh the registration of the `Microsoft.ContainerService` resource provider by using the `az provider register` command:

```console
$ az provider register --namespace Microsoft.ContainerService
```

Then install the aks-preview CLI extension, use the following Azure CLI commands:

```console
$ az extension add --name aks-preview
```

````

`````

```console
$ az aks nodepool add \
    --resource-group <resource group> \
    --cluster-name rapids \
    --name gpunp \
    --node-count 1 \
    --node-vm-size Standard_NC48ads_A100_v4 \
    --node-taints sku=gpu:NoSchedule \
    --aks-custom-headers UseGPUDedicatedVHD=true \
    --enable-cluster-autoscaler \
    --min-count 1 \
    --max-count 3
```

Here we have added a new pool made up of `Standard_NC48ads_A100_v4` instances which each have two A100 GPUs. We've also enabled autoscaling on the pool and added the `gpu:NoSchedule` taint to ensure that only our GPU pods end up on those nodes.

Once our new pool has been created we should be able to test that we can schedule GPU pods.

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
  tolerations:
  - key: "sku"
    operator: "Equal"
    value: "gpu"
    effect: "NoSchedule"
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

Now that you have a GPU enables Kubernetes cluster on AKS you can install RAPIDS with [any of the supported methods](../../platforms/kubernetes).

## Clean up

You can also delete the AKS cluster to stop billing with the following command.

```console
$ az aks delete -g <resource group> -n rapids
/ Running ..
```
