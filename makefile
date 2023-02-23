DOCKER_REGISTRY=docker.io
DOCKER_USERNAME=aquasw
IMAGE1_NAME=app
IMAGE2_NAME=ml
TAG=latest
LOG_DIR=logs

.PHONY: build-image1
build-image1:
	docker buildx build --platform linux/amd64 --file recommend-docker/Dockerfile --tag $(DOCKER_REGISTRY)/$(DOCKER_USERNAME)/$(IMAGE1_NAME):$(TAG) .

.PHONY: build-image2
build-image2:
	docker buildx build --platform linux/amd64 --file mlearning-docker/Dockerfile --tag $(DOCKER_REGISTRY)/$(DOCKER_USERNAME)/$(IMAGE2_NAME):$(TAG) .

.PHONY: push-image1
push-image1:
	docker push $(DOCKER_REGISTRY)/$(DOCKER_USERNAME)/$(IMAGE1_NAME):$(TAG)

.PHONY: push-image2
push-image2:
	docker push $(DOCKER_REGISTRY)/$(DOCKER_USERNAME)/$(IMAGE2_NAME):$(TAG)

.PHONY: docker
docker: build-image1 build-image2 push-image1 push-image2