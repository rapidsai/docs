# Release Checklist

On release day, the following changes need to be made to the site:

- **Update [\_data/releases.json](_data/releases.json)**: Update versions, dates
- **Update [\_data/docs.yml](_data/docs.yml)**: Verify legacy/stable/nightly versions are enabled/disabled appropriately
- **Update [releases/schedule.md](releases/schedule.md)**: Update release schedule
- **Update symlinks and re-customize docs**:
  - Run codeblock below (from project's root directory) to update all symlinks and re-customize docs to reflect new RAPIDS versions.

```sh
NIGHTLY_VERSION="19" # new nightly version (i.e. version after release version)

update_symlinks.sh # ensures symlink accuracy

customization/lib_map.sh # generates a JSON file needed by customize_docs.py

customization/customize_docs_in_folder.sh api/ ${NIGHTLY_VERSION}

```

- **Delete Old Docs & Tag Release**: Run the Jenkins job below after the release PR is merged to delete old docs and tag new release
  - <https://gpuci.gpuopenanalytics.com/job/rapidsai/job/doc-builds/job/docs-release/>
