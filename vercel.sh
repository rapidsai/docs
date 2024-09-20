#!/bin/bash
set -euo pipefail
USAGE="Usage:
  build:           vercel.sh
  install deps:    vercel.sh install
"
if [ $# -eq 0 ]; then
  CMD="build"
elif [ $# -eq 1 ]; then
  CMD="$1"
else
  echo "${USAGE}"
  exit 1
fi
INSTALL_PREFIX="/usr/local"
export PATH="${PATH}:${INSTALL_PREFIX}/go/bin"

install_dependencies() {
  echo "installing dependencies..."
  ruby --version
  echo "search ruby versions..."
  yum list available | grep -i "ruby.*devel"
  bundle install
  npm install
}

build() {
  echo "printing env..."
  env | sort

  echo "clean output directories..."
  rm -rf ./.vercel/output ./_site

  echo "building..."
  jekyll build
  mkdir -p .vercel/output/
  node scripts/vercel/config.mjs > .vercel/output/config.json
  cp -r _site .vercel/output/static
}

case "${CMD}" in
  "install")
    install_dependencies
    ;;
  "build")
    build
    ;;
  *)
    echo "${USAGE}"
    exit 1
    ;;
esac
