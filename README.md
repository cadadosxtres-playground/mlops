# mlops

This repo is a POC based on the previous experiences run in the [Kubernetes Book Club](https://community.cncf.io/kubernetes-virtual-book-club/) based on 

* The book [Machine Learning on Kubernetes](https://www.packtpub.com/product/machine-learning-on-kubernetes/9781803241807) 
* The repository [microsoft/MLOpsPython](https://github.com/microsoft/MLOpsPython)
* Example of [Heart Disease Prediction using Logistic Regression](https://github.com/eduai-repo/ML-Demo/blob/main/2%20Classification/2.%20One%20with%20Heart%20Disease%20Prediction.ipynb)



## ML project Life cycle

According to the book [Machine Learning on Kubernetes](https://www.packtpub.com/product/machine-learning-on-kubernetes/9781803241807), the life of a ML project should cover the stages:
- Codifiy the problem and define success metrics
- Ingest, clean, and label data
- Feature Ingineering
- Model Building
- Model Validaton
- Model Deployment
- Monitoring and Validation


This repo covers only the stages below:
- Model Building
- Model Deployment: locally and in Kubernetes without a helm chart


## Model Building

### Requirements
* Python 3.10
* Poetry
* docker

### Building

If you deploy the model in kubernetes you don't need to follow the instructions below as the docker images are already built and during the deployment stage is build the model and the exposed an API to test it.

If you deploy the model localy, please at the root of the repo run the makfile macros below

* Building package and docker image: ```make build_image```
* Checking out the image mlservice:latest has being created
* Running a container to training the model ```make run_genmodel``` as result you will get the model packaged in the file [./model/heart_model.pkl](./model/heart_model.pkl)

## Model Deployment

### Local deployment

After checking out the file [./model/heart_model.pkl](./model/heart_model.pkl) exists. Please run the command below to run a container which expose the model through an API.

```
make run_modelapi
```

As result, you should have an output similar to the one below

```
### if 8080 is not empty then Running Model API image
if [ -n "8080" ]; then docker run --rm -it --name mlservice -p 127.0.0.1:8080:5000/tcp -v $PWD/model:/model -v $PWD/scripts:/scripts -t mlservice python /scripts/model_api.py; else docker run --rm -it --name mlservice -v $PWD/data:/data -v $PWD/model:/model -v $PWD/scripts:/scripts -t mlservice python /scripts/model_api.py; fi
 * Serving Flask app 'model_api'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 255-048-223
```

### Kubernetes deployment

Please folow the instructions of the document placed on the directory k8s [k8s/READM.md](./k8s/READM.md)


## Testing the deployment

Please follow the instructions of section Testing Deployment from kubernetes deployment document [k8s/READM.md](./k8s/READM.md#testing-deployment)