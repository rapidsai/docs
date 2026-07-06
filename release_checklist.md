# Release Checklist

The complete source-of-truth definitions, preparation timeline, ownership, and
recovery steps are in the [Release Data Maintenance](releases/maintenance.md)
runbook.

On release day:

1. Confirm the future calendar record, platform policy, package lifecycle, and docs
   channel decisions are complete.
2. Run `./ci/roll-release.py --new-next-nightly YY.MM --dry-run`.
3. Run the same command without `--dry-run`.
4. Review source and generated diffs, then run `pre-commit run --all-files`.

Do not edit `_data/releases.json`, `_data/previous_releases.json`,
`ci/customization/projects-to-versions.json`, or `_redirects` directly.
