# Dask Operator

Many libraries in RAPIDS can leverage Dask to scale out computation onto multiple GPUs and multiple nodes.
[Dask has an operator for Kubernetes](https://kubernetes.dask.org/en/latest/operator.html) which allows you to launch Dask clusters as native Kubernetes resources.

With the operator and associated Custom Resource Definitions (CRDs)
you can create `DaskCluster`, `DaskWorkerGroup` and `DaskJob` resources that describe your Dask components and the operator will
create the appropriate Kubernetes resources like `Pods` and `Services` to launch the cluster.

```{mermaid}
graph TD
    DaskJob(DaskJob)
    DaskCluster(DaskCluster)
    SchedulerService(Scheduler Service)
    SchedulerPod(Scheduler Pod)
    DaskWorkerGroup(DaskWorkerGroup)
    WorkerPodA(Worker Pod A)
    WorkerPodB(Worker Pod B)
    WorkerPodC(Worker Pod C)
    JobPod(Job Runner Pod)

    DaskJob --> DaskCluster
    DaskJob --> JobPod
    DaskCluster --> SchedulerService
    SchedulerService --> SchedulerPod
    DaskCluster --> DaskWorkerGroup
    DaskWorkerGroup --> WorkerPodA
    DaskWorkerGroup --> WorkerPodB
    DaskWorkerGroup --> WorkerPodC

    classDef dask stroke:#FDA061,stroke-width:4px
    classDef dashed stroke-dasharray: 5 5
    class DaskJob dask
    class DaskCluster dask
    class DaskWorkerGroup dask
    class SchedulerService dashed
    class SchedulerPod dashed
    class WorkerPodA dashed
    class WorkerPodB dashed
    class WorkerPodC dashed
    class JobPod dashed
```

## Installation

Your Kubernetes cluster must have GPU nodes and have [up to date NVIDIA drivers installed](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/getting-started.html).

To install the Dask operator follow the [instructions in the Dask documentation](https://kubernetes.dask.org/en/latest/operator_installation.html).

## Configuring a RAPIDS `DaskCluster`

To configure the `DaskCluster` resource to run RAPIDS you need to set a few things:

- The container image must contain RAPIDS, the [official RAPIDS container images](/tools/rapids-docker) are a good choice for this.
- The Dask workers must be configured with one or more NVIDIA GPU resources.
- The worker command must be set to `dask-cuda-worker`.

## Example using `kubectl`

Here is an example resource manifest for launching a RAPIDS Dask cluster.

```yaml
# rapids-dask-cluster.yaml
apiVersion: kubernetes.dask.org/v1
kind: DaskCluster
metadata:
  name: rapids-dask-cluster
  labels:
    dask.org/cluster-name: rapids-dask-cluster
spec:
  worker:
    replicas: 2
    spec:
      containers:
        - name: worker
          image: "rapidsai/rapidsai-core:22.06-cuda11.5-runtime-ubuntu20.04-py3.9"
          imagePullPolicy: "IfNotPresent"
          env:
            - name: DISABLE_JUPYTER
              value: "true"
          args:
            - dask-cuda-worker
            - --name
            - $(DASK_WORKER_NAME)
          resources:
            limits:
              nvidia.com/gpu: "1"
  scheduler:
    spec:
      containers:
        - name: scheduler
          image: "rapidsai/rapidsai-core:22.06-cuda11.5-runtime-ubuntu20.04-py3.9"
          imagePullPolicy: "IfNotPresent"
          env:
            - name: DISABLE_JUPYTER
              value: "true"
          args:
            - dask-scheduler
          ports:
            - name: tcp-comm
              containerPort: 8786
              protocol: TCP
            - name: http-dashboard
              containerPort: 8787
              protocol: TCP
          readinessProbe:
            httpGet:
              port: http-dashboard
              path: /health
            initialDelaySeconds: 5
            periodSeconds: 10
          livenessProbe:
            httpGet:
              port: http-dashboard
              path: /health
            initialDelaySeconds: 15
            periodSeconds: 20
    service:
      type: ClusterIP
      selector:
        dask.org/cluster-name: rapids-dask-cluster
        dask.org/component: scheduler
      ports:
        - name: tcp-comm
          protocol: TCP
          port: 8786
          targetPort: "tcp-comm"
        - name: http-dashboard
          protocol: TCP
          port: 8787
          targetPort: "http-dashboard"
```

You can create this cluster with `kubectl`.

```console
$ kubectl apply -f rapids-dask-cluster.yaml
```

### Manifest breakdown

Let's break this manifest down section by section.

#### Metadata

At the top we see the `DaskCluster` resource type and general metadata.

```yaml
apiVersion: kubernetes.dask.org/v1
kind: DaskCluster
metadata:
  name: rapids-dask-cluster
  labels:
    dask.org/cluster-name: rapids-dask-cluster
spec:
  worker:
    # ...
  scheduler:
    # ...
```

Then inside the `spec` we have `worker` and `scheduler` sections.

#### Worker

The worker contains a `replicas` option to set how many workers you need and a `spec` that describes what each worker pod should look like.
The spec is a nested [`Pod` spec](https://kubernetes.io/docs/concepts/workloads/pods/) that the operator will use when creating new `Pod` resources.

```yaml
# ...
spec:
  worker:
    replicas: 2
    spec:
      containers:
        - name: worker
          image: "rapidsai/rapidsai-core:22.06-cuda11.5-runtime-ubuntu20.04-py3.9"
          imagePullPolicy: "IfNotPresent"
          env:
            - name: DISABLE_JUPYTER
              value: "true"
          args:
            - dask-cuda-worker
            - --name
            - $(DASK_WORKER_NAME)
          resources:
            limits:
              nvidia.com/gpu: "1"
  scheduler:
    # ...
```

Inside our pod spec we are configuring one container that uses the `rapidsai/rapidsai-core` container image.
It also sets the `args` to start the `dask-cuda-worker` and configures one NVIDIA GPU.

```{note}
We also have to set the environment variable `DISABLE_JUPYTER=true` because the RAPIDS container images will run Jupyter instead of our supplied command.
```

#### Scheduler

Next we have a `scheduler` section that also contains a `spec` for the scheduler pod and a `service` which will be used by the operator to create a `Service` resource to expose the scheduler.

```yaml
# ...
spec:
  worker:
    # ...
  scheduler:
    spec:
      containers:
        - name: scheduler
          image: "rapidsai/rapidsai-core:22.06-cuda11.5-runtime-ubuntu20.04-py3.9"
          imagePullPolicy: "IfNotPresent"
          env:
            - name: DISABLE_JUPYTER
              value: "true"
          args:
            - dask-scheduler
          ports:
            - name: tcp-comm
              containerPort: 8786
              protocol: TCP
            - name: http-dashboard
              containerPort: 8787
              protocol: TCP
          readinessProbe:
            httpGet:
              port: http-dashboard
              path: /health
            initialDelaySeconds: 5
            periodSeconds: 10
          livenessProbe:
            httpGet:
              port: http-dashboard
              path: /health
            initialDelaySeconds: 15
            periodSeconds: 20
    service:
      # ...
```

For the scheduler pod we are also setting the `rapidsai/rapidsai-core` container image, mainly to ensure our Dask versions match between
the scheduler and workers. We also disable Jupyter and ensure that the `dask-scheduler` command is configured.

Then we configure both the Dask communication port on `8786` and the Dask dashboard on `8787` and add some probes so that Kubernetes can monitor
the health of the scheduler.

```{note}
The ports must have the `tcp-` and `http-` prefixes if your Kubernetes cluster uses [Istio](https://istio.io/) to ensure the [Envoy proxy](https://www.envoyproxy.io/) doesn't mangle the traffic.
```

Then we configure the `Service`.

```yaml
# ...
spec:
  worker:
    # ...
  scheduler:
    spec:
      # ...
    service:
      type: ClusterIP
      selector:
        dask.org/cluster-name: rapids-dask-cluster
        dask.org/component: scheduler
      ports:
        - name: tcp-comm
          protocol: TCP
          port: 8786
          targetPort: "tcp-comm"
        - name: http-dashboard
          protocol: TCP
          port: 8787
          targetPort: "http-dashboard"
```

This example shows using a `ClusterIP` service which will not expose the Dask cluster outside of Kubernetes. If you prefer you could set this to
[`LoadBalancer`](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer) or [`NodePort`](https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport) to make this externally accessible.

It has a `selector` that matches the scheduler pod and the same ports configured.

### Accessing your Dask cluster

Once you have created your `DaskCluster` resource we can use `kubectl` to check the status of all the other resources it created for us.

```console
$ kubectl get all -l dask.org/cluster-name=rapids-dask-cluster
NAME                                                             READY   STATUS    RESTARTS   AGE
pod/rapids-dask-cluster-default-worker-group-worker-0c202b85fd   1/1     Running   0          4m13s
pod/rapids-dask-cluster-default-worker-group-worker-ff5d376714   1/1     Running   0          4m13s
pod/rapids-dask-cluster-scheduler                                1/1     Running   0          4m14s

NAME                                  TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)             AGE
service/rapids-dask-cluster-service   ClusterIP   10.96.223.217   <none>        8786/TCP,8787/TCP   4m13s
```

Here you can see our scheduler pod and two worker pods along with the scheduler service.

If you have a Python session running within the Kubernetes cluster (like the [example one on the Kubernetes page](/platforms/kubernetes)) you should be able
to connect a Dask distributed client directly.

```python
from dask.distributed import Client

client = Client("rapids-dask-cluster-service:8786")
```

Alternatively if you are outside of the Kubernetes cluster you can change the `Service` to use [`LoadBalancer`](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer) or [`NodePort`](https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport) or use `kubectl` to port forward the connection locally.

```console
$ kubectl port-forward svc/rapids-dask-cluster-service 8786:8786
Forwarding from 127.0.0.1:8786 -> 8786
```

```python
from dask.distributed import Client

client = Client("localhost:8786")
```

## Example using `KubeCluster`

In additon to creating clusters via `kubectl` you can also do so from Python with {class}`dask_kubernetes.experimental.KubeCluster`. This class implements the Dask Cluster Manager interface and under the hood creates and manages the `DaskCluster` resource for you.

```python
from dask_kubernetes.experimental import KubeCluster

cluster = KubeCluster(
    name="rapids-dask",
    image="rapidsai/rapidsai-core:22.06-cuda11.5-runtime-ubuntu20.04-py3.9",
    n_workers=3,
    resources={"limits": {"nvidia.com/gpu": "1"}},
    env={"DISABLE_JUPYTER": "true"},
    worker_command="dask-cuda-worker",
)
```

If we check with `kubectl` we can see the above Python generated the same `DaskCluster` resource as the `kubectl` example above.

```console
$ kubectl get daskclusters
NAME                  AGE
rapids-dask-cluster   3m28s

$ kubectl get all -l dask.org/cluster-name=rapids-dask-cluster
NAME                                                             READY   STATUS    RESTARTS   AGE
pod/rapids-dask-cluster-default-worker-group-worker-07d674589a   1/1     Running   0          3m30s
pod/rapids-dask-cluster-default-worker-group-worker-a55ed88265   1/1     Running   0          3m30s
pod/rapids-dask-cluster-default-worker-group-worker-df785ab050   1/1     Running   0          3m30s
pod/rapids-dask-cluster-scheduler                                1/1     Running   0          3m30s

NAME                                  TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)             AGE
service/rapids-dask-cluster-service   ClusterIP   10.96.200.202   <none>        8786/TCP,8787/TCP   3m30s
```

With this cluster object in Python we can also connect a client to it directly without needing to know the address as Dask will discover that for us. It also automatically sets up port forwarding if you are outside of the Kubernetes cluster.

```python
from dask.distributed import Client

client = Client(cluster)
```

This object can also be used to scale the workers up and down.

```python
cluster.scale(5)
```

And to manually close the cluster.

```python
cluster.close()
```

```{note}
By default the `KubeCluster` command registers an exit hook so when the Python process exits the cluster is deleted automatically. You can disable this by setting `KubeCluster(..., shutdown_on_close=False)` when launching the cluster.

This is useful if you have a multi-stage pipeline made up of multiple Python processes and you want your Dask cluster to persist between them.

You can also connect a `KubeCluster` object to your existing cluster with `cluster = KubeCluster.from_name(name="rapids-dask")` if you wish to use the cluster or manually call `cluster.close()` in the future.
```

```{relatedexamples}

```
