# Module 5: Deployment and CI/CD

## Objectives
- Containerize applications using Docker
- Deploy applications to Kubernetes/OpenShift
- Set up automated CI/CD pipelines with GitHub Actions
- Configure environment variables for different deployment stages
- Implement health checks and monitoring
- Understand cloud deployment best practices
- Manage application secrets securely
- Perform zero-downtime deployments

## Key Concepts

### Containerization
Containers package applications with all dependencies:
- **Docker**: Platform for building and running containers
- **Image**: Blueprint for a container (includes code, runtime, dependencies)
- **Container**: Running instance of an image
- **Dockerfile**: Instructions for building a Docker image

### Kubernetes/OpenShift
Container orchestration platforms:
- **Pod**: Smallest deployable unit (one or more containers)
- **Deployment**: Manages desired state and scaling of pods
- **Service**: Exposes pods to network traffic
- **Ingress/Route**: External access to services

### CI/CD Pipeline
Automated workflow for code deployment:
- **Continuous Integration (CI)**: Automatically test code on every commit
- **Continuous Deployment (CD)**: Automatically deploy passing builds
- **GitHub Actions**: GitHub's built-in CI/CD platform

### Environment Separation
Different configurations for each stage:
- **Development**: Local machine with debug enabled
- **Staging**: Cloud environment mirroring production
- **Production**: Live environment serving real users

### Twelve-Factor App
Best practices for cloud-native applications:
1. Codebase: One codebase tracked in version control
2. Dependencies: Explicitly declare dependencies
3. Config: Store config in environment variables
4. Backing services: Treat databases as attached resources
5. Build, release, run: Strictly separate these stages
6. Processes: Execute app as stateless processes
7. Port binding: Export services via port binding
8. Concurrency: Scale out via process model
9. Disposability: Fast startup and graceful shutdown
10. Dev/prod parity: Keep environments as similar as possible
11. Logs: Treat logs as event streams
12. Admin processes: Run admin tasks as one-off processes

## Tools & Commands

### Docker Commands

**Build Image**:
```bash
# Build from Dockerfile in current directory
docker build -t dealership-app:latest .

# Build with specific Dockerfile
docker build -f Dockerfile.prod -t dealership-app:prod .

# Build with build arguments
docker build --build-arg ENV=production -t app:prod .
```

**Run Container**:
```bash
# Run in foreground
docker run -p 8000:8000 dealership-app:latest

# Run in background (detached)
docker run -d -p 8000:8000 dealership-app:latest

# Run with environment variables
docker run -e DATABASE_URL=postgres://... dealership-app:latest

# Run with volume mount
docker run -v $(pwd):/app dealership-app:latest
```

**Container Management**:
```bash
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Stop container
docker stop <container-id>

# Remove container
docker rm <container-id>

# View logs
docker logs <container-id>

# Execute command in running container
docker exec -it <container-id> bash
```

**Docker Compose**:
```bash
# Start all services defined in docker-compose.yml
docker-compose up

# Start in background
docker-compose up -d

# Stop all services
docker-compose down

# View logs
docker-compose logs -f

# Rebuild images
docker-compose build
```

### Kubernetes/OpenShift Commands

**Deploy Application**:
```bash
# Apply deployment configuration
kubectl apply -f deployment.yaml

# Apply service configuration
kubectl apply -f service.yaml

# Create deployment imperatively
kubectl create deployment dealership --image=dealership-app:latest
```

**Manage Deployments**:
```bash
# List deployments
kubectl get deployments

# List pods
kubectl get pods

# Describe deployment
kubectl describe deployment dealership

# Scale deployment
kubectl scale deployment dealership --replicas=3

# Update image
kubectl set image deployment/dealership app=dealership-app:v2
```

**Access and Debugging**:
```bash
# View pod logs
kubectl logs <pod-name>

# Follow logs
kubectl logs -f <pod-name>

# Execute command in pod
kubectl exec -it <pod-name> -- bash

# Port forward to local machine
kubectl port-forward deployment/dealership 8000:8000

# Describe pod (useful for debugging)
kubectl describe pod <pod-name>
```

**Services and Routes**:
```bash
# List services
kubectl get services

# Expose deployment
kubectl expose deployment dealership --port=8000 --target-port=8000

# OpenShift: Create route
oc expose service dealership
```

### GitHub Actions

**Workflow File Location**:
```bash
# GitHub Actions workflows go in .github/workflows/
.github/
└── workflows/
    ├── ci.yml          # Continuous Integration
    └── deploy.yml      # Deployment
```

**Manually Trigger Workflow**:
```bash
# Using GitHub CLI
gh workflow run deploy.yml
```

**View Workflow Runs**:
```bash
# List workflow runs
gh run list

# View specific run
gh run view <run-id>

# View run logs
gh run view <run-id> --log
```

## Code Snippets

### Dockerfile for Django + React
```dockerfile
# Dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY server/ .

# Collect static files
RUN python manage.py collectstatic --no-input

# Expose port
EXPOSE 8000

# Run application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "djangoproj.wsgi:application"]
```

