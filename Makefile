.PHONY : build
build:
	docker build -t pubsub-emulator .

.PHONY : run
run:
	docker run --rm -p "8085:8085" --env 'PROJECT_ID=$(project_id)' pubsub-emulator