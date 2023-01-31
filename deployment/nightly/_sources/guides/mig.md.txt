# Multi-Instance GPU (MIG)

[Multi-Instance GPU](https://www.nvidia.com/en-us/technologies/multi-instance-gpu/) is a technology that allows partitioning a single GPU into multiple instances, making each one seem as a completely independent GPU. Each instance then receives a certain slice of the GPU computational resources and a pre-defined block of memory that is detached from the other instances by on-chip protections.

Due to the protection layer to make MIG secure, certain limitations exist. One such limitation that is generally important for HPC applications is the lack of support for [CUDA Inter-Process Communication (IPC)](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#interprocess-communication), which enables transfers over NVLink and NVSwitch to greatly speed up communication between physical GPUs. When using MIG, [NVLink and NVSwitch](https://www.nvidia.com/en-us/data-center/nvlink/) are thus completely unavailable, forcing the application to take a more expensive communication channel via the system (CPU) memory.

Given limitations in communication capability, we advise users to first understand the tradeoffs that have to be made when attempting to setup a cluster of MIG instances. While the partitioning could be beneficial to certain applications that need only a certain amount of compute capability, communication bottlenecks may be a problem and thus need to be thought of carefully.

## Dask Cluster

Dask clusters of MIG instances are supported via Dask-CUDA as long as all MIG instances are identical with respect to memory. Much like a cluster of physical GPUs, mixing GPUs with different memory sizes is generally not a good idea as Dask may not be able to balance work correctly and eventually could lead to more frequent out-of-memory errors.

For example, partitioning two GPUs into 7 x 10GB instances each and setting up a cluster with all 14 instances should be ok. However, partitioning one of the GPUs into 7 x 10GB instances and another with 3 x 20GB should be avoided.

Unlike for a system composed of unpartitioned GPUs, Dask-CUDA cannot automatically infer the GPUs to be utilized for the cluster. In a MIG setup, the user is then required to specify the GPU instances to be used by the cluster. This is achieved by specifying either the `CUDA_VISIBLE_DEVICES` environment variable for either {class}`dask_cuda.LocalCUDACluster` or `dask-cuda-worker`, or the homonymous argument for {class}`dask_cuda.LocalCUDACluster`.

Physical GPUs can be addressed by their indices `[0..N)` (where `N` is the total number of GPUs installed) or by its name composed of the `GPU-` prefix followed by its UUID. MIG instances have no indices and can only be addressed by their names, composed of the `MIG-` prefix followed by its UUID. The name of a MIG instance will the look similar to: `MIG-41b3359c-e721-56e5-8009-12e5797ed514`.

### Determine MIG Names

The simplest way to determine the names of MIG instances is to run `nvidia-smi -L` on the command line.

```bash
$ nvidia-smi -L
GPU 0: NVIDIA A100-PCIE-40GB (UUID: GPU-84fd49f2-48ad-50e8-9f2e-3bf0dfd47ccb)
  MIG 2g.10gb     Device  0: (UUID: MIG-41b3359c-e721-56e5-8009-12e5797ed514)
  MIG 2g.10gb     Device  1: (UUID: MIG-65b79fff-6d3c-5490-a288-b31ec705f310)
  MIG 2g.10gb     Device  2: (UUID: MIG-c6e2bae8-46d4-5a7e-9a68-c6cf1f680ba0)
```

In the example case above the system has one NVIDIA A100 with 3 x 10GB MIG instances. In the next sections we will see how to use the instance names to startup a Dask cluster composed of MIG GPUs. Please note that once a GPU is partitioned, the physical GPU (named `GPU-84fd49f2-48ad-50e8-9f2e-3bf0dfd47ccb` above) is inaccessible for CUDA compute and cannot be used as part of a Dask cluster.

Alternatively, MIG instance names can be obtained programatically using [NVML](https://developer.nvidia.com/nvidia-management-library-nvml) or [PyNVML](https://github.com/gpuopenanalytics/pynvml). Please refer to the [NVML API](https://docs.nvidia.com/deploy/nvml-api/) to write appropriate utilities for that purpose.

### LocalCUDACluster

Suppose you have 3 MIG instances on the local system:

- `MIG-41b3359c-e721-56e5-8009-12e5797ed514`
- `MIG-65b79fff-6d3c-5490-a288-b31ec705f310`
- `MIG-c6e2bae8-46d4-5a7e-9a68-c6cf1f680ba0`

To start a {class}`dask_cuda.LocalCUDACluster`, the user would run the following:

```python
from dask_cuda import LocalCUDACluster

cluster = LocalCUDACluster(
    CUDA_VISIBLE_DEVICES=[
        "MIG-41b3359c-e721-56e5-8009-12e5797ed514",
        "MIG-65b79fff-6d3c-5490-a288-b31ec705f310",
        "MIG-c6e2bae8-46d4-5a7e-9a68-c6cf1f680ba0",
    ],
    # Other `LocalCUDACluster` arguments
)
```

### dask-cuda-worker

Suppose you have 3 MIG instances on the local system:

- `MIG-41b3359c-e721-56e5-8009-12e5797ed514`
- `MIG-65b79fff-6d3c-5490-a288-b31ec705f310`
- `MIG-c6e2bae8-46d4-5a7e-9a68-c6cf1f680ba0`

To start a `dask-cuda-worker` that the address to the scheduler is located in the `scheduler.json` file, the user would run the following:

```bash
CUDA_VISIBLE_DEVICES="MIG-41b3359c-e721-56e5-8009-12e5797ed514,MIG-65b79fff-6d3c-5490-a288-b31ec705f310,MIG-c6e2bae8-46d4-5a7e-9a68-c6cf1f680ba0" dask-cuda-worker scheduler.json # --other-arguments
```

Please note that in the example above we created 3 Dask-CUDA workers on one node, for a multi-node cluster, the correct MIG names need to be specified, and they will always be different for each host.

## XGBoost with Dask Cluster

Currently [XGBoost](https://www.nvidia.com/en-us/glossary/data-science/xgboost/) only exposes support for GPU communication via NCCL, which does not support MIG. For this reason, A Dask cluster that utilizes XGBoost would have to utilize TCP instead for all communications which will likely cause in considerable performance degradation. Therefore, using XGBoost with MIG is not recommended.

```{relatedexamples}

```
