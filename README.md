# NVIDIA CUDA-X libraries for Data Science Documentation

This repository contains the source for the [NVIDIA CUDA-X libraries for data science documentation site](https://docs.nvidia.ai/datascience). The site is built
with Sphinx and the NVIDIA Sphinx theme.

## Build the site

Install [uv](https://docs.astral.sh/uv/), then run:

```shell
make html
make serve
```

The rendered site is written to `_site`. The server uses port 8000 by default;
override it with `PORT` (for example, `make serve PORT=8080`).

Builds use `https://docs.nvidia.com/datascience/` as the default base URL.
Set `RAPIDS_DOCS_BASE_URL` to override it.

## Validation

Run linting, tests, a strict Sphinx build, and rendered-site validation:

```shell
make check
```

This applies the CUDA-X Library for Data Science and it's version selectors for its imported documentation.

## Publishing

Merges to `main` and the daily scheduled workflow publish the portal to
`docs.nvidia.com/datascience/` using the shared `publish-docs` action.
The independently published `datascience/deployment/` subtree is excluded from
uploads and deletions. A manual run with the `dry-run` input builds everything
and skips the upload, the CDN flush, and the production Netlify deploy.

## Compatibility site

`docs.rapids.ai` continues to host unmigrated API documentation and redirect
migrated content. The `compat` job in the [deploy workflow](.github/workflows/deploy.yaml)
imports the remaining API docs from S3 and publishes them to Netlify, and runs
only after the portal publish to `docs.nvidia.com` has succeeded.

## Repository layout

- `sphinx/` contains the Sphinx configuration, templates, and theme overrides.
- `extensions/` contains custom code extending Sphinx for this site.
- `ci/` contains code used by automated testing and deployment jobs.
- `scripts/` and `tests/` validate rendered routes, content, and publication
  behavior.
