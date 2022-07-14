---
layout: default
nav_order: 3
parent: Resources
grand_parent: RAPIDS Maintainer Docs
title: GitHub Actions
---

# {{ page.title }}

## Overview

Details on the self-hosted GitHub Actions runners provided by the RAPIDS Ops team.

### Intended audience

Operations
{: .label .label-purple}

Developers
{: .label .label-green}

## Details

The RAPIDS Ops team provides a set of self-hosted runners that can be used in GitHub Action workflows throughout supported organizations. The tables below outline the labels that can be utilized and their related specifications.

### CPU Label Combinations

The CPU labels are backed by various EC2 instances and do not have any GPUs installed.

| Label Combination       | EC2 Machine Type            |
| ----------------------- | --------------------------- |
| `[linux, amd64, cpu4]`  | `m5d.xlarge` <sub>1</sub>   |
| `[linux, amd64, cpu8]`  | `m5d.2xlarge` <sub>1</sub>  |
| `[linux, amd64, cpu16]` | `m5d.4xlarge` <sub>1</sub>  |
| `[linux, arm64, cpu4]`  | `m6gd.xlarge` <sub>2</sub>  |
| `[linux, arm64, cpu8]`  | `m6gd.2xlarge` <sub>2</sub> |
| `[linux, arm64, cpu16]` | `m6gd.4xlarge` <sub>2</sub> |

Additional specifications:

1. [https://aws.amazon.com/ec2/instance-types/m5/](https://aws.amazon.com/ec2/instance-types/m5/)
2. [https://aws.amazon.com/ec2/instance-types/m6g/](https://aws.amazon.com/ec2/instance-types/m6g/)

## Usage

The code snippet below shows how the labels above may be utilized in a GitHub Action workflow.

**Note**: It is important to add the `self-hosted` label **in addition to** the labels described in the tables above.

```yaml
name: Test Self Hosted Runners
on: push
jobs:
  self_hosted:
    runs-on: [self-hosted, linux, amd64, cpu8]
    steps:
      - name: hello
        run: echo "hello"
```

For additional details, see the official GitHub Action documentation page here: [https://docs.github.com/en/actions/hosting-your-own-runners/using-self-hosted-runners-in-a-workflow](https://docs.github.com/en/actions/hosting-your-own-runners/using-self-hosted-runners-in-a-workflow)
