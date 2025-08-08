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

### Local macOS development

Upgrade to a new-enough ruby and install `jekyll`, like following https://jekyllrb.com/docs/installation/macos/

```shell
# (one-time) get ruby env-management stuff
brew install chruby ruby-install

# (one time) update to newer ruby
ruby-install ruby 3.4.1

source $(brew --prefix)/opt/chruby/share/chruby/chruby.sh
source $(brew --prefix)/opt/chruby/share/chruby/auto.sh
chruby ruby-3.4.1
ruby -v

# (one time) install Bundler
gem install bundler

# install everything else the project needs
bundle install
```

Build the site (this populates the `_site/` folder)

```shell
bundle exec jekyll build --verbose
```

At this point, the API documentation will not be populated.

To test those and the post-processing that happens on them, get read-only AWS credentials for the relevant resources
and put them in a profile called `[rapids-docs]` in your AWS CLI configuration.

```shell
export AWS_DEFAULT_PROFILE="rapids-docs"
ci/download_from_s3.sh
```

At this point, the site is now built and the API documentation has been downloaded.
Next, some post-processing needs to be done to point links like `/stable` (including those in drop-down selectors)
to the appropriate documentation files.

Those steps include a `pip install`, so create and active a Python virtual environment first.

```shell
python -m venv rapids-docs-env
source ./rapids-docs-env/bin/activate
```

Then run the post-processing.

```shell
ci/post-process.sh
```

At this point, you should be able to view the site locally with a pretty similar experience to what's hosted in deployments.

`jekyll serve` cleans and re-generates the `_site/` folder, but it also does some other bundling and packaging that's needed for links and formatting
to work correctly.

First, back up the `api/` directory:

```shell
BACKUP_DIR=$(mktemp -d)
cp -avR ./_site/api "${BACKUP_DIR}"
```

Then serve the site.

```shell
bundle exec jekyll serve
```

Once it's up, copy all the `api/` files back in.

```shell
cp -avR "${BACKUP_DIR}/api" _site
```

`jekyll serve` should automatically pick up the changes.

In a browser, navigate to the URL shown in the `jekyll serve` output (probably something like `http://127.0.0.1:4000/`) to see the rendered docs.

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
