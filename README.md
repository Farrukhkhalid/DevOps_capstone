# **Udacity DevOps Capstone Project**
**PROJECT CONTENT**
- Config.yml: CI/CD pipeline that deploys aws eks
- k8s-deployment.yml: creates rolling update deployment
- k8s-service.yml: creates ELB
- Dockerfile: instructions to assemble Docker image
- Makefile
- app.py
- requirments

<br/><br/>
**TECH STACK**
- Circleci CI/CD pipeline
- AMAZON WEBSERVICES
  - AWS CloudFormation
  - AWS EKS
  - AWS IAM AUTH
  - AWS ELB
- KUBERNETES
- DOCKER
- DOCKER HUB

<br/><br/>
**ISSUES ENCOUNTERED**
- Kubectl Permitions
- IAM use roles
- IAM auth

<br/><br/>
## WORK FLOW

### **1. Linting**
First we start with linting Docker file with Hado lint and source code with pylint

***creating avirtual env install***

```yaml
python3 -m venv venv
. venv/bin/activate
```

***Install Makefile***

```yaml
make install
```

***install hado and pylint***
```yaml
wget -O /bin/hadolint   https://github.com/hadolint/hadolint/releases/download/v1.16.3/hadolint-Linux-x86_64
```

***Run Docker Lint***
```yaml
hadolint Dockerfile
```

***Run pylint***
```yaml
pylint app.py --errors-only
```

![alt text](https://github.com/Farrukhkhalid/DevOps_capstone/blob/main/screens/01%20capstone-lint.png)

<br/><br/>

### **2. Deploying Cluster Infrastructure**

***installing EKSCTL dependencies***
```yaml
curl --silent --location"https://github.com/weaveworks/eksctl/releases/download/v0.83.0/eksctl_Linux_amd64.tar.gz" | tar xz -C /tmp
 mv /tmp/eksctl /usr/local/bin
```

***Rnning EKSCTL Create cluster stack***
```yaml
eksctl create cluster \
            --name prod-green-$CIRCLE_WORKFLOW_ID \
            --region us-west-2 \
            --nodegroup-name worker-node-$CIRCLE_WORKFLOW_ID \
            --node-type t3.micro \
            --nodes 2 \
            --nodes-min 1 \
            --nodes-max 2
```
![alt text](https://github.com/Farrukhkhalid/DevOps_capstone/blob/main/screens/04%20capstone-cloud%20formation.png)
***Cloud formation stack***
![alt text](https://github.com/Farrukhkhalid/DevOps_capstone/blob/main/screens/02%20capstome-stack-green.png)
***Worker nodes***
![alt text](https://github.com/Farrukhkhalid/DevOps_capstone/blob/main/screens/06%20capstone-green-worker-node.png)
***Instances***
![alt text](https://github.com/Farrukhkhalid/DevOps_capstone/blob/main/screens/05%20capstone-green%20blue%20instances.png)

<br/><br/>
### **3. Build/Push Docker Image**

***Build doceker image***

```yaml
docker build -t capstone-project-$CIRCLE_WORKFLOW_ID .
```

***Longin to docker hub***

```yaml
docker login -u "$DOCKERHUB_USERNAME" -p "$DOCKERHUB_PASSWORD"
```

***Psuh Docker image***
```yaml
docker push farrukhkhalid/capstone-project
```
![alt text](https://github.com/Farrukhkhalid/DevOps_capstone/blob/main/screens/07%20capstone-docker-image.png)

***Docker hub***

![alt text](https://github.com/Farrukhkhalid/DevOps_capstone/blob/main/screens/07-2%20capstone-docker-hub.png)

<br/><br/>
### 4. Deoployment Green

***pull doceker image***

```yaml
docker pull farrukhkhalid/capstone-project
```
***Aws iam auth***

```yaml
curl -o aws-iam-authenticator https://amazon-eks.s3.us-west-2.amazonaws.com/1.21.2/2021-07-05/bin/linux/amd64/aws-iam-authenticator
chmod +x ./aws-iam-authenticator
mkdir -p $HOME/bin && cp ./aws-iam-authenticator $HOME/bin/aws-iam-authenticator && export PATH=$PATH:$HOME/bin
```

***Kubectl dependencies / kubeconfig update***

```yaml
curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.21.2/2021-07-05/bin/linux/amd64/kubectl
chmod +x ./kubectl
mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$PATH:$HOME/bin
aws eks --region us-west-2 update-kubeconfig --name prod-green-$CIRCLE_WORKFLOW_ID
kubectl version --client
export KUBECONFIG=~/.kube/config
```

***Kubectl deploy***

```yaml
kubectl apply -f eks/k8s-deploy.yml
```

***Kubectl ELB service***

```yaml
kubectl apply -f eks/k8s-service.yml
```

***Cleanup***

```yaml
curl --silent --location "https://github.com/weaveworks/eksctl/releases/download/v0.83.0/eksctl_Linux_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin
eksctl delete cluster --name prod-blue
```

![alt text](https://github.com/Farrukhkhalid/DevOps_capstone/blob/main/screens/08%20capstone-deploy-green.png)

![alt text](https://github.com/Farrukhkhalid/DevOps_capstone/blob/main/screens/08-2%20capstome-blue.png)

![alt text](https://github.com/Farrukhkhalid/DevOps_capstone/blob/main/screens/08-3%20capstone-blue%20deoployemnt.png)

![alt text](https://github.com/Farrukhkhalid/DevOps_capstone/blob/main/screens/9%20capstone-green%20cluster.png)

<br/><br/>
### CI/CD pipeline

![alt text](https://github.com/Farrukhkhalid/DevOps_capstone/blob/main/screens/capstone-cicd.png)

<br/><br/>
### OUPUT
![alt text](https://github.com/Farrukhkhalid/DevOps_capstone/blob/main/screens/10%20capstone-out-green.png)
