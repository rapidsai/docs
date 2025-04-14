---
layout: default
title: Installation Guide
nav_order: 2
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
- [SDK Manager](#sdkm)
- [Windows WSL2](#wsl2)
  - [SDK Manager](#wsl2-sdkm)
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
To resolve this error please follow one of these steps:
- If the Conda installation is older than `22.11`, please update to the latest version. This will include [libmamba](https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community/){: target="_blank"}, a Mamba-powered Conda solver that is now included with all conda installations to significantly accelerate environment solving.
- If the Conda installation is version `22.11` or newer, run: `conda install -n base conda-libmamba-solver` and run
`conda create --solver=libmamba ...`
- Use [Mamba directly](https://mamba.readthedocs.io/en/latest/installation.html){: target="_blank"} as `mamba create ...`

<i class="fas fa-info-circle"></i> A `__cuda` constraint conflict occurs:<br/>
You may see something like:
```
LibMambaUnsatisfiableError: Encountered problems while solving:
 - package cuda-version-12.0-hffde075_0 has constraint __cuda >=12 conflicting with __cuda-11.4-0
```
This means the CUDA driver currently installed on your machine (e.g. `__cuda`: 11.4.0) is
incompatible with the `cuda-version` (12.0) you are trying to install. You will have to ensure the [CUDA
driver on your machine supports the CUDA version](#system-req) you are trying to install with conda.

If conda has incorrectly identified the CUDA driver, you can [override by setting the `CONDA_OVERRIDE_CUDA`](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-virtual.html#overriding-detected-packages){: target="_blank"} environment variable.

### **Docker Issues**
<i class="fas fa-exclamation-triangle"></i> RAPIDS `23.08` brought significant Docker changes. <br/>
To learn more about these changes, please see the [RAPIDS Container README](https://hub.docker.com/r/rapidsai/base){: target="_blank"}. Some key notes below:
- `Development` images are no longer being published, RAPIDS now uses [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers){: target="_blank"} for development
  - See cuSpatial for an example and information on [RAPIDS' usage of Dev Containers](https://github.com/rapidsai/cuspatial/tree/main/.devcontainer){: target="_blank"}
- All images are Ubuntu-based
  - CUDA 12.5+ images use Ubuntu 24.04
  - All other images use Ubuntu 22.04
- All images are multiarch (x86_64 and ARM)
- The `base` image starts in an ipython shell
  - To run bash commands inside the ipython shell prefix the command with `!`
  - To run the image without the ipython shell add `/bin/bash` to the end of the `docker run` command
- For a full list of changes please see this [RAPIDS Docker Issue](https://github.com/rapidsai/docker/issues/539){: target="_blank"}


### **pip Issues**
<i class="fas fa-info-circle"></i> pip installations require using the matching wheel to the system's installed CUDA toolkit. For CUDA 11 toolkits, install the `-cu11` wheels, and for CUDA 12 toolkits install the `-cu12` wheels. If your installation has a CUDA 12 driver but a CUDA 11 toolkit, use the `-cu11` wheels. <br/>
<i class="fas fa-info-circle"></i> Infiniband is not supported yet. <br/>
<i class="fas fa-info-circle"></i> These packages are not compatible with Tensorflow pip packages. Please use the [NGC containers](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/tensorflow){: target="_blank"} or conda packages instead. <br/>
<i class="fas fa-info-circle"></i> If you experience a "Failed to import CuPy" error, please uninstall any existing versions of cupy and install `cupy-cuda11x`. For example:
```sh
pip uninstall cupy-cuda115; pip install cupy-cuda11x
```
<br/>

<i class="fas fa-info-circle"></i> The following error message indicates a problem with your environment:
```
ERROR: Could not find a version that satisfies the requirement cudf-cu12 (from versions: 0.0.1, {{ site.data.releases.stable.version }})
ERROR: No matching distribution found for cudf-cu12
```
Check the suggestions below for possible resolutions:

- The pip index has moved from the initial experimental release! Ensure the correct `--extra-index-url=https://pypi.nvidia.com`
- Ensure you're using a Python version that RAPIDS supports (compare the values in the [the install selector](#selector) to the Python version reported by `python --version`).
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

<i class="fas fa-microchip"></i> **GPU:** NVIDIA Volta™ or higher with [compute capability](https://developer.nvidia.com/cuda-gpus){: target="_blank"} 7.0+
- <i class="fas fa-exclamation-triangle"></i> Pascal™ GPU support was [removed in 24.02](https://docs.rapids.ai/notices/rsn0034/). Compute capability 7.0+ is required for RAPIDS 24.02 and later.

<i class="fas fa-desktop"></i> **OS:**
- <i class="fas fa-check-circle"></i> Linux distributions with `glibc>=2.28` (released in August 2018), which include the following:
  - [Arch Linux](https://archlinux.org/), minimum version 2018-08-02
  - [Debian](https://www.debian.org/), minimum version 10.0
  - [Fedora](https://fedoraproject.org/), minimum version 29
  - [Linux Mint](https://linuxmint.com/), minimum version 20
  - [Rocky Linux](https://rockylinux.org/) / [Alma Linux](https://almalinux.org/) / [RHEL](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux), minimum version 8
  - [Ubuntu](https://ubuntu.com/), minimum version 20.04
- <i class="fas fa-check-circle"></i> Windows 11 using a [WSL2 specific install](#wsl2)

<i class="fas fa-download text-purple"></i> **CUDA & NVIDIA Drivers:** One of the following supported versions:
{: .no-tb-margins }

- <i class="fas fa-check-circle"></i> [CUDA 11.2](https://developer.nvidia.com/cuda-11.2.0-download-archive){: target="_blank"} with Driver 470.42.01 or newer
- <i class="fas fa-check-circle"></i> [CUDA 11.4](https://developer.nvidia.com/cuda-11-4-0-download-archive){: target="_blank"} with Driver 470.42.01 or newer
- <i class="fas fa-check-circle"></i> [CUDA 11.5](https://developer.nvidia.com/cuda-11-5-0-download-archive){: target="_blank"} with Driver 495.29.05 or newer
- <i class="fas fa-check-circle"></i> [CUDA 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive){: target="_blank"} with Driver 520.61.05 or newer
- <i class="fas fa-check-circle"></i> [CUDA 12.0](https://developer.nvidia.com/cuda-12-0-1-download-archive){: target="_blank"} with Driver 525.60.13 or newer **see CUDA 12 section below for notes on usage**
- <i class="fas fa-check-circle"></i> [CUDA 12.2](https://developer.nvidia.com/cuda-12-2-2-download-archive){: target="_blank"} with Driver 535.86.10 or newer **see CUDA 12 section below for notes on usage**
- <i class="fas fa-check-circle"></i> [CUDA 12.5](https://developer.nvidia.com/cuda-12-5-1-download-archive){: target="_blank"} with Driver 555.42.06 or newer **see CUDA 12 section below for notes on usage**

 **Note**: RAPIDS is tested with and officially supports the versions listed above. Newer CUDA and driver versions may also work with RAPIDS. See [CUDA compatibility](https://docs.nvidia.com/deploy/cuda-compatibility/index.html) for details.

## **CUDA Support**

### **Docker and Conda**

- <i class="fas fa-info-circle"></i> conda packages and Docker images support CUDA 12 on systems with a CUDA 12 driver.
- <i class="fas fa-info-circle"></i> CUDA 11 conda packages and Docker images can be used on a system with a CUDA 12 driver because they include their own CUDA toolkit.

### **pip**

- <i class="fas fa-info-circle"></i> pip installations require using a wheel matching the system's installed CUDA toolkit.
- <i class="fas fa-info-circle"></i> RAPIDS pip packages require NVRTC for Numba to function properly. For Docker users, this means that RAPIDS wheels require the `devel` flavor of `nvidia/cuda` images for full functionality. The `base` and `runtime` flavors of `nvidia/cuda` Docker images are currently not sufficient.
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
- [Google Colab w/ pip](https://nvda.ws/3XEO6hK)
- [PaperSpace](https://www.paperspace.com/gpu-cloud)

<hr/>
<div id="environment"></div>

# Environment Setup
For most installations, you will need a Conda or Docker environments installed for RAPIDS. Note, these examples are structured for installing on **Ubuntu**. Please modify appropriately for Rocky Linux. **Windows 11** has a [WSL2 specific install](#wsl2).

<br>
<div id="conda"></div>

## **Conda**
RAPIDS can be used with any conda distribution.

Below is an installation guide using miniforge.

**1. Download and Run Install Script**. Copy the command below to download and run the miniforge install script:
```sh
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
```

**2. Customize Conda and Run the Install.** Use the terminal window to finish installation. Note, we recommend enabling `conda-init`.

**3. Start Conda.** Open a new terminal window, which should now show Conda initialized.

**4. Check Conda Configuration.** Installing RAPIDS may require you to use `channel_priority: flexible`.

If you are installing RAPIDS with CUDA 12 or greater, then you can use either `strict` or `flexible` channel priority.

If you are install RAPIDS with CUDA 11, then you must set `channel_priority: flexible`.

You can check this and change it, if required, by doing:
```sh
conda config --show channel_priority
conda config --set channel_priority flexible
```

<br/>
<div id="docker"></div>

## **Docker**
RAPIDS requires both Docker CE v19.03+ and [nvidia-container-toolkit](https://github.com/NVIDIA/nvidia-docker#quickstart){: target="_blank"} installed.
- <i class="fas fa-history text-purple"></i> Legacy Support: Docker CE v17-18 and [nvidia-docker2](https://github.com/NVIDIA/nvidia-docker/wiki/Installation-(version-2.0)){: target="_blank"}

**1. Download and Install.** Copy command below to download and install the latest Docker CE Edition:
```sh
curl https://get.docker.com | sh
```

**2. Install Latest NVIDIA Docker.** Select the [appropriate supported distribution](https://nvidia.github.io/nvidia-container-runtime/){: target="_blank"}:
```sh
curl -s -L https://nvidia.github.io/nvidia-container-runtime/gpgkey | sudo apt-key add - distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-container-runtime/$distribution/nvidia-container-runtime.list | sudo tee /etc/apt/sources.list.d/nvidia-container-runtime.list
sudo apt-get update
sudo apt-get install nvidia-container-runtime
```

**3. Start Docker.** In new terminal window run:
```sh
sudo service docker stop
sudo service docker start
```

**4a. Test NVIDIA Docker.** In a terminal window run:
```sh
docker run --gpus all nvcr.io/nvidia/k8s/cuda-sample:nbody nbody -gpu -benchmark
```

**4b. Legacy Docker Users.** Docker CE v18 & [nvidia-docker2](https://github.com/NVIDIA/nvidia-docker/wiki/Installation-(version-2.0)){: target="_blank"} users will need to replace the following for compatibility:
`docker run --gpus all` with `docker run --runtime=nvidia`

<br/>

### **JupyterLab.**
The command provided from the selector for the `notebooks` Docker image will run [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/){: target="_blank"} on your host machine at port: `8888`.

**Running Multi-Node / Multi-GPU (MNMG) Environment.** To start the container in an MNMG environment:
```sh
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
<div id="sdkm"></div>

## **SDK Manager (Ubuntu Only)**
[NVIDIA SDK Manager](https://developer.nvidia.com/sdk-manager) gives a users a Graphical User Interface (GUI) option to install RAPIDS.  It also attempts to fix any environment issues before installing RAPIDS or updating RAPIDS, making it ideal for new Linux users.
1. Download [SDK Manager's Ubuntu version from their website](https://developer.nvidia.com/sdk-manager){: target="_blank"} (requires sign up or login to NVIDIA's Developer community).  Do not install yet.  It is assumed that your home directory's `Downloads` folder is where the `.deb` file will be stored.  If not, please move `sdkmanager_[version]-[build#]_amd64.deb` file to your current Download folder.
2. Install and run SDK Manager [using the installation guide here](https://docs.nvidia.com/sdk-manager/download-run-sdkm/index.html){: target="_blank"}. For Ubuntu, use the following commands:
```bash
sudo apt install ./sdkmanager_[version]-[build#]_amd64.deb
sdkmanager
```
3. Sign in when asked, and follow SDK Manager's [RAPIDS installation instructions](https://docs.nvidia.com/sdk-manager/install-with-sdkm-rapids/index.html){: target="_blank"}.


<br/>
<div id="wsl2"></div>

## **Windows WSL2**
Windows users can now tap into GPU accelerated data science on their local machines using RAPIDS on [Windows Subsystem for Linux 2](https://learn.microsoft.com/en-us/windows/wsl/install){: target="_blank"}. WSL2 is a Windows feature that enables users to run native Linux command line tools directly on Windows. Using this feature does not require a dual boot environment, removing complexity and saving you time.

### **WSL2 Additional Prerequisites**

<i class="fas fa-desktop text-white"></i> **OS:** Windows 11 with a WSL2 installation of Ubuntu (minimum version 20.04). <br/>
<i class="fas fa-info-circle text-white"></i> **WSL Version:** WSL2 (WSL1 not supported). <br/>
<i class="fas fa-microchip text-white"></i> **GPU:** GPUs with [Compute Capability](https://developer.nvidia.com/cuda-gpus){: target="_blank"} 7.0 or higher (16GB+ GPU RAM is recommended).


### **Limitations**

<i class="fas fa-info-circle text-white"></i> Only single GPU is supported. <br/>
<i class="fas fa-info-circle text-white"></i> GPU Direct Storage is not supported.


<div id="wsl2-troubleshooting"></div>

### **Troubleshooting**

<i class="fas fa-info-circle text-white"></i> When installing with Conda, if an `http 000 connection error` occurs when accessing the repository data, run `wsl --shutdown` and then [restart the WSL instance](https://stackoverflow.com/a/69601760){: target="_blank"}.

<i class="fas fa-info-circle text-white"></i> When installing with Conda or pip, if an `WSL2 Jitify fatal error: libcuda.so: cannot open shared object file` error occurs, follow suggestions in [this WSL issue](https://github.com/microsoft/WSL/issues/8587) to resolve.

<i class="fas fa-info-circle text-white"></i> When installing with Docker Desktop, if the container pull command is successful, but the run command hangs indefinitely, [ensure you're on Docker Desktop >= 4.18](https://docs.docker.com/desktop/release-notes/){: target="_blank"}.

<br/>
<div id="wsl2-sdkm"></div>

### **WSL2 SDK Manager Install**
[NVIDIA's SDK Manager](https://developer.nvidia.com/sdk-manager){: target="_blank"} gives Windows users a Graphical User Interface (GUI) option to install RAPIDS. It also attempts to fix any environment issues before installing RAPIDS or updating RAPIDS, making it ideal for new WSL users.
1. Install the [latest NVIDIA Drivers](https://www.nvidia.com/en-us/drivers/){: target="_blank"} on the Windows host.
2. Download [SDK Manager's Ubuntu version from their website](https://developer.nvidia.com/sdk-manager){: target="_blank"} (requires sign up or login to NVIDIA's Developer community).  Do not install yet.  The rest of the instructions assume that your home directory's `Downloads` folder is where the `.deb` file will be stored.  If this is not the case, please change the directory, as needed, for your system.
3. Install or update WSL2 and the Ubuntu 22.04 or Ubuntu 24.04 package [using Microsoft's instructions](https://docs.microsoft.com/en-us/windows/wsl/install){: target="_blank"}. To install Ubuntu 24.04 from the command line, use this command:
```bash
wsl --install -d Ubuntu-24.04
```
This will install and start Ubuntu in your Windows host system using WSL2.  Make your **sudo** password memorable as you will need it in the next two steps.
4. Install and run SDK Manager inside Ubuntu by pasting this into your command line.  This command will navigate to your Windows users's `Downloads` folder, from your WSL2 instance, and install the latest SDK Manager `.deb` file that you had downloaded. You will have to enter the sudo password you created when you installed Ubuntu.
```bash
sudo apt update && sudo apt install wslu -y
cd "$(wslpath -au "$(cmd.exe /c 'echo %USERPROFILE%' | tr -d '\r')")/Downloads"
sudo apt install "$(ls -t ./sdkmanager_*_amd64.deb | head -n 1)" -y
sdkmanager
```
5. Sign in when asked, and [follow SDK Manager's RAPIDS installation instructions here](https://docs.nvidia.com/sdk-manager/install-with-sdkm-rapids/index.html){: target="_blank"}.

<br/>
<div id="wsl2-conda"></div>

### **WSL2 Conda Install**

1. Install WSL2 and the Ubuntu distribution [using Microsoft's instructions](https://docs.microsoft.com/en-us/windows/wsl/install){: target="_blank"}.
2. Install the [latest NVIDIA Drivers](https://www.nvidia.com/download/index.aspx){: target="_blank"} on the Windows host.
3. Log in to the WSL2 Linux instance.
4. Install Conda in the WSL2 Linux Instance using our [Conda instructions](#conda).
5. Install RAPIDS via Conda, using the RAPIDS [Release Selector](#selector).
6. Run this code to check that the RAPIDS installation is working:
```python
import cudf
print(cudf.Series([1, 2, 3]))
```

<br/>
<div id="wsl2-docker"></div>

### **WSL2 Docker Desktop Install**

1. Install WSL2 and the Ubuntu distribution [using Microsoft's instructions](https://docs.microsoft.com/en-us/windows/wsl/install){: target="_blank"}.
2. Install the [latest NVIDIA Drivers](https://www.nvidia.com/download/index.aspx){: target="_blank"} on the Windows host.
3. Install latest Docker Desktop for Windows
4. Log in to the WSL2 Linux instance.
5. Generate and run the RAPIDS `docker` command based on your desired configuration using the RAPIDS [Release Selector](#selector).
6. Inside the Docker instance, run this code to check that the RAPIDS installation is working:
```python
import cudf
print(cudf.Series([1, 2, 3]))
```

<br/>
<div id="wsl2-pip"></div>

### **WSL2 pip Install**

1. Install WSL2 and the Ubuntu distribution [using Microsoft's instructions](https://docs.microsoft.com/en-us/windows/wsl/install){: target="_blank"}.
2. Install the [latest NVIDIA Drivers](https://www.nvidia.com/download/index.aspx){: target="_blank"} on the Windows host.
3. Log in to the WSL2 Linux instance.
4. Follow [this helpful developer guide](https://docs.nvidia.com/cuda/wsl-user-guide/index.html#cuda-support-for-wsl2){: target="_blank"} and then install the WSL-specific [CUDA 11](https://developer.nvidia.com/cuda-11-8-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local){: target="_blank"} or [CUDA 12](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local){: target="_blank"} Toolkit without drivers into the WSL2 instance.
  - The installed CUDA Toolkit version must match the pip wheel version (`-cu11` or `-cu12`)
  - Any CUDA 12 CTK will work with RAPIDS `-cu12` pip packages
5. Install RAPIDS pip packages on the WSL2 Linux Instance using the [release selector](#selector) commands.
6. Run this code to check that the RAPIDS installation is working:
```python
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
