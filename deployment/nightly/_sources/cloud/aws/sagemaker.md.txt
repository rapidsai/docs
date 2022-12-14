# Sagemaker

RAPIDS also works with AWS SageMaker. We’ve written a **[detailed
blog post](https://medium.com/rapids-ai/running-rapids-experiments-at-scale-using-amazon-sagemaker-d516420f165b)**
with **[examples](https://github.com/rapidsai/cloud-ml-examples/tree/main/aws)**
for how to use Sagemaker with RAPIDS. To get started:

**0. Upload data to S3.** We offer the dataset for this demo in a public bucket hosted in either the [`us-east-1`](https://s3.console.aws.amazon.com/s3/buckets/sagemaker-rapids-hpo-us-east-1/) or [`us-west-2`](https://s3.console.aws.amazon.com/s3/buckets/sagemaker-rapids-hpo-us-west-2/) regions

**1. Create Notebook Instance.** Sign in to the Amazon SageMaker [console](https://console.aws.amazon.com/sagemaker/). Choose Notebook > Notebook Instances > Create notebook instance. If a field is not mentioned below, leave the default values:

- **NOTEBOOK_INSTANCE_NAME** = Name of the notebook instance
- **NOTEBOOK_INSTANCE_TYPE** = Type of notebook instance. We recommend a lightweight instance (e.g., ml.t2.medium) since the instance will only be used to build the container and launch work
- **PLATFORM_IDENTIFIER** = 'Amazon Linux 2, Jupyter Lab 3'
- **IAM_ROLE** = Create a new role > Create role
- **GIT_REPOSITORIES** = Under Default Repository > Repository, select 'Clone a public Git repository to this notebook instance only' and add the [cloud-ml-examples repository](https://github.com/rapidsai/cloud-ml-examples)

**2. Launch Jupyter Notebook.** In a few minutes, Amazon SageMaker launches an ML compute instance — when its ready you should see several links appear in the Actions tab of the 'Notebook Instances' section, click on **Open JupyerLab** to launch into the notebook.

- > Note: If you see Pending to the right of the notebook instance in the Status column, your notebook is still being created. The status will change to InService when the notebook is ready for use.

**3. Run Notebook.** Once inside JupyterLab you should be able to navigate to the notebook in the root directory named **aws/rapids_sagemaker_hpo.ipynb** or **aws/rapids_sagemaker_higgs**.
