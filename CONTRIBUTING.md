# Contributing to RAPIDS Docs

## Environment setup

- Install Ruby
- Install Bundler
- Checkout repo
- Run `bundle install` in checked out repo

## Development

```sh
bundle exec jekyll serve
```

### Dev Containers

If you're using [VSCode](https://code.visualstudio.com/) you can use the jekyll Dev Container.

- This project contains a devcontainer config:
  - If prompted with "Folder contains a Dev Container configuration file." select "Reopen in Container"
  - Alternatively select "Dev Containers: Reopen in Container" from the command palette
- Run `bundle exec jekyll serve`

### Local Docker development

Alternatively, you can use the [jekyll-docker](https://github.com/envygeeks/jekyll-docker) container to build and serve the `docs` site locally:

```sh
docker run --rm \
  --volume="$PWD:/srv/jekyll" \
  --publish [::1]:4000:4000 \
  jekyll/jekyll \
  bash -c 'rm -rf ./_site && jekyll serve'
```

## PR submissions

Once you have code changes, submit a PR to the docs site. Netlify will generate
a preview of your changes and the team will review.

## Developer Certificate of Origin

All contributions to this project must be accompanied by a sign-off indicating that the contribution is made pursuant to the Developer Certificate of Origin (DCO). This is a lightweight way for contributors to certify that they wrote or otherwise have the right to submit the code they are contributing to the project.

The DCO is a simple statement that you, as a contributor, have the legal right to make the contribution. To certify your adherence to the DCO, you must sign off on your commits. This is done by adding a `Signed-off-by` line to your commit messages:

```
Signed-off-by: Random J Developer <random@developer.example.org>
```

You can do this automatically with `git commit -s`.

Here is the full text of the DCO, which you can also find at <https://developercertificate.org/>:

```
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
