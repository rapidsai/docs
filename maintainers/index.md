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

{% include release-schedule.html release=site.data.releases.nightly %}

## _PROPOSED_ Release v{{ site.data.releases.next_nightly.version }} Schedule

{% include release-schedule.html release=site.data.releases.next_nightly %}
