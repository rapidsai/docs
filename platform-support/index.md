---
layout: default
title: Platform Support
nav_order: 3
description: |
  RAPIDS platform support matrix showing CUDA, Python, driver, and GPU architecture requirements for each release.
---

# RAPIDS Platform Support
{: .fs-8 }

This page documents the supported versions of CUDA, Python, GPU drivers, and GPU architectures for each RAPIDS release.
{: .fs-6 .fw-300 }

{% for release in site.data.platform_support.releases %}
---

## RAPIDS {{ release.version }}

| Requirement | Supported |
|:------------|:----------|
| **Python** | {{ release.python }} |
| **glibc** | {{ release.glibc }} |
| **Operating Systems** | {% for os in release.os_support %}{{ os }}{% unless forloop.last %}, {% endunless %}{% endfor %} |

### CUDA 12

| Requirement | Supported |
|:------------|:----------|
| **CUDA Toolkit** | {{ release.cuda_12.toolkit }} |
| **NVIDIA Driver** | {{ release.cuda_12.driver }} |
| **GPU Architectures** | {{ release.cuda_12.architectures }} |

### CUDA 13

| Requirement | Supported |
|:------------|:----------|
| **CUDA Toolkit** | {{ release.cuda_13.toolkit }} |
| **NVIDIA Driver** | {{ release.cuda_13.driver }} |
| **GPU Architectures** | {{ release.cuda_13.architectures }} |

{% endfor %}
---

## Related Resources

- [Installation Guide](/install/) - Detailed installation instructions
- [RAPIDS Notices](/notices/) - Deprecation and support announcements
- [Release Schedule](/releases/schedule/) - Upcoming release dates
