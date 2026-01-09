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

For installation instructions, see the [Installation Guide](/install/).

{% for release in site.data.platform_support.releases %}
---

## RAPIDS {{ release.version }}

<div markdown="1" style="margin-left: 1.5em;">

#### <i class="fab fa-python"></i> Python
{: .fs-5 }

**{{ release.python }}**

#### <i class="fas fa-desktop"></i> Operating Systems
{: .fs-5 }

**glibc {{ release.glibc }}** (tested on {% for os in release.os_support %}{{ os }}{% unless forloop.last %}, {% endunless %}{% endfor %})

#### <i class="fas fa-microchip"></i> CUDA
{: .fs-5 }

| | CUDA 12 | CUDA 13 |
|:--|:--|:--|
| **Toolkit** | {{ release.cuda_12.toolkit }} | {{ release.cuda_13.toolkit }} |
| **Driver** | {{ release.cuda_12.driver }} | {{ release.cuda_13.driver }} |
| **Compute Capability** | {{ release.cuda_12.compute_capability }} | {{ release.cuda_13.compute_capability }} |

#### <i class="fas fa-hammer"></i> Source Builds
{: .fs-5 }

| Dependency | Version |
|:--|:--|
| **CCCL** | {{ release.source_build.cccl }} |

</div>

{% endfor %}
