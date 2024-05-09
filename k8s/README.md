# Kubernete Deployment

## Requirementes
* Already installed kind and kubectl
* Creating a kind cluster following the instructions of document [creating-kind_cluster.md](../doc/creating-kind_cluster.md)

### Caveats
- Please, checkout in each cluster node the path ```/data/heart.csv``` is present and can get the same content of file [data/heart.csv](../data/heart.csv)

## Deployment
* Deploying volume configuration by executing ```kubectl apply -f data_pv_pvc.yaml```
* Deploying a Kubernetes deployment by executing ```kubectl apply -f mlservice.yaml```
* Deploying a kubernetes service

## Testing deployment

From the root of the repo, please run the following makefile macros

### Testing conectivity
* Getting the external IP of the service mlservice provided the LoadBalancer, for the example below is 172.18.0.5 and port 5000
```
$ kubectl get svc
NAME         TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP          17h
mlservice    LoadBalancer   10.96.44.172   172.18.0.5    5000:32308/TCP   9s
```
* Testing the connectivity
```
make test_modelapi_ping IP=172.18.0.5
```

### Testing the model
* By default, for simplicity, the model is tested using the the first row of file [data/heart.csv](../data/heart.csv). So for testing the model. Please execute de command below
```
make test_modelapi IP=172.18.0.5 PORT=5000
```


### Caveats
- Please be aware that mlservice is exposed with LoadBalancer type. Thus you need to have running [cloud-provider-kind](https://kind.sigs.k8s.io/docs/user/loadbalancer/)
- The services exposed uses the port: ```5000```
