# Azure Machine Learning (Azure ML)

```{warning}
This is a legacy page and may contain outdated information. We are working hard to update our documentation with the latest and greatest information, thank you for bearing with us.
```

RAPIDS can be deployed at scale using Azure Machine Learning Service and easily scales up to any size needed. We have written a **[detailed guide](https://medium.com/rapids-ai/rapids-on-microsoft-azure-machine-learning-b51d5d5fde2b)** with **[helper scripts](https://github.com/rapidsai/cloud-ml-examples/tree/main/azure)** to get everything deployed, but the high level procedure is:

**1. Create.** Create your Azure Resource Group.

**2. Workspace.** Within the Resource Group, create an Azure Machine Learning service Workspace.

**3. Config.** Within the Workspace, download the `config.json` file and verify that subscription_id, resource_group, and workspace_name are set correctly for your environment.

**4. Quota.** Within your Workspace, check your Usage + Quota to ensure you have enough quota to launch your desired cluster size.

**5. Clone.** From your local machine, clone the RAPIDS demonstration code and helper scripts.

**6\. Run Utility.** Run the RAPIDS helper utility script to initialize the Azure Machine Learning service Workspace:

```console
$ ./start_azureml.py\
 --config=[CONFIG_PATH]\
 --vm_size=[VM_SIZE]\
 --node_count=[NUM_NODES]

```

[CONFIG_PATH] = the path to the config file you downloaded in step three.

**7. Start.** Open your browser to `http://localhost:8888` and get started!

See **[the guide](https://medium.com/rapids-ai/rapids-on-microsoft-azure-machine-learning-b51d5d5fde2b#fee3)** or **[GitHub](https://github.com/rapidsai/cloud-ml-examples/tree/main/azure)** for more details.
