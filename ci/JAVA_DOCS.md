# Maintaining released Java API docs

## Publish docs for a new version

After a Maven Central release, the release-tracking dispatcher starts
**Deploy released Java docs** in `rapidsai/docs`. The workflow uploads the
published Javadoc to S3 and opens an `Enable <project> docs for <version>`
PR. Review and merge that PR to enable or update the stable link on the
[API docs page](https://docs.rapids.ai/api/).

If a release is missing from the API docs page:

1. Look for an open stable-link PR and check the `Java docs <project> <version>`
   run in Actions.
2. If the run failed, check its upload step. Confirm that the project's
   `-javadoc.jar` is downloadable from Maven Central and contains `index.html`.
3. If no run started or it needs a retry, run **Deploy released Java docs** from
   `main` in `rapidsai/docs`. Enter the project key and the exact published
   Maven version (for example, `cuvs-java` and `26.12.0`).

New projects can appear on the API docs page with only a GitHub link while
`versions.stable` is `0`. The first stable-link PR enables the docs link.
This workflow publishes stable releases only.

## Replace existing docs

To repair an incomplete upload, run **Deploy released Java docs** from `main`
with the same project and version. The workflow downloads the existing Maven
artifact and replaces the files under
`s3://rapidsai-docs/<project>/html/<version>/`, including removing stale files
in that directory. Rerunning an older version leaves the stable link on the
newer release. If the published Javadoc itself needs a correction, publish a
new Maven version and deploy its docs.

## Add a project

1. Add the project key and the Maven `group-id` and `artifact-id` of the module
   that ships the Javadoc JAR to [`java-docs-projects.json`](java-docs-projects.json).
   For example, `cuvs-lucene` uses `cuvs-lucene-10.2` because the unversioned
   Maven artifact is a relocation POM.
2. Add the same key under `apis` in [`_data/docs.yml`](../_data/docs.yml). Use the
   project key as the docs path and leave the version links disabled until the
   first deployment. Run pre-commit to regenerate the project-to-version mapping.
3. For automatic deployment, coordinate the corresponding Maven publication
   registration in release-tracking's `config/java-docs-publications.json`.

## Remove a project

Remove the publication registration from release-tracking if it dispatches
docs for the project. Remove the project from `java-docs-projects.json` and
`_data/docs.yml`, then run pre-commit to regenerate the project-to-version
mapping. This removes the API docs entry. Previously uploaded files remain
available at their versioned URLs.

## Run the tests

Run `make test` for the full suite. To run just the Java docs tests, install
`jq` and `unzip` and run:

```sh
uv run pytest tests/test_update_java_docs.py tests/test_upload_java_docs.py
```

The upload tests substitute local commands for Maven Central and AWS. The PR
workflow runs the full suite through `make check`.
