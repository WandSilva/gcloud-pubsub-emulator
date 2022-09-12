import argparse
import os


from google.cloud import pubsub_v1


def list_subscriptions_in_topic(project_id: str, topic_id: str) -> None:
    """Lists all subscriptions for a given topic."""

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)

    response = publisher.list_topic_subscriptions(request={"topic": topic_path})
    for subscription in response:
        print(subscription)


def list_subscriptions_in_project(project_id: str) -> None:
    """Lists all subscriptions in the current project."""

    subscriber = pubsub_v1.SubscriberClient()
    project_path = f"projects/{project_id}"

    with subscriber:
        for subscription in subscriber.list_subscriptions(
            request={"project": project_path}
        ):
            print(subscription.name)


def create_subscription(project_id: str, topic_id: str, subscription_id: str) -> None:
    """Create a new pull subscription on the given topic."""

    publisher = pubsub_v1.PublisherClient()
    subscriber = pubsub_v1.SubscriberClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    subscription_path = subscriber.subscription_path(project_id, subscription_id)

    with subscriber:
        subscription = subscriber.create_subscription(
            request={"name": subscription_path, "topic": topic_path}
        )

    print(f"Subscription created: {subscription}")


def delete_subscription(project_id: str, subscription_id: str) -> None:
    """Deletes an existing Pub/Sub topic."""

    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, subscription_id)

    with subscriber:
        subscriber.delete_subscription(request={"subscription": subscription_path})

    print(f"Subscription deleted: {subscription_path}.")


if __name__ == "__main__":
    PUBSUB_PROJECT_ID = os.environ.get('PUBSUB_PROJECT_ID')
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command")
    list_in_topic_parser = subparsers.add_parser(
        "list-in-topic", help=list_subscriptions_in_topic.__doc__
    )
    list_in_topic_parser.add_argument("topic_id")

    list_in_project_parser = subparsers.add_parser(
        "list-in-project", help=list_subscriptions_in_project.__doc__
    )

    create_parser = subparsers.add_parser("create", help=create_subscription.__doc__)
    create_parser.add_argument("--topics", nargs="+")
    create_parser.add_argument("--subscriptions", nargs="+")

    delete_parser = subparsers.add_parser("delete", help=delete_subscription.__doc__)
    delete_parser.add_argument("subscription_id")


    args = parser.parse_args()

    if args.command == "list-in-topic":
        list_subscriptions_in_topic(PUBSUB_PROJECT_ID, args.topic_id)
    
    elif args.command == "list-in-project":
        list_subscriptions_in_project(PUBSUB_PROJECT_ID)
    
    elif args.command == "create":
        for topic_id, subscription_id in zip(args.topics, args.subscriptions):
            create_subscription(PUBSUB_PROJECT_ID, topic_id, subscription_id)
    
    elif args.command == "delete":
        delete_subscription(PUBSUB_PROJECT_ID, args.subscription_id)