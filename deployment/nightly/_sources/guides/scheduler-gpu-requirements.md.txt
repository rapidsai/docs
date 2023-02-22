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

When calling [`client.submit`](dask:distributed.Client.submit) and passing data directly to a function the whole graph is serialized and sent to the scheduler. In order for the scheduler to figure out what to do with it the graph is deserialized. If the data uses GPUs this can cause the scheduler to import RAPIDS libraries, attempt to instantiate a CUDA context and populate the data into GPU memory. If those libraries are missing and/or there are no GPUs this will cause the scheduler to fail.

Many Dask collections also have a meta object which represents the overall collection but without any data. For example a Dask Dataframe has a meta Pandas Dataframe which has the same meta properties and is used during scheduling. If the underlying data is instead a cuDF Dataframe then the meta object will be too, which is deserialized on the scheduler.

### Example failure modes

When using the default TCP communication protocol, the scheduler generally does _not_ inspect data communicated between clients and workers, so many workflows will not provoke failure. For example, suppose we set up a Dask cluster and do not provide the scheduler with a GPU. The following simple computation with [CuPy](https://cupy.dev)-backed Dask arrays completes successfully

```python
import cupy
from distributed import Client, wait
import dask.array as da

client = Client(scheduler_file="scheduler.json")

x = cupy.arange(10)

y = da.arange(1000, like=x)

z = (y * 2).persist()
wait(z)
# Now let's look at some results
print(z[:10].compute())
```

We can run this code, giving the scheduler no access to a GPU:

```sh
$ CUDA_VISIBLE_DEVICES="" dask scheduler --protocol tcp --scheduler-file scheduler.json  &
$ dask cuda worker --protocol tcp --scheduler-file scheduler.json &
$ python test.py
...
[ 0  2  4  6  8 10 12 14 16 18]
...
```

In contrast, if you provision an [Infiniband-enabled system](/guides/azure/infiniband.md) and wish to take advantage of the high-performance network, you will want to use the [UCX](https://openucx.org/) protocol, rather than TCP. Using such a setup without a GPU on the scheduler will not succeed. When the client or workers communicate with the scheduler, any GPU-allocated buffers will be sent directly between GPUs (avoiding a roundtrip to host memory). This is more efficient, but will not succeed if the scheduler does not _have_ a GPU. Running the same example from above, but this time using UCX we obtain an error:

```sh
$ CUDA_VISIBLE_DEVICES="" dask scheduler --protocol ucx --scheduler-file scheduler.json  &
$ dask cuda worker --protocol ucx --scheduler-file scheduler.json &
$ python test.py
$ CUDA_VISIBLE_DEVICES="" dask scheduler --protocol ucx --scheduler-file foo.json  &
$ dask-cuda-worker --protocol ucx  --scheduler-file scheduler.json &
$ python test.py
...
2023-01-27 11:01:28,263 - distributed.core - ERROR - CUDA error at: .../rmm/include/rmm/cuda_device.hpp:56: cudaErrorNoDevice no CUDA-capable device is detected
Traceback (most recent call last):
  File ".../distributed/distributed/utils.py", line 741, in wrapper
    return await func(*args, **kwargs)
  File ".../distributed/distributed/comm/ucx.py", line 372, in read
    frames = [
  File ".../distributed/distributed/comm/ucx.py", line 373, in <listcomp>
    device_array(each_size) if is_cuda else host_array(each_size)
  File ".../distributed/distributed/comm/ucx.py", line 171, in device_array
    return rmm.DeviceBuffer(size=n)
  File "device_buffer.pyx", line 85, in rmm._lib.device_buffer.DeviceBuffer.__cinit__
RuntimeError: CUDA error at: .../rmm/include/rmm/cuda_device.hpp:56: cudaErrorNoDevice no CUDA-capable device is detected
2023-01-27 11:01:28,263 - distributed.core - ERROR - Exception while handling op gather
Traceback (most recent call last):
  File ".../distributed/distributed/core.py", line 820, in _handle_comm
    result = await result
  File ".../distributed/distributed/scheduler.py", line 5687, in gather
    data, missing_keys, missing_workers = await gather_from_workers(
  File ".../distributed/distributed/utils_comm.py", line 80, in gather_from_workers
    r = await c
  File ".../distributed/distributed/worker.py", line 2872, in get_data_from_worker
    return await retry_operation(_get_data, operation="get_data_from_worker")
  File ".../distributed/distributed/utils_comm.py", line 419, in retry_operation
    return await retry(
  File ".../distributed/distributed/utils_comm.py", line 404, in retry
    return await coro()
  File ".../distributed/distributed/worker.py", line 2852, in _get_data
    response = await send_recv(
  File ".../distributed/distributed/core.py", line 986, in send_recv
    response = await comm.read(deserializers=deserializers)
  File ".../distributed/distributed/utils.py", line 741, in wrapper
    return await func(*args, **kwargs)
  File ".../distributed/distributed/comm/ucx.py", line 372, in read
    frames = [
  File ".../distributed/distributed/comm/ucx.py", line 373, in <listcomp>
    device_array(each_size) if is_cuda else host_array(each_size)
  File ".../distributed/distributed/comm/ucx.py", line 171, in device_array
    return rmm.DeviceBuffer(size=n)
  File "device_buffer.pyx", line 85, in rmm._lib.device_buffer.DeviceBuffer.__cinit__
RuntimeError: CUDA error at: .../rmm/include/rmm/cuda_device.hpp:56: cudaErrorNoDevice no CUDA-capable device is detected
Traceback (most recent call last):
  File "test.py", line 15, in <module>
    print(z[:10].compute())
  File ".../dask/dask/base.py", line 314, in compute
    (result,) = compute(self, traverse=False, **kwargs)
  File ".../dask/dask/base.py", line 599, in compute
    results = schedule(dsk, keys, **kwargs)
  File ".../distributed/distributed/client.py", line 3144, in get
    results = self.gather(packed, asynchronous=asynchronous, direct=direct)
  File ".../distributed/distributed/client.py", line 2313, in gather
    return self.sync(
  File ".../distributed/distributed/utils.py", line 338, in sync
    return sync(
  File ".../distributed/distributed/utils.py", line 405, in sync
    raise exc.with_traceback(tb)
  File ".../distributed/distributed/utils.py", line 378, in f
    result = yield future
  File ".../tornado/gen.py", line 769, in run
    value = future.result()
  File ".../distributed/distributed/client.py", line 2205, in _gather
    response = await future
  File ".../distributed/distributed/client.py", line 2256, in _gather_remote
    response = await retry_operation(self.scheduler.gather, keys=keys)
  File ".../distributed/distributed/utils_comm.py", line 419, in retry_operation
    return await retry(
  File ".../distributed/distributed/utils_comm.py", line 404, in retry
    return await coro()
  File ".../distributed/distributed/core.py", line 1221, in send_recv_from_rpc
    return await send_recv(comm=comm, op=key, **kwargs)
  File ".../distributed/distributed/core.py", line 1011, in send_recv
    raise exc.with_traceback(tb)
  File ".../distributed/distributed/core.py", line 820, in _handle_comm
    result = await result
  File ".../distributed/distributed/scheduler.py", line 5687, in gather
    data, missing_keys, missing_workers = await gather_from_workers(
  File ".../distributed/distributed/utils_comm.py", line 80, in gather_from_workers
    r = await c
  File ".../distributed/distributed/worker.py", line 2872, in get_data_from_worker
    return await retry_operation(_get_data, operation="get_data_from_worker")
  File ".../distributed/distributed/utils_comm.py", line 419, in retry_operation
    return await retry(
  File ".../distributed/distributed/utils_comm.py", line 404, in retry
    return await coro()
  File ".../distributed/distributed/worker.py", line 2852, in _get_data
    response = await send_recv(
  File ".../distributed/distributed/core.py", line 986, in send_recv
    response = await comm.read(deserializers=deserializers)
  File ".../distributed/distributed/utils.py", line 741, in wrapper
    return await func(*args, **kwargs)
  File ".../distributed/distributed/comm/ucx.py", line 372, in read
    frames = [
  File ".../distributed/distributed/comm/ucx.py", line 373, in <listcomp>
    device_array(each_size) if is_cuda else host_array(each_size)
  File ".../distributed/distributed/comm/ucx.py", line 171, in device_array
    return rmm.DeviceBuffer(size=n)
  File "device_buffer.pyx", line 85, in rmm._lib.device_buffer.DeviceBuffer.__cinit__
RuntimeError: CUDA error at: .../rmm/include/rmm/cuda_device.hpp:56: cudaErrorNoDevice no CUDA-capable device is detected
...
```

The critical error comes from [RMM](https://docs.rapids.ai/api/rmm/stable/), we're attempting to allocate a [`DeviceBuffer`](https://docs.rapids.ai/api/rmm/stable/basics.html#devicebuffers) on the scheduler, but there is no GPU available to do so:

```pytb
  File ".../distributed/distributed/comm/ucx.py", line 171, in device_array
    return rmm.DeviceBuffer(size=n)
  File "device_buffer.pyx", line 85, in rmm._lib.device_buffer.DeviceBuffer.__cinit__
RuntimeError: CUDA error at: .../rmm/include/rmm/cuda_device.hpp:56: cudaErrorNoDevice no CUDA-capable device is detected
```

### Scheduler optimizations and High-Level graphs

The Dask community is actively working on implementing high-level graphs which will both speed up client -> scheduler communication and allow the scheduler to make advanced optmizations such as predicate pushdown.

Much effort has been put into using existing serialization strategies to communicate the HLG but this has proven prohibitively difficult to implement. The current plan is to simplify HighLevelGraph/Layer so that the entire HLG can be pickled on the client, sent to the scheduler as a single binary blob, and then unpickled/materialized (HLG->dict) on the scheduler. The problem with this new plan is that the pickle/un-pickle convention will require the scheduler to have the same environment as the client. If any Layer logic also requires a device allocation, then this approach also requires the scheduler to have access to a GPU.

## So what are the minimum requirements of the scheduler?

From a software perspective we recommend that the Python environment on the client, scheduler and workers all match. Given that the user is expected to ensure the worker has the same environment as the client it is not much of a burden to ensure the scheduler also has the same environment.

From a hardware perspective we recommend that the scheduler has the same capabilities, but not necessarily the same quantity of resource. Therefore if the workers have one or more GPUs we recommend that the scheduler has access to one GPU with matching NVIDIA driver and CUDA versions. In a large multi-node cluster deployment on a cloud platform this may mean the workers are launched on VMs with 8 GPUs and the scheduler is launched on a smaller VM with one GPU. You could also select a less powerful GPU such as those intended for inferencing for your scheduler like a T4, provided it has the same CUDA capabilities, NVIDIA driver version and CUDA/CUDA Toolkit version.

This balance means we can guarantee things function as intended, but reduces cost because placing the scheduler on an 8 GPU node would be a waste of resources.
