# Elastic Compute Cloud (EC2)

## Create Instance

Create a new [EC2 Instance](https://aws.amazon.com/ec2/) with GPUs, the [NVIDIA Driver](https://www.nvidia.co.uk/Download/index.aspx) and the [NVIDIA Container Runtime](https://developer.nvidia.com/nvidia-container-runtime).

NVIDIA maintains an [Amazon Machine Image (AMI) that pre-installs NVIDIA drivers and container runtimes](https://aws.amazon.com/marketplace/pp/prodview-7ikjtg3um26wq), we recommend using this image as the starting point.

1. Open the [**EC2 Dashboard**](https://console.aws.amazon.com/ec2/home).
1. Select **Launch Instance**.
1. In the AMI selection box search for "nvidia", then switch to the **AWS Marketplace AMIs** tab.
1. Select **NVIDIA GPU-Optimized VMI**, then select **Select** and then **Continue**.
1. In **Key pair** select your SSH keys (create these first if you haven't already).
1. Under network settings create a security group (or choose an existing) that allows SSH access on port `22` and also allow ports `8888,8786,8787` to access Jupyter and Dask.
1. Select **Launch**.

## Connect to the instance

Next we need to connect to the instance.

1. Open the [**EC2 Dashboard**](https://console.aws.amazon.com/ec2/home).
2. Locate your VM and note the **Public IP Address**.
3. In your terminal run `ssh ubuntu@<ip address>`

## Install RAPIDS

```{include} ../../_includes/install-rapids-with-docker.md

```

## Test RAPIDS

```{include} ../../_includes/test-rapids-docker-vm.md

```
