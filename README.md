# CI_CD-Pipeline with GitHub Actions deployed to AWS Elastic Beanstalk

## Overview

This repository contains a Python web application built with Flask, configured with a CI/CD pipeline using GitHub Actions for automated testing and deployment to AWS Elastic Beanstalk.

## How It Works

The CI/CD pipeline is triggered on every push to the `main` branch or pull request targeting `main`. It sets up a Python environment, installs dependencies, runs unit tests, and deploys the application to the cloud if all tests pass.

## Schematic Diagram

![Schematic Diagram](https://github.com/Zhagi/CI_CD-Pipeline/blob/main/Images/CI:CD%20Pipeline%20Diagram.png?raw=true)

## Getting Started

### Prerequisites

- Python 3.x
- Git
- AWS account with Elastic Beanstalk and IAM configured

### Installation

1. Clone the repository:
git clone https://github.com/Zhagi/CI-CD-Pipeline.git
cd CI-CD-Pipeline
2. Set up a virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate
3. Install dependencies:
pip install -r requirements.txt

## Running Locally
To run the Flask application locally:
python application.py

## Testing

Run the unit tests with the following command:
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

### Outcome

![IAM Config](https://github.com/Zhagi/CI_CD-Pipeline/blob/main/Images/IAM%20config.png?raw=true)

![Elasticbeanstalk Environment](https://github.com/Zhagi/CI_CD-Pipeline/blob/main/Images/Elastic%20Beanstalk%20Environment.png?raw=true)

![EC2 instance creation](https://github.com/Zhagi/CI_CD-Pipeline/blob/main/Images/EC2%20instance%20created.png?raw=true)

![Elastic Beanstalk environment URL](https://github.com/Zhagi/CI_CD-Pipeline/blob/main/Images/Elastic%20Beanstalk%20environment%20URL.png?raw=true)

(![S3 created by EB](https://github.com/Zhagi/CI_CD-Pipeline/blob/main/Images/S3%20bucket%20created.png?raw=true)
