---
layout: default
nav_order: 1
parent: Releases
title: Issue Triage
---

# Issue Triage

## Overview

Summary of the issue triage methodology used for RAPIDS projects.

### Intended audience

Project Leads
{: .label .label-blue}

### See also

- Issue Types?

## Triage goals

RAPIDS projects are continuously triaging new issues and re-triaging existing issues frequently. This is to ensure that high priority issues are remedied in a timely manner and the community receives frequent updates on a filed issue.

## Triage process

### Timing 

- Label and prioritize new issues within **2 business days**
- Re-prioritize existing issues **every week** using the project's issue tracking boards

### Tracking boards

For each project there are 3 issue tracking boards:

- [Bug Squashing](https://github.com/rapidsai/cudf/projects/1) - track and prioritize bugs
- [Feature Planning](https://github.com/rapidsai/cudf/projects/9) - track and prioritize feature requests
- [Other Issues](https://github.com/rapidsai/cudf/projects/10) - track documentation, questions, and other issues

These boards are permanent, and are used as the basis for release planning. The example boards above are from the [cuDF](https://github.com/rapidsai/cudf) project.

Each project board has the following columns:

| Column | Purpose |
|:-------|:--------|
| Needs prioritizing | Issues that have gone through the `Initial triage` phase and now need to be prioritized |
| Hotfix - current release | Hotfix issues that need to be addressed immediately for the current `M.A` release |
| Next release | Issues that should tackled during the current development cycle for the next `M.B` release |
| Future release | Issues that should be prioritized for the next `M.C` or `M.D` releases |
| Backlog | All other open issues |
| Closed | Issues that are closed will **automatically** be moved to this column |

By placing the issues in one of these boards filers and the community will see updates to the issue and can get a sense of when they can expect feedback. For example, on a given issue a user may see `Future release in Other Issues` and this allows the filer or the community to comment on if they believe the issue should be addressed faster.

### Process cycle

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

### Initial triage

For every new issue the following should be done:

1. Ensure the issue type is correct, i.e. is the issue really a bug or is it a feature request?
2. Review the content of the issue, has the filer provided all of the needed information for that issue type? If not, ask for clarification.
3. Add any relevant project labels like `cuda`, `python`, etc.
4. Consider adding <span class="label" style="background: #7057ff; color: #ffffff; text-transform: none">good first issue</span> or <span class="label" style="background: #008672; color: #ffffff; text-transform: none">help wanted</span> labels to the issue if applicable.
4. Remove the <span class="label" style="background: #e99695; color: #44434d; text-transform: none">? - Needs Triage</span> label.
5. Move issue to its associated tracking board. This will place the issue in the `Needs prioritizing` column of that board and read for the next phase.

### Prioritize & schedule

Once issues have been triaged, we can prioritize and schedule them for a release.

Project Leads - Daily
{: .label .label-blue}

1. For issues in the 


Project Leads - Weekly
{: .label .label-blue}

1. For 

### Hotfix

...

### Next release

...

### Future release

...

### Assign developer

...


### Link to PR

...

## How-to

### Daily

...

### Weekly

...
