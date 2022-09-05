# Gcloud Pub/Sub Emulador

This project was developed with the aim of facilitating the use of [Pub/Sub Emulator](https://cloud.google.com/pubsub/docs/emulator) for testing on localhost or development environment.
Python scripts have been created (based on the scripts provided [here](https://github.com/googleapis/python-pubsub)) to facilitate the management of Topics and Subscriptions.

## Usage

## - Start Pub/Sub Emulator:
clone this repository and run:
```
  $ cd gcloud-pubsub-emulador/

  $ make build

  $ make run project_id=<fake-project-id>
```
The `PROJECT_ID` does not need to represent a real Google Cloud project because the Pub/Sub emulator runs locally

## - Management of Topics and Subscriptions

The scripts present in [/pubsub-utils](/pubsub-utils) can be used to manage topics and subscriptions.
Some functions will be described below:

### 1. Topics Management:

1.1. created topics:
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

### 2 subscriptions Management
2.1. Create subscriptions:

``` 
$ python3 pubsub-utils/subscriber.py create --topics <topic-1> <topic-N> --subscriptions <sub-1> <sub-N> 
```


2.2. Delete subscriptions:

``` 
$ python3 pubsub-utils/subscriber.py delete <subcscrption_id>
```

2.3. List all subscription in the project:

``` 
$ python3 pubsub-utils/subscriber.py list-in-project
```


2.4. List all subscription in a topic:

``` 
$ python3 pubsub-utils/subscriber.py list-in-topic <topic_id>
```

 
