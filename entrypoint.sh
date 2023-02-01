#!/bin/sh
set -e

ulimit -c unlimited

if [[ -z "${PUBSUB_EMULATOR_HOST}" ]]; then
  echo "Missing PUBSUB_EMULATOR_HOST environment variable" >&2
  exit 1
fi

if [[ -z "${PUBSUB_PROJECT_ID}" ]]; then
  echo "Missing PUBSUB_PROJECT_ID environment variable" >&2
  exit 1
fi

gcloud beta emulators pubsub start \
    --host-port=$PUBSUB_EMULATOR_HOST \
    --project=$PUBSUB_PROJECT_ID \
    --data-dir=/data

exec $@