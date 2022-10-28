# Dask Kubernetes

This article introduces the classic way to setup RAPIDS with `dask-kubernetes`.

## Prerequisite

- A kubernetes cluster that can allocate GPU pods.
- [miniconda](https://docs.conda.io/en/latest/miniconda.html)

## Client environment setup

The client environment is used to setup dask cluster and execute user domain code.
In this demo we need to meet minimum requirement of `cudf`, `dask-cudf` and
`dask-kubernetes`. It is recommended to follow RAPIDS
[release-selector](https://rapids.ai/start.html#get-rapids) to setup your environment.

For simplicity, this guide assumes user manages environments with conda and installs
The minimal requiredments mentioned above by:

```bash
conda create -n rapids-22.08 -c rapidsai -c nvidia -c conda-forge  \
    cudf=22.08 dask_cudf=22.08 python=3.9 cudatoolkit=11.5 dask_kubernetes
```

## Cluster setup

User may create dask-cuda cluster either via `KubeCluster` interface:

```python
from dask_kubernetes import KubeCluster, make_pod_spec
gpu_worker_spec = make_pod_spec(
    image='nvcr.io/nvidia/rapidsai/rapidsai-core:22.08-cuda11.5-runtime-ubuntu20.04-py3.9',
    env={"DISABLE_JUPYTER":"true"},
    cpu_limit=2,
    cpu_request=2,
    memory_limit='3G',
    memory_request='3G',
    gpu_limit=1
)
cluster = KubeCluster(gpu_worker_spec)
```

Alternatively, user can specify pod specs with standard kubernetes pod specification.

```{literalinclude} ./dask-kubernetes/gpu-worker-spec.yaml
:language: yaml
```

Load the spec via:

```python
cluster = KubeCluster('gpu-worker-spec.yaml')
```

```{note}
It is recommended that the client's and scheduler's dask version match. User should pick
the same RAPIDS version when installing client environment and when picking the image for
worker pods.
```

At this point, a cluster containing a single dask-scheduler pod is setup.
To create the worker pods, use `cluster.scale`.

```python
cluster.scale(3)
```

### Verification

Create a small `dask_cudf` dataframe and compute the result on the cluster:

```python
import cudf, dask_cudf

ddf = dask_cudf.from_cudf(cudf.DataFrame(
    {'a': list(range(20))}), npartitions=2)
ddf.sum().compute()
# should print a: 190
```
