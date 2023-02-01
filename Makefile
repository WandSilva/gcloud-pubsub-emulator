.PHONY : build
build:
	docker build -t pubsub-emulator .

.PHONY : run-container
run:
	docker run --rm -p "8432:8432" --env 'PUBSUB_PROJECT_ID=$(project_id)' pubsub-emulator

.PHONY: up
up:
	docker-compose up -d

.PHONY: down
down:
	docker-compose down --remove-orphans