---
layout: default
nav_order: 3
parent: Resources
title: Git Methodology 
---

# Git Methodology

## Overview

Details on our git branching method used for RAPIDS and our style conventions for git commits.

### Intended audience

Community
{: .label .label-yellow}

Developers
{: .label .label-green}

### See also

* [Versioning and Tagging]({{ site.baseurl }}docs/resources/versions)
* [Hotfix releases]({{ site.baseurl }}docs/releases/hotfix)
* [Major and minor releases]({{ site.baseurl }}docs/releases/process)

## Git branching

### Approach

Our development approach involves protecting the `master` branch so that it becomes the official release record for any RAPIDS project. Development PRs will be merged into a release branch, which will be merged into master and tagged only when the release is ready. The only other merges to `master` are hotfixes.

### Development workflow

All PRs are merged into a release branch named `branch-M.B` where `M` is the major version and `B` is the minor version number. Release branches are created from the previous release branch when the decision has been made to **freeze** the release. 

To **freeze** a release branch is to stop new development for the release, and focus on completing outstanding features and any bugs discovered from testing. Once this **freeze** happens a new branch `branch-M.C` (where `C=B+1`) is created so development can continue. Updates to `branch-M.B` can be merged as needed to `branch-M.C`, but generally will wait until the release is finished. This means that `branch-M.X` (where `X` is the highest minor version) the latest and greatest code.

Hotfixes (patch releases) related to the current release `M.A` are directly merged to `master` from a PR and then those changes are also merged to the current release branches in progress through an automated process. All merges to `master` trigger an automated CI job that will produce a new release and tag incrementing the patch version off of the previous highest tag in the repo. Once the tag is set, the automated CI build for conda packages creates and pushes new packages for users. This includes the version change enabling known good builds and the ability to rollback.

Minor (and eventually, Major) release development takes place on the current release branch. PRs can be edited on GitHub to set the target base branch for merging the PR. It is the reviewer’s responsibility to ensure the PR is targeted for the correct and planned release branch. Once PRs have passed all tests, they are merged to their release branch, which triggers an automated CI build for conda packages that will be marked as development, such as M.N-dev1. These can be inspected by the team to ensure the build works as intended and perform larger testing.

Once a release has been reviewed and signoff has been given, a PR is created to merge the release branch to master. After the merge, the automated tagging process tags and releases a minor version and kicks off the conda builds for the public release.

### Summary

- The `master` branch is the official release history (including hotfixes).
  - The tip of `master` is intended to be always working given the testing and reviews of merged PRs.
  - Hotfixes (patch releases) are automatically tagged for every push to `master`.
- Release branches are used for development of the next releases and **all PRs except for hotfixes** are merged to the current release branch.
  - A new release branch is created from the previous release branch after the release **freeze** (see above).
  - After the **freeze** and before the release branch is merged, there are two release branches; however, active development should take place in the next release branch, while cleanup and finalization happens in the frozen branch.
  - This gives the highest numbered `branch-M.X` (modulo hot fixes and unmerged frozen release fixes) the latest and greatest code.
- Minor releases are done by creating a PR for the minor release from the associated release branch.
  - After review and sign off by the team, the PR is merged into master.

## Git commits

Git commit messages should convey the change succinctly, but with enough detail to be understood without extra context.

### Commit tags

Consider starting the first line with a tag (e.g. `DOC Update conda install process`):

| Tag | Description                          |
|:----|:-------------------------------------|
| ENH | Enhancement, new functionality       |
| BUG | Bug Fix                              |
| DOC | Additions/updates to documentation   |
| TST | Additions/updates to tests           |
| BLD | Updates to the build process/scripts |
| PRF | Performance improvement              |
| CLN | Code cleanup                         |

These help communicate the actions that are being taken, and help others when trying to review changes in a PR.

### First line

The *first line* should be a short description of the changes made, keeping the following in mind:
- Limit the *first line* to 72 characters or less; use a *third line* for a detailed description
- Begin the *first line* with a commit tag from the table above
- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")

### Multi-line git messages

The *second line* should **always be empty**, if you need to add addtional details start on the *third line*.

For the third and successive lines, keep the following in mind:
- Detail the changes and implementation details
- Reference issues and pull requests by their number, for example `#47`
- Use `- ` to show elements of a list, starting a new line for each new list item

### Sample git commits

Single-line git commit message:
```
DOC Update conda install process
```

Multi-line git commit message:
```
DOC Update conda install process

- This corrects bug #47 that prevents users from installing X because of Y...
- Also fixed spelling mistakes and an incorrect version number
```
