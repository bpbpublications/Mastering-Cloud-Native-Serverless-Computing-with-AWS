# Citizen Feedback System - BackendStack

    This backend CDK stack is built using Python and has the backend AWS resources for managing citizen feedback app

## 1) To start using this backend stack, clone the git repository

    git clone https://github.com/XXXXX/mastering_serverless_backend.git
    ### Replace this with the actual github repository URL

## 2) Once the repository is cloned, it will create a folder "mastering_serverless_backend"
## Navigate to this folder, and open Visual Studio Code

    cd mastering_serverless_backend
    code .

## 3) Create a Python Virtual environment and activate the same

    python -m venv .venv
    .venv\Scripts\activate

## 4) Install the required dependencies from "requirements.txt"

    pip install -r requirements.txt

## 5) Ensure the local AWS profile "feedback-dev" is configured

    aws configure --profile feedback-dev
    # Copy Access Key, Secret from the IAM user which has access in this account

## 5) Perform CDK bootstrap to ensure the AWS account is bootstrapped

    cdk bootstrap
    # This will use the feedback-dev credentials to complete bootstrap

## 6) Synthesize CDK

    cdk synth

## 7) Deploy via CDK

    cdk deploy --profile feedback-dev

## 8) Login to AWS Account, Navigate to CloudFormation and look for the backend stack "FeedbackBackendStack"

    All the resources will be created from this Stack

## 9) Navigate into each of the AWS services to check the resources