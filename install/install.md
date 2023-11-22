---
layout: default
title: Installation Guide
nav_order: 2
permalink: install
description: |
  Guide to installing RAPIDS
---

# RAPIDS Installation Guide
{: .fs-8 }

RAPIDS has several methods for installation, depending on the preferred environment and version.
*New Users* should review the system and environment prerequisites.

**[Install RAPIDS with Release Selector](#selector)** <br/>
- [Installation Troubleshooting](#troubleshooting)

**[System Requirements](#system-req)** <br/>
- [OS, NVIDIA GPU Driver, and CUDA Versions](#system-req)
- [System Recommendations](#system-recommendations)
- [Cloud Instance GPUs](#cloud-gpu)

**[Environment Setup](#environment)** <br/>
- [Conda](#conda)
- [Docker](#docker)
- [pip](#pip)
- [Within WSL2](#wsl2)
	- [Conda](#wsl2-conda)
	- [Docker](#wsl2-docker)
	- [pip](#wsl2-pip)
- [Build From Source](#source)

**[Next Steps](#next-steps)**

<hr/>
<div id="selector"></div>

# Install RAPIDS
Use the selector tool below to select your preferred method, packages, and environment to install RAPIDS. Certain combinations may not be possible and are dimmed automatically.

{% include selector.html %}

<br/>
<div id="troubleshooting"></div>

## Installation Troubleshooting

### **Conda Issues**
<i class="fas fa-info-circle"></i> A `conda create error` occurs:<br/>
RAPIDS has switched the default solver recommendation to [libmamba](https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community/){: target="_blank"}, a Mamba-powered Conda solver that is [now included with all Conda/Miniconda installations](https://www.anaconda.com/blog/new-release-anaconda-distribution-2023-07-miniconda-23-5-0-and-more){: target="_blank"} to significantly accelerate environment solving. The error output shows:
```
conda create: error: argument --solver: invalid choice: 'libmamba' (choose from 'classic')
```

To resolve this error please follow one of these steps:
- If the Conda installation is version `22.11` or newer, run: `conda install -n base conda-libmamba-solver`
- If the Conda installation is older than `22.11`, please update your [Conda or Miniconda to the latest version](https://conda.io/projects/conda/en/stable/user-guide/install/index.html){: target="_blank"}
- Use [Mamba directly](https://mamba.readthedocs.io/en/latest/installation.html){: target="_blank"}
- Use the classic solver by removing `--solver=libmamba` from the `conda create` command provided by the selector

<i class="fas fa-info-circle"></i> CUDA 12.0 ARM packages are not yet available:<br/>
Nightly packages are now available for CUDA 12.0 on ARM! Stable support is coming in 23.12

### **Docker Issues**
<i class="fas fa-exclamation-triangle"></i> RAPIDS `23.08` brings significant Docker changes. <br/>
To learn more about these changes, please see the [RAPIDS Container README](https://hub.docker.com/r/rapidsai/base){: target="_blank"}. Some key notes below:
- `Development` images are no longer being published, in the coming releases RAPIDS will roll out [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers){: target="_blank"} for development
   - See cuSpatial for an example and information on [RAPIDS' usage of Dev Containers](https://github.com/rapidsai/cuspatial/tree/main/.devcontainer){: target="_blank"}
- All images are Ubuntu-based
   - CUDA 11.2 images are Ubuntu `20.04`
   - All other images are Ubuntu `22.04`
- All images are multiarch (x86_64 and ARM)
   - CUDA 12 support is available on the nightly versions when using Docker images on ARM architecture
- The `Base` image starts in an ipython shell
   - To run bash commands inside the ipython shell prefix the command with `!`
   - To run the image without the ipython shell add `/bin/bash` to the end of the `docker run` command
- For a full list of changes please see this [RAPIDS Docker Issue](https://github.com/rapidsai/docker/issues/539){: target="_blank"}


### **pip Issues**
<i class="fas fa-info-circle"></i> pip installations require using the matching wheel to the system's installed CUDA toolkit. For CUDA 11 toolkits, install the `-cu11` wheels, and for CUDA 12 tookits install the `-cu12` wheels. If your installation has a CUDA 12 driver but a CUDA 11 toolkit, use the `-cu11` wheels. <br/>
<i class="fas fa-info-circle"></i> Infiniband is not supported yet. <br/>
<i class="fas fa-info-circle"></i> These packages are not compatible with Tensorflow pip packages. Please use the [NGC containers](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/tensorflow){: target="_blank"} or conda packages instead. <br/>
<i class="fas fa-info-circle"></i> If you experience a "Failed to import CuPy" error, please uninstall any existing versions of cupy and install `cupy-cuda11x`. For example:
```
pip uninstall cupy-cuda115; pip install cupy-cuda11x
```
<br/>

<i class="fas fa-info-circle"></i> The following error message indicates a problem with your environment:
```
ERROR: Could not find a version that satisfies the requirement cudf-cu11 (from versions: 0.0.1, {{ site.data.releases.stable.version }})
ERROR: No matching distribution found for cudf-cu11
```
Check the suggestions below for possible resolutions:
- The pip index has moved from the initial experimental release! Ensure the correct `--extra-index-url=https://pypi.nvidia.com`
- Only Python versions 3.9 and 3.10 are supported
- RAPIDS pip packages require a recent version of pip that [supports PEP600](https://peps.python.org/pep-0600/){: target="_blank"}. Some users may need to update pip: `pip install -U pip`

<br/>

<i class="fas fa-info-circle"></i> Dask / Jupyter / Tornado 6.2 dependency conflicts can occur. Install `jupyter-client` 7.3.4 if the error below occurs: <br/>
```
    ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behavior is the source of the following dependency conflicts.
    jupyter-client 7.4.2 requires tornado>=6.2, but you have tornado 6.1 which is incompatible.
```

<i class="fas fa-info-circle"></i> cuSpatial installation may yield the error below:<br/>
```
    ERROR: GDAL >= 3.2 is required for fiona. Please upgrade GDAL.
```
To resolve, either <code>GDAL</code> needs to be updated, or <code>fiona</code> needs to be pinned to specific versions depending on the installation OS. please see the [cuSpatial README](https://github.com/rapidsai/cuspatial/tree/branch-23.06#install-with-pip){: target="_blank"} to resolve this error.

<br/>

### **WSL2 Issues**
See the WSL2 setup [troubleshooting section](#wsl2-troubleshooting).


<hr/>
<div id="system-req"></div>

# System Requirements
## **OS / GPU Driver / CUDA Versions**
All provisioned systems need to be RAPIDS capable. Here's what is required:

<i class="fas fa-microchip"></i> **GPU:** NVIDIA Pascal™ or better with [compute capability](https://developer.nvidia.com/cuda-gpus){: target="_blank"} 6.0+

<i class="fas fa-desktop"></i> **OS:** One of the following OS versions:
- <i class="fas fa-check-circle"></i> Ubuntu 20.04/22.04 or CentOS 7 / Rocky Linux 8 with <code>gcc/++</code> 9.0+
- <i class="fas fa-check-circle"></i> Windows 11 using a [WSL2 specific install](#wsl2)
- <i class="fas fa-check-circle"></i> RHEL 7/8 support is provided through CentOS 7 / Rocky Linux 8 builds/installs

<i class="fas fa-download text-purple"></i> **CUDA & NVIDIA Drivers:** One of the following supported versions:
{: .no-tb-margins }

- <i class="fas fa-check-circle"></i> [CUDA 11.2](https://developer.nvidia.com/cuda-11.2.0-download-archive){: target="_blank"} with Driver 470.42.01 or newer
- <i class="fas fa-check-circle"></i> [CUDA 11.4](https://developer.nvidia.com/cuda-11-4-0-download-archive){: target="_blank"} with Driver 470.42.01 or newer
- <i class="fas fa-check-circle"></i> [CUDA 11.5](https://developer.nvidia.com/cuda-11-5-0-download-archive){: target="_blank"} with Driver 495.29.05 or newer
- <i class="fas fa-check-circle"></i> [CUDA 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive){: target="_blank"} with Driver 520.61.05 or newer
- <i class="fas fa-check-circle"></i> [CUDA 12.0](https://developer.nvidia.com/cuda-12-0-1-download-archive){: target="_blank"} with Driver 525.60.13 or newer **see CUDA 12 section below for notes on usage**

 **Note**: RAPIDS is tested with and officially supports the versions listed above. Newer CUDA and driver versions may also work with RAPIDS. See [CUDA compatibility](https://docs.nvidia.com/deploy/cuda-compatibility/index.html) for details. 

## **CUDA 12 Support**

### **Docker and Conda**

- <i class="fas fa-info-circle"></i> CUDA 12 conda packages and Docker images currently support CUDA 12.0
- <i class="fas fa-info-circle"></i> CUDA 11 conda packages and Docker images can be used on a system with a CUDA 12 driver because they include their own CUDA toolkit
- <i class="fas fa-info-circle"></i> ARM is currently supported by nightly CUDA 12 conda packages or Docker images, use CUDA 11 or pip packages for stable version ARM support
 
### **pip**

- <i class="fas fa-info-circle"></i> pip installations require using a wheel matching the system's installed CUDA toolkit. 
- <i class="fas fa-info-circle"></i> For CUDA 11 toolkits, install the <code>-cu11</code> wheels, and for CUDA 12 toolkits install the <code>-cu12</code> wheels. If your installation has a CUDA 12 driver but a CUDA 11 toolkit, use the <code>-cu11</code> wheels.

<br/>
<div id="system-recommendations"></div>

## **System Recommendations**
Aside from the system requirements, other considerations for best performance include:
{: .no-tb-margins }

- <i class="fas fa-check-circle"></i> SSD drive (NVMe preferred)
- <i class="fas fa-check-circle"></i> Approximately **2:1** ratio of system Memory to total GPU Memory (especially useful for Dask)
- <i class="fas fa-check-circle"></i> [NVLink](https://www.nvidia.com/en-us/data-center/nvlink/) with 2 or more GPUs

<br/>
<div id="cloud-gpu"></div>

## **Cloud Instance GPUs**
If you do not have access to GPU hardware, there are several cloud service providers (CSP) that are RAPIDS enabled. Learn how to deploy RAPIDS on AWS, Azure, GCP, and IBM cloud on our [Cloud Deployment Page](https://docs.rapids.ai/deployment/stable/cloud/index.html){: target="_blank"}.

Several services also offer **free and limited** trials with GPU resources:
- [Amazon SageMaker Studio Lab](https://studiolab.sagemaker.aws/)
- [Google CoLab w/ pip](https://colab.research.google.com/drive/13sspqiEZwso4NYTbsflpPyNFaVAAxUgr)
- [Google CoLab w/ Conda](https://colab.research.google.com/drive/1TAAi_szMfWqRfHVfjGSqnGVLr_ztzUM9)
- [PaperSpace](https://www.paperspace.com/gpu-cloud)

<hr/>
<div id="environment"></div>

# Environment Setup
For most installations, you will need a Conda or Docker environments installed for RAPIDS. Note, these examples are structured for installing on **Ubuntu**. Please modify appropriately for CentOS / Rocky Linux. **Windows 11** has a [WSL2 specific install](#wsl2).

<br>
<div id="conda"></div>

## **Conda**
RAPIDS can use several versions of conda:
- Full installation with [Anaconda](https://www.anaconda.com/download){: target="_blank"} (with optional faster [libmamba solver](https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community/){: target="_blank"}).
- Minimal installation with [Miniconda](https://conda.io/miniconda.html){: target="_blank"}
- Faster environment solving installation with standalone [Mamba](https://mamba.readthedocs.io/en/latest/installation.html){: target="_blank"}.

Below is a quick installation guide using miniconda.

**1. Download and Run Install Script**. Copy the command below to download and run the miniconda install script:
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

**2. Customize Conda and Run the Install.** Use the terminal window to finish installation. Note, we recommend enabling `conda-init`.

**3. Start Conda.** Open a new terminal window, which should now show Conda initialized.


<br/>
<div id="docker"></div>

## **Docker**
RAPIDS requires both Docker CE v19.03+ and [nvidia-container-toolkit](https://github.com/NVIDIA/nvidia-docker#quickstart){: target="_blank"} installed.
- <i class="fas fa-history text-purple"></i> Legacy Support: Docker CE v17-18 and [nvidia-docker2](https://github.com/NVIDIA/nvidia-docker/wiki/Installation-(version-2.0)){: target="_blank"}

**1. Download and Install.** Copy command below to download and install the latest Docker CE Edition:
```
curl https://get.docker.com | sh
```

**2. Install Latest NVIDIA Docker.** Select the [appropriate supported distribution](https://nvidia.github.io/nvidia-container-runtime/){: target="_blank"}:
```
curl -s -L https://nvidia.github.io/nvidia-container-runtime/gpgkey | sudo apt-key add - distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-container-runtime/$distribution/nvidia-container-runtime.list | sudo tee /etc/apt/sources.list.d/nvidia-container-runtime.list
sudo apt-get update
sudo apt-get install nvidia-container-runtime
```

**3. Start Docker.** In new terminal window run:
```
sudo service docker stop
sudo service docker start
```

**4a. Test NVIDIA Docker.** In a terminal window run:
```
docker run --gpus all nvcr.io/nvidia/k8s/cuda-sample:nbody nbody -gpu -benchmark
```

**4b. Legacy Docker Users.** Docker CE v18 & [nvidia-docker2](https://github.com/NVIDIA/nvidia-docker/wiki/Installation-(version-2.0)){: target="_blank"} users will need to replace the following for compatibility:
`docker run --gpus all` with `docker run --runtime=nvidia`

<br/>

### **JupyterLab.** 
The command provided from the selector for the `notebooks` Docker image will run [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/){: target="_blank"} on your host machine at port: `8888`.

**Running Multi-Node / Multi-GPU (MNMG) Environment.** To start the container in an MNMG environment:
```
docker run -t -d --gpus all --shm-size=1g --ulimit memlock=-1 --ulimit stack= 67108864 -v $PWD:/ws <container label>
```

The standard docker command may be sufficient, but the additional arguments ensures more stability.  See the [NCCL docs](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/troubleshooting.html#sharing-data){: target="_blank"} and [UCX docs](https://github.com/openucx/ucx/blob/master/docs/source/running.md#running-in-docker-containers){: target="_blank"} for more details on MNMG usage.


**Custom Datasets.** See the [RAPIDS Container README](https://hub.docker.com/r/rapidsai/rapidsai){: target="_blank"} for more information about using custom datasets. [Docker Hub](https://hub.docker.com/r/rapidsai/rapidsai/){: target="_blank"} and [NVIDIA GPU Cloud](https://ngc.nvidia.com/catalog/containers/nvidia:rapidsai:rapidsai){: target="_blank"} host RAPIDS containers with a full list of [available tags](https://hub.docker.com/r/rapidsai/rapidsai/tags){: target="_blank"}.


<br/>
<div id="pip"></div>

## **pip**
RAPIDS pip packages are available for CUDA 11 and CUDA 12 on the NVIDIA Python Package Index.

### **pip Additional Prerequisites**
<i class="fas fa-info-circle"></i> The CUDA toolkit version on your system must match the pip CUDA version you install (`-cu11` or `-cu12`). <br/>
<i class="fas fa-info-circle"></i> **glibc version:** x86_64 wheels require glibc >= 2.17. <br/>
<i class="fas fa-info-circle"></i> **glibc version:** ARM architecture (aarch64) wheels require glibc >= 2.32 (only ARM Server Base System Architecture is supported).


<br/>
<div id="wsl2"></div>

## **Windows WSL2**
Windows users can now tap into GPU accelerated data science on their local machines using RAPIDS on [Windows Subsystem for Linux 2](https://learn.microsoft.com/en-us/windows/wsl/install){: target="_blank"}. WSL2 is a Windows feature that enables users to run native Linux command line tools directly on Windows. Using this feature does not require a dual boot environment, removing complexity and saving you time.

### **WSL2 Additional Prerequisites**

<i class="fas fa-desktop text-white"></i> **OS:** Windows 11 with Ubuntu 22.04 instance for WSL2. <br/>
<i class="fas fa-info-circle text-white"></i> **WSL Version:** WSL2 (WSL1 not supported). <br/>
<i class="fas fa-microchip text-white"></i> **GPU:** GPUs with [Compute Capability](https://developer.nvidia.com/cuda-gpus){: target="_blank"} 7.0 or higher (16GB+ GPU RAM is recommended).


### **Limitations**

<i class="fas fa-info-circle text-white"></i> Only single GPU is supported. <br/>
<i class="fas fa-info-circle text-white"></i> GPU Direct Storage is not supported.


<div id="wsl2-troubleshooting"></div>

### **Troubleshooting**

<i class="fas fa-info-circle text-white"></i> When installing with Conda, if an `http 000 connection error` occurs when accessing the repository data, run `wsl --shutdown` and then [restart the WSL instance](https://stackoverflow.com/questions/67923183/miniconda-on-wsl2-ubuntu-20-04-fails-with-condahttperror-http-000-connection){: target="_blank"}.

<i class="fas fa-info-circle text-white"></i> When installing with Conda or pip, if an `WSL2 Jitify fatal error: libcuda.so: cannot open shared object file` error occurs, follow suggestions in [this WSL issue](https://github.com/microsoft/WSL/issues/8587) to resolve.

<i class="fas fa-info-circle text-white"></i> When installing with Docker Desktop, if the container pull command is successful, but the run command hangs indefinitely, [ensure you're on Docker Desktop >= 4.18](https://docs.docker.com/desktop/release-notes/){: target="_blank"}.

<br/>
<div id="wsl2-conda"></div>

### **WSL2 Conda Install (Preferred Method)**

1. Install WSL2 and the Ubuntu 22.04 package [using Microsoft's instructions](https://docs.microsoft.com/en-us/windows/wsl/install){: target="_blank"}.
2. Install the [latest NVIDIA Drivers](https://www.nvidia.com/download/index.aspx){: target="_blank"} on the Windows host.
3. Log in to the WSL2 Linux instance.
4. Install Conda in the WSL2 Linux Instance using our [Conda instructions](#conda).
5. Install RAPIDS via Conda, using the RAPIDS [Release Selector](#selector).
6. Run this code to check that the RAPIDS installation is working:
	```
	import cudf
	print(cudf.Series([1, 2, 3]))
	```

<br/>
<div id="wsl2-docker"></div>

### **WSL2 Docker Desktop Install**

1. Install WSL2 and the Ubuntu 22.04 package [using Microsoft's instructions](https://docs.microsoft.com/en-us/windows/wsl/install){: target="_blank"}.
2. Install the [latest NVIDIA Drivers](https://www.nvidia.com/download/index.aspx){: target="_blank"} on the Windows host.
3. Install latest Docker Desktop for Windows
4. Log in to the WSL2 Linux instance.
5. Generate and run the RAPIDS `docker` command based on your desired configuration using the RAPIDS [Release Selector](#selector).
6. Inside the Docker instance, run this code to check that the RAPIDS installation is working:
	```
	import cudf
	print(cudf.Series([1, 2, 3]))
    ```

<br/>
<div id="wsl2-pip"></div>

### **WSL2 pip Install**

1. Install WSL2 and the Ubuntu 22.04 package [using Microsoft's instructions](https://docs.microsoft.com/en-us/windows/wsl/install){: target="_blank"}.
2. Install the [latest NVIDIA Drivers](https://www.nvidia.com/download/index.aspx){: target="_blank"} on the Windows host.
3. Log in to the WSL2 Linux instance.
4. Follow [this helpful developer guide](https://docs.nvidia.com/cuda/wsl-user-guide/index.html#cuda-support-for-wsl2){: target="_blank"} and then install the WSL-specific [CUDA 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local){: target="_blank"} or [CUDA 12.0](https://developer.nvidia.com/cuda-12-0-1-download-archive?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local){: target="_blank"} Toolkit without drivers into the WSL2 instance.
	- The installed CUDA Toolkit version must match the pip wheel version (`-cu11` or `-cu12`)
5. Install RAPIDS pip packages on the WSL2 Linux Instance using the [release selector](#selector) commands.
6. Run this code to check that the RAPIDS installation is working:
	```
	import cudf
	print(cudf.Series([1, 2, 3]))
	```
<br/>

<div id="source"></div>

## **Build from Source**
To build from source, check each [RAPIDS GitHub](https://github.com/rapidsai){: target="_blank"} README, such as the [cuDF's](https://github.com/rapidsai/cudf#buildinstall-from-source){: target="_blank"} source environment set up and build instructions. Further links are provided in the [selector tool](#selector). If additional help is needed reach out on our [Slack Channel]({{ site.social.slack.url }}).


<hr/>
<div id="next-steps"></div>

# Next Steps
After installing the RAPIDS libraries, the best place to get started is our [User Guide](/user-guide). Our [RAPIDS.ai](https://rapids.ai/){: target="_blank"} home page also provides a great deal of information, as does our [Blog Page](https://medium.com/rapids-ai){: target="_blank"} and the [NVIDIA Developer Blog](https://developer.nvidia.com/blog/?search_posts_filter=rapids){: target="_blank"}. We are also always available on our [RAPIDS GoAi Slack Channel]({{ site.social.slack.url }}).

<br/><br/>
