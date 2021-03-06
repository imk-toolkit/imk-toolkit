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
    echo "๐งน Time for cleanup"

    echo "โ Logging out of dockerhub"
    docker "logout"
}

echo "๐ This script is located at '${SOURCE_DIR}'."
echo "๐ This script was executed from '${WORKING_DIR}'."
echo "๐ Using tag '${DOCKER_TAG}' on docker."

DOCKER_VERSION_NUMBER="imktk/imktk:${DOCKER_TAG}"
DOCKER_FILE="${SOURCE_DIR}/../"
DOCKER_VERSION_RELATIVE="imktk/imktk:testing"

if [[ $DOCKER_TAG != *"rc"* ]]; then
  DOCKER_VERSION_RELATIVE="imktk/imktk:latest"
fi

echo "๐ง Building and tagging docker image"
docker build --tag "${DOCKER_VERSION_NUMBER}" --tag "${DOCKER_VERSION_RELATIVE}" "${DOCKER_FILE}"

echo "๐ Logging in to dockerhub"
docker login --username="${DOCKER_USERNAME}" --password="${DOCKER_SECRET}"

echo "๐ Pushing ${DOCKER_VERSION_NUMBER} to dockerhub"
docker push "imktk/imktk" --all-tags

echo "๐ Script ended successfully"
