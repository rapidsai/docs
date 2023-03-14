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

RAPIDS has several methods for installation, depending on the preferred environment and versioning. Get started by following these four steps:
{: .fs-6 .fw-300 }

**[1. Provision System](#provision)** <br/>
**[2A. Setup Environment](#setup)** <br/>
**[2B. Setup WSL2 Environment](#WSL2)** <br/>
**[3A. Install RAPIDS](#selector)** <br/>
**[3B. Install RAPIDS (PiP)](#pip)** <br/>
**[4. Getting Started](#start)**  

<hr/>
<br/>
<div id="provision"></div>

## 1. Provision System

### **Requirements**
All provisioned systems need to be RAPIDS capable. Here's what is required:

<i class="fas fa-microchip"></i> **GPU:** NVIDIA Pascal™ or better with [compute capability](https://developer.nvidia.com/cuda-gpus){: target="_blank"} 6.0+

<i class="fas fa-desktop"></i> **OS:** One of the following OS versions:
- <i class="fas fa-check-circle"></i> Ubuntu 20.04/22.04 or CentOS 7 / Rocky Linux 8 with <code>gcc/++</code> 9.0+
- <i class="fas fa-check-circle"></i> Windows 11 using a [WSL2 specific install](#WSL2)
- <i class="fas fa-check-circle"></i> RHEL 7/8 support is provided through CentOS 7 / Rocky Linux 8 builds/installs

<i class="fas fa-download text-purple"></i> **CUDA & NVIDIA Drivers:** One of the following supported versions:
{: .no-tb-margins }

- <i class="fas fa-check-circle"></i> [CUDA 11.2](https://developer.nvidia.com/cuda-11.2.0-download-archive){: target="_blank"} with Driver 460.27.03 or newer
- <i class="fas fa-check-circle"></i> [CUDA 11.4](https://developer.nvidia.com/cuda-11-4-0-download-archive){: target="_blank"} with Driver 470.42.01 or newer
- <i class="fas fa-check-circle"></i> [CUDA 11.5](https://developer.nvidia.com/cuda-11-5-0-download-archive){: target="_blank"} with Driver 495.29.05 or newer
- <i class="fas fa-check-circle"></i> [CUDA 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive){: target="_blank"} with Driver 520.61.05 or newer
 
 **Note**: RAPIDS is tested with and officially supports the versions listed above. Newer CUDA and driver versions may also work with RAPIDS. See [CUDA compatibility](https://docs.nvidia.com/deploy/cuda-compatibility/index.html) for details.

<br/>

### **System Recommendations**
Aside from the system requirements, other considerations for best performance include:
{: .no-tb-margins }

- <i class="fas fa-check-circle"></i> SSD drive (NVMe preferred)
- <i class="fas fa-check-circle"></i> Approximately **2:1** ratio of system Memory to total GPU Memory (especially useful for Dask)
- <i class="fas fa-check-circle"></i> [NVLink](https://www.nvidia.com/en-us/data-center/nvlink/) with 2 or more GPUs

<br/>

### **Cloud Instance GPUs**
If you do not have access to GPU hardware, there are several cloud service providers (CSP) that are RAPIDS enabled. Learn how to deploy RAPIDS on AWS, Azure, GCP, and IBM cloud on our [Cloud Deployment Page](https://docs.rapids.ai/deployment/stable/cloud/index.html){: target="_blank"}.

Several services also offer **free and limited** trials with GPU resources:
- [Amazon SageMaker Studio Lab](https://studiolab.sagemaker.aws/)
- [Google CoLab w/ PiP](https://colab.research.google.com/drive/13sspqiEZwso4NYTbsflpPyNFaVAAxUgr)
- [Google CoLab w/ Conda](https://colab.research.google.com/drive/1TAAi_szMfWqRfHVfjGSqnGVLr_ztzUM9)
- [PaperSpace](https://www.paperspace.com/gpu-cloud)

<hr/>
<br/>
<div id="setup"></div>

## 2A. Setup Environment
For most installations, you will need a Conda or Docker environments installed for RAPIDS. Note, these examples are structured for installing on **Ubuntu**. Please modify appropriately for CentOS / Rocky Linux. **Windows 11** has a [WSL2 specific install](#WSL2). Jump to your preferred environment:
- [Conda](#conda) 
- [Docker](#docker)
- [PiP (Experimental)](#pip)
- [Build from Source](#source)
- [Within WSL2](#WSL2)



<br>
<div id="conda"></div>

### **Conda**
RAPIDS can use several version of conda: 
- Full installation with [Anaconda](https://www.anaconda.com/download){: target="_blank"}. 
- Minimal installation with [Miniconda](https://conda.io/miniconda.html){: target="_blank"}
- Faster environment solving installation with [Mamba](https://mamba.readthedocs.io/en/latest/installation.html){: target="_blank"}. 

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

### **Docker**
RAPIDS requires both Docker CE v19.03+ and [nvidia-container-toolkit](https://github.com/NVIDIA/nvidia-docker#quickstart){: target="_blank"} installed.
- <i class="fas fa-history text-purple"></i> Legacy Support: Docker CE v17-18 and [nvidia-docker2](https://github.com/NVIDIA/nvidia-docker/wiki/Installation-(version-2.0)){: target="_blank"}

**1. Download and Install.** Copy command below to download and install the latest Docker CE Edition:
```
curl https://get.docker.com | sh
```

**2. Install Latest NVIDIA Docker.** Select the [appropriate supported distribution](https://nvidia.github.io/nvidia-container-runtime/){: target="_blank"}:
```
curl -s -L https://nvidia.github.io/nvidia-container-runtime/gpgkey | \ sudo apt-key add - distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-container-runtime/$distribution/nvidia-container-runtime.list | \ sudo tee /etc/apt/sources.list.d/nvidia-container-runtime.list
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

**JupyterLab.** Defaults will run [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/){: target="_blank"} on your host machine at port: `8888`.

**Running Multi-Node / Multi-GPU (MNMG) Environment.** To start the container in an MNMG environment:
```
docker run -t -d --gpus all --shm-size=1g --ulimit memlock=-1 -v $PWD:/ws <container label>
```

The standard docker command may be sufficient, but the additional arguments ensures more stability.  See the [NCCL docs](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/troubleshooting.html#sharing-data){: target="_blank"} and [UCX docs](https://github.com/openucx/ucx/blob/master/docs/source/running.md#running-in-docker-containers){: target="_blank"} for more details on MNMG usage.


**Start / Stop Jupyter Lab Notebooks.** Either the standard single GPU or the modified MNMG Docker command above should auto-run a Jupyter Lab Notebook server. If it does not, or a restart is needed, run the following command within the Docker container to launch the notebook server:
```
bash /rapids/utils/start-jupyter.sh
```

If, for whatever reason, you need to shut down the Jupyter Lab server, use:
```
bash /rapids/utils/stop-jupyter.sh
```

**Custom Datasets.** See the[RAPIDS Container README](https://hub.docker.com/r/rapidsai/rapidsai){: target="_blank"} for more information about using custom datasets. [Docker Hub](https://hub.docker.com/r/rapidsai/rapidsai/){: target="_blank"} and [NVIDIA GPU Cloud](https://ngc.nvidia.com/catalog/containers/nvidia:rapidsai:rapidsai){: target="_blank"} host RAPIDS containers with a full list of [available tags](https://hub.docker.com/r/rapidsai/rapidsai#full-tag-list){: target="_blank"}.


<br/>

### **PiP (Experimental)**
The package installer for python (PiP) is currently in experimental mode, but available to try in both WSL2 or Ubuntu. See below for details.


<br/>
<div id="source"></div>

### **Build from Source**
To build from source, check each [RAPIDS GitHub](https://github.com/rapidsai){: target="_blank"} README, such as the [cuDF's](https://github.com/rapidsai/cudf#buildinstall-from-source){: target="_blank"} source environment setup and build instructions. Further links are provided in the selector tool. If additional help is needed reach out on our Slack Channel.

<hr/>
<br/>
<div id="WSL2"></div>

## 2B. **WINDOWS WSL2**
Windows users can now tap into GPU accelerated data science on their local machines using RAPIDS on [Windows Subsystem for Linux 2](https://learn.microsoft.com/en-us/windows/wsl/install){: target="_blank"}. WSL2 is a Windows feature that enables users to run native Linux command line tools directly on Windows. Using this feature does not require a dual boot environment, removing complexity and saving you time.

<br/>

### **WSL Enhanced Prerequisites**
<i class="fas fa-desktop text-white"></i> **OS:** Windows 11 with Ubuntu 22.04 instance for WSL2. <br/>
<i class="fas fa-info-circle text-white"></i> **WSL Version:** WSL12 (WSL1 not supported). <br/>
<i class="fas fa-microchip text-white"></i> **GPU:** GPUs with [Compute Capability](https://developer.nvidia.com/cuda-gpus){: target="_blank"} 7.0 or higher (16GB+ GPU RAM is recommended).

<br/>

### **Limitations**
<i class="fas fa-info-circle text-white"></i> Only single GPU is supported. <br/>
<i class="fas fa-info-circle text-white"></i> GPU Direct Storage is not supported.

<br/>

### **Troubleshooting**
<i class="fas fa-info-circle text-white"></i> When installing with conda, if an `http 000 connection error` occurs when accessing the repository data, run `wsl --shutdown` and then [restart the WSL instance](https://stackoverflow.com/questions/67923183/miniconda-on-wsl2-ubuntu-20-04-fails-with-condahttperror-http-000-connection){: target="_blank"}.

<br/>

### **WSL Conda (Preferred Method)**
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

### **WSL Docker Desktop**
1. Install WSL2 and the Ubuntu 22.04 package [using Microsoft's instructions](https://docs.microsoft.com/en-us/windows/wsl/install){: target="_blank"}.
2. Install the [latest NVIDIA Drivers](https://www.nvidia.com/download/index.aspx){: target="_blank"} on the Windows host.
3. Install latest Docker Desktop for Windows [according to your applicable licensing terms](https://docs.docker.com/desktop/install/windows-install/){: target="_blank"}.
4. Log in to the WSL2 Linux instance.
5. Generate and run the RAPIDS `docker pull` and `docker run` commands based on your desired configuration using the RAPIDS [Release Selector](#selector).
6. Inside the Docker instance, run this code to check that the RAPIDS installation is working:
	```
	import cudf
	print(cudf.Series([1, 2, 3]))
    ```
<br/>

###  **WSL and PiP**
1. Install WSL2 and the Ubuntu 22.04 package [using Microsoft's instructions](https://docs.microsoft.com/en-us/windows/wsl/install){: target="_blank"}.
2. Install the [latest NVIDIA Drivers](https://www.nvidia.com/download/index.aspx){: target="_blank"} on the Windows host.
3. Log in to the WSL2 Linux instance.
4. Follow [this helpful developer guide](https://docs.nvidia.com/cuda/wsl-user-guide/index.html#cuda-support-for-wsl2){: target="_blank"} and then [install the CUDA Toolkit without drivers](https://developer.nvidia.com/cuda-11-8-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_network){: target="_blank"} into the WSL2 instance.
5. Install RAPIDS pip packages on the WSL2 Linux Instance using the [pip instructions](#pip).
6. Run this code to check that the RAPIDS installation is working:
	```
	import cudf
	print(cudf.Series([1, 2, 3]))
	```

<hr/>
<br>
<div id="selector"></div>

## 3A. Install RAPIDS

### **RAPIDS Release Selector**
Use the selector tool below to select your preferred method, packages, and environment to install RAPIDS. Certain combinations may not be possible and are dimmed automatically. 

{% include selector.html %}

<hr/>
<br/>
<div id="pip"></div>

## 3B. Install RAPIDS with PiP (Experimental)
This is an experimental release supporting single GPU usage. cuDF, dask-cuDF, cuML, cuGraph, RMM and RAFT release 22.10 pip packages are now available. The team is excited to get these packages out into the wild and see the RAPIDS community uses them.

<br/>

### **PiP Enhanced Prerequisites**
<i class="fas fa-info-circle"></i> **Glibc version:** x86_64 wheels require glibc >= 2.17. <br/>
<i class="fas fa-info-circle"></i> **Glibc version:** ARM architecture (aarch64) wheels require glibc >= 2.31 (only ARM Server Base System Architecture is supported). <br/>
<i class="fas fa-download"></i> **CUDA >= 11.8**, with at least the **v520.61.05** driver. To use older CUDA 11.x versions, please see Troubleshooting and Known Issues. <br/>
<i class="fab fa-python"></i> **Python and pip version:** Python 3.8 or 3.10 using pip 20.3+ with [PEP600 support](https://peps.python.org/pep-0600/){: target="_blank"}.

<br/>

### **PiP Install**
The RAPIDS pip packages are hosted on NVIDIA NGC index via:
```
pip install cudf-cu11 dask-cudf-cu11 --extra-index-url=https://pypi.nvidia.com
pip install cuml-cu11 --extra-index-url=https://pypi.nvidia.com
pip install cugraph-cu11 --extra-index-url=https://pypi.nvidia.com
```

On ARM architecture (aarch64), cupy needs to be installed separately: <br/>
```
pip install cupy-cuda11x -f https://pip.cupy.dev/aarch64
```

### **Troubleshooting and Known Issues**
<i class="fas fa-info-circle"></i> Infiniband is not supported yet. <br/>
<i class="fas fa-info-circle"></i> These packages are not compatible with Tensorflow pip packages. Please use the [NGC containers](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/tensorflow){: target="_blank"} or conda packages instead. <br/>
<i class="fas fa-info-circle"></i> If you experience a “Failed to import CuPy” error, please uninstall any existing versions of cupy and install cupy-cuda11x. For example:
```
pip uninstall cupy-cuda115; pip install cupy-cuda11x
```

<i class="fas fa-info-circle"></i> The following error message indicates a problem with your environment: 
```
ERROR: Could not find a version that satisfies the requirement cudf-cu11 (from versions: 0.0.1, 22.10.0)
ERROR: No matching distribution found for cudf-cu11
```
Check the suggestions below for possible resolutions:
- Your Python version must be 3.8 or 3.10.
- RAPIDS pip packages require a recent version of pip that [supports PEP600](https://peps.python.org/pep-0600/){: target="_blank"}. Some users may need to update pip: `pip install -U pip` <br/>

<i class="fas fa-info-circle"></i> Dask / Jupyter / Tornado 6.2 dependency conflicts can occur. Install jupyter-client 7.3.4 if the error below occurs: <br/>
```
    ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behavior is the source of the following dependency conflicts.
    jupyter-client 7.4.2 requires tornado>=6.2, but you have tornado 6.1 which is incompatible.
```

<hr/>
<br/>
<div id="start"></div>

## Getting Started
After installing the RAPIDS libraries, the best place to get started is our [User Guide](/user-guide). Our [RAPIDS.ai](https://rapids.ai/){: target="_blank"} home page also provides a great deal of information, as does our [Blog Page](https://medium.com/rapids-ai){: target="_blank"} and the [NVIDIA Developer Blog](https://developer.nvidia.com/blog/?search_posts_filter=rapids){: target="_blank"}. We are also always available on our [RAPIDS GoAi Slack Channel]({{ site.social.slack.url }}).

<br/><br/>
