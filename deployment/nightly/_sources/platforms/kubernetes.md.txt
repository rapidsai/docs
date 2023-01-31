# Kubernetes

RAPIDS integrates with Kubernetes in many ways depending on your use case.

## Interactive Notebook

For single-user interactive sessions you can run the [RAPIDS docker image](/tools/rapids-docker) which contains a conda environment with the RAPIDS libraries and Jupyter for interactive use.

You can run this directly on Kubernetes as a `Pod` and expose Jupyter via a `Service`. For example:

```yaml
# rapids-notebook.yaml
apiVersion: v1
kind: Service
metadata:
  name: rapids-notebook
  labels:
    app: rapids-notebook
spec:
  type: NodePort
  ports:
    - port: 8888
      name: http
      targetPort: 8888
      nodePort: 30002
  selector:
    app: rapids-notebook
---
apiVersion: v1
kind: Pod
metadata:
  name: rapids-notebook
  labels:
    app: rapids-notebook
spec:
  securityContext:
    fsGroup: 0
  containers:
    - name: rapids-notebook
      image: rapidsai/rapidsai-core:22.06-cuda11.5-runtime-ubuntu20.04-py3.9
      resources:
        limits:
          nvidia.com/gpu: 1
      ports:
        - containerPort: 8888
          name: notebook
```

```console
$ kubectl apply -f rapids-notebook.yaml
```

This makes Jupyter accessible on port `30002` of your Kubernetes nodes via `NodePort` service. Alternatvely you could use a `LoadBalancer` service type [if you have one configured](https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/) or a `ClusterIP` and use `kubectl` to port forward the port locally and access it that way.

```console
$ kubectl port-forward service/rapids-notebook 8888
```

Then you can open port `8888` in your browser to access Jupyter and use RAPIDS.

```{figure} /images/kubernetes-jupyter.png
---
alt: Screenshot of the RAPIDS container running Jupyter showing the nvidia-smi command with a GPU listed
---
```

## Helm Chart

Individual users can also install the [Dask Helm Chart](https://helm.dask.org) which provides a `Pod` running Jupyter alongside a Dask cluster consisting of pods running the Dask scheduler and worker components. You can customize this helm chart to run the RAPIDS container images as both the notebook server and Dask cluster components so that everything can benefit from GPU acceleration.

Find out more on the [Dask Helm Chart page](/tools/kubernetes/dask-helm-chart).

## Dask Operator

[Dask has an operator](https://kubernetes.dask.org/en/latest/operator.html) that empowers users to create Dask clusters as native Kubernetes resources. This is useful for creating, scaling and removing Dask clusters dynamically and in a flexible way. Usually this is used in conjunction with an interactive session such as the [interactive notebook](#interactive-notebook) example above or from another service like [KubeFlow Notebooks](/platforms/kubeflow). By dynamically launching Dask clusters configured to use RAPIDS on Kubernetes user's can burst beyond their notebook session to many GPUs spreak across many nodes.

Find out more on the [Dask Operator page](/tools/kubernetes/dask-operator).

## Dask Kubernetes (classic)

```{warning}
Unless you are already using the [classic Dask Kubernetes integration](https://kubernetes.dask.org/en/latest/kubecluster.html) we recommend using the [Dask Operator](#dask-operator) instead.
```

Dask has an older tool for dynamically launching Dask clusters on Kubernetes that does not use an operator. It is possible to configure this to run RAPIDS too but it is being phased out in favour of the operator.

Find out more on the [Dask Kubernetes page](/tools/kubernetes/dask-kubernetes).

## Dask Gateway

Some organisations may want to provide Dask cluster provisioning as a central service where users are abstracted from the underlying platform like Kubernetes. This can be useful for reducing user permissions, limiting resources that users can consume and exposing things in a centralised way. For this you can deploy Dask Gateway which provides a server that users interact with programatically and in turn launches Dask clusters on Kubernetes and proxies the connection back to the user.

Users can configure what they want their Dask cluster to look like so it is possible to utilize GPUs and RAPIDS for an accelerated cluster.

Find out more on the [Dask Gateway page](/tools/kubernetes/dask-gateway).

## KubeFlow

If you are using KubeFlow you can integrate RAPIDS right away by using the RAPIDS container images within notebooks and pipelines and by using the Dask Operator to launch GPU accelerated Dask clusters.

Find out more on the [KubeFlow page](/platforms/kubeflow).

```{relatedexamples}

```
