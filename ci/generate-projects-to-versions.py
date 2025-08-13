#!/usr/bin/env python3
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
import json
import sys
import yaml
from collections import OrderedDict

with open("_data/docs.yml") as f:
    DOCS_YML_DICT = yaml.safe_load(f)

with open("_data/releases.json") as f:
    RELEASES_JSON_DICT = json.load(f)

# using OrderedDict minimizes churn in the output as projects are added and removed
PROJECTS_TO_VERSIONS_DICT = OrderedDict()

for docs_key in ["apis", "libs", "inactive-projects"]:
    for project_name, project_details in DOCS_YML_DICT[docs_key].items():
        print(f"Processing: {project_name}", file=sys.stderr)
        # what entry from releases.json should be used to find version numbers?
        version_key = "version"
        if "ucxx" in project_name:
            version_key = "ucxx_version"

        # what versions should be built for this project?
        versions_for_this_project = OrderedDict()
        for version_name, should_include in project_details["versions"].items():
            if should_include == 1:
                version_override = project_details.get("version-overrides", dict()).get(
                    version_name, ""
                )
                if version_override:
                    versions_for_this_project[version_name] = version_override
                else:
                    versions_for_this_project[version_name] = RELEASES_JSON_DICT[
                        version_name
                    ][version_key]
            else:
                print(f"Skipping: {project_name} | {version_name}", file=sys.stderr)

        # update overall mapping
        PROJECTS_TO_VERSIONS_DICT[project_name] = versions_for_this_project


with open("ci/customization/projects-to-versions.json", "w") as f:
    json.dump(PROJECTS_TO_VERSIONS_DICT, f, indent=2)
    f.write("\n")
