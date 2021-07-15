#!/bin/bash
set -e

if [ "$#" -ne 1 ]; then
  echo "A script to help delete old versions of RAPIDS docs"
  echo "Example:"
  echo "  rm_old_versions.sh 21.06"
  exit 1
fi

VERSION=$1

for FOLDER in api/*/ ; do
  rm -rf "${FOLDER}${VERSION}"
done
