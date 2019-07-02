---
layout: default
nav_order: 1
parent: Release Docs
grand_parent: RAPIDS Maintainer Docs
title: Issue Triage
---

# Issue Triage

## Overview

Summary of the issue triage methodology used for RAPIDS projects.

### Intended audience

Developers
{: .label .label-green}

Project Leads
{: .label .label-blue}

### See also

- [Issues]({{ site.url }}{{ site.baseurl }}/contributing/issues)

## Triage goals

RAPIDS projects are continuously triaging new issues and re-triaging existing issues frequently. This is to ensure that high priority issues are remedied in a timely manner and the community receives frequent updates on a filed issue.

## Triage process

### Timing 

- Label and prioritize new issues within **2 business days**
- Re-prioritize existing issues **every week** using the project's issue tracking boards

### Tracking boards

For each project there are 3 issue tracking boards and 1 release tracking board:

- [Bug Squashing](https://github.com/rapidsai/cudf/projects/1) - track and prioritize bugs
- [Feature Planning](https://github.com/rapidsai/cudf/projects/9) - track and prioritize feature requests
- [Other Issues](https://github.com/rapidsai/cudf/projects/10) - track documentation, questions, and other issues
- [Release](https://github.com/rapidsai/cudf/projects/14) - tracks the progress of the current release

Bug Squashing, Feature Planning and Other Issues are permanent tracking boards, and are used as the basis for release planning. The Release board is not pernament and is closed once a release is completed.  The example boards above are from the [cuDF](https://github.com/rapidsai/cudf) project.

Each permanent project board has the following columns:

| Column | Purpose |
|:-------|:--------|
| Needs prioritizing | Issues that have gone through the `Initial triage` phase and now need to be prioritized |
| Hotfix - current release | Hotfix issues that need to be addressed immediately for the current `M.A` release |
| Next release | Issues that should tackled during the current development cycle for the next `M.B` release |
| Future release | Issues that should be prioritized for the next `M.C` or `M.D` releases |
| Backlog | All other open issues |
| Closed | Issues that are closed will **automatically** be moved to this column |

See [Release Board](https://docs.rapids.ai/releases/planning/) for the column definition that pertain to the Relase Board.

**IMPORTANT:** 
Leveraging the tracking boards for issues management: PICs can _schedule_ issues by placing them in the appropriate column and then _prioritize_ issues by dragging & sorting the issues from highest priority at the top of the column to lowest at the bottom.

By placing the issues in one of these boards (Bug Squashing, Feature Planning, or Other Issues filers and the community will see updates to the issue and can get a sense of when they can expect feedback. For example, on a given issue a user may see `Future release in Other Issues` and this allows the filer or the community to comment on if they believe the issue should be addressed faster.

## Process cycle

The general process cycle for every issue is:

```
                                                  /------------> Hotfix --> Assign developer --> Link to PR --> Automatically close issue on PR merge
                                                  |
New issue filed --> Initial triage --> Prioritize & schedule --> Next release --> Prioritize in release --> Assign developer --> Link to PR --> Automatically close issue on PR merge
                                                  |
                                                  \------------> Future release --> Re-prioritize every week
```

Issues can be closed during the `Initial triage` step and will be appropriately documented as to why. Examples include: duplicate issues, issues determined to be out of scope, and/or issues that won't be fixed.

### New issue filed

New issues are typically filed with an issue template from the project. This automatically labels an issue with the type of the issue and the <span class="label" style="background: #e99695; color: #44434d; text-transform: none">? - Needs Triage</span> label. This helps identify and move issues to the correct project boards for triage.

For issues not using the issue template, these should be marked with the <span class="label" style="background: #e99695; color: #44434d; text-transform: none">? - Needs Triage</span> label and correct issue type label. Once labeled they should be moved to the appropriate project board for the given issue type.

### Finding issues

Each tracking board type has a filter that can be used on when using the `Add cards` feature. This limits the results displayed to those that are for the tracking board and does not show pull requests.

| Board | Filter |
|:------|:-------|
| Bug Squashing | `is:open is:issue label:bug no:project` |
| Feature Planning | `is:open is:issue label:"feature request" no:project` |
| Other Issues | `is:open is:issue -label:bug -label:"feature request" no:project` |

### Initial triage

Project Leads - Daily
{: .label .label-blue}

1. Ensure the issue type is correct, i.e. is the issue really a bug or is it a feature request?
2. Review the content of the issue, has the filer provided all of the needed information for that issue type? If not, ask for clarification.
3. Add any relevant project labels like `cuda`, `python`, etc.
4. Consider adding <span class="label" style="background: #7057ff; color: #ffffff; text-transform: none">good first issue</span> or <span class="label" style="background: #008672; color: #ffffff; text-transform: none">help wanted</span> labels to the issue if applicable.
4. Remove the <span class="label" style="background: #e99695; color: #44434d; text-transform: none">? - Needs Triage</span> label.
5. Move issue to its associated tracking board. This will place the issue in the `Needs prioritizing` column of that board and read for the next phase.

### Prioritize & schedule

Once issues have been triaged, we can prioritize and schedule them for a release. 

**IMPORTANT:** Leveraging the tracking boards for issues, we can _schedule_ issues by placing them in the appropriate column and then _prioritize_ issues by dragging & sorting the issues from highest priority at the top of the column to lowest at the bottom.

Project Leads - Daily
{: .label .label-blue}

1. For each issue in the `Needs prioritizing` column, review the issue and prioritize it.
2. For issues added to `Hotfix` and  `Next release` columns follow the steps below.
3. Repeat this process for all 3 tracking boards.

Project Leads - Weekly
{: .label .label-blue}

1. Archvie all issues in the `Closed` column.
2. Review all issues in each column of `Next release`, `Future release`, and `Backlog` to make sure issues are still scheduled appropriately.
3. Prioritize any issues in `Future release`, and `Backlog` columns. `Hotfix` and `Next release` do not need to be re-prioritized as they should be in active development already.
4. Discuss the status of all issues in `Hotfix` and `Next release` columns to ensure development progress is being made and there are no blockers.
5. Repeat this process for all 3 tracking boards.

#### Hotfix

1. Verify the issue is a [hotfix]({{ site.url }}{{ site.baseurl }}/releases/hotfix).
2. Identify the project lead(s) needed to resolve the hotfix.
3. Host a meeting about the proposed hotfix with the stakeholders and operations to determine the path forward.
4. Assign a developer or team to fix the issue ASAP.

#### Next release

1. Ensure each issue is added to the release board project.
2. Communicate to the project lead(s) the priority of the issue.
3. Update the issue on the release board with the agreed upon priority.
4. Based on priority of the issue assign a developer or wait for other higher priority issues to be completed first.

### Assign developer

Developers should be assigned to issues as they are responsible for and limit overcommitting developers. A general rule is to limit active development to **5 or fewer** issues.

**IMPORTANT:** This is crucial for community involvement as an assigned issue looks like the issue is covered and won't receive any input or help.

### Link to PR

Every [Pull Request]({{ site.url }}{{ site.baseurl }}/contributing/prs) should have the issue number in the descriptions of the PR with `Addresses #[issue number]` so when the PR is merged the issue that created the PR will automatically close as well.
