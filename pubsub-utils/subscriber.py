import argparse

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
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("project_id", help="Your Google Cloud project ID")

    subparsers = parser.add_subparsers(dest="command")
    list_in_topic_parser = subparsers.add_parser(
        "list-in-topic", help=list_subscriptions_in_topic.__doc__
    )
    list_in_topic_parser.add_argument("topic_id")

    list_in_project_parser = subparsers.add_parser(
        "list-in-project", help=list_subscriptions_in_project.__doc__
    )

    create_parser = subparsers.add_parser("create", help=create_subscription.__doc__)
    create_parser.add_argument("--topic_ids", nargs="+")
    create_parser.add_argument("--subscription_ids", nargs="+")

    delete_parser = subparsers.add_parser("delete", help=delete_subscription.__doc__)
    delete_parser.add_argument("subscription_id")


    args = parser.parse_args()

    if args.command == "list-in-topic":
        list_subscriptions_in_topic(args.project_id, args.topic_id)
    
    elif args.command == "list-in-project":
        list_subscriptions_in_project(args.project_id)
    
    elif args.command == "create":
        for topic_id, subscription_id in zip(args.topic_ids, args.subscription_ids):
            create_subscription(args.project_id, topic_id, subscription_id)
    
    elif args.command == "delete":
        delete_subscription(args.project_id, args.subscription_id)