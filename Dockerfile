FROM google/cloud-sdk:alpine

ENV PROJECT_ID default

RUN apk --no-cache update && \
    apk --no-cache add openjdk8-jre && \
    rm -rf /var/cache/apk/*

RUN gcloud components install --quiet beta pubsub-emulator && \
    gcloud components update

EXPOSE 8085

VOLUME /data

CMD gcloud beta emulators pubsub start --host-port=0.0.0.0:8085 --project=$PROJECT_ID --data-dir=/data

