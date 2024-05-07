DOCKER_GENMODEL = lmservice

build:
	poetry build

build_image: build
	docker image build \
	--build-arg USER_ID=$(shell id -u) \
    --build-arg GROUP_ID=$(shell id -g) \
	-t $(DOCKER_GENMODEL) \
	-f docker/baseimage.Dockerfile .

clean:
	docker rmi -f $(DOCKER_GENMODEL)
	docker rm -f $(DOCKER_GENMODEL)
	rm -f model/heart_model.pkl
	rm -rf dist



debug_image:
	$(call run_image,bash,)

run_genmodel:
	$(call run_image,python,/ml_service/cli.py)

run_modelapi:
	$(call run_image,python,/ml_service/model_api.py,8080)


define run_image
### if $(3) is not empty then Running Model API image
    if [ -n "$(3)" ]; then \
		docker run --rm -it --name $(DOCKER_GENMODEL) \
		-p 127.0.0.1:$(3):5000/tcp \
	    -v $$PWD/model:/model \
		-t $(DOCKER_GENMODEL) $(1) $(2); \
    else \
		docker run --rm -it --name $(DOCKER_GENMODEL) \
		-v $$PWD/data:/data \
		-v $$PWD/model:/model \
		-t $(DOCKER_GENMODEL) $(1) $(2); \
    fi

endef

.PHONY: debug_image run_genmodel run_modelapi clean build_image build