---
layout: default
nav_order: 3
parent: Maintainer Docs
title: Forward Mergers
---

# Forward Mergers

## Overview

The forward mergers are automated pull requests to merge a branch in burndown into the next versioned branch. For example merging `branch-22.12` into `branch-23.02`. This ensures all changes to the current branch are reflected in the next version.

Forward merging is implemented with the [ops-bot](https://github.com/rapidsai/ops-bot) forward-merger plugin. The plugin is activated for a repository by adding `forward_merger: true` to `.github/ops-bot.yaml`.

### Intended audience

Developers
{: .label .label-green}

Project Leads
{: .label .label-blue}

Operations
{: .label .label-purple}

## Forward Mergers

During the release process, the branch for the next release is created and set as default. For any repository in which the `forward-merger` plugin is enabled, forward-mergers automatically merge any commits made to the release branch to the latest default branch during burn down.

**When Forward Merging Fails**

It is important to note that the forward-merge jobs will sometimes fail due to merge conflicts, and will request a manual merge to be done. *Never* use the GitHub Web UI to fix the merge conflicts as it will cause changes in the default branch to be merged into the release branch. Please use the following steps to fix the merge conflicts manually:

Using the example of `branch-{{ site.data.releases.stable.version }}` release branch and a new default `branch-{{ site.data.releases.nightly.version }}`.

```sh
git checkout branch-{{ site.data.releases.stable.version }}
git pull <rapidsai remote>
git checkout branch-{{ site.data.releases.nightly.version }}
git pull <rapidsai remote>
git checkout -b branch-{{ site.data.releases.nightly.version }}-merge-branch-{{ site.data.releases.stable.version }}
git merge --no-squash branch-{{ site.data.releases.stable.version }}
# Fix any merge conflicts caused by this merge
git commit -am "Merge branch-{{ site.data.releases.stable.version }} into branch-{{ site.data.releases.nightly.version }}"
git push <personal fork> branch-{{ site.data.releases.nightly.version }}-merge-branch-{{ site.data.releases.stable.version }}
```

Once this is done, open a PR that targets the new default branch (`branch-{{ site.data.releases.nightly.version }}` in this example) with your changes.

**IMPORTANT**:
- When merging this PR, do not use the [auto-merger]({% link resources/auto-merger.md %}) (i.e. the `/merge` comment). Instead, use the `/merge nosquash` comment. This ensures that branch history is preserved and branches remain compatible.

Once this PR is merged, the original forward-merger PR should automatically be merged since it will contain the same commit hashes.
