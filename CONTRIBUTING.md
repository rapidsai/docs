# Contributing to RAPIDS Docs

## Environment setup

Install [uv](https://docs.astral.sh/uv/), check out the repository, and install
the locked development environment:

```shell
uv sync --locked
```

## Development

Build the portal and serve the rendered site at <http://localhost:8004/>:

```shell
make html
make serve
```

Pass a different port when needed:

```shell
make serve PORT=8080
```

Run the complete credential-free validation suite before submitting a change:

```shell
make check
```

This runs formatting and lint checks, unit tests, a strict Sphinx build, and
route and rendered-content validation.

## Full documentation assembly

The portal-only build does not include the versioned API documentation or the
deployment documentation. To test the complete site and its post-processing,
obtain read-only AWS credentials for the documentation bucket and configure an
AWS CLI profile named `rapids-docs`. Then run:

```shell
AWS_PROFILE=rapids-docs make full
```

This builds the Sphinx portal into `_site`, downloads the imported
documentation, creates the stable, latest, nightly, and legacy aliases, adds
the RAPIDS library and version selectors, and validates the assembled site.
Serve the result without rebuilding it with:

```shell
make serve
```

## PR submissions

Submit changes as a pull request to `rapidsai/docs`. The RAPIDS copy-PR bot
copies the pull request head to a `pull-request/<number>` branch in the upstream
repository. CI validates that branch, assembles the complete documentation
site, and creates a non-production Netlify preview for review.

## Developer Certificate of Origin

All contributions to this project must be accompanied by a sign-off indicating
that the contribution is made pursuant to the Developer Certificate of Origin
(DCO). This is a lightweight way for contributors to certify that they wrote
or otherwise have the right to submit the code they are contributing to the
project.

The DCO is a simple statement that you, as a contributor, have the legal right
to make the contribution. To certify your adherence to the DCO, you must sign
off on your commits. This is done by adding a `Signed-off-by` line to your
commit messages:

```text
Signed-off-by: Random J Developer <random@developer.example.org>
```

You can do this automatically with `git commit -s`.

Here is the full text of the DCO, which you can also find at
<https://developercertificate.org/>:

```text
Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.
```
