---
layout: default
nav_order: 3
parent: Release Docs
grand_parent: RAPIDS Maintainer Docs
title: Hotfix Process
---

# Hotfix Process

## Overview

Summary of the RAPIDS release process for hotfixes.

### Intended audience

Developers
{: .label .label-green}

Project Leads
{: .label .label-blue}

Operations
{: .label .label-purple}

### See also

* [Hotfix versioning]({% link resources/versions.md %})
* [Major and minor releases]({% link releases/process.md %})

## Hotfixes

Hotfix (or patch) releases are not preplanned and are made to address critical issues with the current release. The criteria and process below are set as a guideline to help determine what is a hotfix.

### Criteria

A hotfix is a _significant_ bug that affects the _majority_ of users for which there is no _reasonable_ workaround.

So consider these questions:

- __Is this bug significant?__
  - Does it produces incorrect results?
  - Are there compile or runtime errors with valid input?
  - Is there major incorrect functionality?
- __Does it affect the majority of users?__
  - Does the bug affect a common or major function?
  - Is the input that causes the bug a common or edge case?
  - Will the average user encounter the bug during normal, average usage?
- __Is there a reasonable workaround?__
  - Is there even a workaround?
  - Can a potential workaround be communicated effectively to the community?
  - Will the average user understand the workaround?
  - How many steps/code changes does a workaround take?
  - When the bug is fixed, does the workaround continue to work?

Also consider the timing of when the next release is scheduled. If the freeze or release date is within a few days, consider waiting and including the hotfix in the next release instead.

### Process

**NOTE:** The processes below use these releases as examples:
- Current release `M.A.X`
- Next minor release `M.B.0`  (where `B=A+1`)
- Next patch release `M.A.Y` (where `Y=X+1`)

Developers
{: .label .label-green}
1. Hotfix issues will be assigned to you
2. Create your branch from the `branch-M.B` branch
3. Implement the fix succinctly
  1. Change the minimal amount of code required
  2. Update related documentation and unit tests
  3. It is acceptable to implement a quick fix and open a new issue for a more in depth solution
4. Once complete, create a [pull request]({% link contributing/prs.md %}) targeting `branch-M.B`
5. Notify the project lead

Project Leads
{: .label .label-blue}
1. During [triage]({% link releases/triage.md %}), identify potential hotfixes
2. Ensure that the [hotfix criteria](#criteria) is met
3. Assign the issue and track its progress
4. Notify Operations that a hotfix is being worked on
5. Once notified that the pull request is created, review and approve it. Do NOT merge the pull request.
6. Notify Operations that the hotfix pull request is ready for merging

Operations
{: .label .label-purple}
1. Once notified by a Project Lead, review the pull request
2. Begin testing of conda and containers for correctness and functionality
3. Review documentation to ensure version numbers (updating to `M.A.Y`) and instructions are correct
4. Merge release PR targeting `branch-M.B` after approval
5. Create a new PR from `branch-M.B` targeting `main`
6. Merge the PR targeting `main` after review and approval
7. Monitor process of automated tools
8. Spot check deliverables to ensure correctness
