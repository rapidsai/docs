# SageMaker

RAPIDS can be used in a few ways with [AWS SageMaker](https://aws.amazon.com/sagemaker/).

## SageMaker Notebooks

[SageMaker Notebook Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html) can be augmented with a RAPIDS conda environment.

We can add a RAPIDS conda environment to the set of Jupyter ipython kernels available in our SageMaker notebook instance by installing in a [lifecycle configuration script](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html).

To get started head to SageMaker and create a [new SageMaker Notebook Instance](https://console.aws.amazon.com/sagemaker/home#/notebook-instances/create).

### Select your instance

Select a [RAPIDS compatible GPU](https://medium.com/dropout-analytics/which-gpus-work-with-rapids-ai-f562ef29c75f) (NVIDIA Pascal or greater with compute capability 6.0+) as the SageMaker Notebook instance type (e.g., `ml.p3.2xlarge`).

![Screenshot of the create new notebook screen with a ml.p3.2xlarge selected](../../images/sagemaker-create-notebook-instance.png)

### Create a RAPIDS lifecycle configuration

Create a new lifecycle configuration (via the 'Additional Options' dropdown).

![Screenshot of the create lifecycle configuration screen](../../images/sagemaker-create-lifecycle-configuration.png)

Give your configuration a name like `rapids` and paste the following script into the "start notebook" script.

```bash
#!/bin/bash

set -e

sudo -u ec2-user -i <<'EOF'

mamba create -y -n rapids -c rapidsai -c conda-forge -c nvidia rapids=22.12 python=3.9 cudatoolkit=11.5 ipykernel
conda activate rapids

# optionally install AutoGluon for AutoML GPU demo
# anaconda3/envs/rapids/bin/python -m pip install --pre autogluon

anaconda3/envs/rapids/bin/python -m ipykernel install --user --name rapids
echo "kernel install completed"
EOF
```

Set the volume size to at least `15GB`, to accommodate the conda environment.

Then launch the instance.

### Select the RAPIDS environment

Once your Notebook Instance is `InService` select "Open JupyterLab"

Then in Jupyter select the `rapids` kernel when working with a new notebook.

![Screenshot of Jupyter with the rapids kernel highlighted](../../images/sagemaker-choose-rapids-kernel.png)

## SageMaker Estimators

RAPIDS can also be used in [SageMaker Estimators](https://sagemaker.readthedocs.io/en/stable/api/training/estimators.html). Estimators allow you to launch training jobs on ephemeral VMs which SageMaker manages for you. The benefit of this is that your Notebook Instance doesn't need to have a GPU, so you are only charged for GPU instances for the time that your training job is running.

### Upload data to S3

We offer the dataset for this demo in a public bucket hosted in either the [`us-east-1`](https://s3.console.aws.amazon.com/s3/buckets/sagemaker-rapids-hpo-us-east-1/) or [`us-west-2`](https://s3.console.aws.amazon.com/s3/buckets/sagemaker-rapids-hpo-us-west-2/) regions

### Create Notebook Instance

Sign in to the Amazon SageMaker [console](https://console.aws.amazon.com/sagemaker/). Choose Notebook > Notebook Instances > Create notebook instance. If a field is not mentioned below, leave the default values:

- **NOTEBOOK_INSTANCE_NAME** = Name of the notebook instance
- **NOTEBOOK_INSTANCE_TYPE** = Type of notebook instance. We recommend a lightweight instance (e.g., ml.t2.medium) since the instance will only be used to build the container and launch work
- **PLATFORM_IDENTIFIER** = 'Amazon Linux 2, Jupyter Lab 3'
- **IAM_ROLE** = Create a new role > Create role
- **GIT_REPOSITORIES** = Under Default Repository > Repository, select 'Clone a public Git repository to this notebook instance only' and add the [RAPIDS deployment repository](https://github.com/rapidsai/deployment)

### Launch Jupyter Notebook

In a few minutes, Amazon SageMaker launches an ML compute instance — when its ready you should see several links appear in the Actions tab of the 'Notebook Instances' section, click on **Open JupyerLab** to launch into the notebook.

```{note}
If you see Pending to the right of the notebook instance in the Status column, your notebook is still being created. The status will change to InService when the notebook is ready for use.
```

### Run the Example Notebook

Once inside JupyterLab you should be able to navigate to the example notebook named [source/examples/rapids-sagemaker-higgs/notebook.ipynb](/examples/rapids-sagemaker-higgs/notebook) and continue following those instructions.

## Further reading

We’ve also written a **[detailed blog post](https://medium.com/rapids-ai/running-rapids-experiments-at-scale-using-amazon-sagemaker-d516420f165b)** on how to use SageMaker with RAPIDS.

```{relatedexamples}

```
