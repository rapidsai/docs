# Contributing to RAPIDS Docs

## Environment setup

- Install Ruby
- Install Bundler
- Checkout repo
- Run `bundle install` in checked out repo

## Development

### Preferred - Excluding API docs

Given the size of the API docs the following config file setup will greatly
speed up renderings:

```
bundle exec jekyll serve --config _config_ignore_api.yml
```

### Alternative - Including API docs

The folder `api/` has a lot of files and can cause the initial and subsequent
renderings to take 30 seconds or more. Running the following command will
include the API docs which can be necessary for debugging purposes:

```
bundle exec jekyll serve
```

## PR submissions

Once you have code changes, submit a PR to the docs site. Netlify will generate
a preview of your changes and the team will review.
