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
- Re-prioritize existing issues **every week** using project boards

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

New issues are typically filed with an issue template from the project. This automatically labels an issue with the type of the issue and the <span class='label' style='background: #e99695'>? - Needs triage</span> label. This helps identify and move issues to the correct project boards for triage.

For issues not using the issue template, these should be marked with the <span class='label' style='background: #e99695'>? - Needs triage</span> label and correct issue type label. Once labeled they should be moved to the appropriate project board for the given issue type.

### Initial triage

...

### Prioritize & schedule

...

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
