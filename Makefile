UV ?= uv
PORT ?= 8004
AWS_PROFILE ?=

.PHONY: assemble check clean full html lint serve test validate

clean:
	rm -rf _site

html: clean
	$(UV) run sphinx-build -E -b dirhtml source _site -W --keep-going -n

assemble:
	AWS_PROFILE=$(AWS_PROFILE) $(UV) run bash ci/download_from_s3.sh
	$(UV) run bash ci/post-process.sh
	$(UV) run python scripts/validate_site.py _site --full

full: html assemble

lint:
	$(UV) run ruff check ci extensions scripts source/conf.py tests
	$(UV) run ruff format --check ci extensions scripts source/conf.py tests

test:
	$(UV) run pytest

validate:
	$(UV) run python scripts/validate_site.py _site
	$(UV) run python scripts/compare_routes.py tests/fixtures/jekyll_manifest.json _site

check: lint test html validate

serve:
	$(UV) run python -m http.server $(PORT) --bind 0.0.0.0 --directory _site
