# Contributing to RAPIDS Docs

## Environment setup

- Install Ruby
- Install Bundler
- Checkout repo
- Run `bundle install` in checked out repo

## Development

```
bundle exec jekyll serve
```

### Local Docker development

Alternatively, you can use the [jekyll-docker](https://github.com/envygeeks/jekyll-docker) container to build and serve the `docs` site locally:

```
docker run --rm \
  --volume="$PWD:/srv/jekyll" \
  --publish [::1]:4000:4000 \
  jekyll/jekyll \
  jekyll serve
```

## PR submissions

Once you have code changes, submit a PR to the docs site. Netlify will generate
a preview of your changes and the team will review.
