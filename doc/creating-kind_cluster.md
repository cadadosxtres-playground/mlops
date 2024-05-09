# Creating a kind cluster

```bash
cat <<EOF | kind create cluster --name mlops --config=-
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  kubeadmConfigPatches:
  - |
    kind: InitConfiguration
    nodeRegistration:
      kubeletExtraArgs:
        node-labels: "ingress-ready=true"
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
    protocol: TCP
  - containerPort: 443
    hostPort: 443
    protocol: TCP
- role: worker
  extraMounts:
    - hostPath: ../data
      containerPath: /data
- role: worker
  extraMounts:
    - hostPath: ../data ## WARNING!! <<<--- This a relative path from this file
      containerPath: /data
EOF
```


## Installing Cloud Provider KIND
* Please follow the instractions from https://kind.sigs.k8s.io/docs/user/loadbalancer/
* Run cloud-provider-kind binary from ~/go/bin/cloud-provider-kind if you have installed using goland otherwise from where you have placed the binary.




## Setting up JupyterHub in Kubernetes

* Setting up JupyterHub  in Kubernetes Kind Cluster following the instractions from https://cloudyuga.guru/blogs/empowering-data-science-running-jupyter-notebooks-at-scale-with-kubernetes/

## Setting the environment 

* Access to your JupyterHub
* Upload the dataset from [data/heart.csv](../data/heart.csv) to your Jupyter Notbook root directory
* Upload the file [requirements_exploring.txt](./requirements_exploring.txt) to your Jupyter Notbook root directory
* Upload the Jupyter Notebook [Exploring_Data.ipynb](Exploring_Data.ipynb)

![](./img/Screenshot%20from%202024-05-06%2019-52-43.png)

