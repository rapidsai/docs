# Vertex AI

RAPIDS can be deployed on [Vertex AI Workbench](https://cloud.google.com/vertex-ai-workbench).

For new, user-managed notebooks, it is recommended to use a RAPIDS docker image to access the latest RAPIDS software.

## Prepare RAPIDS Docker Image

Before configuring a new notebook, the [RAPIDS Docker image](#rapids-docker) will need to be built to expose port 8080 to be used as a notebook service.

```dockerfile
FROM rapidsai/rapidsai-core:22.12-cuda11.5-runtime-ubuntu20.04-py3.9
EXPOSE 8080

ENTRYPOINT ["jupyter-lab", "--allow-root", "--ip=0.0.0.0", "--port=8080", "--no-browser", "--NotebookApp.token=''", "--NotebookApp.allow_origin='*'"]
```

Once you have built this image, it needs to be pushed to [Google Container Registry](https://cloud.google.com/container-registry/docs/pushing-and-pulling) for Vertex AI to access.

```console
$ docker build -t gcr.io/<project>/<folder>/rapidsai-core:22.12-cuda11.5-runtime-ubuntu20.04-py3.9 .
$ docker push gcr.io/<project>/<folder>/rapidsai-core:22.12-cuda11.5-runtime-ubuntu20.04-py3.9
```

## Create a New Notebook

1. From the Google Cloud UI, navigate to [**Vertex AI**](https://console.cloud.google.com/vertex-ai) -> **Dashboard** and select **+ CREATE NOTEBOOK INSTANCE**.
2. Under the **Environment** section, specify **Custom container**, and in the section below, select the `gcr.io` path to your pushed RAPIDS Docker image.
3. Under **Machine Configuration** select an NVIDIA GPU.
4. Check the **Install NVIDIA GPU Driver** option.
5. After customizing any other aspects of the machine you wish, click **CREATE**.

## TEST RAPIDS

Once the managed notebook is fully configured, you can click **OPEN JUPYTERLAB** to navigate to another tab running JupyterLab to use the latest version of RAPIDS with Vertex AI.

For example we could import and use RAPIDS libraries like `cudf`.

```ipython
In [1]: import cudf
In [2]: df = cudf.datasets.timeseries()
In [3]: df.head()
Out[3]:
                       id     name         x         y
timestamp
2000-01-01 00:00:00  1020    Kevin  0.091536  0.664482
2000-01-01 00:00:01   974    Frank  0.683788 -0.467281
2000-01-01 00:00:02  1000  Charlie  0.419740 -0.796866
2000-01-01 00:00:03  1019    Edith  0.488411  0.731661
2000-01-01 00:00:04   998    Quinn  0.651381 -0.525398
```

```{relatedexamples}

```
