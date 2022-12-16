# Azure VM Cluster (via Dask)

```{warning}
This is a legacy page and may contain outdated information. We are working hard to update our documentation with the latest and greatest information, thank you for bearing with us.
```

RAPIDS can be deployed at scale using Azure Machine Learning Service and easily scales up to any size needed. We have written a **[detailed guide](https://medium.com/rapids-ai/rapids-on-microsoft-azure-machine-learning-b51d5d5fde2b)** with **[helper scripts](https://github.com/rapidsai/cloud-ml-examples/tree/main/azure)** to get everything deployed, but the high level procedure is:

**1. Create.** Create your Azure Resource Group.

**2. Workspace.** Within the Resource Group, create an Azure Machine Learning service Workspace.

**3. Config.** Within the Workspace, download the config.json file and verify that subscription_id, resource_group, and workspace_name are set correctly for your environment.

**4. Quota.** Within your Workspace, check your Usage + Quota to ensure you have enough quota to launch your desired cluster size.

**5. Clone.** From your local machine, clone the RAPIDS demonstration code and helper scripts.

**6. Run Utility.** Run the RAPIDS helper utility script to initialize the Azure Machine Learning service Workspace:

```console
$ ./start_azureml.py\
 --config=[CONFIG_PATH]\
 --vm_size=[VM_SIZE]\
 --node_count=[NUM_NODES]

```

[CONFIG_PATH] = the path to the config file you downloaded in step three.

**7. Start.** Open your browser to `http://localhost:8888` and get started!

See **[the guide](https://medium.com/rapids-ai/rapids-on-microsoft-azure-machine-learning-b51d5d5fde2b#fee3)** or **[GitHub](https://github.com/rapidsai/cloud-ml-examples/tree/main/azure)** for more details.RAPIDS can be deployed on a Dask cluster on Azure ML Compute using dask-cloud provider.

**1. Install.** Install Azure tools (azure-cli).

**2. Install dask-cloudprovider:**

```console
$ pip install dask-cloudprovider

```

**3. Config.** Create your workspace config file -see **[Azure docs](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-configure-environment#workspace)** for details.

**4. Environment.** Setup your Azure ML core environment using the RAPIDS docker container:

```python
>>> from azureml.core import Environment
>>> # create the environment
>>> rapids_env = Environment('rapids_env')
>>> # create the environment inside a Docker container
>>> rapids_env.docker.enabled = True
>>> # specify docker steps as a string. Alternatively, load the string from a file
>>> dockerfile = """
>>> FROM [CONTAINER]:[TAG]
>>> RUN source activate rapids &&\
>>> pip install azureml-sdk &&\
>>> [ADDITIONAL_LIBRARIES]
>>> """
>>> # set base image to None since the image is defined by dockerfile
>>> rapids_env.docker.base_image = None
>>> rapids_env.docker.base_dockerfile = dockerfile
>>> # use rapids environment in the container
>>> rapids_env.python.user_managed_dependencies = True

```

[CONTAINER] = RAPIDS container to be used, for example, `rapidsai/rapidsai`\
[TAG] = Docker container tag.\
[ADDITIONAL_LIBRARIES] = Additional libraries required by the user can be installed by either using `conda` or `pip` install.

**5. Setup.** Setup your Azure ML Workspace using the config file created in the previous step:

```python
>>> from azureml.core import Workspace
>>> ws = Workspace.from_config()

```

**6. Create the AzureMLCluster:**

```python
>>> from dask_cloudprovider import AzureMLCluster
>>> cluster = AzureMLCluster(ws,
                             datastores=ws.datastores.values(),
                             environment_definition=rapids_env,
                             initial_node_count=[NUM_NODES])

```

[NUM_NODES] = Number of nodes to be used.

**7. Run Notebook.** In a Jupyter notebook, the cluster object will return a widget allowing you to scale up and containing links to the Jupyter Lab session running on the headnode and Dask dashboard, which are forwarded to local ports for you -unless running on a remote Compute Instance.
