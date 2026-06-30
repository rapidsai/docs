---
layout: default
nav_order: 4
parent: Release Docs
grand_parent: Maintainer Docs
title: Release Data Maintenance
---

# Release Data Maintenance

This runbook defines which files contain release policy, which files are generated,
when to run each automation command, and which decisions still require a human.
Use it for normal support updates, release preparation, release-day rollover, and
delayed API documentation publication.

## Source of truth

RAPIDS docs intentionally has several focused sources of truth. Do not combine
these domains into one file: their policies have different owners and schedules.

| Policy domain | Source of truth | What maintainers decide |
| --- | --- | --- |
| Release channels, dates, phases, cohorts, and UCXX versions | `_data/release_calendar.yml` | The four channel assignments, future schedule dates, and cohort membership |
| Platform support | `_data/platform_support.yml` | Python, CUDA, driver, GPU, OS, architecture, and source-build support per release |
| API documentation projects | `_data/docs.yml` | Published channels, version overrides, release version field, and root redirect behavior |
| Exceptional redirects | `_data/redirects.yml` | Redirects that cannot be derived from a docs project |
| Install selector package policy | `_data/install_packages.yml` | Package names, method availability, bundles, lifecycle, dependencies, PyPI status, and CUDA constraints |
| Notices | `_notices/*.md` | Notice prose, status, dates, version, topic, and pinning |

The current installation requirements, platform support page, and install selector
all consume `_data/platform_support.yml`. A support change belongs there first.

### Generated files

The following files are projections. **Never edit them directly.** A direct edit
will be overwritten and CI will reject it if it does not match its source data.

| Generated file | Generator | Inputs |
| --- | --- | --- |
| `_data/releases.json` | `ci/generate-release-data.py` | `_data/release_calendar.yml`, `_data/platform_support.yml` |
| `_data/previous_releases.json` | `ci/generate-release-data.py` | `_data/release_calendar.yml`, `_data/platform_support.yml` |
| `ci/customization/projects-to-versions.json` | `ci/generate-projects-to-versions.py` | `_data/docs.yml`, generated release channels |
| `_redirects` | `ci/generate-projects-to-versions.py` | `_data/docs.yml`, `_data/redirects.yml`, generated release channels |

Pre-commit runs the generators in dependency order: release projections first,
then docs artifacts. Generated changes belong in the same commit as their source
change so reviewers can see the complete effect.

## Release cadence

### During development

Make policy changes when they become known instead of waiting for release day.

1. Update `_data/platform_support.yml` when support policy changes. Exactly the
   release used by the `nightly` channel must have `nightly: true`.
2. Update `_data/install_packages.yml` when a package joins or leaves the selector,
   changes package names, changes bundle membership, or gains PyPI availability.
3. Update `_data/docs.yml` when a project starts or stops publishing an API docs
   channel. Every stable-enabled project must explicitly choose a generated stable
   redirect, an absolute custom target, or `redirect: false`.
4. Add notices with `ci/new-notice.py` as soon as a user-facing policy decision is
   ready to announce. Automation creates front matter only; authors own the prose.

Run the relevant generator after every source edit. Running all hooks is the
simplest local check:

```sh
pre-commit run --all-files
```

### Before the rollover PR

Prepare the source records before rotating any channel. For the rollover after
26.08, the new `next_nightly` is 26.12; substitute the appropriate version later.

1. Add a complete `26.12` record to `_data/release_calendar.yml`. Include an ISO
   `released_on` date, all schedule phases, the UCXX version, and a valid cohort set.
2. Confirm the existing `next_nightly` release, 26.10 in this example, has a complete
   platform record. It is about to become `nightly`.
3. Move `nightly: true` in `_data/platform_support.yml` from the old nightly release
   to the release that will become nightly. There must be exactly one marker.
4. Review package lifecycle boundaries. `added_in_release` is the first included
   release; `removed_after_release` is the last included release. For example,
   cuxfilter has `removed_after_release: "26.06"`, so it is absent in 26.08 onward.
