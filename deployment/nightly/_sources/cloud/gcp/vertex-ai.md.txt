# Vertex AI

RAPIDS can be deployed on Vertex AI.

## Managed Notebooks

For new, user-managed notebooks, it is recommended to use a RAPIDS docker image to access the latest RAPIDS software.

**1. Prepare RAPIDS Docker Image.** Before configuring a new notebook, the [RAPIDS Docker image](#rapids-docker) will need to be built to expose port 8080 to be used as a notebook service.

```dockerfile
ARG RAPIDS_IMAGE
FROM $RAPIDS_IMAGE as rapids
EXPOSE 8080

ENTRYPOINT [ "jupyter-lab", "--allow-root", "--ip=0.0.0.0", "--port=8080", "--no-browser", "--NotebookApp.token=''", "--NotebookApp.allow_origin='*'" ]
```

Once you have built this image, it needs to be pushed to [Google Container Registry](https://cloud.google.com/container-registry/docs/pushing-and-pulling) for Vertex AI.

**2. Create a New Notebook.** From the Google Cloud UI, nagivate to `Vertex AI` -> `Dashboard` and select `+ CREATE NOTEBOOK INSTANCE`. Under the `Environment` section, specify `Custom container`, and in the section below, select the `gcr.io` path to your pushed RAPIDS Docker image. After customizing other aspects of the machine, click `CREATE`

**3. TEST RAPIDS** Once the managed notebook is fully configured, you can click `OPEN JUPYTERLAB` to navigate to another tab running JupyterLab to use the latest version of RAPIDS with Vertex AI.
