# Azure Machine Learning (Azure ML)

RAPIDS can be deployed at scale using [Azure Machine Learning Service](https://learn.microsoft.com/en-us/azure/machine-learning/overview-what-is-azure-machine-learning) and easily scales up to any size needed. You can configure your environment on a local computer, Azure Machine Learning notebook service via compute instance or cluster.

## Pre-requisites

Use existing or create new Azure Machine Learning workspace through the [Azure portal](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-workspace?tabs=azure-portal#create-a-workspace), [Azure ML Python SDK](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-workspace?tabs=python#create-a-workspace), [Azure CLI](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-workspace-cli?tabs=createnewresources) or [Azure Resource Manager templates](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-create-workspace-template?tabs=azcli).

Follow these steps to get started:

**1. Create.** Create your Azure Resource Group.

**2. Workspace.** Within the Resource Group, create an Azure Machine Learning service Workspace.

**3. Config.** Within the Workspace, download the `config.json` file and verify that `subscription_id`, `resource_group`, and `workspace_name` are set correctly for your environment. You will load the details from this config file to initialize a workspace object for running ML training jobs from within your notebook.

**4. Quota.** Within your Workspace, check your Usage + Quota to ensure you have enough quota within your region to launch your desired cluster size.

## Azure ML Compute instance

Azure's [ML Compute instances](https://learn.microsoft.com/en-us/azure/machine-learning/concept-compute-instance) are a fully managed and secure development environment that can also serve as compute target for ML training and inferencing purposes. It comes with integrated Jupyter notebook server, JupyterLab, AzureML Python SDK and other tools.

### Select your instance

Sign in to [Azure Machine Learning Studio](https://ml.azure.com/) and navigate to your workspace. On the left side, select **Compute** > **+ New** and choose a [RAPIDS compatible GPU](https://medium.com/dropout-analytics/which-gpus-work-with-rapids-ai-f562ef29c75f) (NVIDIA Pascal or greater with compute capability 6.0+) as the SageMaker Notebook instance type (e.g., `Standard_NC12s_v3`)

![Screenshot of the create new notebook screen with a gpu-instance selected](../../images/azureml-create-notebook-instance.png)

### Provision RAPIDS setup script

Create a new "startup script" (via the 'Advanced Settings' dropdown). You can upload the script from your `Notebooks` files or local computer.
Optional to enable SSH access to your compute (if needed)

![Screenshot of the provision setup script screen](../../images/azureml-provision-setup-script.png)

See the [Azure ML documentation](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-customize-compute-instance) for more details on how to create the setup script but it should resemble:

```bash
#!/bin/bash

sudo -u azureuser -i <<'EOF'

conda create -y -n rapids {{ rapids_conda_channels }} {{ rapids_conda_packages }} ipykernel
conda activate rapids

# optionally install AutoGluon for AutoML GPU demo
# python -m pip install --pre autogluon

python -m ipykernel install --user --name rapids
echo "kernel install completed"
EOF
```

Launch the instance.

### Select the RAPIDS environment

Once your Notebook Instance is `Running` select "JupyterLab"

Then in JupyterLab select the `rapids` kernel when working with a new notebook

```{relatedexamples}

```
