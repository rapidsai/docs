---
layout: default
nav_order: 1
parent: Datasets
grand_parent: Demos
title: Mortgage Data
permalink: datasets/mortgage-data
---

# Mortgage Data

## Data source

Dataset is derived from [Fannie Mae's Single-Family Loan Performance Data](http://www.fanniemae.com/portal/funding-the-market/data/loan-performance-data.html) with all rights reserved by Fannie Mae. This processed dataset is redistributed with permission and consent from Fannie Mae.

For the full raw dataset visit [Fannie Mae](http://www.fanniemae.com/portal/funding-the-market/data/loan-performance-data.html) to register for an account and to download.

## Using data with RAPIDS container

The RAPIDS container hosted on our [Docker Hub](https://hub.docker.com/r/rapidsai/rapidsai/) has notebooks that use the following datasets.
1. Download the datasets inside the container using `wget` or to the local host and use a docker volume mount to `/rapids/data/`
2. Decompress the dataset using `tar xzvf NAME_OF_DATASET.tgz`
3. Confirm that the following directory structure exists in `/rapids/data/`
```
/rapids/data/mortgage/acq/         <- all acquisition data
/rapids/data/mortgage/perf/        <- all performance data
/rapids/data/mortgage/names.csv    <- lender name normalization
```

## Available mortgage datasets

| Dataset | 1GB Splits\* | Loan Years | Download Size | Uncompressed Size | # Loans | # Perf. Records |
| --- | --- | --- | --- | --- | --- | --- |
| [1 Year](http://rapidsai-data.s3-website.us-east-2.amazonaws.com/notebook-mortgage-data/mortgage_2000.tgz) | [1 Year](http://rapidsai-data.s3-website.us-east-2.amazonaws.com/notebook-mortgage-data/mortgage_2000_1gb.tgz) | 2000 | 449 MB | 3.9 GB | 1.21 Million | 36 Million |
| [2 Years](http://rapidsai-data.s3-website.us-east-2.amazonaws.com/notebook-mortgage-data/mortgage_2000-2001.tgz) | [2 Years](http://rapidsai-data.s3-website.us-east-2.amazonaws.com/notebook-mortgage-data/mortgage_2000-2001_1gb.tgz) | 2000-2001 | 1.8 GB | 16 GB | 4.22 Million | 148 Million |
| [4 Years](http://rapidsai-data.s3-website.us-east-2.amazonaws.com/notebook-mortgage-data/mortgage_2000-2003.tgz) | [4 Years](http://rapidsai-data.s3-website.us-east-2.amazonaws.com/notebook-mortgage-data/mortgage_2000-2003_1gb.tgz) | 2000-2003 | 9.2 GB | 78 GB | 13.5 Million | 743 Million |
| [8 Years](http://rapidsai-data.s3-website.us-east-2.amazonaws.com/notebook-mortgage-data/mortgage_2000-2007.tgz) | [8 Years](http://rapidsai-data.s3-website.us-east-2.amazonaws.com/notebook-mortgage-data/mortgage_2000-2007_1gb.tgz) | 2000-2007 | 14.0 GB | 117 GB | 19.1 Million | 1.12 Billion |
| [16 Years](http://rapidsai-data.s3-website.us-east-2.amazonaws.com/notebook-mortgage-data/mortgage_2000-2015.tgz) | [16 Years](http://rapidsai-data.s3-website.us-east-2.amazonaws.com/notebook-mortgage-data/mortgage_2000-2015_1gb.tgz) | 2000-2015 | 22.8 GB | 192 GB | 34.7 Million | 1.85 Billion |
| [17 Years](http://rapidsai-data.s3-website.us-east-2.amazonaws.com/notebook-mortgage-data/mortgage_2000-2016.tgz) | [17 Years](http://rapidsai-data.s3-website.us-east-2.amazonaws.com/notebook-mortgage-data/mortgage_2000-2016_1gb.tgz) | 2000-2016 | 23.3 GB | 195 GB | 37.0 Million | 1.89 Billion |

\* 1GB splits are the same data with the individual performance data files split into 1GB pieces. This is useful for GPUs with less memory.
