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

The current release schedule is posted on the [RAPIDS Maintainers Docs]({% link maintainers/index.md %}) page.

## Completed Releases

Historical list of completed releases

{% for release in site.data.previous_releases %}
### Release v{{ release.version }} Schedule

{% include release-schedule.html release=release %}
{% endfor %}
