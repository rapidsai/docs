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
