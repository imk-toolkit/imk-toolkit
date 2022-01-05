#!/usr/bin/env bash

set -Ee                               # fail script, if single command fails
set -u                                # unset variables are treated as errors
set -f                                # no filename extension
# set -x                                # verbose mode
set -o pipefail                       # if a subcommand from a pipe fails, the whole pipe fails
trap cleanup SIGINT SIGTERM ERR EXIT  # execute cleanup function at following signals

SOURCE_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd -P)  # location of script
WORKING_DIR=$(pwd -P)  # working directory

cleanup() {
    trap - SIGINT SIGTERM ERR EXIT
    # script cleanup here
    echo "🧹 Time for cleanup"
}

echo "😊 This script is located at '${SOURCE_DIR}'."
echo "😊 This script was exectued from '${WORKING_DIR}'."
echo "😊 Executing branch is ${CURRENT_BRANCH}"
echo "😊 Executing branch is ${CURRENT_TAG}"

get_pyproject_version() {
    cat pyproject.toml | grep ^version | cut -d'=' -f2 | sed -e 's: ::g' | sed -e 's:"::g' | awk '{print "v" $0}'
}

PYPROJECT_TOML_VERSION="$(get_pyproject_version)"

echo "😊 Application version according to pyproject.toml is ${PYPROJECT_TOML_VERSION}"

if [ "${CURRENT_BRANCH}" = "master" ]; then
   PYPI_LOCATION="pypi"
   POETRY_PYPI_TOKEN="${PYPI_TOKEN}"
else
   echo "🔧 Setting up test upload to Test PYPI."
   poetry config repositories.test-pypi https://test.pypi.org/legacy/
   PYPI_LOCATION="test-pypi"
   POETRY_PYPI_TOKEN="${PYPI_TEST_TOKEN}"
fi

echo "🐍 Configure Token for upload to PYPI."
poetry config --no-interaction -vv --no-ansi http-basic."${PYPI_LOCATION}" "__token__" "${POETRY_PYPI_TOKEN}"

echo "🔧 Build packages for upload to PYPI."
poetry build --no-interaction -vv --no-ansi

echo "👆 Publish packages to PYPI."
poetry publish --no-interaction -vv --no-ansi --repository "${PYPI_LOCATION}"

echo "🌟 Script ended successfully"
