---
layout: default
nav_order: 6
parent: Resources
grand_parent: Maintainer Docs
title: Versions and Tags
---

# Versions and Tags

## Overview

Summary of the versioning and release methodology used by RAPIDS projects.

### Intended audience

Community
{: .label .label-yellow}

Developers
{: .label .label-green}

Project Leads
{: .label .label-blue}

## Versioning method

All RAPIDS projects use the [CalVer](https://calver.org/) versioning method for all releases starting with June 2021 release.

The RAPIDS team is aware of the impacts that public API changes cause to users, so API & ABI compatibility is guaranteed within each `YY.MM` version.

## Release types and tagging

Using CalVer for versioning, RAPIDS projects use the notation `YY.MM.PP` for releases/tags where `YY` indicates the zero padded year, `MM` indicates the zero padded month, and `PP` indicates the zero padded hotfix/patch version. Each release is accompanied by a tag in the git repo with the same formatting and leading `v`.

### Hotfix/Patch

A hotfix/patch release occurs for the current release, incrementing the hotfix/patch version number by 1.

There is no limit or time constraint of these releases as they are governed by the need to fix critical issues in the current release. Generally, hotfix/patch releases contain only one change and are typically bug fixes; new features should not be introduced in this way.

## Cleaning up accidental publications on anaconda.org

These commands require that the logged-in user (`anaconda login`) is in the owner group for the involved channels. More information on how to manage groups and channels ("organizations") is on [Anaconda's documentation](https://www.anaconda.com/docs/tools/anaconda-org/user-guide/work-with-groups).

### Remove all files for a given package name with a specific version

When release procedures are not well-established or some other accident has resulted in packages that may cause problems, we need to remove packages.

`anaconda remove <channel>/<package>/<version>`

A real example of this would be removing an accidentally published package for rapids-logger, with a version that doesn't make sense:

`anaconda remove rapidsai-nightly/rapids-logger/0.2.27`

### Copy files from one channel to another

 The recommended install command right now is `conda create -n rapids-25.10 -c rapidsai-nightly -c conda-forge -c nvidia rapids=25.10 python=3.13 'cuda-version>=12.0,<=12.9'`. If a release is uploaded to the rapidsai channel and not the rapidsai-nightly channel, our install command will not see the packages on the `rapidsai`. If both channels were added, we would have to be very careful about strict channel priority, which could easily pick up older or alpha releases.

 One solution to this is to just copy the published packages to both `rapidsai` and `rapidsai-nightly`.

`anaconda copy <source channel>/<package>/<version> --to-owner <destination channel>`

and a real example:

`anaconda copy rapidsai/rapids-logger/0.2.2 --to-owner rapidsai-nightly`
