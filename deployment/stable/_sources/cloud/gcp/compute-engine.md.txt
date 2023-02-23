# Compute Engine Instance

## Create Virtual Machine

Create a new [Compute Engine Instance](https://cloud.google.com/compute/docs/instances) with GPUs, the [NVIDIA Driver](https://www.nvidia.co.uk/Download/index.aspx) and the [NVIDIA Container Runtime](https://developer.nvidia.com/nvidia-container-runtime).

NVIDIA maintains a [Virtual Machine Image (VMI) that pre-installs NVIDIA drivers and container runtimes](https://console.cloud.google.com/marketplace/product/nvidia-ngc-public/nvidia-gpu-optimized-vmi), we recommend using this image.

1. Open [**Compute Engine**](https://console.cloud.google.com/compute/instances).
1. Select **Create Instance**.
1. Select **Marketplace**.
1. Search for "nvidia" and select **NVIDIA GPU-Optimized VMI**, then select **Launch**.
1. In the **New NVIDIA GPU-Optimized VMI deployment** interface, fill in the name and any required information for the vm (the defaults should be fine for most users).
1. **Read and accept** the Terms of Service
1. Select **Deploy** to start the virtual machine.

## Allow network access

To access Jupyter and Dask we will need to set up some firewall rules to open up some ports.

### Create the firewall rule

1. Open [**VPC Network**](https://console.cloud.google.com/networking/networks/list).
2. Select **Firewall** and **Create firewall rule**
3. Give the rule a name like `rapids` and ensure the network matches the one you selected for the VM.
4. Add a tag like `rapids` which we will use to assign the rule to our VM.
5. Set your source IP range. We recommend you restrict this to your own IP address or your corporate network rather than `0.0.0.0/0` which will allow anyone to access your VM.
6. Under **Protocols and ports** allow TCP connections on ports `8786,8787,8888`.

### Assign it to the VM

1. Open [**Compute Engine**](https://console.cloud.google.com/compute/instances).
2. Select your VM and press **Edit**.
3. Scroll down to **Networking** and add the `rapids` network tag you gave your firewall rule.
4. Select **Save**.

## Connect to the VM

Next we need to connect to the VM.

1. Open [**Compute Engine**](https://console.cloud.google.com/compute/instances).
2. Locate your VM and press the **SSH** button which will open a new browser tab with a terminal.
3. **Read and accept** the NVIDIA installer prompts.

## Install RAPIDS

```{include} ../../_includes/install-rapids-with-docker.md

```

## Test RAPIDS

```{include} ../../_includes/test-rapids-docker-vm.md

```

## Clean up

Once you are finished head back to the [Deployments](https://console.cloud.google.com/dm/deployments) page and delete the marketplace deployment you created.

```{relatedexamples}

```
