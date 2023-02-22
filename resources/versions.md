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