### Entrypoint Script
```bash
#!/bin/bash
# entrypoint.sh

echo "Applying database migrations..."
python manage.py migrate --no-input

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Starting Gunicorn..."
exec gunicorn --bind 0.0.0.0:8000 --workers 3 djangoproj.wsgi:application
```

### Docker Compose Configuration
```yaml
# docker-compose.yml
version: '3.8'

services:
  db:
    image: postgres:13
    environment:
      POSTGRES_DB: dealership
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - ./server:/app
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://admin:password@db:5432/dealership
      - DEBUG=True
    depends_on:
      - db

volumes:
  postgres_data:
```

### Kubernetes Deployment
```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: dealership
  labels:
    app: dealership
spec:
  replicas: 2
  selector:
    matchLabels:
      app: dealership
  template:
    metadata:
      labels:
        app: dealership
    spec:
      containers:
      - name: dealership
        image: dealership-app:latest
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: url
        - name: SECRET_KEY
          valueFrom:
            secretKeyRef:
              name: app-secret
              key: secret-key
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
```

### Kubernetes Service
```yaml
# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: dealership-service
spec:
  selector:
    app: dealership
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8000
  type: LoadBalancer
```

### GitHub Actions CI/CD Workflow
```yaml
# .github/workflows/deploy.yml
name: Deploy to OpenShift

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        cd server
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        cd server
        python manage.py test
    
    - name: Run linter
      run: |
        pip install flake8
        flake8 server/ --max-line-length=120

  build:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Build Docker image
      run: |
        docker build -t dealership-app:${{ github.sha }} .
        docker tag dealership-app:${{ github.sha }} dealership-app:latest
    
    - name: Push to registry
      run: |
        echo ${{ secrets.DOCKER_PASSWORD }} | docker login -u ${{ secrets.DOCKER_USERNAME }} --password-stdin
        docker push dealership-app:${{ github.sha }}
        docker push dealership-app:latest

  deploy:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Deploy to OpenShift
      run: |
        oc login ${{ secrets.OPENSHIFT_SERVER }} --token=${{ secrets.OPENSHIFT_TOKEN }}
        oc project ${{ secrets.OPENSHIFT_PROJECT }}
        kubectl set image deployment/dealership dealership=dealership-app:${{ github.sha }}
        kubectl rollout status deployment/dealership
```

### Environment Configuration
```python
# server/djangoproj/settings.py
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

# Database
if os.environ.get('DATABASE_URL'):
    # Production: Use PostgreSQL
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600
        )
    }
else:
    # Development: Use SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Security settings for production
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
```

### Health Check Endpoint
```python
# djangoapp/views.py
from django.http import JsonResponse
from django.db import connection

def health_check(request):
    """
    Health check endpoint for Kubernetes liveness/readiness probes
    """
    try:
        # Check database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        
        return JsonResponse({
            "status": "healthy",
            "database": "connected"
        })
    except Exception as e:
        return JsonResponse({
            "status": "unhealthy",
            "error": str(e)
        }, status=500)
```

## Common Pitfalls

### 1. Hardcoded Configuration
**Problem**: Sensitive data in source code
**Solution**: Use environment variables
```python
# ❌ Wrong
SECRET_KEY = 'my-secret-key-123'

# ✅ Correct
SECRET_KEY = os.environ.get('SECRET_KEY')
```

### 2. Large Docker Images
**Problem**: Slow builds and deployments
**Solution**: Use multi-stage builds and minimize layers
```dockerfile
# Use slim base images
FROM python:3.9-slim

# Combine RUN commands to reduce layers
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

# Use .dockerignore to exclude unnecessary files
```

### 3. Missing Database Migrations
**Problem**: Application fails with database errors
**Solution**: Run migrations in entrypoint script
```bash
#!/bin/bash
python manage.py migrate --no-input
exec gunicorn djangoproj.wsgi:application
```

### 4. No Health Checks
**Problem**: Kubernetes can't determine if app is healthy
**Solution**: Implement health check endpoints
```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8000
```

### 5. Exposing Debug Mode in Production
**Problem**: Security vulnerability and information leakage
**Solution**: Always disable DEBUG in production
```python
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
```

## Mini Quiz

1. **What is the purpose of a Dockerfile?**
   - **Answer**: A Dockerfile contains instructions for building a Docker image. It specifies the base image, copies application code, installs dependencies, and defines how to run the application. Docker reads this file to create a reproducible image that can run consistently across different environments, from development to production.

2. **What's the difference between a Docker image and a Docker container?**
   - **Answer**: An image is a read-only template containing application code, dependencies, and configuration. A container is a running instance of an image. Think of an image as a class and a container as an object: you can create multiple containers from one image, each with its own state and process.

3. **Why use environment variables instead of hardcoding configuration?**
   - **Answer**: Environment variables allow the same codebase to work in different environments (dev, staging, production) without code changes. They keep sensitive data (passwords, API keys) out of source control, support the Twelve-Factor App methodology, and make configuration changes possible without rebuilding the application.

