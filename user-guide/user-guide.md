---
layout: default
title: User Guides
nav_order: 3
permalink: user-guide
description: |
  Guide to Getting Started Using RAPIDS
---

# User Guides
{: .fs-8 }

The RAPIDS data science framework is a collection of libraries for running end-to-end data science pipelines completely on the GPU. The interaction is designed to have a familiar look and feel to working in Python, but utilizes optimized NVIDIA® CUDA® primitives and high-bandwidth GPU memory under the hood. Below are some links to help getting started with the RAPIDS libraries.
{: .fs-6 .fw-300 .mb-8 }


### <i class="fa-sharp fa-solid fa-database"></i> ETL and Dataframe Processing with [cuDF](https://github.com/rapidsai/cudf){: target="_blank"}
Start with [10 Minutes to cuDF and Dask-cuDF](/api/cudf/stable/user_guide/10min.html){: target="_blank"}. Modeled after 10 Minutes to Pandas, this is a short introduction to cuDF that is geared mainly for new users. The [cuDF User Guide](https://docs.rapids.ai/api/cudf/stable/user_guide/index.html){: target="_blank"} is generally very extensive and helpful.
{: .mb-8 }


### <i class="fa-light fa-list-tree"></i> Accelerated Machine Learning with [cuML](https://github.com/rapidsai/cuml){: target="_blank"}
Start with the [Estimator Intro](https://github.com/rapidsai/cuml/notebooks/estimator_intro.ipynb){: target="_blank"}, showcasing basic machine learning for training and evaluating machine learning models in cuML. The [Intro and key concepts for cuML](https://docs.rapids.ai/api/cuml/stable/cuml_intro.html) is helpful as well.
{: .mb-8 }


### <i class="fa-light fa-chart-network"></i> Graph Analytics with [cuGraph](https://github.com/rapidsai/cugraph){: target="_blank"}
Start with the [Easy Path](https://docs.rapids.ai/api/cugraph/stable/basics/nx_transition.html#easy-path-use-networkx-graph-objects-accelerated-algorithms){: target="_blank"} to use NetworkX graph objects with accelerated algorithms. There is also general [cuGraph Introduction](https://docs.rapids.ai/api/cugraph/stable/basics/cugraph_intro.html){: target="_blank"}.
{: .mb-8 }


### <i class="fa-light fa-location-crosshairs"></i> Spatial Analytics with [cuSpatial](https://github.com/rapidsai/cuspatial){: target="_blank"}
Start with the [cuSpatial API Examples](https://github.com/rapidsai/cuspatial/docs/source/user_guide/cuspatial_api_examples.ipynb){: target="_blank"} for an intro to GPU Accelerated Spatial Analytics. The [demo notebooks](https://github.com/rapidsai/cuspatial/tree/branch-{{ site.data.releases.stable.version }}/python/cuspatial/demos) are also a good showcase.
{: .mb-8 }


### <i class="fa-light fa-chart-scatter-bubble"></i> Accelerated Cross-filtered Dashboards with [cuxfilter](https://github.com/rapidsai/cuxfilter)
Start with [10 Minutes to Cuxfilter](https://github.com/rapidsai/cuxfilter/notebooks/10_minutes_to_cuxfilter.ipynb) to get an overview of how to quickly create a dashboard and [the examples section](https://docs.rapids.ai/api/cuxfilter/stable/examples/examples.html){: target="_blank"} for real dataset examples.
{: .mb-8 }


### <i class="fa-regular fa-signal-stream"></i> Signal Analytics with [cuSignal]((https://github.com/rapidsai/cusignal)){: target="_blank"}
Start with the [End to End Example](https://github.com/rapidsai/cusignal/blob/branch-{{ site.data.releases.stable.version }}/notebooks/E2E_Example.ipynb){: target="_blank"} for simulating signals and influencing guide as well as the [API Guide](https://github.com/rapidsai/cusignal/tree/branch-{{ site.data.releases.stable.version }}/notebooks/api_guide){: target="_blank"}.
{: .mb-8 }


### <i class="fa-light fa-images"></i> Computer Vision and Analytics with [cuCIM](https://github.com/rapidsai/cucim){: target="_blank"}
Start with the [Welcome Notebook](https://github.com/rapidsai/cucim/blob/branch-{{ site.data.releases.stable.version }}/notebooks/Welcome.ipynb){: target="_blank"} for links to resources guides and a good overview of the project structure.
{: .mb-8 }


### <i class="fa-light fa-file-binary"></i> Algorithms and Primitives for Scientific Computing, Data Science and Machine Learning with [RAFT](https://github.com/rapidsai/raft){: target="_blank"}
Start with the [Quick Start](https://docs.rapids.ai/api/raft/stable/quick_start.html){: target="_blank"} guide for simple python and C++ examples.
{: .mb-8 }


### <i class="fa-light fa-hat-wizard"></i> Cyber Security Analytic Workflows with [CLX](https://github.com/rapidsai/clx){: target="_blank"}
Start with [10 Minutes to CLX](https://github.com/rapidsai/clx/notebooks/10mins.ipynb){: target="_blank"} for an guide to accelerated cyber security log analytics as well as the [introduction](https://docs.rapids.ai/api/clx/stable/intro-clx-predictive-maintenance.html#Introduction){: target="_blank"}.
{: .mb-8 }


### <i class="fa-light fa-bolt"></i> Accelerated Apache Spark with [Spark RAPIDS](https://nvidia.github.io/spark-rapids/){: target="_blank"}
Start with [the Examples Repository](https://github.com/NVIDIA/spark-rapids-examples){: target="_blank"} for Spark related utilities and examples using the RAPIDS Accelerator, including ETL, ML/DL, and more. A good [overview](https://nvidia.github.io/spark-rapids/){: target="_blank"} is available on their docs introduction. 
{: .mb-8 }


### <i class="fa-light fa-notebook"></i> Full Collection of our Notebooks with [RAPIDS Notebooks](https://github.com/rapidsai/notebooks){: target="_blank"}
A GitHub repository with our introductory examples of XGBoost, cuDF, cuML, cuGraph, and more. Most notebooks above are included in this repo.
{: .mb-8 }


###  <i class="fa-light fa-notebook"></i>Extended Collection of [Community Notebooks](https://github.com/rapidsai/notebooks-contrib){: target="_blank"}
A collection of examples and tutorials used to introduce new users to the features and capabilities of RAPIDS.
{: .mb-8 }


### <i class="fa-light fa-cloud"></i> Machine Learning Services Integration for [RAPIDS Cloud](https://github.com/rapidsai/cloud-ml-examples){: target="_blank"}
A repository with example notebooks and "getting started" code samples to help you integrate RAPIDS with the hyperparameter optimization services from Azure ML, AWS Sagemaker, Google Cloud, and Databricks. 
{: .mb-8 }


### <i class="fa-light fa-screwdriver-wrench"></i> Tools and Guides for [RAPIDS Deployment](/deployment/stable/){: target="_blank"}
Deployment documentation to get you up and running with RAPIDS in AWS, GCP, Azure, IBM and more. Also includes guides for HPC, HPO, Kubernetes, Dask, and more.
{: .mb-8 }