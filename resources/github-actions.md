---
layout: default
nav_order: 3
parent: Resources
grand_parent: Maintainer Docs
title: GitHub Actions
---

# {{ page.title }}
{:.no_toc}

## Overview
{:.no_toc}

The RAPIDS team uses GitHub Actions for CI/CD. The official documentation for GitHub Actions can be viewed [here](https://docs.github.com/en/actions).

### Intended audience
{: .no_toc }

Operations
{: .label .label-purple}

Developers
{: .label .label-green}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

RAPIDS uses self-hosted runners provided by NVIDIA for GPU-enabled testing. More information about these self-hosted runners can be found on the official documentation site [here](https://docs.gha-runners.nvidia.com/).

Additionally, the section [here](https://docs.gha-runners.nvidia.com/pull-request-testing) about pull request testing may be useful for users who are not already familiar with the process.

Finally, the page [here](https://docs.gha-runners.nvidia.com/runners/) outlines the list of runner labels that are available for use.

## Downloading CI Artifacts

For NVIDIA employees with VPN access, artifacts from both pull-requests and branch builds can be accessed on [https://downloads.rapids.ai/](https://downloads.rapids.ai/).

There is a link provided at the end of every C++ and Python build job where the build artifacts for that particular workflow run can be accessed.

![](/assets/images/downloads.png)

## Skipping CI for Commits

See the GitHub Actions documentation page below on how to prevent GitHub Actions from running on certain commits. This is useful for preventing GitHub Actions from running on pull requests that are not fully complete. This also helps preserve the finite GPU resources provided by the RAPIDS Ops team.

With GitHub Actions, it is not possible to configure all commits for a pull request to be skipped. It must be specified at the commit level.

**Link**: [https://docs.github.com/en/actions/managing-workflow-runs/skipping-workflow-runs](https://docs.github.com/en/actions/managing-workflow-runs/skipping-workflow-runs)

## Rerunning Failed GitHub Actions

See the GitHub Actions documentation page below on how to rerun failed workflows. In addition to rerunning an entire workflow, GitHub Actions also provides the ability to rerun only the failed jobs in a workflow.

At this time there are no alternative ways to rerun tests with GitHub Actions beyond what is described in the documentation (e.g. there is no `rerun tests` comment for GitHub Actions).

**Link**: [https://docs.github.com/en/actions/managing-workflow-runs/re-running-workflows-and-jobs](https://docs.github.com/en/actions/managing-workflow-runs/re-running-workflows-and-jobs)
