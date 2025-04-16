
# Gcloud Pub/Sub Emulator

<!-- PROJECT SHIELDS -->
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GNU License][license-shield]][license-url]

<div align="center">

[![Cover][cover]][repo]

</div>

> This project was developed to help the usage of [Pub/Sub Emulator](https://cloud.google.com/pubsub/docs/emulator) for testing on localhost or development environment.

### Python Scripts

They scripts provided by this repository have been created to support the management of **Topics** and **Subscriptions**. Those scripts are based on the resources provided by [googleapis/python-pubsub](https://github.com/googleapis/python-pubsub).

### Adjusments and Improvements

The project is under construction and the next updates will cover the following topics:

- [ ] Real usage example (or very similar to a real usage);
- [ ] Support for Avro schemas

## 💻 Prerequisites

Before starting, verify if you have the following requisites:

* Python 3.10
* Docker

## 🚀 Setup

Clone the repository:
```bash
git clone git@github.com:WandSilva/gcloud-pubsub-emulator.git
```

In the `gcloud-pubsub-emulator` folder, install the Python dependencies using [Poetry](https://python-poetry.org/):
```bash
poetry install
```

## ☕ Usage

Please follow the initial steps in the order below.

First, spawn the Poetry shell. This session will be used on the remaining instructions:
```bash
poetry shell
```



Export the required environment variables. You must replace `<fake-project-id>` by any project ID that you want, it won't represent a real Google Cloud project because the Pub/Sub emulator runs locally:
```
export PUBSUB_EMULATOR_HOST=localhost:8085
export PUBSUB_PROJECT_ID=<fake-project-id>
```
just make sure your service is trying to connect to pubsub using the same project id
 
Start the Emulator:
```bash
make up
```

### Managing a PubSub Topic

* Create a Topic
  ```sh
  python3 pubsub-utils/publisher.py create <topic-1> <topic-N>
  ```
* Delete a Topic
  ```sh
  python3 pubsub-utils/publisher.py delete <topic-1> <topic-N>
  ```
* List topics
  ```sh
  python3 pubsub-utils/publisher.py list
  ```
* Publish a message in a topic \*\*
  ```sh
  python3 pubsub-utils/publisher.py publish <topic_id>
  ```

\*\* The message hasn't been passed by parameter yet, so to send custom messages, it's mandatory to edit the `publisher.publish_in_topic()`.

### Managing PubSub Subscriptions


* Create a Subscription
  ```sh
  python3 pubsub-utils/subscriber.py create --topics <topic-1> <topic-N> --subscriptions <sub-1> <sub-N> 
  ```
* Delete a Subscription
  ```sh
  python3 pubsub-utils/subscriber.py delete <subcscrption_id>
  ```
* List all subscriptions in a given project
  ```sh
  python3 pubsub-utils/subscriber.py list-in-project
  ```
* List all subscriptions in a topic
  ```sh
  python3 pubsub-utils/subscriber.py list-in-topic <topic_id>
  ```

## 📫 Contributing
If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🤝 Maintainers & Contributors

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/12944524" width="100px;" alt="Photo of Wanderson Silva on GitHub"/><br>
        <sub>
          <b>Wanderson Silva</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/4166006" width="100px;" alt="Photo of Cristiano Santos on GitHub"/><br>
        <sub>
          <b>Cristiano Santos</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

## 📝 License

Distributed under the GNU GPLv3 License. See `LICENSE.txt` for more information.

[⬆ Back to top](#gcloud-pubsub-emulator)<br>

<!-- MARKDOWN LINKS & IMAGES -->
[cover]: cover.png
[repo]: https://github.com/WandSilva/gcloud-pubsub-emulator
[stars-shield]: https://img.shields.io/github/stars/WandSilva/gcloud-pubsub-emulator.svg?style=for-the-badge
[stars-url]: https://github.com/WandSilva/gcloud-pubsub-emulator/stargazers
[issues-shield]: https://img.shields.io/github/issues/WandSilva/gcloud-pubsub-emulator.svg?style=for-the-badge
[issues-url]: https://github.com/WandSilva/gcloud-pubsub-emulator/issues
[license-shield]: https://img.shields.io/github/license/WandSilva/gcloud-pubsub-emulator.svg?style=for-the-badge
[license-url]: https://github.com/WandSilva/gcloud-pubsub-emulator/blob/main/LICENSE.txt
