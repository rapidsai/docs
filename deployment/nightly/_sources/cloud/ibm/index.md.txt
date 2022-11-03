# IBM Cloud

```{toctree}
---
maxdepth: 2
caption: IBM Cloud
---
virtual-server
```

RAPIDS can be deployed on IBM Cloud in several ways. See the
list of accelerated instance types below:

| Cloud <br> Provider | Inst. <br> Type       | vCPUs | Inst. <br> Name    | GPU <br> Count | GPU <br> Type | xGPU <br> RAM | xGPU <br> RAM Total |
| :------------------ | --------------------- | ----- | ------------------ | -------------- | ------------- | ------------- | ------------------: |
| IBM                 | V100 GPU Virtual      | 8     | gx2-8x64x1v100     | 1              | NVIDIA Tesla  | 16 (GB)       |             64 (GB) |
| IBM                 | V100 GPU Virtual      | 16    | gx2-16x128x1v100   | 1              | NVIDIA Tesla  | 16 (GB)       |            128 (GB) |
| IBM                 | V100 GPU Virtual      | 16    | gx2-16x128x2v100   | 2              | NVIDIA Tesla  | 16 (GB)       |            128 (GB) |
| IBM                 | V100 GPU Virtual      | 32    | gx2-32x256x2v100   | 2              | NVIDIA Tesla  | 16 (GB)       |            256 (GB) |
| IBM                 | P100 GPU Bare Metal\* | 32    | mg4c.32x384.2xp100 | 2              | NVIDIA Tesla  | 16 (GB)       |            384 (GB) |
| IBM                 | V100 GPU Bare Metal\* | 48    | mg4c.48x384.2xv100 | 2              | NVIDIA Tesla  | 16 (GB)       |            384 (GB) |

```{warning}
*Bare Metal instances are billed in monthly intervals rather than hourly intervals.
```
