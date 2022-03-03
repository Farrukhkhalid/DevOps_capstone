# **Udacity DevOps Capstone Project**
**PROJECT CONTENT**
- Config.yml: CI/CD pipeline that deploys aws eks
- k8s-deployment.yml: creates rolling update deployment
- k8s-service.yml: creates ELB
- Dockerfile: instructions to assemble Docker image
- Makefile
- app.py
- requirments


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


**Issue encountered**
- Kubectl Permitions
- IAM use roles
- IAM auth

## WORK FLOW

### **1. Linting**
First we start with linting Docker file with Hado lint and source code with pylint

***creating avirtual env install***
`python3 -m venv venv` `. venv/bin/activate`

***Install Makefile***
`make install`

***install hado and pylint***
`wget -O /bin/hadolint   https://github.com/hadolint/hadolint/releases/download/v1.16.3/hadolint-Linux-x86_64`

***Run Docker Lint***
`hadolint Dockerfile`

***Run pylint***
`pylint app.py --errors-only`

![alt text](https://github.com/Farrukhkhalid/DevOps_capstone/blob/main/screens/01%20capstone-lint.png)




### **2. Deploying Cluster**

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
