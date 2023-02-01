FROM google/cloud-sdk:alpine

ENV PUBSUB_PROJECT_ID=default
ENV PUBSUB_EMULATOR_HOST=0.0.0.0:8432
ENV PYTHONUNBUFFERED=1

RUN apk --no-cache update && \
    apk --no-cache add openjdk8-jre python3 && \
    rm -rf /var/cache/apk/*

RUN ln -sf python3 /usr/bin/python

RUN python3 -m ensurepip

RUN pip3 install --no-cache --upgrade pip setuptools poetry==1.3.1

RUN gcloud components install --quiet beta pubsub-emulator && \
    gcloud components update

WORKDIR /pubsub-utils

COPY pubsub-utils .

COPY entrypoint.sh .

RUN poetry install --only main --no-root

RUN echo 'alias publisher="python3 /pubsub-utils/publisher.py"' >> ~/.bashrc
RUN echo 'alias subscriber="python3 /pubsub-utils/subscriber.py"' >> ~/.bashrc

EXPOSE 8432

VOLUME /data

RUN chmod +x ./entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]