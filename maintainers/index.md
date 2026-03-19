---
layout: default
title: Maintainer Docs
nav_order: 6
has_children: true
---

# RAPIDS Maintainers Docs
{:.no_toc}

RAPIDS projects use an established set of guidelines and procedures for all projects. These are available for the community to review and provide feedback on.
{: .fs-6 .fw-300 }

### Intended audience

Developers
{: .label .label-green}

Project Leads
{: .label .label-blue}

Operations
{: .label .label-purple}

## Release v{{ site.data.releases.nightly.version }} Schedule

**NOTE:** *Dates are subject to change at anytime. Completed release schedules are posted [here]({% link releases/schedule.md %}).*

Phase | Start | End | Duration
-- | -- | -- | --
Development | {{ site.data.releases.nightly.dev.start | date: "%a, %b %e, %Y" }} | {{ site.data.releases.nightly.dev.end | date: "%a, %b %e, %Y" }} | {{ site.data.releases.nightly.dev.days }} days
[Burn Down]({% link releases/process.md %}#burn-down) (cuDF group[^1]) | {{ site.data.releases.nightly.burndown.start | date: "%a, %b %e, %Y" }} | {{ site.data.releases.nightly.burndown.end | date: "%a, %b %e, %Y" }} | {{ site.data.releases.nightly.burndown.days }} days
[Code Freeze/Testing]({% link releases/process.md %}#code-freeze) (cuDF group[^1]) | {{ site.data.releases.nightly.cudf_codefreeze.start | date: "%a, %b %e, %Y" }} | {{ site.data.releases.nightly.cudf_codefreeze.end | date: "%a, %b %e, %Y" }} | {{ site.data.releases.nightly.cudf_codefreeze.days }} days
[Burn Down]({% link releases/process.md %}#burn-down) (others) | {{ site.data.releases.nightly.other_burndown.start | date: "%a, %b %e, %Y" }} | {{ site.data.releases.nightly.other_burndown.end | date: "%a, %b %e, %Y" }} | {{ site.data.releases.nightly.other_burndown.days }} days
[Code Freeze/Testing]({% link releases/process.md %}#code-freeze) (others) | {{ site.data.releases.nightly.other_codefreeze.start | date: "%a, %b %e, %Y" }} | {{ site.data.releases.nightly.other_codefreeze.end | date: "%a, %b %e, %Y" }} | {{ site.data.releases.nightly.other_codefreeze.days }} days
[Release]({% link releases/process.md %}#releasing) | {{ site.data.releases.nightly.release.start | date: "%a, %b %e, %Y" }} | {{ site.data.releases.nightly.release.end | date: "%a, %b %e, %Y" }} | {{ site.data.releases.nightly.release.days }} days

## _PROPOSED_ Release v{{ site.data.releases.next_nightly.version }} Schedule

Phase | Start | End | Duration
-- | -- | -- | --
Development | {{ site.data.releases.next_nightly.dev.start | date: "%a, %b %e, %Y" }} | {{ site.data.releases.next_nightly.dev.end | date: "%a, %b %e, %Y" }} | {{ site.data.releases.next_nightly.dev.days }} days
[Burn Down]({% link releases/process.md %}#burn-down) (cuDF group[^1]) | {{ site.data.releases.next_nightly.burndown.start | date: "%a, %b %e, %Y" }} | {{ site.data.releases.next_nightly.burndown.end | date: "%a, %b %e, %Y" }} | {{ site.data.releases.next_nightly.burndown.days }} days
[Code Freeze/Testing]({% link releases/process.md %}#code-freeze) (cuDF group[^1]) | {{ site.data.releases.next_nightly.cudf_codefreeze.start | date: "%a, %b %e, %Y" }} | {{ site.data.releases.next_nightly.cudf_codefreeze.end | date: "%a, %b %e, %Y" }} | {{ site.data.releases.next_nightly.cudf_codefreeze.days }} days
[Burn Down]({% link releases/process.md %}#burn-down) (others) | {{ site.data.releases.next_nightly.other_burndown.start | date: "%a, %b %e, %Y" }} | {{ site.data.releases.next_nightly.other_burndown.end | date: "%a, %b %e, %Y" }} | {{ site.data.releases.next_nightly.other_burndown.days }} days
[Code Freeze/Testing]({% link releases/process.md %}#code-freeze) (others) | {{ site.data.releases.next_nightly.other_codefreeze.start | date: "%a, %b %e, %Y" }} | {{ site.data.releases.next_nightly.other_codefreeze.end | date: "%a, %b %e, %Y" }} | {{ site.data.releases.next_nightly.other_codefreeze.days }} days
[Release]({% link releases/process.md %}#releasing) | {{ site.data.releases.next_nightly.release.start | date: "%a, %b %e, %Y" }} | {{ site.data.releases.next_nightly.release.end | date: "%a, %b %e, %Y" }} | {{ site.data.releases.next_nightly.release.days }} days

[^1]: cuDF group: cuDF, RMM, rapids-cmake, raft, dask-cuda, KvikIO, ucxx, rapidsmpf
