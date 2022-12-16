# Tools

## Packages

`````{grid} 1 2 2 3
:gutter: 2 2 2 2

````{grid-item-card}
:link: rapids-docker
:link-type: doc
Container Images
^^^
Container images containing the RAPIDS software environment.
````

`````

## Kubernetes

`````{grid} 1 2 2 3
:gutter: 2 2 2 2

````{grid-item-card}
:link: kubernetes/dask-operator
:link-type: doc
Dask Kubernetes Operator (Classic)
^^^
Launch RAPIDS containers and clusters as native Kubernetes resources with the Dask Operator.
````

````{grid-item-card}
:link: kubernetes/dask-kubernetes
:link-type: doc
Dask Kubernetes (Classic)
^^^
Spawn RAPIDS Pods on Kubernetes with `dask-kubernetes` (deprecated).
````

````{grid-item-card}
:link: kubernetes/dask-helm-chart
:link-type: doc
Dask Helm Chart
^^^
Install a single user notebook and cluster on Kubernetes with the Dask Helm Chart.
````

`````

```{toctree}
:hidden:
:maxdepth: 2
:caption: Tools

rapids-docker
kubernetes/dask-kubernetes
kubernetes/dask-operator
kubernetes/dask-helm-chart
```
