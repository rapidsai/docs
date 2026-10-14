# Released Java documentation

Registered projects are `cudf-java`, `cuvs-java`, and `cuvs-lucene`. Each release
uses a separate concurrency group and PR branch so dispatching one project does
not displace another project's pending documentation deployment.

`deploy-java-docs.yaml` receives `project` and `version` through workflow dispatch
after the shared Maven publisher confirms publication. It also supports
`workflow_call`; `deploy-cudf-java-docs.yaml` delegates to it for manual recovery.

Add each Java project to `ci/java-docs-projects.json` with its Maven group and
artifact IDs, and add the corresponding entry under `apis` in `_data/docs.yml`.
Only registered projects can upload to the documentation bucket. The project key
defines the destination `s3://rapidsai-docs/<project>/html/<version>/`.

The workflow downloads the published javadoc jar from Maven Central, retrying
temporary availability failures, then uploads it using the docs repository's
existing AWS configuration. It opens a version-specific PR enabling the stable
link and setting a `version-overrides.stable` value. The override preserves
the actual Maven patch version when `generate-projects-to-versions.py` runs.
Repeated dispatches reuse the same PR branch; an older release cannot lower the
stable version already recorded on main.

The source repository's GitHub App needs Actions write permission on this
repository to dispatch the workflow. Its token is used only for dispatch; AWS
and PR creation credentials remain in the docs workflow. The caller confirms
publication, while this workflow independently requires a valid javadoc jar with
`index.html` before uploading. It can also be dispatched directly to repair docs
for an existing Maven release without republishing artifacts.
