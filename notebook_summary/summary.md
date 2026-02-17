# Workshop Notebooks - Quick Guide

## 00-start-here.ipynb
**Setup notebook - Run this first!**

- Installs SageMaker SDK, MLflow, and other required packages
- Sets up MLflow tracking server for experiment management
- Downloads the Bank Marketing dataset from UCI
- Uploads data to S3 for SageMaker access
- Installs Docker for local testing
- Configures AWS environment (region, buckets, roles)

## 01-idea-development.ipynb
**Traditional ML development in a notebook**

- Explores the bank marketing dataset with charts and stats
- Engineers features (age groups, indicators, scaling)
- Trains XGBoost model with different hyperparameters
- Tracks experiments with MLflow (parameters, metrics, models)
- Registers best model in MLflow registry
- Everything runs locally in the notebook

## 02-sagemaker-containers.ipynb
**Moving from local to cloud execution**

- Converts notebook code into standalone Python scripts
- Runs data processing as SageMaker Processing jobs
- Tests jobs locally first, then runs on cloud
- Uses @remote decorator to run functions as SageMaker jobs
- Trains models on SageMaker infrastructure
- Integrates MLflow tracking with cloud jobs
- Learns about containers and scalable compute

## 03-sagemaker-pipeline.ipynb
**Building automated ML workflows**

- Creates a SageMaker Pipeline with multiple steps
- Automates: data processing → training → evaluation → registration
- Adds conditional logic (only register if model is good enough)
- Uses Feature Store to manage and share features
- Registers models in SageMaker Model Registry
- Makes workflows repeatable and parameterized

## 04-sagemaker-project.ipynb
**Adding CI/CD for model building**

- Creates MLOps project from SageMaker template
- Connects to GitHub repositories
- Sets up CodePipeline for automation
- Code commits trigger automatic model training
- Models get registered in Model Registry automatically
- Implements GitOps for ML workflows

## 05-deploy.ipynb
**Automated model deployment**

- Approves models in Model Registry
- Automatically deploys to staging endpoint
- Runs tests on staging
- Manual approval before production
- Deploys to production endpoint
- Enables data capture for monitoring
- Uses CloudFormation for infrastructure

## 06-monitoring.ipynb
**Continuous quality monitoring**

- Monitors data quality (detects drift in input data)
- Monitors model quality (tracks prediction accuracy)
- Creates baselines from training data
- Sets up automated monitoring schedules
- Generates reports on violations and anomalies
- Integrates with CloudWatch for alerts
- Can trigger automatic retraining

## 07-clean-up.ipynb
**Removing all resources**

- Deletes SageMaker Projects
- Removes monitoring schedules
- Deletes endpoints
- Cleans up Feature Groups
- Removes S3 data
- Deletes MLflow servers
- Prevents ongoing AWS charges
- Interactive - asks before deleting each resource
