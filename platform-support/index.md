---
layout: default
title: Platform Support
nav_order: 3
description: |
  RAPIDS platform support matrix showing CUDA, Python, driver, and GPU architecture requirements for each release.
---

# RAPIDS Platform Support
{: .fs-8 }

RAPIDS libraries are supported on a specific set of platforms for each release. RAPIDS depends on CUDA and Python, and each release is built and tested against specific versions of these dependencies.

RAPIDS uses [CUDA compatibility](https://docs.nvidia.com/deploy/cuda-compatibility/){: target="_blank"} to support a range of CUDA toolkit and driver versions.
The NVIDIA Developer documentation contains a reference of [Compute Capability](https://developer.nvidia.com/cuda-gpus){: target="_blank"} for each GPU architecture.
Note that for the list of supported compute capabilities below, newer GPUs are supported via [forward-compatible PTX instructions](https://developer.nvidia.com/blog/understanding-ptx-the-assembly-language-of-cuda-gpu-computing/){: target="_blank"} built for the latest virtual architecture.

For installation instructions, see the [Installation Guide](/install/).

{% for release in site.data.platform_support.releases %}
---

## RAPIDS {{ release.version }}

<div markdown="1" style="margin-left: 1.5em;">

#### <i class="fas fa-desktop"></i> Operating Systems
{: .fs-5 }

- <i class="fab fa-linux"></i> **Linux (glibc {{ release.glibc_min }}+):** {{ release.cpu_arch | join: ", " }} (tested on {% for os in release.os_support %}{{ os }}{% unless forloop.last %}, {% endunless %}{% endfor %})
- <i class="fab fa-windows"></i> **Windows:** Supported via [WSL](/install/#wsl2) with a compatible Linux distribution

#### <i class="fab fa-python"></i> Python
{: .fs-5 }

**{{ release.python | join: ", " }}**

#### <i class="fas fa-microchip"></i> CUDA
{: .fs-5 }

| | {% for cuda in release.cuda %}CUDA {{ cuda.major }}{% unless forloop.last %} | {% endunless %}{% endfor %} |
|:--|{% for cuda in release.cuda %}:--|{% endfor %}
| **Toolkit** | {% for cuda in release.cuda %}{{ cuda.toolkit_min }}{% if cuda.toolkit_min != cuda.toolkit_max %} - {{ cuda.toolkit_max }}{% endif %}{% unless forloop.last %} | {% endunless %}{% endfor %} |
| **Driver** | {% for cuda in release.cuda %}{{ cuda.driver_min }}+{% unless forloop.last %} | {% endunless %}{% endfor %} |
| **Compute Capability** | {% for cuda in release.cuda %}{% for cc in cuda.compute_capability %}{{ cc.name }} ({% if cc.sm.first %}{{ cc.sm | join: ", " }}{% else %}{{ cc.sm }}{% endif %}){% unless forloop.last %}, {% endunless %}{% endfor %} or newer{% unless forloop.last %} | {% endunless %}{% endfor %} |

#### <i class="fas fa-hammer"></i> Source Builds
{: .fs-5 }

| Dependency | Version |
|:--|:--|
| **GCC** | {{ release.source_build.gcc }} |
| **CCCL** | {{ release.source_build.cccl }} |
| **nvCOMP** | {{ release.source_build.nvcomp }} |

</div>

{% endfor %}