4. **What is the purpose of health check probes in Kubernetes?**
   - **Answer**: Liveness probes determine if a container is running; if it fails, Kubernetes restarts the container. Readiness probes determine if a container is ready to receive traffic; if it fails, Kubernetes removes the pod from service endpoints. Together, they ensure only healthy pods serve traffic and unhealthy pods are automatically recovered.

5. **What does CI/CD stand for and what's the benefit?**
   - **Answer**: Continuous Integration/Continuous Deployment. CI automatically tests code on every commit, catching bugs early. CD automatically deploys passing builds to production. Benefits include faster releases, reduced manual errors, consistent deployment process, and quicker feedback loops. GitHub Actions, Jenkins, and GitLab CI are common CI/CD tools.

## Practice Task

### Task: Deploy Full-Stack Application to Kubernetes

**Objective**: Containerize the dealership application and deploy it to a Kubernetes cluster with automated CI/CD.

**Requirements**:
1. Create Dockerfile for the application
2. Write docker-compose.yml for local development with PostgreSQL
3. Create Kubernetes deployment and service manifests
4. Set up GitHub Actions workflow for automated testing and deployment
5. Configure environment variables for production
6. Implement health check endpoint
7. Test deployment with kubectl

**Steps**:
1. Write Dockerfile with multi-stage build
2. Create docker-compose.yml with web and db services
3. Test locally with `docker-compose up`
4. Write deployment.yaml with replicas, env vars, and health checks
5. Write service.yaml to expose the application
6. Create .github/workflows/deploy.yml
7. Push code and verify GitHub Actions runs
8. Deploy to Kubernetes cluster
9. Verify application is accessible

**Expected Outcomes**:
- Application runs in Docker container locally
- PostgreSQL database accessible from application
- Kubernetes deployment creates 2 replicas
- Service exposes application on port 80
- GitHub Actions workflow runs on push to main
- Health check endpoint returns 200 OK
- Application accessible via external IP/domain

**Deployment Commands**:
```bash
# Build and test locally
docker build -t dealership-app .
docker run -p 8000:8000 dealership-app

# Deploy to Kubernetes
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# Verify deployment
kubectl get deployments
kubectl get pods
kubectl get services

# Check logs
kubectl logs -f deployment/dealership

# Access application
kubectl port-forward service/dealership-service 8000:80
```

**Hints**:
- Use `COPY --chown` in Dockerfile to set proper permissions
- Set `DEBUG=False` in production environment
- Use Kubernetes secrets for sensitive data
- Test health check: `curl localhost:8000/health`
- Check GitHub Actions logs for deployment errors

## Career Notes

### Relevant Job Roles
- **DevOps Engineer**: Manages CI/CD pipelines, infrastructure, and deployments
- **Site Reliability Engineer (SRE)**: Ensures system reliability and automates operations
- **Cloud Engineer**: Deploys and manages applications on cloud platforms
- **Full-Stack Developer**: Understands full application lifecycle including deployment
- **Platform Engineer**: Builds and maintains deployment platforms and tooling

### Industry Expectations
- Proficiency with Docker and containerization concepts
- Understanding of Kubernetes/cloud orchestration platforms
- Experience with CI/CD tools (GitHub Actions, Jenkins, GitLab CI)
- Knowledge of cloud providers (AWS, Azure, GCP, IBM Cloud)
- Infrastructure as Code (IaC) with Terraform or similar
- Monitoring and logging (Prometheus, Grafana, ELK stack)
- Security best practices for deployments
- Understanding of networking and load balancing

### Interview Topics
- "Describe a deployment pipeline you've built"
- "How do you handle secrets in containerized applications?"
- "What's your strategy for zero-downtime deployments?"
- "Explain how you would debug a failing pod in Kubernetes"
- "What's the difference between a deployment and a statefulset?"
- "How do you ensure high availability in production?"
- "Describe your approach to monitoring and alerting"

### Skills Demonstrated
- Containerization and Docker expertise
- Kubernetes deployment and management
- CI/CD pipeline development
- Infrastructure automation
- Environment management
- Security and secrets handling
- Troubleshooting and debugging production issues
- Cloud platform proficiency

### Industry Trends
- **Serverless**: AWS Lambda, Cloud Functions for event-driven apps
- **GitOps**: Argo CD, Flux for declarative deployments
- **Service Mesh**: Istio, Linkerd for microservices communication
- **Observability**: Distributed tracing, metrics, and logs
- **Platform Engineering**: Building internal developer platforms
- **FinOps**: Cloud cost optimization and management

### Certifications Worth Considering
- Certified Kubernetes Administrator (CKA)
- Certified Kubernetes Application Developer (CKAD)
- AWS Certified Solutions Architect
- Google Cloud Professional Cloud Architect
- Docker Certified Associate
- Red Hat Certified Specialist in OpenShift
