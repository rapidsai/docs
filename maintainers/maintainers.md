---
layout: default
title: RAPIDS Maintainer Docs
nav_order: 8
has_children: true
permalink: maintainers
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
Development (cuDF/RMM/rapids-cmake) | {{ site.data.releases.nightly.cudf_dev.start | date: "%a, %b %e" }} | {{ site.data.releases.nightly.cudf_dev.end | date: "%a, %b %e" }} | {{ site.data.releases.nightly.cudf_dev.days }} days
Development (others) | {{ site.data.releases.nightly.other_dev.start | date: "%a, %b %e" }} | {{ site.data.releases.nightly.other_dev.end | date: "%a, %b %e" }} | {{ site.data.releases.nightly.other_dev.days }} days
[Burn Down]({% link releases/process.md %}#burn-down)(cuDF/RMM/rapids-cmake) | {{ site.data.releases.nightly.cudf_burndown.start | date: "%a, %b %e" }} | {{ site.data.releases.nightly.cudf_burndown.end | date: "%a, %b %e" }} | {{ site.data.releases.nightly.cudf_burndown.days }} days
[Burn Down]({% link releases/process.md %}#burn-down) (others) | {{ site.data.releases.nightly.other_burndown.start | date: "%a, %b %e" }} | {{ site.data.releases.nightly.other_burndown.end | date: "%a, %b %e" }} | {{ site.data.releases.nightly.other_burndown.days }} days
[Code Freeze/Testing]({% link releases/process.md %}#code-freeze) (cuDF/RMM/rapids-cmake) | {{ site.data.releases.nightly.cudf_codefreeze.start | date: "%a, %b %e" }} | {{ site.data.releases.nightly.cudf_codefreeze.end | date: "%a, %b %e" }} | {{ site.data.releases.nightly.cudf_codefreeze.days }} days
[Code Freeze/Testing]({% link releases/process.md %}#code-freeze) (others) | {{ site.data.releases.nightly.other_codefreeze.start | date: "%a, %b %e" }} | {{ site.data.releases.nightly.other_codefreeze.end | date: "%a, %b %e" }} | {{ site.data.releases.nightly.other_codefreeze.days }} days
[Release]({% link releases/process.md %}#releasing) | {{ site.data.releases.nightly.release.start | date: "%a, %b %e" }} | {{ site.data.releases.nightly.release.end | date: "%a, %b %e" }} | {{ site.data.releases.nightly.release.days }} days

## _PROPOSED_ Release v{{ site.data.releases.next_nightly.version }} Schedule

Phase | Start | End | Duration
-- | -- | -- | --
Development (cuDF/RMM/rapids-cmake) | {{ site.data.releases.next_nightly.cudf_dev.start | date: "%a, %b %e" }} | {{ site.data.releases.next_nightly.cudf_dev.end | date: "%a, %b %e" }} | {{ site.data.releases.next_nightly.cudf_dev.days }} days
Development (others) | {{ site.data.releases.next_nightly.other_dev.start | date: "%a, %b %e" }} | {{ site.data.releases.next_nightly.other_dev.end | date: "%a, %b %e" }} | {{ site.data.releases.next_nightly.other_dev.days }} days
[Burn Down]({% link releases/process.md %}#burn-down)(cuDF/RMM/rapids-cmake) | {{ site.data.releases.next_nightly.cudf_burndown.start | date: "%a, %b %e" }} | {{ site.data.releases.next_nightly.cudf_burndown.end | date: "%a, %b %e" }} | {{ site.data.releases.next_nightly.cudf_burndown.days }} days
[Burn Down]({% link releases/process.md %}#burn-down) (others) | {{ site.data.releases.next_nightly.other_burndown.start | date: "%a, %b %e" }} | {{ site.data.releases.next_nightly.other_burndown.end | date: "%a, %b %e" }} | {{ site.data.releases.next_nightly.other_burndown.days }} days
[Code Freeze/Testing]({% link releases/process.md %}#code-freeze) (cuDF/RMM/rapids-cmake) | {{ site.data.releases.next_nightly.cudf_codefreeze.start | date: "%a, %b %e" }} | {{ site.data.releases.next_nightly.cudf_codefreeze.end | date: "%a, %b %e" }} | {{ site.data.releases.next_nightly.cudf_codefreeze.days }} days
[Code Freeze/Testing]({% link releases/process.md %}#code-freeze) (others) | {{ site.data.releases.next_nightly.other_codefreeze.start | date: "%a, %b %e" }} | {{ site.data.releases.next_nightly.other_codefreeze.end | date: "%a, %b %e" }} | {{ site.data.releases.next_nightly.other_codefreeze.days }} days
[Release]({% link releases/process.md %}#releasing) | {{ site.data.releases.next_nightly.release.start | date: "%a, %b %e" }} | {{ site.data.releases.next_nightly.release.end | date: "%a, %b %e" }} | {{ site.data.releases.next_nightly.release.days }} days
