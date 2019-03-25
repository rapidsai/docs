---
layout: default
nav_order: 3
parent: RAPIDS Release Process
title: Release Process
---

# Release Process

## Overview

Summary of the RAPIDS release process for major and minor releases.

### Intended audience

Project Leads
{: .label .label-blue}

Operations
{: .label .label-purple}

### See also

* [Git branching model]({{ site.baseurl }}resources/git)
* [Major and minor release versioning]({{ site.baseurl }}resources/versions)

## Git branching model

RAPIDS uses a custom git branching model, adapted from git-flow to leverage the tools GitHub provides and also focus on release-driven development. From more details see our guide for our [git branching]({{ site.baseurl }}resources/git) methodology. 

### Migrating projects

For RAPIDS projects that are using another branching/development model, continue to develop with that approach until the next **minor** release. Given the version `M.A.0` (where `M` is the major version and `A` is the minor version), create a development branch `branch-M.B` where `B=A+1` from the `master` branch that has the latest minor release.

From this point forward you can follow the git branching & release model used by the RAPIDS team.

## Major and minor releases

Both major and minor releases follow the same steps with little variation. For both, release types there are two key dates that need to be known well in advance:

* `Burn down date`
* `Release date`

The `burn down date` will always be several days before the `release date`. This is to ensure there is enough time to finish active development, and to handle any unknown bugs/issues.

### Hotfixes

Hotfixes have their own process and are described [here]({{ site.baseurl }}releases/hotfix).

## Burn down

Burn down is the process of locking down all issues slated for the release and moving issues not in this release to the following release. Additionally, all pending pull requests should be reviewed and aim to be merged before the release date.

### Timing

For the selection of a `burn down date`, the general guidelines should be followed:
* Choose a `burn down date` at least **3 business days** before a `release date`
* Consult project leads to ensure key features will make the release with the anticipated date
* Communicate the decided `burn down date` to the development team immediately to ensure they can meet the deadline

### Process

**NOTE:** The processes below use the current release of `M.A`, the next release of `M.B` and future release `M.C` (where `B=A+1`, `C=B+1`) for examples.

Project Leads
{: .label .label-blue}

1. Beginning of the `burn down date` remind development team to stop accepting new issues for the `M.B` release (unless they are critical bugs/issues)
2. Wait for confirmation from operations on the branch switch and project board updates
3. Move any issues that are no longer a part of the `M.B` release to the `M.C` project board or backlog (for backlog remove the issue from the project board)
4. Check open PRs that are no longer a part of the `M.B` release to ensure they are targeted for merge on the `branch-M.C`

Operations
{: .label .label-purple}

1. Beginning of the `burn down date` announce the burn down of `branch-M.B`
2. Fork `branch-M.B` into `branch-M.C` for the new development branch
3. Switch GitHub default branch of project to `branch-M.C`
4. Create release `M.C` project board
5. Notify project leads process is complete

## Releasing

### Timing

For the selection of a `release date`, the general guidelines should be followed:
* Choose a `release date` at least **3-4 weeks** from the previous `release date`
* Consult project leads to ensure key features will make the release with the anticipated date
* Communicate the decided `release date` to the development team immediately to ensure they can meet the deadline

### Process

**NOTE:** The processes below use the current release of `M.A`, the next release of `M.B` and future release `M.C` (where `B=A+1`, `C=B+1`) for examples.

Project Leads
{: .label .label-blue}

1. Beginning of the `release date` work with developers to close all outstanding issues and PRs
2. Assist operations team in testing and verifying documentation in release `M.B` PR
3. Review release `M.B` for approval
4. Help operations team in spot checking the deliverables post-release

Operations
{: .label .label-purple}

1. Beginning of the `release date` announce the release of `branch-M.B`
2. Create release PR from `branch-M.B` that targets `master`
3. Begin testing of conda, containers, and pip for correctness and functionality
4. Work with development team to close outstanding PRs
5. Review documentation to ensure version numbers and instructions are correct
6. Enlist project reviewers to approve the release PR
7. Merge release PR after approval
8. Monitor process of automated tools
9. Spot check deliverables to ensure correctness

