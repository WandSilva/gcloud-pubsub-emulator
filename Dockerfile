FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1
ENV PATH=/etc/poetry/bin:$PATH
ENV POETRY_VIRTUALENVS_CREATE=0
ENV POETRY_HOME=/etc/poetry/

RUN apk --no-cache update && \
    apk --no-cache add \
    openjdk8-jre \
    curl \
    linux-headers \
    g++ \
    gcc \
    libc-dev \
    libffi-dev \
    which \
    bash && \
    rm -rf /var/cache/apk/*

# Poetry

RUN python3 -m ensurepip

RUN pip3 install --no-cache --upgrade pip setuptools poetry==1.3.1

# GCP SDK

# RUN curl https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz > /tmp/google-cloud-sdk.tar.gz

# RUN mkdir -p /usr/local/gcloud \
#     && tar -C /usr/local/gcloud -xvf /tmp/google-cloud-sdk.tar.gz \
#     && /usr/local/gcloud/google-cloud-sdk/install.sh

# ENV PATH $PATH:/usr/local/gcloud/google-cloud-sdk/bin

RUN curl -sSL https://sdk.cloud.google.com | bash

ENV PATH $PATH:/root/google-cloud-sdk/bin

# GCP Emulator
ENV PUBSUB_PROJECT_ID=default
ENV PUBSUB_EMULATOR_HOST=0.0.0.0:8432

RUN gcloud components install --quiet beta pubsub-emulator && \
    gcloud components update

# App configuration
WORKDIR /app

ADD . .

RUN cd pubsub-utils

RUN poetry config virtualenvs.create false

RUN poetry install

RUN cd ..

EXPOSE 8432

VOLUME /opt/data

RUN chmod +x ./entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]