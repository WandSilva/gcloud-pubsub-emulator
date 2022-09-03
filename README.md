# Gcloud Pub/Sub Emulador

This project was developed to facilitate the use of [Pub/Sub Emulator](https://cloud.google.com/pubsub/docs/emulator) for testing on localhost or development environment.

Python scripts have been created (based on the scripts provided [here](https://github.com/googleapis/python-pubsub)) to facilitate the management of Topics and Subscriptions.

## Usage

## - Start Pub/Sub Emulator:
clone this repository and run:
```
  $ cd gcloud-pubsub-emulador/
  $ docker build -t pubsub-emulator .
  $ docker run --rm -p "8085:8085" --env 'PROJECT_ID=<fake-project-id>' pubsub-emulator
```
The `PROJECT_ID` does not need to represent a real Google Cloud project because the Pub/Sub emulator runs locally

## - Management of Topics and Subscriptions

The scripts present in [/pubsub-utils](/pubsub-utils) can be used to manage topics and subscriptions.
Some functions will be described below:

Before run the python scripts is necessary install the dependencies and export the environment variables. If you don't want to use [Poetry](https://python-poetry.org/) to configure the environment, just install the dependencies present in [pyproject.toml](pyproject.toml) as you see fit.


```
install project dependencies and spawns a shell
$ poetry install
$ poetry shell
```

```
export the environment variables:
$ export PUBSUB_EMULATOR_HOST=localhost:8085
$ export PUBSUB_PROJECT_ID=<fake-project-id>
```

### 1. Topics Management:

1.1. Created topics:
```
$ python3 pubsub-utils/publisher.py create <topic-1> <topic-N>
```

1.2. Delete topics:
```
$ python3 pubsub-utils/publisher.py delete <topic-1> <topic-N>
```

1.3. List topics:
```
$ python3 pubsub-utils/publisher.py list
```

### 2 Subscriptions Management
2.1. Create subscriptions:

``` 
$ python3 pubsub-utils/subscriber.py create --topics <topic-1> <topic-N> --subscriptions <sub-1> <sub-N> 
```


2.2. Delete subscriptions:

``` 
$ python3 pubsub-utils/subscriber.py delete <subcscrption_id>
```

2.3. List all subscriptions in the project:

``` 
$ python3 pubsub-utils/subscriber.py list-in-project
```


2.4. List all subscriptions in a topic:

``` 
$ python3 pubsub-utils/subscriber.py list-in-topic <topic_id>
```

 
