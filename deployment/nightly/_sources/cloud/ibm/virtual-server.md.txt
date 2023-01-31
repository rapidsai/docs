# Virtual Server for VPC

## Create Instance

Create a new [Virtual Server (for VPC)](https://www.ibm.com/cloud/virtual-servers) with GPUs, the [NVIDIA Driver](https://www.nvidia.co.uk/Download/index.aspx) and the [NVIDIA Container Runtime](https://developer.nvidia.com/nvidia-container-runtime).

1. Open the [**Virtual Server Dashboard**](https://cloud.ibm.com/vpc-ext/compute/vs).
1. Select **Create**.
1. Give the server a **name** and select your **resource group**.
1. Under **Operating System** choose **Ubuntu Linux**.
1. Under **Profile** select **View all profiles** and select a profile with NVIDIA GPUs.
1. Under **SSH Keys** choose your SSH key.
1. Under network settings create a security group (or choose an existing) that allows SSH access on port `22` and also allow ports `8888,8786,8787` to access Jupyter and Dask.
1. Select **Create Virtual Server**.

## Create floating IP

To access the virtual server we need to attach a public IP address.

1. Open [**Floating IPs**](https://cloud.ibm.com/vpc-ext/network/floatingIPs)
1. Select **Reserve**.
1. Give the Floating IP a **name**.
1. Under **Resource to bind** select the virtual server you just created.

## Connect to the instance

Next we need to connect to the instance.

1. Open [**Floating IPs**](https://cloud.ibm.com/vpc-ext/network/floatingIPs)
1. Locate the IP you just created and note the address.
1. In your terminal run `ssh root@<ip address>`

```{note}
For a short guide on launching your instance and accessing it, read the
[Getting Started with IBM Virtual Server Documentation](https://cloud.ibm.com/docs/virtual-servers?topic=virtual-servers-getting-started-tutorial).
```

## Install NVIDIA Drivers

Next we need to install the NVIDIA drivers and container runtime.

1. Ensure build essentials are installed `apt-get update && apt-get install build-essential -y`.
1. Install the [NVIDIA drivers](https://www.nvidia.com/Download/index.aspx?lang=en-us).
1. Install [Docker and the NVIDIA Docker runtime](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html).

````{dropdown} How do I check everything installed successfully?
:color: info
:icon: info

You can check everything installed correctly by running `nvidia-smi` in a container.

```console
$ docker run --rm --gpus all nvidia/cuda:11.6.2-base-ubuntu20.04 nvidia-smi
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 510.108.03   Driver Version: 510.108.03   CUDA Version: 11.6     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla V100-PCIE...  Off  | 00000000:04:01.0 Off |                    0 |
| N/A   33C    P0    36W / 250W |      0MiB / 16384MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```

````

## Install RAPIDS

```{include} ../../_includes/install-rapids-with-docker.md

```

## Test RAPIDS

```{include} ../../_includes/test-rapids-docker-vm.md

```

```{relatedexamples}

```
