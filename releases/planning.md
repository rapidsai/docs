---
layout: default
nav_order: 2
parent: Release Docs
grand_parent: Maintainer Docs
title: Release Planning
---

# Release Planning

## Overview

Summary of the release planning process used by RAPIDS projects.

### Intended audience

Project Leads
{: .label .label-blue}

### See also

- [Versions and Tags]({% link resources/versions.md %})
- [Release Process]({% link releases/process.md %})

## Planning process

### Timing

**NOTE:** The processes below use the current release of `YY.MA`, the next release of `YY.MB` and future release `YY.MC` (where `MB=MA+2`, `MC=MB+2`) for examples.

Releases are planned in two phases:
1. `Fuzzy planning` from [Issue Triage]({% link releases/triage.md %}) which is ongoing.
2. `Focus planning` which starts when release `YY.MB` is **frozen**.

### Fuzzy planning

During `Fuzzy planning` issues are triaged and scheduled in their respective tracking boards. This naturally creates a pool of issues to consider from across the tracking boards during `Focus planning` under the columns `Future release`.

### Focus planning

Once a **freeze** has occurred for the release that is a WIP (i.e. release `YY.MB`), then planning for release `YY.MC` will start.

Project Leads
{: .label .label-blue}

1. Review all issues in the current WIP release `YY.MB` and find issues that will slip.
2. Move issues that will not make the release `YY.MB` to the release board for `YY.MC`.
3. Review each of the tracking boards and examine all issues in the `Future release` columns.
4. Add issues determined to be in-scope for the `YY.MC` release to the release board and move the issue to the `Next release` column in the tracking board.
5. Prioritize all issues into columns `P0`, `P1`, or `P2` on the `YY.MC` release board with input from project leads.
6. Rank issues within columns `P0`, `P1`, or `P2` to communicate priority for developers.
7. Review with team on day after release of `YY.MB` for feedback and input before adopting as the initial release plan.
