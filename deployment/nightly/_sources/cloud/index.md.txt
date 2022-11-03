---
html_theme.sidebar_secondary.remove: true
---

# Cloud

## Amazon Web Services

`````{grid} 1 2 2 3
:gutter: 2 2 2 2

````{grid-item-card}
:link: aws/ec2
:link-type: doc
Elastic Compute Cloud (EC2)
^^^
Launch an EC2 instance and run RAPIDS.

{bdg-primary}`single-node`
````

````{grid-item-card}
:link: aws/eks
:link-type: doc
Elastic Kubernetes Service (EKS)
^^^
Launch a RAPIDS cluster on managed Kubernetes.

{bdg-primary}`multi-node`
````

````{grid-item-card}
:link: aws/ecs
:link-type: doc
Elastic Container Service (ECS)
^^^
Launch a RAPIDS cluster on managed container service.

{bdg-primary}`multi-node`
````

````{grid-item-card}
:link: aws/sagemaker
:link-type: doc
Sagemaker
^^^
Launch the RAPIDS container as a Sagemaker notebook.

{bdg-primary}`single-node`
{bdg-primary}`multi-node`
````

`````

## Microsoft Azure

`````{grid} 1 2 2 3
:gutter: 2 2 2 2

````{grid-item-card}
:link: azure/azure-vm
:link-type: doc
Azure Virtual Machine
^^^
Launch an Azure VM instance and run RAPIDS.

{bdg-primary}`single-node`
````

`````

## Google Cloud Platforms

`````{grid} 1 2 2 3
:gutter: 2 2 2 2

````{grid-item-card}
:link: gcp/compute-engine
:link-type: doc
Compute Engine Instance
^^^
Launch an Compute Engine instance and run RAPIDS.

{bdg-primary}`single-node`
````

````{grid-item-card}
:link: gcp/vertex-ai
:link-type: doc
Vertex AI
^^^
Launch the RAPIDS container in Vertex AI managed notebooks.

{bdg-primary}`single-node`
````

`````

## IBM Cloud

`````{grid} 1 2 2 3
:gutter: 2 2 2 2

````{grid-item-card}
:link: ibm/virtual-server
:link-type: doc
IBM Virtual Server
^^^
Launch a virtual server and run RAPIDS.

{bdg-primary}`single-node`
````

`````

```{toctree}
:maxdepth: 2
:caption: Cloud
:hidden:

aws/index
azure/index
gcp/index
ibm/index
```
