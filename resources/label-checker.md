---
layout: default
nav_order: 6
parent: Resources
grand_parent: RAPIDS Maintainer Docs
title: Label Checker
---

# Label Checker

## Overview

Summary of _Label Checker_ GitHub check used by some RAPIDS projects.

### Intended audience

Community
{: .label .label-yellow}

Developers
{: .label .label-green}

Project Leads
{: .label .label-blue}

Operations
{: .label .label-purple}

## Summary

Some RAPIDS repositories have a _Label Checker_ check on GitHub pull requests. The _Label Checker_ helps ensure that each pull request can be categorized correctly in our automated changelogs that get published for each release (i.e. [cudf v21.06.00](https://github.com/rapidsai/cudf/releases/tag/v21.06.00)).

In order for the _Label Checker_ check to pass, pull requests must include **one** label from **each** of the following categories:

- `category` - categorizes the pull request
  - `bug`
  - `doc`
  - `feature request`
  - `improvement`
- `breaking` - determines whether or not the pull request breaks functionality for end-users
  - `breaking`
  - `non-breaking`

Additionally, the _Label Checker_ check will **fail** when the pull request includes any label which contains the string `DO NOT MERGE` (case insensitive).

### _Label Checker_ Statuses

Below is a table of the possible statuses for the _Label Checker_ and their corresponding required actions.

| Status                                                                                                          | Required Action                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| ![](/assets/images/label-checker/missing_cat_breaking.png)                                                      | Add **one** label from each list above              |
| ![](/assets/images/label-checker/missing_cat.png)                                                               | Add **one** label from `category label` list        |
| ![](/assets/images/label-checker/missing_breaking.png)                                                          | Add **one** label from `breaking label` list        |
| ![](/assets/images/label-checker/many_breaking.png)<br>**OR**<br>![](/assets/images/label-checker/many_cat.png) | Ensure only **one** label from each list is applied |
| ![](/assets/images/label-checker/do_not_merge.png)                                                              | Remove the `DO NOT MERGE` label                 |
| ![](/assets/images/label-checker/correct.png)                                                                   | ✅ None, all labels correctly applied               |
