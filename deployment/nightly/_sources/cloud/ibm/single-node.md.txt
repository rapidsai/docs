# Single Node

There are multiple ways you can deploy RAPIDS on a single instance, but the easiest is to use the RAPIDS docker image:

## Launch a VM instance

Launch an instance supported by RAPIDS. See the [introduction
section for a list of supported instance types](index).

## Configure networking

Create a Floating IP and associate that with the created instance to access the instance on the web.

## Login

Using the credentials supplied by IBM, log into the instance
via SSH. For a short guide on launching your instance and accessing it, read the
[Getting Started with IBM Virtual Server Documentation](https://cloud.ibm.com/docs/virtual-servers?topic=virtual-servers-getting-started-tutorial).

## Install pre-requisites

Install the [NVIDIA drivers](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#nvidia-drivers) and [Docker and the NVIDIA Docker
runtime](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)
in the IBM virtual server instance.

## Install RAPIDS

Install RAPIDS docker image. The docker container can be
customized by using the options provided in the **[Getting
Started](https://rapids.ai/start.html)** page of RAPIDS. Example of an image
that can be used is provided below:

```shell
$ docker pull rapidsai/rapidsai:22.10-cuda11.5-runtime-ubuntu20.04-py3.9
$ docker run --gpus all --rm -it --shm-size=1g --ulimit memlock=-1 -p 8888:8888 -p 8787:8787 -p 8786:8786 \
    rapidsai/rapidsai:22.10-cuda11.5-runtime-ubuntu20.04-py3.9
```

## Test RAPIDS

Test it! The RAPIDS docker image will start a Jupyter
notebook instance automatically. You can log into it by going to the Floating IP address
associated with the instance on port 8888.
