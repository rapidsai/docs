---
layout: default
nav_order: 4
parent: Resources
grand_parent: RAPIDS Maintainer Docs
title: Style Guide
---

# Style Guide

## Overview

Summary of style formats for various aspects of RAPIDS projects.

### Intended audience

Community
{: .label .label-yellow}

Developers
{: .label .label-green}

## Code style

### Python

All Python code in RAPIDS projects is style checked using [`flake8`](https://github.com/PyCQA/flake8)

Individual projects should configure `flake8` to suit their needs, for example to exclude specific directories or files.

## Git commits

Git commit messages should convey the change succinctly, but with enough detail to be understood without extra context.

See the [Git Methodology]({% link resources/git.md %}#git-commits) for further details.

## GitHub Pull Requests

Draft Pull Requests should be opened while work is in progress. This lets other
developers know draft changes are coming without initialing a the review process
immediately. Once the pull request is ready, click "Ready for review" to get
feedback on the changes.