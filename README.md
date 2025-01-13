# ML API Deployment on AWS with Docker and CI/CD

This repository contains the code for deploying a machine learning API using **FastAPI**, **Docker**, and automating the deployment using **GitHub Actions**. The API serves predictions from a pre-trained model hosted on **AWS** with continuous integration and deployment (CI/CD) set up using **AWS ECS** (Elastic Container Service).

### Overview

- **FastAPI** is used to build a RESTful API that serves machine learning predictions.
- **Docker** is used to containerize the FastAPI application.
- **GitHub Actions** automates the build and deployment pipeline to AWS.
- **AWS ECS** is used to manage the containerized application on the cloud.

---

## Prerequisites

- **AWS Account**: Required to use AWS services like **ECR**, **ECS**, **IAM**, etc.
- **Docker**: Installed and running on your local machine for containerization.
- **AWS CLI**: Installed and configured with appropriate permissions.
- **GitHub**: A GitHub account to use GitHub Actions for automation.

---

## Project Structure

```
ml-api/
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions workflow file
├── app/
│   ├── main.py             # FastAPI application
│   ├── model.pkl           # Pre-trained ML model (for prediction)
│   ├── requirements.txt    # Python dependencies
├── Dockerfile              # Dockerfile to containerize the app
└── README.md               # This file
```

---

## Setting Up the Project

### 1. Clone the Repository

Start by cloning this repository to your local machine:

```bash
git clone https://github.com/yourusername/ml-api.git
cd ml-api
```

### 2. Dockerize the FastAPI Application

The FastAPI application is containerized using Docker.

#### Dockerfile:

The `Dockerfile` builds the image using the following steps:

1. Use the `python:3.9-slim` image.
2. Install the required Python packages using `pip`.
3. Run the FastAPI app with `uvicorn`.

To build the Docker image, run:

```bash
docker build -t ml-api .
```

Then, to test the container locally:

```bash
docker run -p 8000:8000 ml-api
```

Visit `http://127.0.0.1:8000` in your browser to check if the FastAPI app is running.

### 3. Push Docker Image to AWS ECR

#### Step 1: Create an ECR Repository

Go to the AWS Console, navigate to **ECR (Elastic Container Registry)**, and create a new repository.

#### Step 2: Log in to ECR

Run the following command to authenticate Docker with your AWS ECR:

```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <your_ecr_uri>
```

Replace `<your_ecr_uri>` with your ECR repository URI.

#### Step 3: Tag and Push the Docker Image

Tag the Docker image and push it to your AWS ECR repository:

```bash
docker tag ml-api:latest <your_ecr_uri>/ml-api:latest
docker push <your_ecr_uri>/ml-api:latest
```

---

## CI/CD Setup with GitHub Actions

The deployment pipeline is automated using **GitHub Actions**.

### Workflow File

The `.github/workflows/deploy.yml` file defines the CI/CD pipeline. It runs when there is a push to the `main` branch. The pipeline:

1. **Checks out** the code from the repository.
2. **Logs in** to AWS using GitHub Secrets (`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`).
3. **Builds the Docker image**.
4. **Pushes the image** to the AWS ECR repository.

### Setting up GitHub Secrets

To securely store your AWS credentials, you can use GitHub Secrets:

1. Go to **Settings** → **Secrets** in your GitHub repository.
2. Create new secrets:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`

---

## Deploying to AWS ECS

After pushing the Docker image to ECR, the application is ready to be deployed to **AWS ECS** (Elastic Container Service).

### Step 1: Create an ECS Cluster

1. In AWS Console, navigate to **ECS** and create a new cluster (Fargate or EC2).
2. Configure networking, task definitions, and any necessary permissions.

### Step 2: Create an ECS Task Definition

In ECS, a **Task Definition** tells ECS how to run your Docker containers. Create a task definition that points to the Docker image in your ECR repository.

### Step 3: Set Up ECS Service

Create an ECS Service to run the container, set scaling policies, and ensure high availability.

---

## How to Use the API

Once deployed, you can interact with the ML API by sending **POST** requests to the `/predict` endpoint.

### Example Request (using `curl`)

```bash
curl -X POST "http://<ecs-service-url>/predict" -H "Content-Type: application/json" -d "[[5.1, 3.5, 1.4, 0.2]]"
```

This will send the input data to the model, and the API will return a prediction.

### Example Response

```json
{
    "prediction": [0.0]
}
```

---

## Troubleshooting

- **"Error loading ASGI app"**: Ensure that `main.py` contains the correct FastAPI instance and that you're running Uvicorn correctly.
- **Docker Image Push Issues**: Double-check your AWS ECR repository URI and ensure your AWS credentials are properly configured.
- **ECS Deployment Failures**: Review your ECS Task Definition and Service configuration.

---

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make changes, and create a pull request.

---

## License

This project is licensed under the MIT License.

---
