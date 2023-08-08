---
layout: default
nav_order: 3
parent: Release Docs
grand_parent: Maintainer Docs
title: Release Schedule
---

### Intended audience
{:.no_toc}

Community
{: .label .label-yellow}

Developers
{: .label .label-green}

Operations
{: .label .label-purple}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Current release

The current release schedule is posted on the [RAPIDS Maintainers Docs]({% link maintainers/maintainers.md %}) page.

## Completed Releases

Historical list of completed releases

{% for release in site.data.previous_releases %}
### Release v{{ release.version }} Schedule

{% if release.dev %}
Phase | Start | End | Duration
-- | -- | -- | --
Development | {{ release.dev.start | date: "%a, %b %e, %Y" }} | {{ release.dev.end | date: "%a, %b %e, %Y" }} | {{ release.dev.days }} days
Burn Down | {{ release.burndown.start | date: "%a, %b %e, %Y" }} | {{ release.burndown.end | date: "%a, %b %e, %Y" }} | {{ release.burndown.days }} days
Code Freeze/Testing | {{ release.codefreeze.start | date: "%a, %b %e, %Y" }} | {{ release.codefreeze.end | date: "%a, %b %e, %Y" }} | {{ release.codefreeze.days }} days
Release | {{ release.release.start | date: "%a, %b %e, %Y" }} | {{ release.release.end | date: "%a, %b %e, %Y" }} | {{ release.release.days }} days

{% else %}
{% if release.date %}
Phase | Date
-- | --
Release | {{ release.date | date: "%a, %b %e, %Y" }}
{% else %}
Phase | Start | End | Duration
-- | -- | -- | --
Development (cuDF/RMM{% if release.version >= '23.06' %}/rapids-cmake/cugraph-ops/raft{% endif %}) | {{ release.cudf_dev.start | date: "%a, %b %e, %Y" }} | {{ release.cudf_dev.end | date: "%a, %b %e, %Y" }} | {{ release.cudf_dev.days }} days
Development (others) | {{ release.other_dev.start | date: "%a, %b %e, %Y" }} | {{ release.other_dev.end | date: "%a, %b %e, %Y" }} | {{ release.other_dev.days }} days
[Burn Down]({% link releases/process.md %}#burn-down)(cuDF/RMM{% if release.version >= '23.06' %}/rapids-cmake/cugraph-ops/raft{% endif %}) | {{ release.cudf_burndown.start | date: "%a, %b %e, %Y" }} | {{ release.cudf_burndown.end | date: "%a, %b %e, %Y" }} | {{ release.cudf_burndown.days }} days
[Burn Down]({% link releases/process.md %}#burn-down) (others) | {{ release.other_burndown.start | date: "%a, %b %e, %Y" }} | {{ release.other_burndown.end | date: "%a, %b %e, %Y" }} | {{ release.other_burndown.days }} days
[Code Freeze/Testing]({% link releases/process.md %}#code-freeze) (cuDF/RMM/rapids-cmake/cugraph-ops/raft) | {{ release.cudf_codefreeze.start | date: "%a, %b %e, %Y" }} | {{ release.cudf_codefreeze.end | date: "%a, %b %e, %Y" }} | {{ release.cudf_codefreeze.days }} days
[Code Freeze/Testing]({% link releases/process.md %}#code-freeze) (others) | {{ release.other_codefreeze.start | date: "%a, %b %e, %Y" }} | {{ release.other_codefreeze.end | date: "%a, %b %e, %Y" }} | {{ release.other_codefreeze.days }} days
[Release]({% link releases/process.md %}#releasing) | {{ release.release.start | date: "%a, %b %e, %Y" }} | {{ release.release.end | date: "%a, %b %e, %Y" }} | {{ release.release.days }} days
{% endif %}
{% endif %}
{% endfor %}
