# Elastic Kubernetes Service (EKS)

RAPIDS can be deployed on AWS via AWS’s managed Kubernetes service (EKS) using Helm. More details can be found at our **[helm docs.](https://helm.rapids.ai/docs/csp.html)**

**1. Install.** Install and configure dependencies in your local environment: kubectl, helm, awscli, and eksctl.

**2. Public Key.** Create a public key if you don't have one.

**3. Create your cluster:**

```shell
$ eksctl create cluster \
    --name [CLUSTER_NAME] \
    --version 1.14 \
    --region [REGION] \
    --nodegroup-name gpu-workers \
    --node-type [NODE_INSTANCE] \
    --nodes  [NUM_NODES] \
    --nodes-min 1 \
    --nodes-max [MAX_NODES] \
    --node-volume-size [NODE_SIZE] \
    --ssh-access \
    --ssh-public-key ~/path/to/id_rsa.pub \
    --managed
```

[CLUSTER_NAME] = Name of the EKS cluster. This will be auto generated if not specified. <br>
[NODE_INSTANCE] = Node instance type to be used. Select one of the instance types supported by RAPIDS Refer to the introduction section for a list of supported instance types. <br>
[NUM_NODES] = Number of nodes to be used. <br>
[MAX_NODES] = Maximum size of the nodes. <br>
[NODE_SIZE] = Size of the nodes. <br>

Update the path to the ssh-public-key to point to the folder and file where your public key is saved.

**4. Install GPU addon:**

```shell
$ kubectl create -f https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/1.0.0-beta4/nvidia-device-plugin.yml
```

**5. Install RAPIDS helm repo:**

```shell
$ helm repo add rapidsai https://helm.rapids.ai
$ helm repo update
```

**6. Install helm chart:**

```shell
$ helm install --set dask.scheduler.serviceType="LoadBalancer" --set dask.jupyter.serviceType="LoadBalancer" rapidstest rapidsai/rapidsai
```

**7. Accessing your cluster:**

```shell
$ kubectl get svc
NAME                TYPE          CLUSTER-IP      EXTERNAL-IP                                                               PORT(S)                         AGE
kubernetes          ClusterIP     10.100.0.1      <none>                                                                    443/TCP                         12m
rapidsai-jupyter    LoadBalancer  10.100.251.155  a454a9741455544cfa37fc4ac71caa53-868718558.us-east-1.elb.amazonaws.com    80:30633/TCP                    85s
rapidsai-scheduler  LoadBalancer  10.100.11.182   a9c703f1c002f478ea60d9acaf165bab-1146605388.us-east-1.elb.amazonaws.com   8786:30346/TCP,8787:32444/TCP   85s
```

**7. ELB IP address:** **[Convert the DNS address provided above as the
EXTERNAL-IP address to an IPV4
address](https://aws.amazon.com/premiumsupport/knowledge-center/elb-find-load-balancer-IP/)**.
Then use the obtained IPV4 address to visit the rapidsai-jupyter service in your
browser!

**8. Delete the cluster:** List and delete services running in the cluster to release resources

```shell
$ kubectl get svc --all-namespaces
$ kubectl delete svc [SERVICE_NAME]
```

[SERVICE_NAME] = Name of the services which have an EXTERNAL-IP value and are required to be removed to release resources.

Delete the cluster and its associated nodes

```shell
$ eksctl delete cluster --region=[REGION] --name=[CLUSTER_NAME]
```

**9. Uninstall the helm chart:**

```shell
$ helm uninstall rapidstest
```
