DOCKER_GENMODEL = mlservice

IP = localhost
PORT = 5000


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
	$(call run_image,python,/scripts/cli.py)

run_modelapi:
	$(call run_image,python,/scripts/model_api.py,8080)

test_modelapi:
	curl -X POST -H "Content-Type: application/json" \
	-d '{"tobacco": [0.0], "ldl": [6], "adiposity": [22.5], "famhist" : [1], "typea" : [55], "obesity" :  [29.14], "alcohol" : [3.81], "age" : [38] }' \
	http://$(IP):$(PORT)/prediction

test_modelapi_ping:
	curl http://$(IP):$(PORT)/ping

define run_image
### if $(3) is not empty then Running Model API image
    if [ -n "$(3)" ]; then \
		docker run --rm -it --name $(DOCKER_GENMODEL) \
		-p 127.0.0.1:$(3):5000/tcp \
	    -v $$PWD/model:/model \
		-v $$PWD/scripts:/scripts \
		-t $(DOCKER_GENMODEL) $(1) $(2); \
    else \
		docker run --rm -it --name $(DOCKER_GENMODEL) \
		-v $$PWD/data:/data \
		-v $$PWD/model:/model \
		-v $$PWD/scripts:/scripts \
		-t $(DOCKER_GENMODEL) $(1) $(2); \
    fi

endef

.PHONY: debug_image run_genmodel run_modelapi clean build_image build test_modelapi