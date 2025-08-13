#!/bin/bash
# SPDX-FileCopyrightText: Copyright (c) 2025, NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# [description]
#
# Determines:
#
#   * which RAPIDS libraries to host docs for
#   * what types of docs to host ('legacy', 'nightly', 'stable', etc.)
#   * what versions to map to those types
#
# The libraries that should be copied are read from "_data/docs.yml".
#
# The versions that should be copied are read from a mix of sources:
#
#   - active projects: "_data/releases.json"
#   - inactive projects: 'version-overrides' field in entries in "_data/docs.yml"
#
# Produces a JSON mapping of the form:
#
#     {
#         "{project}": {
#             "stable": {version_number},
#             "legacy": {version_number},
#             "nightly": {version_number}
#          },
#      }
#
# With keys omitted based on configuration in _data/docs.yml.
#
# e.g. if a project has 'stable: 0' in that file, it will not have a '{project}.stable'
# key in the mapping produced by this script.
#
# Only that mapping is written to stdout, so this is safe to use inline like this:
#
#     PROJECTS_TO_VERSIONS=$(./ci/generate-projects-to-versions.sh)
#
# WARNING: no guarantees are made about the ordering of output in this mapping.
#

set -e -E -u -o pipefail

log-stderr() {
    echo "${1}" >&2
}

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
            log-stderr "Skipping: $PROJECT | $VERSION_NAME | $VERSION_NUMBER"
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

# inactive projects have specific versions hard-coded in their configuration, process those separately
for PROJECT in $(yq -r 'keys | .[]' <<< "$INACTIVE_PROJECT_MAP"); do
    THIS_PROJECT_MAP="{\"${PROJECT}\":{}}"
    for VERSION_NAME in $(jq -r 'keys | .[]' <<< "$VERSION_MAP"); do
        # do not attempt updates for any versions where the corresponding key is '0' in docs.yml
        INACTIVE_PROJECT_MAP_JSON=$(yq -r -o json '.' <<< "$INACTIVE_PROJECT_MAP")
        if [ "$(jq -r --arg pr "$PROJECT" --arg vn "$VERSION_NAME" '.[$pr].versions[$vn]' <<< "$INACTIVE_PROJECT_MAP_JSON")" == "0" ]; then
            log-stderr "Skipping: $PROJECT | $VERSION_NAME"
            continue
        fi

        # get the version from the 'version-overrides' field in docs.yml, hard-coded there
        # so it doesn't change from release-to-release for inactive projects
        VERSION_NUMBER=$(
            jq -r                               \
            --arg vn "$VERSION_NAME"          \
            --arg pr "${PROJECT}"             \
            '.[$pr]."version-overrides"[$vn]' \
            <<< "${INACTIVE_PROJECT_MAP_JSON}"
        )
        PROJECT_MAP_JSON=$(yq -r -o json '.' <<< "$PROJECT_MAP")
        if [ "$(jq -r --arg pr "$PROJECT" --arg vn "$VERSION_NAME" '.[$pr].versions[$vn]' <<< "$PROJECT_MAP_JSON")" == "0" ]; then
            log-stderr "Skipping: $PROJECT | $VERSION_NAME | $VERSION_NUMBER"
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

echo "${PROJECTS_TO_VERSIONS}" > ./ci/customization/projects-to-versions.json
