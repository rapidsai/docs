---
html_theme.sidebar_secondary.remove: true
---

# Microsoft Azure

```{include} ../../_includes/menus/azure.md

```

RAPIDS can be deployed on Microsoft Azure in several ways. Azure supports various kinds of GPU VMs for different needs.
For RAPIDS users we recommend NC/ND VMs for computation and deep learning optimized instances.

NC (>=v3) series

| Size                     | vCPU | Memory: GiB | Temp Storage (with NVMe) : GiB | GPU | GPU Memory: GiB | Max data disks | Max uncached disk throughput: IOPS / MBps | Max NICs/network bandwidth (MBps) |
| ------------------------ | ---- | ----------- | ------------------------------ | --- | --------------- | -------------- | ----------------------------------------- | --------------------------------- |
| Standard_NC24ads_A100_v4 | 24   | 220         | 1123                           | 1   | 80              | 12             | 30000/1000                                | 2/20,000                          |
| Standard_NC48ads_A100_v4 | 48   | 440         | 2246                           | 2   | 160             | 24             | 60000/2000                                | 4/40,000                          |
| Standard_NC96ads_A100_v4 | 96   | 880         | 4492                           | 4   | 320             | 32             | 120000/4000                               | 8/80,000                          |
| Standard_NC4as_T4_v3     | 4    | 28          | 180                            | 1   | 16              | 8              | 2 / 8000                                  |
| Standard_NC8as_T4_v3     | 8    | 56          | 360                            | 1   | 16              | 16             | 4 / 8000                                  |
| Standard_NC16as_T4_v3    | 16   | 110         | 360                            | 1   | 16              | 32             | 8 / 8000                                  |
| Standard_NC64as_T4_v3    | 64   | 440         | 2880                           | 4   | 64              | 32             | 8 / 32000                                 |
| Standard_NC6s_v3         | 6    | 112         | 736                            | 1   | 16              | 12             | 20000/200                                 | 4                                 |
| Standard_NC12s_v3        | 12   | 224         | 1474                           | 2   | 32              | 24             | 40000/400                                 | 8                                 |
| Standard_NC24s_v3        | 24   | 448         | 2948                           | 4   | 64              | 32             | 80000/800                                 | 8                                 |
| Standard_NC24rs_v3\*     | 24   | 448         | 2948                           | 4   | 64              | 32             | 80000/800                                 | 8                                 |

\* RDMA capable

ND (>=v2) series

| Size                      | vCPU | Memory: GiB | Temp Storage (with NVMe) : GiB | GPU                            | GPU Memory: GiB | Max data disks | Max uncached disk throughput: IOPS / MBps | Max NICs/network bandwidth (MBps) |
| ------------------------- | ---- | ----------- | ------------------------------ | ------------------------------ | --------------- | -------------- | ----------------------------------------- | --------------------------------- |
| Standard_ND96asr_v4       | 96   | 900         | 6000                           | 8 A100 40 GB GPUs (NVLink 3.0) | 40              | 32             | 80,000 / 800                              | 8/24,000                          |
| Standard_ND96amsr_A100_v4 | 96   | 1900        | 6400                           | 8 A100 80 GB GPUs (NVLink 3.0) | 80              | 32             | 80,000 / 800                              | 8/24,000                          |
| Standard_ND40rs_v2        | 40   | 672         | 2948                           | 8 V100 32 GB (NVLink)          | 32              | 32             | 80,000 / 800                              | 8/24,000                          |

## Useful Links

- [GPU VM availability by region](https://azure.microsoft.com/en-us/explore/global-infrastructure/products-by-region/?products=virtual-machines)
- [For GPU VM sizes overview](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes-gpu)

```{toctree}
---
hidden: true
---
azure-vm
aks
azureml
```