5. Review each docs project's legacy, stable, and nightly publication flags. Do not
   enable delayed artifacts merely because a channel rotates.
6. Validate the prepared state without writing:

```sh
./ci/roll-release.py --new-next-nightly 26.12 --dry-run
```

The rollover command deliberately refuses to invent dates, platform policy, docs
availability, or package lifecycle. A failed dry run is a checklist of missing
source decisions, not a reason to bypass validation.

### On release day

After artifacts and support policy are confirmed, rotate the channels once:

```sh
./ci/roll-release.py --new-next-nightly 26.12
```

The command performs this transformation:

| Before | After |
| --- | --- |
| `stable` | `legacy` |
| `nightly` | `stable` |
| `next_nightly` | `nightly` |
| Prepared new release | `next_nightly` |

It then regenerates release projections and docs artifacts. Inspect both source and
generated diffs, review the policy reminders printed by the script, and run:

```sh
./ci/generate-release-data.py --check
./ci/generate-projects-to-versions.py --check
./ci/validate-platform-support.py
./ci/validate-install-packages.py
./ci/validate-notices.py
pre-commit run --all-files
bundle exec jekyll build
node ci/test-selector.mjs
```

The last two commands validate rendered Liquid and selector behavior. They also run
in PR CI, so Ruby is not required on every maintainer workstation.

### After release: delayed API docs

Some projects publish docs after the main rollover. Do not edit
`projects-to-versions.json` to expose them. Update `_data/docs.yml` through the
catalog helper, then regenerate both derived docs artifacts:

```sh
./ci/update-docs-project.py \
  --project cudf-java \
  --channel stable \
  --version 26.06
./ci/generate-projects-to-versions.py
```

The version must match the selected channel or be a point release such as 26.06.1.
Point releases are stored as an explicit `version-overrides` value. The
`deploy-cudf-java-docs` workflow runs this same sequence after uploading docs.

## Common policy updates

### Add a future release

Add the version to `_data/release_calendar.yml` before it is assigned to a channel.
Use `YYYY-MM-DD` dates, reference a declared cohort set, and keep each cohort's
development, burn-down, and code-freeze phases contiguous. The release phase starts
after the latest cohort finishes. Historical exceptions require a documented
`schedule_exception`; do not add one to avoid correcting a new schedule.

### Add or remove a selector package

Edit only `_data/install_packages.yml`. A package may use different display names or
package lists for Conda and pip, and may declare nightly-only dependencies. Set
method-specific bundle membership intentionally. Use inclusive release bounds:

```yaml
added_in_release: "26.04"
removed_after_release: "26.06"
```

When both bounds are present, the added release must not follow the removed release.
Changing docs publication in `_data/docs.yml` does not implicitly change install
availability.

### Add an API docs project

Add one record to `_data/docs.yml`, including channel flags and explicit redirect
behavior. Use `release_version_field: ucxx_version` only for projects that follow
the UCXX release line. Put redirects in `_data/redirects.yml` only when they cannot
be represented by the project record. Then run the docs artifact generator.

### Add a platform support release

Copying a prior record is only a starting point. Platform owners must review every
field, especially CUDA toolkit bounds, driver minimums, compute capabilities, tested
OSes, and source-build dependencies. The install selector and current requirements
page will publish these values immediately when the release becomes stable/nightly.

## Review ownership

Release Operations reviews channel rotation, dates, UCXX versions, and cohorts.
Platform owners review all platform support fields. Project or docs owners review
API publication and redirects. Packaging owners review install package names,
lifecycle, dependencies, and bundle membership. Site maintainers review generator
behavior and rendered output.

Automation propagates approved policy; passing automation is not approval of the
policy itself.

## Recovery

If a generated diff is wrong, correct or revert the corresponding source file and
run its generator again. Do not repair the JSON or `_redirects` output by hand.
`ci/roll-release.py --dry-run` does not write. If a completed rollover must be
undone before merge, restore the prior channel mapping and platform nightly marker,
then regenerate all projections.

The analysis behind these boundaries is recorded in `automation-proposal.md` at the
repository root.
