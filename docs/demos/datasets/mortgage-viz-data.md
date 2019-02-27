---
layout: default
nav_order: 1
parent: Datasets
title: Mortgage Visualization Data
permalink: datasets/mortgage-viz-data
---

# Mortgage Visualization Demo Data

## Data Details

For the cuXfilter GTC mortgage visualization demo to work, the properly scored and formatted dataset (2006-2017) is required and available for [download here (1.9GB)](https://s3.us-east-2.amazonaws.com/rapidsai-data/viz-data/146M_predictions_v2.arrow.gz). 

For more details about its context read our blog [Accelerating Cross Filtering with cuDF](https://medium.com/rapids-ai/accelerating-cross-filtering-with-cudf-3b4c29c89292).

The raw data comes from the [Mortgage Data Section](https://rapidsai.github.io/demos/datasets/mortgage-data) and the risk score is generated from a model trained on an end to end workflow using the RAPIDS framework. 

146 million active and non-delinquent loans are given a score from 0-1 to indicate the likelihood of the loan being risky for purchase as part of a loan portfolio. Riskiness could mean a chance of delinquency during the lifetime of the loan, or that the loan will be paid off soon and cease generating interest payments.

The data is visualized with the following features:
* 3-zip boundary: postal zip code with the last 2 digests removed for privacy (951XX)
* 3-zip boundary bar height: total unpaid balance of all loans in that 3-zip area
* 3-zip boundary color: mean risk score of all loans in the 3-zip area
* Risk scores distribution histogram (dynamic bin size)
* Debt to Income ratio ( gross monthly income to gross monthly debt ) distribution histogram of loan recipients (dynamic bin sizes)
* Credit score (FICO) distribution histogram of loan recipients  (dynamic bin sizes)
* Bank ( generally loan originator )
