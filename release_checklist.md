# Release Checklist

On release day, the following changes need to be made to the site:

- **Update [\_data/releases.json](_data/releases.json)**: Update versions, dates
- **Update [\_data/docs.yml](_data/docs.yml)**: Verify legacy/stable/nightly versions are enabled/disabled appropriately
- **Update [releases/schedule.md](releases/schedule.md)**: Update release schedule
- **Update symlinks and re-customize docs**:
  - Run codeblock below (from project's root directory) to update all symlinks and re-customize docs to reflect new RAPIDS versions.

```sh
update_symlinks.sh # ensures symlink accuracy

customization/lib_map.sh # generates a JSON file needed by customize_docs.py

customization/customize_docs_in_folder.sh api/

```

- **Remove old docs** - Use [rm_old_docs.sh](/rm_old_docs.sh) script to remove previous legacy docs
- **Tag Commit** - After the release PR is merged, tag the commit so it appears on the release page - https://github.com/rapidsai/docs/releases
