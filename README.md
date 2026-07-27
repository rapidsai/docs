# NVIDIA RAPIDS Documentation

This repository contains the source for the
[NVIDIA RAPIDS documentation site](https://docs.rapids.ai/). The site is built
with Sphinx and the NVIDIA Sphinx theme.

## Build the site

Install [uv](https://docs.astral.sh/uv/), then run:

```shell
make html
make serve
```

The rendered site is written to `_site`. The server uses port 8000 by default;
override it with `PORT` (for example, `make serve PORT=8080`).

## Build the full site

The complete docs site imports versioned API documentation and the deployment
documentation from the private `rapidsai-docs` S3 bucket. Configure a read-only
AWS profile named `rapids-docs`, then run:

```shell
AWS_PROFILE=rapids-docs make full
```

This applies the RAPIDS library/version selectors to the imported documentation.

## Validation

```shell
make check
```

Run checks including linting, tests, and a local build.

Pull requests opened against `rapidsai/docs` are copied to a
`pull-request/<number>` branch by the RAPIDS copy-PR bot. That branch runs the
same validation and dry-runs assembly of the complete S3-backed documentation
tree without deploying it. Netlify's repository integration separately creates
a site preview. Merges to `main` deploy the production site.

## Repository layout

- `sphinx/` contains the Sphinx configuration, templates, and theme overrides.
- `extensions/` contains custom code extending Sphinx for this site.
- `ci/` contains code used by automated testing and deployment jobs.
- `scripts/` and `tests/` validate rendered routes, content, and publication
  behavior.
