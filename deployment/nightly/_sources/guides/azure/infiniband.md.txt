# How to Setup InfiniBand on Azure

[Azure GPU optmized virtual machines](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes-gpu) provide
a low latency and high bandwidth InfiniBand network. This guide walks through the steps to enable InfiniBand to
optimize network performance.

## Build a Virtual Machine

Start by creating a GPU optimized VM from the Azure portal. Below is an example that we will use
for demonstration.

- Create new VM instance.
- Select `East US` region.
- Change `Availability options` to `Availability set` and create a set.
  - If building multiple instances put additional instances in the same set.
- Use the 2nd Gen Ubuntu 20.04 image.
  - Search all images for `Ubuntu Server 20.04` and choose the second one down on the list.
- Change size to `ND40rs_v2`.
- Set password login with credentials.
  - User `someuser`
  - Password `somepassword`
- Leave all other options as default.

Then connect to the VM using your preferred method.

## Install Software

Before installing the drivers ensure the system is up to date.

```shell
sudo apt-get update
sudo apt-get upgrade -y
```

### NVIDIA Drivers

The commands below should work for Ubuntu. See the [CUDA Toolkit documentation](https://docs.nvidia.com/cuda/index.html#installation-guides) for details on installing on other operating systems.

```shell
sudo apt-get install -y linux-headers-$(uname -r)
distribution=$(. /etc/os-release;echo $ID$VERSION_ID | sed -e 's/\.//g')
wget https://developer.download.nvidia.com/compute/cuda/repos/$distribution/x86_64/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb
sudo apt-get update
sudo apt-get -y install cuda-drivers
```

Restart VM instance

```shell
sudo reboot
```

Once the VM boots, reconnect and run `nvidia-smi` to verify driver installation.

```shell
nvidia-smi
```

```shell
Mon Nov 14 20:32:39 2022
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 520.61.05    Driver Version: 520.61.05    CUDA Version: 11.8     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla V100-SXM2...  On   | 00000001:00:00.0 Off |                    0 |
| N/A   34C    P0    41W / 300W |    445MiB / 32768MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   1  Tesla V100-SXM2...  On   | 00000002:00:00.0 Off |                    0 |
| N/A   37C    P0    43W / 300W |      4MiB / 32768MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   2  Tesla V100-SXM2...  On   | 00000003:00:00.0 Off |                    0 |
| N/A   34C    P0    42W / 300W |      4MiB / 32768MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   3  Tesla V100-SXM2...  On   | 00000004:00:00.0 Off |                    0 |
| N/A   35C    P0    44W / 300W |      4MiB / 32768MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   4  Tesla V100-SXM2...  On   | 00000005:00:00.0 Off |                    0 |
| N/A   35C    P0    41W / 300W |      4MiB / 32768MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   5  Tesla V100-SXM2...  On   | 00000006:00:00.0 Off |                    0 |
| N/A   36C    P0    43W / 300W |      4MiB / 32768MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   6  Tesla V100-SXM2...  On   | 00000007:00:00.0 Off |                    0 |
| N/A   37C    P0    44W / 300W |      4MiB / 32768MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   7  Tesla V100-SXM2...  On   | 00000008:00:00.0 Off |                    0 |
| N/A   38C    P0    44W / 300W |      4MiB / 32768MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      1396      G   /usr/lib/xorg/Xorg                427MiB |
|    0   N/A  N/A      1762      G   /usr/bin/gnome-shell               16MiB |
|    1   N/A  N/A      1396      G   /usr/lib/xorg/Xorg                  4MiB |
|    2   N/A  N/A      1396      G   /usr/lib/xorg/Xorg                  4MiB |
|    3   N/A  N/A      1396      G   /usr/lib/xorg/Xorg                  4MiB |
|    4   N/A  N/A      1396      G   /usr/lib/xorg/Xorg                  4MiB |
|    5   N/A  N/A      1396      G   /usr/lib/xorg/Xorg                  4MiB |
|    6   N/A  N/A      1396      G   /usr/lib/xorg/Xorg                  4MiB |
|    7   N/A  N/A      1396      G   /usr/lib/xorg/Xorg                  4MiB |
+-----------------------------------------------------------------------------+
```

### InfiniBand Driver

On Ubuntu 20.04

```shell
sudo apt-get install -y automake dh-make git libcap2 libnuma-dev libtool make pkg-config udev curl librdmacm-dev rdma-core \
    libgfortran5 bison chrpath flex graphviz gfortran tk dpatch quilt swig tcl ibverbs-utils
```

Check install

```shell
ibv_devinfo
```

```shell
hca_id: mlx5_0
        transport:                      InfiniBand (0)
        fw_ver:                         16.28.4000
        node_guid:                      0015:5dff:fe33:ff2c
        sys_image_guid:                 0c42:a103:00b3:2f68
        vendor_id:                      0x02c9
        vendor_part_id:                 4120
        hw_ver:                         0x0
        board_id:                       MT_0000000010
        phys_port_cnt:                  1
                port:   1
                        state:                  PORT_ACTIVE (4)
                        max_mtu:                4096 (5)
                        active_mtu:             4096 (5)
                        sm_lid:                 7
                        port_lid:               115
                        port_lmc:               0x00
                        link_layer:             InfiniBand

hca_id: rdmaP36305p0s2
        transport:                      InfiniBand (0)
        fw_ver:                         2.43.7008
        node_guid:                      6045:bdff:feed:8445
        sys_image_guid:                 043f:7203:0003:d583
        vendor_id:                      0x02c9
        vendor_part_id:                 4100
        hw_ver:                         0x0
        board_id:                       MT_1090111019
        phys_port_cnt:                  1
                port:   1
                        state:                  PORT_ACTIVE (4)
                        max_mtu:                4096 (5)
                        active_mtu:             1024 (3)
                        sm_lid:                 0
                        port_lid:               0
                        port_lmc:               0x00
                        link_layer:             Ethernet
```

#### Enable IPoIB

```shell
sudo sed -i -e 's/# OS.EnableRDMA=y/OS.EnableRDMA=y/g' /etc/waagent.conf
```

Reboot and reconnect.

```shell
sudo reboot
```

#### Check IB

```shell
ip addr show
```

```shell
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 60:45:bd:a7:42:cc brd ff:ff:ff:ff:ff:ff
    inet 10.6.0.5/24 brd 10.6.0.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::6245:bdff:fea7:42cc/64 scope link
       valid_lft forever preferred_lft forever
3: eth1: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether 00:15:5d:33:ff:16 brd ff:ff:ff:ff:ff:ff
4: enP44906s1: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc mq master eth0 state UP group default qlen 1000
    link/ether 60:45:bd:a7:42:cc brd ff:ff:ff:ff:ff:ff
    altname enP44906p0s2
5: ibP59423s2: <BROADCAST,MULTICAST> mtu 4092 qdisc noop state DOWN group default qlen 256
    link/infiniband 00:00:09:27:fe:80:00:00:00:00:00:00:00:15:5d:ff:fd:33:ff:16 brd 00:ff:ff:ff:ff:12:40:1b:80:1d:00:00:00:00:00:00:ff:ff:ff:ff
    altname ibP59423p0s2
```

```shell
nvidia-smi topo -m
```

```shell
        GPU0  GPU1  GPU2  GPU3  GPU4  GPU5  GPU6  GPU7  mlx5_0  CPU Affinity  NUMA Affinity
GPU0    X     NV2   NV1   NV2   NODE  NODE  NV1   NODE  NODE    0-19          0
GPU1    NV2   X     NV2   NV1   NODE  NODE  NODE  NV1   NODE    0-19          0
GPU2    NV1   NV2   X     NV1   NV2   NODE  NODE  NODE  NODE    0-19          0
GPU3    NV2   NV1   NV1   X     NODE  NV2   NODE  NODE  NODE    0-19          0
GPU4    NODE  NODE  NV2   NODE  X     NV1   NV1   NV2   NODE    0-19          0
GPU5    NODE  NODE  NODE  NV2   NV1   X     NV2   NV1   NODE    0-19          0
GPU6    NV1   NODE  NODE  NODE  NV1   NV2   X     NV2   NODE    0-19          0
GPU7    NODE  NV1   NODE  NODE  NV2   NV1   NV2   X     NODE    0-19          0
mlx5_0  NODE  NODE  NODE  NODE  NODE  NODE  NODE  NODE  X

Legend:

  X    = Self
  SYS  = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI)
  NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node
  PHB  = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU)
  PXB  = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge)
  PIX  = Connection traversing at most a single PCIe bridge
  NV#  = Connection traversing a bonded set of # NVLinks

```

### Install UCX-Py and tools

```shell
wget https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh
bash Mambaforge-Linux-x86_64.sh
```

Accept the default and allow conda init to run. Then start a new shell.

Create a conda environment (see [UCX-Py](https://ucx-py.readthedocs.io/en/latest/install.html) docs)

```shell
mamba create -n ucxpy {{ rapids_conda_channels }} {{ rapids_conda_packages }} ipython ucx-proc=*=gpu ucx ucx-py dask distributed numpy cupy pytest pynvml -y
mamba activate ucxpy
```

Clone UCX-Py repo locally

```shell
git clone https://github.com/rapidsai/ucx-py.git
cd ucx-py
```

### Run Tests

Start by running the UCX-Py test suite, from within the `ucx-py` repo:

```shell
pytest -vs tests/
pytest -vs ucp/_libs/tests/
```

Now check to see if InfiniBand works, for that you can run some of the benchmarks that we include in UCX-Py, for example:

```shell
# cd out of the ucx-py directory
cd ..
# Let UCX pick the best transport (expecting NVLink when available,
# otherwise InfiniBand, or TCP in worst case) on devices 0 and 1
python -m ucp.benchmarks.send_recv --server-dev 0 --client-dev 1 -o rmm --reuse-alloc -n 128MiB

# Force TCP-only on devices 0 and 1
UCX_TLS=tcp,cuda_copy python -m ucp.benchmarks.send_recv --server-dev 0 --client-dev 1 -o rmm --reuse-alloc -n 128MiB
```

We expect the first case above to have much higher bandwidth than the second. If you happen to have both
NVLink and InfiniBand connectivity, then you may limit to the specific transport by specifying `UCX_TLS`, e.g.:

```shell
# NVLink (if available) or TCP
UCX_TLS=tcp,cuda_copy,cuda_ipc

# InfiniBand (if available) or TCP
UCX_TLS=tcp,cuda_copy,rc

```

## Run Benchmarks

Finally, let's run the [merge benchmark](https://github.com/rapidsai/dask-cuda/blob/HEAD/dask_cuda/benchmarks/local_cudf_merge.py) from `dask-cuda`.

This benchmark uses Dask to perform a merge of two dataframes that are distributed across all the available GPUs on your
VM. Merges are a challenging benchmark in a distributed setting since they require communication-intensive shuffle
operations of the participating dataframes
(see the [Dask documentation](https://docs.dask.org/en/stable/dataframe-best-practices.html#avoid-full-data-shuffling)
for more on this type of operation). To perform the merge, each dataframe is shuffled such that rows with the same join
key appear on the same GPU. This results in an [all-to-all](<https://en.wikipedia.org/wiki/All-to-all_(parallel_pattern)>)
communication pattern which requires a lot of communication between the GPUs. As a result, network
performance will be very important for the throughput of the benchmark.

Below we are running for devices 0 through 7 (inclusive), you will want to adjust that for the number of devices available on your VM, the default
is to run on GPU 0 only. Additionally, `--chunk-size 100_000_000` is a safe value for 32GB GPUs, you may
adjust that proportional to the size of the GPU you have (it scales linearly, so `50_000_000` should
be good for 16GB or `150_000_000` for 48GB).

```shell
# Default Dask TCP communication protocol
python -m dask_cuda.benchmarks.local_cudf_merge --devs 0,1,2,3,4,5,6,7 --chunk-size 100_000_000 --no-show-p2p-bandwidth
```

```shell
Merge benchmark
--------------------------------------------------------------------------------
Backend                   | dask
Merge type                | gpu
Rows-per-chunk            | 100000000
Base-chunks               | 8
Other-chunks              | 8
Broadcast                 | default
Protocol                  | tcp
Device(s)                 | 0,1,2,3,4,5,6,7
RMM Pool                  | True
Frac-match                | 0.3
Worker thread(s)          | 1
Data processed            | 23.84 GiB
Number of workers         | 8
================================================================================
Wall clock                | Throughput
--------------------------------------------------------------------------------
48.51 s                   | 503.25 MiB/s
47.85 s                   | 510.23 MiB/s
41.20 s                   | 592.57 MiB/s
================================================================================
Throughput                | 532.43 MiB/s +/- 22.13 MiB/s
Bandwidth                 | 44.76 MiB/s +/- 0.93 MiB/s
Wall clock                | 45.85 s +/- 3.30 s
```

```shell
# UCX protocol
python -m dask_cuda.benchmarks.local_cudf_merge --devs 0,1,2,3,4,5,6,7 --chunk-size 100_000_000 --protocol ucx --no-show-p2p-bandwidth
```

```shell
Merge benchmark
--------------------------------------------------------------------------------
Backend                   | dask
Merge type                | gpu
Rows-per-chunk            | 100000000
Base-chunks               | 8
Other-chunks              | 8
Broadcast                 | default
Protocol                  | ucx
Device(s)                 | 0,1,2,3,4,5,6,7
RMM Pool                  | True
Frac-match                | 0.3
TCP                       | None
InfiniBand                | None
NVLink                    | None
Worker thread(s)          | 1
Data processed            | 23.84 GiB
Number of workers         | 8
================================================================================
Wall clock                | Throughput
--------------------------------------------------------------------------------
9.57 s                    | 2.49 GiB/s
6.01 s                    | 3.96 GiB/s
9.80 s                    | 2.43 GiB/s
================================================================================
Throughput                | 2.82 GiB/s +/- 341.13 MiB/s
Bandwidth                 | 159.89 MiB/s +/- 8.96 MiB/s
Wall clock                | 8.46 s +/- 1.73 s
```

```{relatedexamples}

```
