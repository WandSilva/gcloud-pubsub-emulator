# Gcloud Pub/Sub Emulador

This project was developed with the aim of facilitating the use of [Pub/Sub Emulator](https://cloud.google.com/pubsub/docs/emulator) for testing on localhost or development environment.
Python scripts have been created (based on the scripts provided [here](https://github.com/googleapis/python-pubsub)) to facilitate the management of Topics and Subscriptions.

## Usage

### 1. Start Pub/Sub Emulator:
clone this repository and run:
```
  $ cd gcloud-pubsub-emulador/

  $ docker build -t pubsub-emulator .

  $ docker run --rm -p "8085:8085" --env 'PROJECT_ID=<fake-project-id>' pubsub-emulator
```
The `PROJECT_ID` does not need to represent a real Google Cloud project because the Pub/Sub emulator runs locally

### 2. Management of Topics and Subscriptions

The scripts present in [/pubsub-utils](/pubsub-utils) can be used to manage topics and subscriptions.
Some functions will be described below:

created topics:

```python3 pubsub-utils/publisher.py <fake-project-id> create <topic-1> <topic-2> ```

Create subscriptions:

``` python3 pubsub-utils/subscriber.py <fake-project-id> create --topic_ids <topic1> <topic2> --subscription_ids <sub1> <sub2> ```

 
