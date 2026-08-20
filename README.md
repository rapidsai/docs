# NVIDIA RAPIDS Documentation

This repository contains the source for the
[NVIDIA RAPIDS documentation site](https://docs.nvidia.com/datascience/). The site is built
with Sphinx and the NVIDIA Sphinx theme.

## Build the site

Install [uv](https://docs.astral.sh/uv/), then run:

```shell
make html
make serve
```

The rendered site is written to `_site`. The server uses port 8000 by default;
override it with `PORT` (for example, `make serve PORT=8080`).

## Build the docs.rapids.ai compatibility site

The compatibility site imports versioned API documentation and deployment
documentation from the private `rapidsai-docs` S3 bucket. It continues to serve
real API content from `docs.rapids.ai/api/<library>` until each library migrates
to `docs.nvidia.com`. Configure a read-only AWS profile named `rapids-docs`, then
run:

```shell
AWS_PROFILE=rapids-docs make full
```

This applies the RAPIDS library/version selectors to the imported documentation.
Generate the Netlify redirect file after assembly:

```shell
uv run python scripts/generate_redirect_site.py --output _site/_redirects --status 302
```

The generated rules redirect portal pages and only those library versions whose
migration metadata points at `docs.nvidia.com`. Unmatched API routes and shared
assets remain real files in the assembled site.

## Validation

```shell
make check
```

Run checks including linting, tests, and a local build.

Pull requests opened against `rapidsai/docs` are copied to a
`pull-request/<number>` branch by the RAPIDS copy-PR bot. That branch builds the
full `docs.rapids.ai` compatibility site and validates its generated redirects.
Netlify's repository integration separately creates a site preview.

Merges to `main` and the daily scheduled workflow publish the portal to
`docs.nvidia.com/datascience/`. The independently published
`docs.nvidia.com/datascience/deployment/` subtree is explicitly preserved.
The companion compatibility workflow assembles and publishes the remaining API
documentation to `docs.rapids.ai`, with redirects for migrated API versions and
portal routes. Redirects default to temporary status `302`; set the
`DOCS_RAPIDSAI_REDIRECT_STATUS` repository variable to `301` after the cutover is
verified, or select a status in a manual workflow run.

## Repository layout

- `sphinx/` contains the Sphinx configuration, templates, and theme overrides.
- `extensions/` contains custom code extending Sphinx for this site.
- `ci/` contains code used by automated testing and deployment jobs.
- `scripts/` and `tests/` validate rendered routes, content, and publication
  behavior.
