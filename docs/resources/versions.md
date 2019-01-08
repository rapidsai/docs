---
layout: default
nav_order: 2
parent: Resources
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

Managers
{: .label .label-blue}

## Versioning method

All RAPIDS projects use the [SemVer](https://semver.org/) versioning method for all releases. 

It is **important** to be aware that RAPIDS, like other `v0.Y.Z` projects, makes use of [SemVer specification item #4](https://semver.org/#spec-item-4):

> Major version zero (0.y.z) is for initial development. Anything may change at any time. The public API should not be considered stable.

The RAPIDS team is aware of the impacts that public API changes cause to users, even pre `v1.0.0`, so we will do our best to avoid them if possible. In a circumstance where they are unavoidable, the RAPIDS team will create a new minor release with documentation on how to migrate. This way users are able to stay operating on an older stable release, while they can test and adopt the new changes in the current release.

## Release types and tagging

Using SemVer for versioning, RAPIDS projects use the notation `vX.Y.Z` for releases/tags where `X` indicates the major version, `Y` indicates the minor version, and `Z` indicates the hotfix/patch version. Each release is accompained by a tag in the git repo with the same formatting and leading `v`. Below is a description of each release type:

### Major

A major release occurs in two ways:
- Pre `v1.0.0` - voting from the RAPIDS team on whether the following have been achieved:
  - the API is stable enough to not trigger another major release within an agreed upon timeframe
  - the project goals to achive a major release are met
- Post `v1.0.0` - following the SemVer convetions, breaking API changes will trigger this release

Major releases result in incrementing the major version number by 1 and resetting the minor & hotfix/patch version numbers to 0.

### Minor

A minor release occurs after a development cycle has been completed, incrementing the minor version number by 1 and resetting the hotfix/patch version number to 0. 

The goals of this release are to introduce new features and bug fixes for the previous release. 

### Hotfix/Patch

A hotfix/patch release occurs for the current minor release, incrementing the hotfix/patch version number by 1. 

There is no limit or time constraint of these releases as they are governed by the need to fix critical issues in the current release. Generally, hotfix/patch releases contain only one change and are typically bug fixes; new features should not be introduced in this way.
