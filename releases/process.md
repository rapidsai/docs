---
layout: default
nav_order: 3
parent: Release Docs
grand_parent: RAPIDS Maintainer Docs
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

* [Git branching model]({% link resources/git.md %})
* [Major and minor release versioning]({% link resources/versions.md %})

## Git branching model

RAPIDS uses a custom git branching model, adapted from git-flow to leverage the tools GitHub provides and also focus on release-driven development. From more details see our guide for our [git branching]({% link resources/git.md %}) methodology. 

### Migrating projects

For RAPIDS projects that are using another branching/development model, continue to develop with that approach until the next **minor** release. Given the version `M.A.0` (where `M` is the major version and `A` is the minor version), create a development branch `branch-M.B` where `B=A+1` from the `main` branch that has the latest minor release.

From this point forward you can follow the git branching & release model used by the RAPIDS team.

## Major and minor releases

Both major and minor releases follow the same steps with little variation. For both, release types there are two key dates that need to be known well in advance:

* `Burn down date`
* `Code freeze data`
* `Release date`

The `burn down date` will always be several days before the `code freeze date` which in turn is several days before the `release date`. This is to ensure there is enough time to finish active development, and to handle any unknown bugs/issues.

### Hotfixes

Hotfixes have their own process and are described [here]({% link releases/hotfix.md %}).

## Burn down

Burn down is the process of locking down all issues slated for the release and moving issues not in this release to the following release. Additionally, all pending pull requests should be reviewed and aim to be merged before the code freeze date.

### Timing

For the selection of a `burn down date`, the general guidelines should be followed:
* Choose a `burn down date` at least **3 business days** before a `code freeze date`
* Consult project leads to ensure key features will make the release with the anticipated date
* Communicate the decided `burn down date` to the development team immediately to ensure they can meet the deadline

Burn down ends at 11:59 PM PT on the final day of the process.

### Process

**NOTE:** The processes below use the current release of `M.A`, the next release of `M.B` and future release `M.C` (where `B=A+1`, `C=B+1`) for examples.

Project Leads
{: .label .label-blue}

1. Beginning of the `burn down date` remind development team to stop accepting new issues for the `M.B` release (unless they are critical bugs/issues)
2. Work to merge existing pull requests targeting `M.B`
3. Move any pull requests or issues that are no longer a part of the `M.B` release to the `M.C` project board or backlog (for backlog remove the issue from the project board)

Operations
{: .label .label-purple}

1. Beginning of the `burn down date` announce the burn down of `branch-M.B`
2. Fork `branch-M.B` into `branch-M.C` for the new development branch
3. Create release `M.C` project board
4. Notify project leads process is complete

Also see the [Burn down guide]({% link resources/burn-down-guide.md %})


## Code freeze

Code freeze is the process when the release undergoes thorough testing. Pull requests are no longer accepted into the development branch. An exception may be made for [hotfix]({% link releases/hotfix.md %}) issues. All pull requests from Burn Down should be merged before Code Freeze begins or be moved to the next release.
### Timing

For the selection of a `code freeze date`, the general guidelines should be followed:
* Choose a `code freeze date` at least **3 business days** before the `release date`
* Communicate the decided `code freeze date` to the development team immediately to ensure they can meet the deadline

Code freeze begins at 12:00AM PT the day immediately after Burn Down ends.

For example, if Burn down runs from Wednesday Feb 3rd until Tuesday Feb 9th, then Burn down ends at 11:59PM PT on Feb 9th and Code Freeze begins 12:00AM PT Feb 10th.
### Process

**NOTE:** The processes below use the current release of `M.A`, the next release of `M.B` and future release `M.C` (where `B=A+1`, `C=B+1`) for examples.

Generally the process for Code Freeze occurs around 10:00AM PT on the first day of Code Freeze.

Project Leads
{: .label .label-blue}

1. Move any open pull requests targeting `branch-M.B` to target `branch-M.C` instead
2. Wait for confirmation from operations on the branch switch
3. Continue `M.C` development
4. Respond promptly to operations if any issues are found with the `M.B` release

Operations
{: .label .label-purple}

1. Beginning of the `code freeze date` announce the code freeze of `branch-M.B`
2. Switch GitHub default branch of project to `branch-M.C`
3. Create `M.B` release tracking project board
4. Notify project leads process is complete

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
2. Create release PR from `branch-M.B` that targets `main`
3. Begin testing of conda, containers, and notebooks for correctness and functionality
4. Work with development team to close outstanding PRs
5. Review documentation to ensure version numbers and instructions are correct
6. Enlist project reviewers to approve the release PR
7. Merge release PR after approval
8. Monitor process of automated tools
9. Spot check deliverables to ensure correctness
