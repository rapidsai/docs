# Does the Dask scheduler need a GPU?

A common question from users deploying Dask clusters is whether the scheduler has different minimum requirements to the workers. This question is compounded when using RAPIDS and GPUs.

```{warning}
This guide outlines our current advice on scheduler hardware requirements, but this may be subject to change.
```

**TLDR; It is strongly suggested that your Dask scheduler has matching hardware/software capabilities to the other components in your cluster.**

Therefore, if your workers have GPUs and the RAPIDS libraries installed we recommend that your scheduler does too. However the GPU attached to your scheduler doesn't need to be as powerful as the GPUs on your workers, as long as it has the same capabilities and driver/CUDA versions.

## What does the scheduler use a GPU for?

The Dask client generates a task graph of operations that it wants to be performed and serializes any data that needs to be sent to the workers. The scheduler handles allocating those tasks to the various Dask workers and passes serialized data back and forth. The workers deserialize the data, perform calculations, serialize the result and pass it back.

This can lead users to logically ask if the scheduler needs the same capabilities as the workers/client. It doesn't handle the actual data or do any of the user calculations, it just decides where work should go.

Taking this even further you could even ask "Does the Dask scheduler even need to be written in Python?". Some folks even [experimented with a Rust implementation of the scheduler](https://github.com/It4innovations/rsds) a couple of years ago.

There are two primary reasons why we recommend that the scheduler has the same capabilities:

- There are edge cases where the scheduler does deserialize data.
- Some scheduler optimizations require high-level graphs to be pickled on the client and unpickled on the scheduler.

If your workload doesn't trigger any edge-cases and you're not using the high-level graph optimizations then you could likely get away with not having a GPU. But it is likely you will run into problems eventually and the failure-modes will be potentially hard to debug.

### Known edge cases

When calling `client.submit` and passing data directly to a function the whole graph is serialized and sent to the scheduler. In order for the scheduler to figure out what to do with it the graph is deserialized. If the data uses GPUs this can cause the scheduler to import RAPIDS libraries, attempt to instantiate a CUDA context and populate the data into GPU memory. If those libraries are missing and/or there are no GPUs this will cause the scheduler to fail.

Many Dask collections also have a meta object which represents the overall collection but without any data. For example a Dask Dataframe has a meta Pandas Dataframe which has the same meta properties and is used during scheduling. If the underlying data is instead a cuDF Dataframe then the meta object will be too, which is deserialized on the scheduler.

### Scheduler optimizations and High-Level graphs

The Dask community is actively working on implementing high-level graphs which will both speed up client -> scheduler communication and allow the scheduler to make advanced optmizations such as predicate pushdown.

Much effort has been put into using existing serialization strategies to communicate the HLG but this has proven prohibitively difficult to implement. The current plan is to simplify HighLevelGraph/Layer so that the entire HLG can be pickled on the client, sent to the scheduler as a single binary blob, and then unpickled/materialized (HLG->dict) on the scheduler. The problem with this new plan is that the pickle/un-pickle convention will require the scheduler to have the same environment as the client. If any Layer logic also requires a device allocation, then this approach also requires the scheduler to have access to a GPU.

## So what are the minimum requirements of the scheduler?

From a software perspective we recommend that the Python environment on the client, scheduler and workers all match. Given that the user is expected to ensure the worker has the same environment as the client it is not much of a burden to ensure the scheduler also has the same environment.

From a hardware perspective we recommend that the scheduler has the same capabilities, but not necessarily the same quantity of resource. Therefore if the workers have one or more GPUs we recommend that the scheduler has access to one GPU with matching NVIDIA driver and CUDA versions. In a large multi-node cluster deployment on a cloud platform this may mean the workers are launched on VMs with 8 GPUs and the scheduler is launched on a smaller VM with one GPU. You could also select a less powerful GPU such as those intended for inferencing for your scheduler like a T4, provided it has the same CUDA capabilities, NVIDIA driver version and CUDA/CUDA Toolkit version.

This balance means we can guarantee things function as intended, but reduces cost because placing the scheduler on an 8 GPU node would be a waste of resources.
