---
layout: default
nav_order: 9
parent: Resources
grand_parent: RAPIDS Maintainer Docs
title: Burn Down Guide
---

# Burn down guide

## Overview

This is a guide for the steps required to perform at the start of [burn down]({% link releases/process.md %}#burn-down).

Given the current development version is `v0.A.0`, then the next version is `v0.B.0` where `B=A+1`.

### Intended audience

Operations
{: .label .label-purple}

# Tasks

* Create `branch-0.B` branches
* Create `0.B` project board
* Create `0.B` gpuCI jobs
* Announce burn down

## Branches

### Create
In each RAPIDS project, create a new branch for `0.B` such as:

```bash
git fetch origin
git checkout -b branch-0.B origin/branch-0.A`
```

### Update

On this new branch, update documentation and version numbers.

* `README.md` - including build badges
* `CHANGELOG.md` - Add new section for `0.B.0`
* Files in `ci/release/update-version.sh`
* Any other documentation files

### Push

Commit, tag, and push the changes:

```bash
git commit -am "DOC Update to v0.B"
git tag v0.B.0a
git push origin HEAD:branch-0.B
git push origin v0.B.0a
```

## Project boards

For each RAPIDS project, navigate to the current release board and follow [these instructions](https://help.github.com/en/articles/copying-a-project-board) to copy it as the `v0.B` board.

## gpuCI jobs

Update the gpuCI configuration file to include the `branch-0.B`. Then run the RAPIDS Seed Job to generate the new jobs.

### Auto-mergers

Update each of the [auto-mergers](https://gpuci.gpuopenanalytics.com/view/gpuCI%20-%20auto-mergers/) to merge from `0.A` to `0.B`.

Make sure to update all of the following
* Job name
* Job description
* SCM Branch
* `GH_HEAD` & `GH_BASE` parameters in the downstream job

## Announce

Announce that burn down has begun and when it will end.

Suggested template:

```markdown
@channel  :fire::arrow_down: *RAPIDS v0.9 Burn Down Announcement* :fire::arrow_down:

:warning: cuDF/cuML/cuGraph/RMM/cuStrings/dask-cuda v0.9 have moved to the burn down stage - `branch-0.10` is available but *not the default branch yet*

*Burn down ends Tuesday, August 13*
See https://docs.rapids.ai/maintainers for full v0.9 schedule

Please keep the following in mind:
- *Stop adding issues/PRs for v0.9*; unless deemed critical by the PICs
- *Concentrate all dev efforts* to close any issues or PRs on the v0.9 boards
- *Check open PRs* to ensure they target the correct branch before merging
- *Move open issues/PRs* to the new v0.9 boards and branch
- Auto-mergers are in place to merge updates from v0.9 to v0.10 - https://gpuci.gpuopenanalytics.com/view/gpuCI%20-%20auto-mergers/

See https://docs.rapids.ai/releases/process/#burn-down for more details on the burn down and development process.

*v0.9 boards:*
- cuDF - https://github.com/rapidsai/cudf/projects/15
- cuML - https://github.com/rapidsai/cuml/projects/8
- cuGraph - https://github.com/rapidsai/cugraph/projects/7
- RMM - https://github.com/rapidsai/rmm/projects/5
- cuStrings - https://github.com/rapidsai/custrings/projects/4
- dask-cuda - https://github.com/rapidsai/dask-cuda/projects/2

*v0.10 boards:*
- cuDF - https://github.com/rapidsai/cudf/projects/16
- cuML - https://github.com/rapidsai/cuml/projects/10
- cuGraph - https://github.com/rapidsai/cugraph/projects/10
- RMM - https://github.com/rapidsai/rmm/projects/6
- cuStrings - https://github.com/rapidsai/custrings/projects/5
- dask-cuda – https://github.com/rapidsai/dask-cuda/projects/3
```
