---
layout: default
nav_order: 3
parent: Releases
title: Hotfix Process
---

# Hotfix Process

## Overview

Summary of the RAPIDS release process for hotfixes.

### Intended audience

Project Leads
{: .label .label-blue}

Operations
{: .label .label-purple}

### See also

* [Hotfix versioning]({{ site.baseurl }}docs/resources/versions)
* [Major and minor releases]({{ site.baseurl }}docs/releases/process)

## Hotfixes

Hotfix (or patch) releases are not preplanned and are made to address critical issues with the current release. The criteria and process below are set as a guideline to help determine what is a hotfix.

### Criteria

A hotfix is a significant bug that affects the _majority_ of users for which there is no _reasonable_ workaround.

So consider:

- __What makes a bug significant?__
  - Produces incorrect results
  - Compile or runtime errors with valid input
  - Major incorrect functionality
- __Does it affect the majority of users?__
  - Does the bug affect a common or major function?
  - Is the input that causes the bug a common or edge case?
  - Will the average user encounter the bug during normal, average usage?
- __Is there a reasonable workaround?__
  - Is there even a workaround? Can it be communicated effectively?
  - How many steps or code changes does a workaround take?
  - When the bug is fixed, does the workaround continue to work?
  - Will the average user understand the workaround?

Also consider the timing and when the next release is scheduled. If the freeze or release date is within a few days, consider waiting and including the hotfix in the release.

### Process

**NOTE:** The processes below use the current release of `M.A`, the next release of `M.B` and future release `M.C` (where `B=A+1`, `C=B+1`) for examples.

Developers
{: .label .label-green}
- Implement the fix succinctly
- Change the minimal amount of code required
- Update related documentation and unit tests
- It is acceptable to implement a quick fix and open a new issue for a more in depth solution

Project Leads
{: .label .label-blue}

...

Operations
{: .label .label-purple}

...
