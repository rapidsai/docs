# Single Node

There are multiple ways you can deploy RAPIDS on a single instance, but the easiest is to use the RAPIDS docker image:

**1. Initiate.** Initiate an instance supported by RAPIDS. See the introduction
section for a list of supported instance types. It is recommended to use an AMI
that already includes the required NVIDIA drivers, such as the **[AWS Deep Learning
AMI.](https://docs.aws.amazon.com/dlami/latest/devguide/what-is-dlami.html)**

**2. Credentials.** Using the credentials supplied by AWS, log into the instance
via SSH. For a short guide on launching your instance and accessing it, read the
Getting Started with Amazon EC2 documentation.

**3. Install.** Install [Docker and the NVIDIA Docker
runtime](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)
in the AWS instance. This step is not required if you are using AWS Deep
Learning AMI.

**4. Install.** Install RAPIDS docker image. The docker container can be
customized by using the options provided in the **[Getting
Started](https://rapids.ai/start.html)** page of RAPIDS. Example of an image
that can be used is provided below:

```shell
$ docker pull rapidsai/rapidsai:22.10-cuda11.5-runtime-ubuntu18.04-py3.9
$ docker run --gpus all --rm -it -p 8888:8888 -p 8787:8787 -p 8786:8786 \
         rapidsai/rapidsai:22.10-cuda11.5-runtime-ubuntu18.04-py3.9
```

**5. Test RAPIDS.** Test it! The RAPIDS docker image will start a Jupyter
notebook instance automatically. You can log into it by going to the IP address
provided by AWS on port 8888.
