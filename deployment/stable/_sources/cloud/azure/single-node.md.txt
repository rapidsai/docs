# Azure Single Node RAPIDS

## Create Azure Virtual Machine with GPU, Nvidia Driver and Nvidia Container Runtime

Nvidia maintains an image that pre-installs Nvidia drivers and container runtimes,
we recommend using [this image](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/nvidia.ngc_azure_17_11?tab=Overview) as the starting point.

### Option 1: Create VM Via Azure Portal

1. Select the latest Nvidia GPU-Optimized VMI version from the drop down list, then select _Get It Now_.
2. If already logged in on Azure, select continue clicking _Create_.
3. In _Create a virtual machine_ interface, fill in required information for the vm.
   Select a GPU enabled VM size.

```{note}
Note that not all region support availability zone for GPU VMs. When the GPU VM size is not selectable
with notice: **The size is not available in zone x. No zones are supported.** It means the GPU VM does not
support availability zone. Try other availability options.

![azure-gpuvm-availability-zone-error](../../_static/azure_availability_zone.PNG)
```

Click _Review+Create_ to start the virtual machine.

### Option 2: Create VM Via Azure-CLI

Prepare the following environment variables.

| Name             | Description          | Example                                                      |
| ---------------- | -------------------- | ------------------------------------------------------------ |
| AZ_VMNAME        | Name for VM          | RapidsAI-V100                                                |
| AZ_RESOURCEGROUP | Resource group of VM | rapidsai-deployment                                          |
| AZ_LOCATION      | Region of VM         | westus2                                                      |
| AZ_IMAGE         | URN of image         | nvidia:ngc_azure_17_11:ngc-base-version-22_06_0-gen2:22.06.0 |
| AZ_SIZE          | VM Size              | Standard_NC6s_v3                                             |
| AZ_USERNAME      | User name of VM      | rapidsai                                                     |
| AZ_SSH_KEY       | public ssh key       | ~/.ssh/id_rsa.pub                                            |

```bash
az vm create \
        --name ${AZ_VMNAME} \
        --resource-group ${AZ_RESOURCEGROUP} \
        --image ${AZ_IMAGE} \
        --location ${AZ_LOCATION} \
        --size ${AZ_SIZE} \
        --admin-username ${AZ_USERNAME} \
        --ssh-key-value ${AZ_SSH_KEY}
```

```{note}
Use `az vm image list --publisher Nvidia --all --output table` to inspect URNs of official
Nvidia images on Azure.
```

```{note}
See [this link](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/mac-create-ssh-keys)
for supported ssh keys on Azure.
```

## Create Network Security Group

### Option 1: Create NSG Via Azure Portal

1. Select _Networking_ in the left panel.
2. Select _Add inbound port rule_.
3. Set _Destination port ranges_ to `8888,8787`. Keep rest unchanged. Select _Add_.

### Option 2: Create NSG Via Azure-CLI

| Name           | Description         | Example                  |
| -------------- | ------------------- | ------------------------ |
| AZ_NSGNAME     | NSG name for the VM | ${AZ_VMNAME}NSG          |
| AZ_NSGRULENAME | Name for NSG rule   | Allow-Dask-Jupyter-ports |

```bash
az network nsg rule create \
    -g ${AZ_RESOURCEGROUP} \
    --nsg-name ${AZ_NSGNAME} \
    -n ${AZ_NSGRULENAME} \
    --priority 1050 \
    --destination-port-ranges 8888 8787
```

## Install RAPIDS

It can take up to 10 minutes to provision a GPU VM. When available, ssh into the machine.

Visit [rapids release selector](https://rapids.ai/start.html#get-rapids) and choose `Docker` in `METHOD`
column. For example, to pull 22.10 stable image and run the container:

```bash
docker pull nvcr.io/nvidia/rapidsai/rapidsai-core:22.10-cuda11.5-runtime-ubuntu20.04-py3.9
docker run --gpus all --rm -it \
    --shm-size=1g --ulimit memlock=-1 \
    -p 8888:8888 -p 8787:8787 -p 8786:8786 \
    nvcr.io/nvidia/rapidsai/rapidsai-core:22.10-cuda11.5-runtime-ubuntu20.04-py3.9
```

## Test RAPIDS

Access the jupyter-lab portal via `<ip>:8888` in the browser. Visit `cudf/10-min.ipynb` and
execute the cells. Open dask dashboard on the left and enter `<ip>:8787` in the url blank
to monitor dask worker status.

### Useful Links

- [Using NGC with Azure](https://docs.nvidia.com/ngc/ngc-azure-setup-guide/index.html)
