# GreenTech Analytics - Cloud Prototype Service

## Project Overview
A serverless prototype built to process live weather data (OpenWeatherMap API) and historical climate datasets (Kaggle) using AWS Lambda and Azure Functions based on the NIST cloud model.

## Features
- **NIST Compliance:** On-demand self-service, rapid elasticity, and measured service.
- **Multi-Cloud Implementation:** AWS Lambda and Azure Functions.
- **Data Integration:** Live REST APIs + Historical Climate CSV chunks.
- **Security:** HTTPS and environment variable configuration for API keys.

## Setup & Deployment Instructions
1. Clone the repository to your local machine.
2. Set up environment variables (e.g., `OPENWEATHER_API_KEY`).
3. Deploy `aws_lambda_function.py` on AWS Lambda console.
4. Deploy `azure_function.py` on Azure Functions via VS Code extension.