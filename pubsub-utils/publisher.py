
import argparse
import os


from google.cloud import pubsub_v1


def create_topic(project_id: str, topic_id: str) -> None:
    """Create a new PubSub topic."""

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    topic = publisher.create_topic(request={"name": topic_path})

    print(f"Created topic: {topic.name}")


def list_topics(project_id: str) -> None:
    """Lists all Pub/Sub topics in the given project."""

    publisher = pubsub_v1.PublisherClient()
    project_path = f"projects/{project_id}"

    for topic in publisher.list_topics(request={"project": project_path}):
        print(topic)


def delete_topic(project_id: str, topic_id: str) -> None:
    """Deletes an existing Pub/Sub topic."""

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)

    publisher.delete_topic(request={"topic": topic_path})

    print(f"Topic deleted: {topic_path}")



if __name__ == "__main__":
    PUBSUB_PROJECT_ID = os.environ.get('PUBSUB_PROJECT_ID')
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("list", help=list_topics.__doc__)

    create_parser = subparsers.add_parser("create", help=create_topic.__doc__)
    create_parser.add_argument("topic_ids", nargs="+")

    delete_parser = subparsers.add_parser("delete", help=delete_topic.__doc__)
    delete_parser.add_argument("topic_ids", nargs="+")
    
    args = parser.parse_args()

    if args.command == "list":
        list_topics(PUBSUB_PROJECT_ID)
    
    elif args.command == "create":
        for topic_id in args.topic_ids:
            create_topic(PUBSUB_PROJECT_ID, topic_id)
    
    elif args.command == "delete":
        for topic_id in args.topic_ids:
            delete_topic(PUBSUB_PROJECT_ID, topic_id)

