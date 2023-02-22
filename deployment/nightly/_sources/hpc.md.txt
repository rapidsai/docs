# HPC

RAPIDS works extremely well in traditional HPC (High Performance Computing) environments where GPUs are often co-located with accelerated networking hardware such as InfiniBand. Deploying on HPC often means using queue management systems such as SLURM, LSF, PBS, etc.

## SLURM

If you are unfamiliar with SLURM or need a refresher, we recommend the [quickstart guide](https://slurm.schedmd.com/quickstart.html).
Depending on how your nodes are configured, additional settings may be required such as defining the number of GPUs `(--gpus)` desired or the number of gpus per node `(--gpus-per-node)`.
In the following example, we assume each allocation runs on a DGX1 with access to all eight GPUs.

### Start Scheduler

First, start the scheduler with the following SLURM script. This and the following scripts can deployed with `salloc` for interactive usage or `sbatch` for batched run.

```bash
#!/usr/bin/env bash

#SBATCH -J dask-scheduler
#SBATCH -n 1
#SBATCH -t 00:10:00

module load cuda/11.0.3
CONDA_ROOT=/nfs-mount/user/miniconda3
source $CONDA_ROOT/etc/profile.d/conda.sh
conda activate rapids

LOCAL_DIRECTORY=/nfs-mount/dask-local-directory
mkdir $LOCAL_DIRECTORY
CUDA_VISIBLE_DEVICES=0 dask-scheduler \
    --protocol tcp \
    --scheduler-file "$LOCAL_DIRECTORY/dask-scheduler.json" &

dask-cuda-worker \
    --rmm-pool-size 14GB \
    --scheduler-file "$LOCAL_DIRECTORY/dask-scheduler.json"
```

Notice that we configure the scheduler to write a `scheduler-file` to a NFS accessible location. This file contains metadata about the scheduler and will
include the IP address and port for the scheduler. The file will serve as input to the workers informing them what address and port to connect.

The scheduler doesn't need the whole node to itself so we can also start a worker on this node to fill out the unused resources.

### Start Dask CUDA Workers

Next start the other [dask-cuda workers](https://dask-cuda.readthedocs.io/). Dask-CUDA extends the traditional Dask `Worker` class with specific options and enhancements for GPU environments. Unlike the scheduler and client, the workers script should be _scalable_ and allow the users to tune how many workers are created.
For example, we can scale the number of nodes to 3: `sbatch/salloc -N3 dask-cuda-worker.script` . In this case, because we have 8 GPUs per node and we have 3 nodes,
our job will have 24 workers.

```bash
#!/usr/bin/env bash

#SBATCH -J dask-cuda-workers
#SBATCH -t 00:10:00

module load cuda/11.0.3
CONDA_ROOT=/nfs-mount/miniconda3
source $CONDA_ROOT/etc/profile.d/conda.sh
conda activate rapids

LOCAL_DIRECTORY=/nfs-mount/dask-local-directory
mkdir $LOCAL_DIRECTORY
dask-cuda-worker \
    --rmm-pool-size 14GB \
    --scheduler-file "$LOCAL_DIRECTORY/dask-scheduler.json"
```

### cuDF Example Workflow

Lastly, we can now run a job on the established Dask Cluster.

```bash
#!/usr/bin/env bash

#SBATCH -J dask-client
#SBATCH -n 1
#SBATCH -t 00:10:00

module load cuda/11.0.3
CONDA_ROOT=/nfs-mount/miniconda3
source $CONDA_ROOT/etc/profile.d/conda.sh
conda activate rapids

LOCAL_DIRECTORY=/nfs-mount/dask-local-directory

cat <<EOF >>/tmp/dask-cudf-example.py
import cudf
import dask.dataframe as dd
from dask.distributed import Client

client = Client(scheduler_file="$LOCAL_DIRECTORY/dask-scheduler.json")
cdf = cudf.datasets.timeseries()

ddf = dd.from_pandas(cdf, npartitions=10)
res = ddf.groupby(['id', 'name']).agg(['mean', 'sum', 'count']).compute()
print(res)
EOF

python /tmp/dask-cudf-example.py
```

### Confirm Output

Putting the above together will result in the following output:

```raw
                      x                          y
                   mean        sum count      mean        sum count
id   name
1077 Laura     0.028305   1.868120    66 -0.098905  -6.527731    66
1026 Frank     0.001536   1.414839   921 -0.017223 -15.862306   921
1082 Patricia  0.072045   3.602228    50  0.081853   4.092667    50
1007 Wendy     0.009837  11.676199  1187  0.022978  27.275216  1187
976  Wendy    -0.003663  -3.267674   892  0.008262   7.369577   892
...                 ...        ...   ...       ...        ...   ...
912  Michael   0.012409   0.459119    37  0.002528   0.093520    37
1103 Ingrid   -0.132714  -1.327142    10  0.108364   1.083638    10
998  Tim       0.000587   0.747745  1273  0.001777   2.262094  1273
941  Yvonne    0.050258  11.358393   226  0.080584  18.212019   226
900  Michael  -0.134216  -1.073729     8  0.008701   0.069610     8

[6449 rows x 6 columns]
```

<br/><br/>
