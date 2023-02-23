---
html_theme.sidebar_secondary.remove: true
---

# Amazon Web Services

```{include} ../../_includes/menus/aws.md

```

RAPIDS can be deployed on Amazon Web Services (AWS) in several ways. See the
list of accelerated instance types below:

| Cloud <br> Provider | Inst. <br> Type | Inst. <br> Name | GPU <br> Count | GPU <br> Type | xGPU <br> RAM | xGPU <br> RAM Total |
| :------------------ | --------------- | --------------- | -------------- | ------------- | ------------- | ------------------: |
| AWS                 | G4dn            | g4dn\.xlarge    | 1              | T4            | 16 (GB)       |             16 (GB) |
| AWS                 | G4dn            | g4dn\.12xlarge  | 4              | T4            | 16 (GB)       |             64 (GB) |
| AWS                 | G4dn            | g4dn\.metal     | 8              | T4            | 16 (GB)       |            128 (GB) |
| AWS                 | P3              | p3\.2xlarge     | 1              | V100          | 16 (GB)       |             16 (GB) |
| AWS                 | P3              | p3\.8xlarge     | 4              | V100          | 16 (GB)       |             64 (GB) |
| AWS                 | P3              | p3\.16xlarge    | 8              | V100          | 16 (GB)       |            128 (GB) |
| AWS                 | P3              | p3dn\.24xlarge  | 8              | V100          | 32 (GB)       |            256 (GB) |
| AWS                 | P4              | p4d\.24xlarge   | 8              | A100          | 40 (GB)       |            320 (GB) |
| AWS                 | G5              | g5\.xlarge      | 1              | A10G          | 24 (GB)       |             24 (GB) |
| AWS                 | G5              | g5\.2xlarge     | 1              | A10G          | 24 (GB)       |             24 (GB) |
| AWS                 | G5              | g5\.4xlarge     | 1              | A10G          | 24 (GB)       |             24 (GB) |
| AWS                 | G5              | g5\.8xlarge     | 1              | A10G          | 24 (GB)       |             24 (GB) |
| AWS                 | G5              | g5\.16xlarge    | 1              | A10G          | 24 (GB)       |             24 (GB) |
| AWS                 | G5              | g5\.12xlarge    | 4              | A10G          | 24 (GB)       |             96 (GB) |
| AWS                 | G5              | g5\.24xlarge    | 4              | A10G          | 24 (GB)       |             96 (GB) |
| AWS                 | G5              | g5\.48xlarge    | 8              | A10G          | 24 (GB)       |            192 (GB) |

```{toctree}
---
hidden: true
---
ec2
ec2-multi
eks
ecs
sagemaker
```
