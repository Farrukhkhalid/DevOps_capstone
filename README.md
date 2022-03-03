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

**1. Linting**
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
