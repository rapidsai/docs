# RAPIDS on Databricks

## 0. Pre-requisites

1. Your Databricks workspace must have Databricks Container Services [enabled](https://docs.databricks.com/administration-guide/clusters/container-services.html).

2. Your machine must be running a recent Docker daemon (one that is tested and works with Version 18.03.0-ce) and the `docker` command must be available on your PATH:

3. It is recommended to build from a [Databricks base image](https://hub.docker.com/u/databricksruntime). But you can also build your Docker base from scratch. The Docker image must meet these [requirements](https://docs.databricks.com/clusters/custom-containers.html#option-2-build-your-own-docker-base)

## 1. Build custom RAPIDS container

```console
ARG RAPIDS_IMAGE

FROM $RAPIDS_IMAGE as rapids

RUN conda list -n rapids --explicit > /rapids/rapids-spec.txt

FROM databricksruntime/gpu-conda:cuda11

COPY --from=rapids /rapids/rapids-spec.txt /tmp/spec.txt

RUN conda create --name rapids --file /tmp/spec.txt && \
    rm -f /tmp/spec.txt
```

```console
$ docker build --tag <username>/rapids_databricks:latest --build-arg RAPIDS_IMAGE={{ rapids_container }} ./docker
```

Push this image to a Docker registry (DockerHub, Amazon ECR or Azure ACR).

## 2. Configure and create GPU-enabled cluster

1. Compute > Create compute > Name your cluster > Select `Multi` or `Single` Node
2. Select a Standard Databricks runtime.
   - **Note** Databricks ML Runtime does not support Databricks Container Services
3. Under **Advanced Options**, in the the **Docker** tab select **"Use your own Docker container"**
   - In the Docker Image URL field, enter the image that you created above
   - Select the authentication type
4. Select a GPU enabled worker and driver type
   - Selected GPU must be Pascal generation or greater (eg: `g4dn.xlarge`)
5. Create and launch your cluster

## 3. Test Rapids

For more details on Integrating Databricks Jobs with MLFlow and RAPIDS, check out this [blog post](https://medium.com/rapids-ai/managing-and-deploying-high-performance-machine-learning-models-on-gpus-with-rapids-and-mlflow-753b6fcaf75a).
