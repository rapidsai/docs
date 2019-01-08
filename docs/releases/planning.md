---
layout: default
nav_order: 2
parent: Releases
title: Release Planning
---

# Release Planning

## Overview

Summary ...

### Intended audience

Project Leads
{: .label .label-blue}

### See also

- ?

## Planning process

### Timing

**NOTE:** The processes below use the current release of `M.A`, the next release of `M.B` and future release `M.C` (where `B=A+1`, `C=B+1`) for examples.

Releases are planned in two phases:
1. `Fuzzy planning` from [Issue Triage](triage) which is ongoing.
2. `Focus planning` which starts when release `M.B` is **frozen**.

### Release boards

RAPIDS projects use GitHub project boards for tracking releases with a customized setup and automation that is copied from existing boards.

For each project there is a release board for each release. As an example [v0.5 Release](https://github.com/rapidsai/cudf/projects/5) tracks the progress for the v0.5 release. Release boards are closed once a release is completed, and are labeled `vM.A Release` where `M` & `A` are the major & minor release version numbers.

Each release board has the following columns:

| Column | Purpose |
|:-------|:--------|
| Issue-Needs prioritizing | Issues that have gone through the [Issue Triage](triage) process and need to be prioritized |
| Issue-P0 | Issues that should be worked on first |
| Issue-P1 | Issues that should be worked on only if all `P0` issues are complete or assigned |
| Issue-P2 | Issues that should be worked on only if all `P1` issues are complete or assigned |
| PR-WIP | Newly opened PRs and re-opened PRs |
| PR-Needs Review | PRs move **automatically** to this column when pending approval by reviewer |
| PR-Reviewer approved | PRs move **automatically** to this column when approved by reviewer |
| Done | Issues and PRs that are closed will **automatically** be moved to this column |

**IMPORTANT:** Leveraging the release board for issues, we can _schedule_ issues by placing them in the appropriate column and then _prioritize_ issues by dragging & sorting the issues from highest priority at the top of the column to lowest at the bottom.

#### Using the release board
- Assigning and priortizing work
  - Scroll to the left to see all the columns labeled `Issue-*`
  - Re-prioritize issues in `P0`, `P1`, `P2` by moving issuses between columns
  - Move high priority issues within a column to the top; this promotes "pop off the top of the stack" development
- Expediting and finishing work
  - Scroll to the right to see all columns labeled `PR-*`
  - Identify PRs that need reviewers, input from authors, and other help

### Fuzzy planning

During `Fuzzy planning` issues are triaged and scheduled in their respective tracking boards. This naturally creates a pool of issues to consider from across the tracking boards during `Focus planning` under the columns `Future release`.

### Focus planning

Once a **freeze** has occurred for the release that is a WIP (i.e. release `M.B`), then planning for release `M.C` will start.

Project Leads
{: .label .label-blue}

1. Review all issues in the current WIP release `M.B` and find issues that will slip.
2. Move issues that will not make the release `M.B` to the release board for `M.C`.
3. Review each of the tracking boards and examine all issues in the `Future release` columns.
4. Add issues determined to be in-scope for the `M.C` release to the release board and move the issue to the `Next release` column in the tracking board.
5. Prioritize all issues into columns `P0`, `P1`, or `P2` on the `M.C` release board with input from project leads.
6. Rank issues within columns `P0`, `P1`, or `P2` to communicate priority for developers.
7. Review with team on day after release of `M.B` for feedback and input before adopting as the initial release plan.
