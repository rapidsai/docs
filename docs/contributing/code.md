---
layout: default
nav_order: 2
parent: Contributing
title: Code Contributions
---

# Code Contributions

## Overview

Outlines the best way for developers and the community to contribute to RAPIDS projects.

Contributions can be made in three ways:
- [File a bug report]({{ site.baseurl }}docs/contributing/issues)
- [Suggest a new feature or improvement]({{ site.baseurl }}docs/contributing/issues)
- [Implement code for an issue](#your-first-issue)

### Intended audience

Community
{: .label .label-yellow}

Developers
{: .label .label-green}

### See also

- [Issues]({{ site.baseurl }}docs/contributing/issues)
- [Pull Requests]({{ site.baseurl }}docs/contributing/prs)

## New developers

If you are new to RAPIDS, make sure to check out <https://rapids.ai/> to help understand the purpose of RAPIDS.

### Your first issue

1. Read the project's README to learn how to setup the development environment
2. Find an issue to work on. The best way is to look for the <span class="label" style="background: #7057ff; color: #ffffff; text-transform: none">good first issue</span> or <span class="label" style="background: #008672; color: #ffffff; text-transform: none">help wanted</span> labels
3. Comment on the issue saying you are going to work on it
4. Code! Make sure to update unit tests!
5. When done, [create your pull request]({{ site.baseurl }}docs/contributing/prs)
6. Verify that CI passes all [status checks](https://help.github.com/articles/about-status-checks/). Fix if needed
7. Wait for other developers to review your code and update code as needed
8. Once reviewed and approved, a RAPIDS developer will merge your pull request

Remember, if you are unsure about anything, don't hesitate to comment on issues and ask for clarifications!

## Seasoned developers

Once you have gotten your feet wet and are more comfortable with the code, follow these steps to find prioritized issues.

All RAPIDS projects have project boards for triaging [issues]({{ site.baseurl }}docs/releases/issue-triage) and planning [features]({{ site.baseurl }}docs/releases/planning).

### What do I work on?

__Note:__ If you are have been assigned issues, work on those issues first.

For all others:

1. Find the project board for the next release (named `[version] Release`)
2. Issues are prioritized from high to low: `P0`, `P1`, and `P2`.
<br>Within each column, the issues are ordered top to bottom from most important to least.
3. Select the highest priority issue that you are comfortable working on
4. If you are in the RAPIDS org, assign the issue to yourself. If not, comment on the issue saying you are going to work on it
5. Code! Make sure to update unit tests!
6. When done, [create your pull request]({{ site.baseurl }}docs/contributing/prs)
7. Verify that CI passes all [status checks](https://help.github.com/articles/about-status-checks/). Fix if needed
8. Wait for other developers to review your code and update code as needed
9. Once reviewed and approved, a RAPIDS developer will merge your pull request

### Reviewing pull requests

1. Find the project board for the next release (named `[version] Release`)
2. Scroll right to find the `PR-Needs Review`
3. Review the PR (Make sure you follow the [Code of Conduct]({{ site.baseurl }}docs/resources/conduct))

If you are maintainer, also review pull requests in the `PR-Reviewer Approved` column and merge as needed.
