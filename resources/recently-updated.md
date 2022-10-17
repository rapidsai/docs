---
layout: default
nav_order: 6
parent: Resources
grand_parent: RAPIDS Maintainer Docs
title: Recently Updated Check
---

# _Recently Updated_ Check

## Overview

A GitHub action that checks whether a pull-request is up-to-date with the latest changes from the source repository.

### Intended audience

Community
{: .label .label-yellow}

Developers
{: .label .label-green}

Project Leads
{: .label .label-blue}

Operations
{: .label .label-purple}

## Summary

GitHub Actions are configured to run tests on the _HEAD_ commit of pull requests (e.g. not the pull request's merge commit, which would be the result of merging the pull request into the target branch).

Therefore, if a pull request is not up-to-date with the latest changes in the source repository, there is a possibility that breaking changes could be introduced even if the CI tests are passing.

GitHub does provide a way to ensure that pull requests are entirely up-to-date before merging, but for high volume repositories like `cudf`, this would dramatically increase the amount of time it takes to get a pull request merged.

As a compromise, the _Recently Updated_ check has been introduced to ensure that pull requests are "reasonably up-to-date" with the corresponding source repository.

This method doesn't guarantee that breaking changes will not be introduced, but it does help provide some assurances that pull requests aren't significantly out-of-date (similar to how testing merge commits work).

Additional testing confidence comes from RAPIDS' nightly testing, which tests the _HEAD_ commit of each development branch.

The _Recently Updated_ check is configurable by editing the following values in the `.github/ops-bot.yaml` file:

```yaml
# enables/disables the Recently Updated Check
recently_updated: true

# sets the threshold for how many commits behind the pull request must be to trigger a failure.
# defaults to 5 if not set
recently_updated_threshold: 5
```

Note that since RAPIDS uses squash commits for pull requests, the `recently_updated_threshold` value effectively means "how many pull requests have been merge into the source repository since the current pull request has last been updated".
