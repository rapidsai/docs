---
layout: default
nav_order: 3
parent: Resources
grand_parent: Maintainer Docs
title: Telemetry
---

# {{ page.title }}
{:.no_toc}

## Overview
{:.no_toc}

The RAPIDS team collects build-time and test-time telemetry from our CI jobs.
These data are used to provide insights into potential speed impacts and
optimizations that might be worthwhile.

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

This is an overview of how telemetry data is collected, how it is transmitted and recorded, and how visualizations can be obtained using Grafana.

## Collecting data

We can collect telemetry data from possibly multiple sources. Right now, the
main source of timing information is the Github Actions job metadata, which we
obtain using the [Github Actions REST
API](https://docs.github.com/en/rest/actions/workflow-jobs?apiVersion=2022-11-28#list-jobs-for-a-workflow-run-attempt).
These data contain jobs, which generally correspond to calls to reusable
workflows from our shared-workflows repository. They also itemize each step
within any given workflow.

The general implementation for telemetry is as follows:

1. Creating initial variables that get loaded
2. add metadata in shared-workflows using OTEL_ATTRIBUTES, run workflow, stash variables to collect in final job
3. On a self-hosted node, parse Github Actions job metadata, and associate jobs with attributes passed in from step 2). Send data to Tempo via a FluentBit agent that is also used to aggregate logs.

Steps 1 and 3 happen as jobs in the "top-level repository" - the workflow that initiates all subsequent workflows.

### Code changes for projects to add telemetry

These are the general steps necessary to add telemetry to a repository that does
not currently have it. This does not describe changes to shared-workflows as
implementation details. In the top-level workflow, such as
`cudf/.github/workflows/pr.yaml`:

1. Add a job for telemetry-setup, and add that job name to the pr-builder `needs` collection.
```
jobs:
    # Please keep pr-builder as the top job here
  pr-builder:
    needs:
      - check-nightly-ci
      - changed-files
      ... <other job names> ...
      - telemetry-setup
  telemetry-setup:
    continue-on-error: true
    runs-on: ubuntu-latest
    env:
      OTEL_SERVICE_NAME: 'pr-cudf'
    steps:
      - name: Telemetry setup
        if: ${{ vars.TELEMETRY_ENABLED == 'true' }}
        uses: rapidsai/shared-actions/telemetry-dispatch-stash-base-env-vars@main
```

`OTEL_SERVICE_NAME` serves as one identifier in telemetry. It's not strictly necessary.

2. Add `telemetry-setup` as a `needs` entry for all jobs at the top of the tree. The purpose is to communicate telemetry variables that any job may use - even the checks.yaml job. `needs` that generally catch the required jobs are:

* checks
* changed-files
* devcontainer

3. Add an entry to skip the final job, `ignored_pr_jobs`:

```
  checks:
    secrets: inherit
    needs: telemetry-setup
    uses: rapidsai/shared-workflows/.github/workflows/checks.yaml@branch-25.02
    with:
      enable_check_generated_files: false
      ignored_pr_jobs: "telemetry-summarize"
```

Syntax for the `ignored_pr_jobs` is [space-separated within the quotes](https://github.com/rapidsai/shared-workflows/blob/branch-25.02/.github/workflows/checks.yaml#L30).

4. Run the parsing and submission script job as the final job - after `pr-builder`:

```
  telemetry-summarize:
    # This job must use a self-hosted runner to record telemetry traces.
    runs-on: linux-amd64-cpu4
    needs: pr-builder
    if: ${{ vars.TELEMETRY_ENABLED == 'true' && !cancelled() }}
    continue-on-error: true
    steps:
      - name: Telemetry summarize
        uses: rapidsai/shared-actions/telemetry-dispatch-summarize@main
```

### Implementation details

The "meat" implementation of telemetry lives primarily in the `shared-actions`
repository. As the middle layer, the reusable workflows in the shared-workflows
repo download the stashed environment variables from the top-level
`telemetry-setup`, load them in the local worker's environment, run the command,
and stash possible variables of interest, which capture metadata for that
particular job. You should not generally need to change shared-actions or
shared-workflows when maintaining other RAPIDS repositories. This section is
only necessary for someone looking to change or improve something like:

* Adding new metadata to associate with a job
* Adding telemetry from new sources, such as sccache statistics or build logs
* fixing one or more of what is surely multitudinous bugs

#### Shared-actions

[Shared-actions](https://github.com/rapidsai/shared-actions) use a pattern we
call "dispatch actions," which is broadly described as running an action that
clones the shared-actions repo, which enables referring to local files in the
clone. Folders at the top level in the shared-actions repo that start with
telemetry-dispatch are all dispatch actions.

Most of these scripts start with the `load-then-clone` action, which downloads
the initial file that contains the basic environment variables that should be
propagated. The main exception to this is
`telemetry-dispatch-stash-base-env-vars` which is used to populate the basic
environment variable file in the first place. Passing the environment variable
file is used instead of parameters to save on lots of bloat.

The ability to refer to local files is employed in the
[`telemetry-impls/summarize`](https://github.com/rapidsai/shared-actions/tree/main/telemetry-impls/summarize)
action, where a python file is used to parse and send OpenTelemetry data with
the OpenTelemetry Python SDK. If some value here seems like it's magically
coming from nowhere, it is probably being passed in an environment variable
file.

#### Shared-workflows

At this level, we load the base environment variables and add our own, then run our process. The
environment variables that we load ensures that if any build tool natively
supports OpenTelemetry, it has the necessary information to send that data (job
needs to be on a self-hosted runner)

```
jobs:
  build:
    steps:
      - name: Telemetry setup
        uses: rapidsai/shared-actions/telemetry-dispatch-setup@main
        continue-on-error: true
        if: ${{ vars.TELEMETRY_ENABLED == 'true' }}
        with:
            extra_attributes: "rapids.operation=build-cpp,rapids.package_type=conda,rapids.cuda=${{ matrix.CUDA_VER }},rapids.py=${{ matrix.PY_VER }},rapids.arch=${{ matrix.ARCH }},rapids.linux=${{ matrix.LINUX_VER }}"
```

Passing in the `extra_attibutes` parameter appends these comma-separated
key=value pairs to the `OTEL_RESOURCE_ATTRIBUTES` environment variable. This is
the way that we associate matrix values, such as CUDA version, architecture, and
python version with a particular job.

As implemented today, the `telemetry-dispatch-setup` action uploads an
environment variable file before running the action's command. That saves us
from needing to have that as a separate step in our shared-workflows workflows,
but also means that if our action changes any telemetry-related environment
variable, it won't be reflected in stored metadata.

TODO: Seems like we should move the upload AFTER the action command.

## Receiving and storing data

## Viewing captured data