# CI/CD Pipeline Project

## Overview

This is practice repository demonstrates the implementation of a  CI/CD pipeline using modern DevOps practices. The project showcases the integration of various tools and techniques to ensure smooth development and deployment processes.

## Tech Stack

- **Docker**: Containerization platform used to build and run applications in isolated environments.
- **Python**: Programming language for application development and testing.
- **GitHub Actions**: CI/CD service for automating workflows directly from GitHub.
- **unittest**: Python module used for writing and running unit tests.

## Project Structure

- `Dockerfile`: Defines the Docker image for the project.
- `hello.py`: A simple Python script that prints "Hello Docker."
- `tests.py`: Contains unit tests for the Python script.
- `.github/workflows`: Directory for GitHub Actions workflows (currently empty).

## Getting Started

### Prerequisites

- Docker installed on your local machine(wsl)
- Python 3.x installed
- GitHub account

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/ci-cd-pipeline-project.git
   cd ci-cd-pipeline-project
   
2. **Build and Run the Docker Container**

```bash
docker build -t hello-docker .
docker run hello-docker
```

3. **Run Tests**

```bash
python -m unittest tests.py
