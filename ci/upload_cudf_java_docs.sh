#!/bin/bash
# Copyright (c) 2024, NVIDIA CORPORATION.

set -euo pipefail

validate_version() {
    local version=$1
    if ! [[ $version =~ ^[0-9]{2}\.[0-9]{2}(\.[0-9]+)?$ ]]; then
        echo "Error: Version must be in format YY.MM or YY.MM.P" >&2
        return 1
    fi
}

cleanup() {
    rm -rf cudf-*-javadoc.jar cudf-docs 2>/dev/null || true
}

main() {
    trap cleanup EXIT

    if [ $# -ne 1 ]; then
        echo "Usage: $0 <version>"
        echo "Version format: YY.MM or YY.MM.P"
        echo "Examples: 23.12, 24.02, 23.12.1"
        exit 1
    fi

    DOCS_VERSION=$1
    if ! validate_version "$DOCS_VERSION"; then
        exit 1
    fi

    IFS='.' read -r major minor patch <<< "$DOCS_VERSION"
    patch=${patch:-0} # when no patch is given, use 0
    patch=$(echo "$patch" | sed 's/^0*//') # strip leading zeros if present
    patch=${patch:-0} # handle patch values like 00

    local url="https://repo1.maven.org/maven2/ai/rapids/cudf/${major}.${minor}.${patch}/cudf-${major}.${minor}.${patch}-javadoc.jar"

    if ! wget --spider "$url" 2>/dev/null; then
        echo "Error: Documentation not found at $url" >&2
        exit 1
    fi

    wget "$url"
    unzip cudf-*-javadoc.jar -d cudf-docs
    aws s3 sync --delete cudf-docs/ "s3://rapidsai-docs/cudf-java/html/${DOCS_VERSION}/"
    echo "Documentation successfully uploaded to s3://rapidsai-docs/cudf-java/html/${DOCS_VERSION}/"
}

main "$@"
