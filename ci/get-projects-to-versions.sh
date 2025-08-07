#!/bin/bash
# produces a YAML mapping of the form:
#
# {project}:
#   stable: {version_number}
#   legacy: {version_number}
#   nightly: {version_number}
#
# With keys omitted based on configuration in _data/docs.yml.
#
# e.g. if a project has 'stable: 0' in that file, it will not have a '{project}.stable'
# key in the mapping produced by this script.

set -e -u -o pipefail

PROJECT_MAP=$(yq '.apis + .libs'  _data/docs.yml)
INACTIVE_PROJECT_MAP=$(yq '.inactive-projects' _data/docs.yml)

VERSION_MAP=$(jq '{
    "legacy": { "version": .legacy.version, "ucxx_version": .legacy.ucxx_version },
    "stable": { "version": .stable.version, "ucxx_version": .stable.ucxx_version },
    "nightly": { "version": .nightly.version, "ucxx_version": .nightly.ucxx_version }
}' _data/releases.json)

PROJECTS_TO_VERSIONS='{}'

for PROJECT in $(yq -r 'keys | .[]' <<< "$PROJECT_MAP"); do
    THIS_PROJECT_MAP="{\"${PROJECT}\":{}}"
    for VERSION_NAME in $(jq -r 'keys | .[]' <<< "$VERSION_MAP"); do
        VERSION_NUMBER=$(jq -r --arg vn "$VERSION_NAME" --arg pr "$PROJECT" '
        if ($pr | contains("ucxx")) then
            .[$vn].ucxx_version
        else
            .[$vn].version
        end' <<< "$VERSION_MAP")
        PROJECT_MAP_JSON=$(yq -r -o json '.' <<< "$PROJECT_MAP")
        if [ "$(jq -r --arg pr "$PROJECT" --arg vn "$VERSION_NAME" '.[$pr].versions[$vn]' <<< "$PROJECT_MAP_JSON")" == "0" ]; then
            echo "Skipping: $PROJECT | $VERSION_NAME | $VERSION_NUMBER"
            continue
        fi
        THIS_PROJECT_MAP=$(
            jq \
                --arg pr "${PROJECT}" \
                --arg version_name "${VERSION_NAME}" \
                --arg version_number "${VERSION_NUMBER}" \
                '.[$pr] |= . + {$version_name: $version_number}' \
            <<< "${THIS_PROJECT_MAP}"
        )
    done
    # add this new entry to the mapping
    PROJECTS_TO_VERSIONS=$(
        jq --slurp \
            'map(to_entries) | flatten | group_by(.key) | map({key: .[0].key, value: map(.value) | add}) | from_entries' \
        <<< "${PROJECTS_TO_VERSIONS}${THIS_PROJECT_MAP}"
    )
done

echo -n "${PROJECTS_TO_VERSIONS}"
