# CI/CD Pipeline with GitHub Actions and AWS Elastic Beanstalk

## Overview

This repository contains a Python web application built with Flask, configured with a CI/CD pipeline using GitHub Actions for automated testing and deployment to AWS Elastic Beanstalk.

## How It Works

The CI/CD pipeline is triggered on every push to the `main` branch or pull request targeting `main`. It sets up a Python environment, installs dependencies, runs unit tests, and deploys the application to the cloud if all tests pass.

## Schematic Diagram

![Schematic Diagram](https://github.com/Zhagi/CI_CD-Pipeline/blob/main/Images/CI:CD%20Pipeline%20Diagram.png?raw=true)

The diagram above simplifies the understanding of the CI/CD process and shows the path from a developer's push to the deployment of a live application.


## Getting Started

### Prerequisites

- Python 3.x
- Git
- AWS account with Elastic Beanstalk and IAM configured

### Installation

# Clone the repository
git clone https://github.com/Zhagi/CI-CD-Pipeline.git
cd CI-CD-Pipeline

# Set up and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask application locally
python application.py

# Run the unit tests
pytest

## Deployment

The application is automatically deployed to AWS Elastic Beanstalk through the configured GitHub Actions workflow.

## GitHub Actions Workflow

The `.github/workflows/ci-cd-pipeline.yml` file contains the workflow configuration. It includes the following steps:

1. Setup Python environment
2. Install dependencies
3. Run unit tests
4. Deploy to AWS Elastic Beanstalk (on push to `main`)

## Configuration

### GitHub Secrets

- `AWS_ACCESS_KEY_ID`: AWS access key for deployment.
- `AWS_SECRET_ACCESS_KEY`: AWS secret access key for deployment.

Below are the images showing the health of the EB environment, the environment URL, and the Flask application in action:

Health of the EB Environment:

![Elasticbeanstalk Environment](https://github.com/Zhagi/CI_CD-Pipeline/blob/main/Images/Elastic%20Beanstalk%20Environment.png?raw=true)

Accessing the Environment URL and the Flask App:

![Elastic Beanstalk environment URL](https://github.com/Zhagi/CI_CD-Pipeline/blob/main/Images/Elastic%20Beanstalk%20environment%20URL.png?raw=true)


