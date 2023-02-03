.PHONY : build
build:
	docker build -t pubsub-emulator .

.PHONY : run-container
run-container:
	docker run --rm -p "8085:8085" --env 'PUBSUB_PROJECT_ID=$(project_id)' pubsub-emulator

.PHONY: up
up:
	docker-compose up -d
	@echo "Wait a few seconds for the emulator to complete initialization."

.PHONY: down
down:
	docker-compose down --remove-orphans