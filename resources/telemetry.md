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

> NOTE: pay special attention to the `runs-on` entry. This is what dictates that the job runs on a self-hosted runner, which is necessary for network access control.

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

Passing in the `extra_attributes` parameter appends these comma-separated
key=value pairs to the `OTEL_RESOURCE_ATTRIBUTES` environment variable. This is
the way that we associate matrix values, such as CUDA version, architecture, and
python version with a particular job.

As implemented today, the `telemetry-dispatch-setup` action uploads an
environment variable file before running the action's command. That saves us
from needing to have that as a separate step in our shared-workflows workflows,
but also means that if our action changes any telemetry-related environment
variable, it won't be reflected in stored metadata.

TODO: Seems like we should move the upload AFTER the action command.

## Sending data

Telemetry data is sent from [a python script that uses the python OpenTelemetry
SDK](https://github.com/rapidsai/shared-actions/blob/main/telemetry-impls/summarize/send_trace.py).
Configuration for this SDK is done with environment variables. Defaults are set
in [the github action that stashes base environment
variables](https://github.com/rapidsai/shared-actions/blob/main/telemetry-impls/stash-base-env-vars/action.yml),
which runs at the start of each root workflow, e.g.
[rmm](https://github.com/rapidsai/rmm/blob/45a44463472003e86c7ade2248d8d799fb97758e/.github/workflows/pr.yaml#L43).

### Debugging

It is helpful to be able to send telemetry to some testing server without running workflows. The general steps are:

1. Run your own instance of tempo locally. The [official example docker-compose
configuration](https://github.com/grafana/tempo/blob/main/example/docker-compose/local/docker-compose.yaml)
works fine.

2. Download a JSON file of your github actions jobs. These are removed by
default when a job finishes, but you can preserve it by re-running a job with
debug output. The filename is `all_jobs.json`. Alternatively, you can fetch it
with the [Github Actions
API](https://docs.github.com/en/rest/actions/workflow-jobs?apiVersion=2022-11-28#list-jobs-for-a-workflow-run-attempt).
If you use the Github Actions API, bear in mind that it is paginated and your
results may be incomplete without proper handling of pagination.

3. Clone the shared-actions repo locally

4. copy the `all_jobs.json` file into `shared-actions/telemetry-impls/summarize`

5. cd into `shared-actions/telemetry-impls/summarize`

6. Set key environment variables

  * Set them on the terminal
    ```
    export OTEL_EXPORTER_OTLP_ENDPOINT: "http://localhost:4318"
    export OTEL_EXPORTER_OTLP_PROTOCOL: "http/protobuf"
    export OTEL_TRACES_EXPORTER: "otlp_proto_http"
    ```
  * Use VS Code run configurations
    ```
        {
            "name": "send-tempo",
            "type": "debugpy",
            "request": "launch",
            "program": "send_trace.py",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}/telemetry-impls/summarize",
            "justMyCode": false,
            "env": {
                "OTEL_EXPORTER_OTLP_ENDPOINT": "http://localhost:4318",
                "OTEL_PYTHON_LOG_LEVEL": "DEBUG",
                "OTEL_EXPORTER_OTLP_PROTOCOL": "http/protobuf",
                "OTEL_TRACES_EXPORTER": "otlp_proto_http"
            }
        },
    ```

7. (optional) Run bump_time.py script to adjust timestamps in your
`all_jobs.json` file. The Grafana UI shows data that is a certain amount of time
prior to the present. Not updating timestamps can lead to your data points being
too far back in time to show up.

8. Run send_trace.py

## Receiving data

Authentication is the biggest complication with receiving data. We use mTLS to
allow exposing the Tempo server to the internet without restricting IPs. This
means that any server interacting with Tempo needs a set of certificates. It is
not viable to manage that for our workers. Instead, we have a FluentBit
forwarder that is only accessible to self-hosted runners. Our runners
communicate with the FluentBit forwarder without needing authentication, and the
FluentBit forwarder is configured with certificates so that it can send the data
on to the Tempo instance.

Important reiteration: only our self-hosted runners can send telemetry data.
Github-hosted runners will error out.

If you run tempo locally, be sure to adjust Grafana's datasources.yaml file to
point to your desired tempo instance.

## Storing data

This is an implementation detail of Tempo. The RAPIDS ops team currently has
Tempo backed by S3 to avoid ongoing upkeep requirements of a database server.

## Viewing captured data: Grafana dashboards

### Dashboard variables

Grafana has something called ["dashboard
variables,"](https://grafana.com/docs/grafana/latest/dashboards/variables/)
which serve to select some value for a particular dimension. Using this as the
input to the data filters makes it easy to make multiple plots for different
values of the variable (e.g. different machine labels or different RAPIDS repos)

There is a gotcha with variables. Grafana has a way of automatically detecting
values for variables - the "Query" variable type. This is the same as Tempo's [search tag values
API](https://grafana.com/docs/tempo/latest/api_docs/#search-tag-values). When it
works, it is very convenient. However, it only works on recent data. [If your
data was collected some time ago, Grafana may fail to populate these
fields](https://community.grafana.com/t/missing-resource-attributes-in-tempo-labels-and-values/140856).
Because of this, it is generally worthwhile to use the "Custom" variable type
and manually input variable values, instead of relying on Grafana/Tempo
detecting them.

![](/assets/images/telemetry/grafana_variable_definition.png)

While configuring your variable, if you want to show multiple plots with
different values of this variable, be sure to check the "Include All Option"
checkbox.

When finished defining your variable and its values, click the blue "Save
dashboard" in the upper right. If you navigate away from this page without
clicking this button, your variable will not be saved.

### Queries

[Queries provide the data from the data source to the panel/visualization](https://grafana.com/docs/tempo/latest/traceql/). Queries differ based on the data source being used. [Tempo's queries use TraceQL](https://grafana.com/docs/tempo/latest/traceql/).

Attributes must be included as selectors in the query, or else they won't be available for filtering down the line. The TraceQL line can get pretty long:

```
{ } | select(span:duration, name, resource.rapids.labels, resource.service.name, resource.rapids.cuda, resource.rapids.cuda, resource.git.run_url, resource.rapids.py, resource.rapids.gpu)
```

![](/assets/images/telemetry/panel_query.png)

On the right side, take note of the "Repeat options" - this is how you get multiple plots (one per variable value).

On the bottom, take note of the limits and table format. For limits, each trace
represents one top-level workflow run. Scale this accordingly, especially if you
are looking back far in time. The span limit is less important - you just want
this number high enough to capture the largest number of spans for a given
trace. It's fine to set it to a high number, such as 1000 spans. Regarding table
format, we are interested in spans, not traces. You will not see the additional
metadata columns in the trace table format, because they apply to the spans.

As always, remember to click the upper-right save button after making any
changes.

### Filtering and grouping data

The workhorse ideas of the grafana plots are:

* filtering data such that it matches a given value
* Using groupby operations to aggregate multiple values of a given type

These are on the [Transform tab](https://grafana.com/docs/grafana/latest/panels-visualizations/query-transform-data/transform-data/) of the same box where the query was entered.

![](/assets/images/telemetry/filter_by_values.png)

An example useful set of transforms:

* [Filter data by values](https://grafana.com/docs/grafana/latest/panels-visualizations/query-transform-data/transform-data/#filter-data-by-values)
    * `Regex` is useful for matching strings
    * If using a variable, [ensure that Grafana is formatting the variable value](https://grafana.com/docs/grafana/latest/dashboards/variables/variable-syntax)
      correctly. The `regex` formatter is appropriate for escaping annoying characters. If your
      data filter is not functioning correctly - either not filtering values that should be
      filtered, or not yielding any results, you probably have the wrong formatter.

![](/assets/images/telemetry/filter_by_values_with_var.png)

* [Group-by](https://grafana.com/docs/grafana/latest/panels-visualizations/query-transform-data/transform-data/#group-by) is generally useful for averaging or summing multiple values for a given span kind.
  * You can average the span time for all `wheel-build-cpp` by project to compare the average wheel build time for each project. This would be a good bar chart.
  * You can sum the span time for all usage by machine label to show resource usage. This is particularly useful when combined with filters and dashboard variables to make multiple plots.
  * You may need to transform a column of string labels into an enum field for correct grouping. This is done with the [Convert field type transformation](https://grafana.com/docs/grafana/latest/panels-visualizations/query-transform-data/transform-data/#convert-field-type)

![](/assets/images/telemetry/field_type_and_value_options.png)

On any chart, Grafana often guesses wrong on the data to display. On the right
side of the image above, check the "Value options -> Show". This often defaults to "Calculate". It should generally be set to "All values" for our purposes.

Similarly, the "Value options -> Fields" combobox often defaults to "Numeric
fields," but we usually want to point it to a specific field.

* After a group-by aggregation, Grafana can lose track of the duration in terms of nanoseconds. To compensate for this, add an "Add field from calculation" transformation. You can divide nanoseconds by 60E9 to obtain minutes. Keep in mind that this is adding a new column, not altering the old one. You'll need to select the new column in the "Value options -> Fields" combobox.

![](/assets/images/telemetry/calculate_field.png)
