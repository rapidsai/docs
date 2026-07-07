# NVIDIA RAPIDS Documentation

This repository contains the source for the
[NVIDIA RAPIDS documentation portal](https://docs.rapids.ai/). The portal is
built with Sphinx and the NVIDIA Sphinx theme.

## Build the portal

Install [uv](https://docs.astral.sh/uv/), then run:

```shell
make html
make serve
```

The rendered portal is written to `_site`. The server uses port 8000 by default;
override it with `PORT` (for example, `make serve PORT=8080`).

## Build the complete site

The complete docs site imports versioned API documentation and the deployment
documentation from the private `rapidsai-docs` S3 bucket. Configure a read-only
AWS profile named `rapids-docs`, then run:

```shell
AWS_PROFILE=rapids-docs make full
```

This preserves the stable, latest, nightly, and legacy aliases and applies the
RAPIDS library/version selectors to the imported documentation.

## Validation

```shell
make check
```

This runs Python linting, unit tests, a warning-free Sphinx build, and output
validation.

Pull requests opened against `rapidsai/docs` are copied to a
`pull-request/<number>` branch by the RAPIDS copy-PR bot. That branch runs the
same validation and dry-runs assembly of the complete S3-backed documentation
tree without deploying it. Netlify's repository integration separately creates
a portal-only preview. Merges to `main` continue to deploy the production site.

## Repository layout

- Portal content, data, includes, and assets retain their established paths at
  the repository root.
- `sphinx/` contains the Sphinx configuration, templates, and theme overrides.
- `extensions/` contains the portal's data-rendering and publication extension.
- `ci/` downloads and post-processes versioned API and deployment documentation.
- `scripts/` and `tests/` validate rendered routes, content, and publication
  behavior.

## Migration history

The Sphinx portal was initially migrated from the Jekyll site at
[`rapidsai/docs@b6afa0c`](https://github.com/rapidsai/docs/commit/b6afa0cbf4ddfc4c0a21f7c79b18631f214fd759).
