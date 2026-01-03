# Commands Cheatsheet

Quick reference for common commands used in full-stack development with Django, React, Docker, and Kubernetes.

## Django Commands

### Project Management
```bash
# Create new project
django-admin startproject projectname

# Create new app
python manage.py startapp appname

# Run development server
python manage.py runserver
python manage.py runserver 0.0.0.0:8000  # All interfaces
python manage.py runserver 8080          # Custom port

# Interactive Python shell with Django context
python manage.py shell
```

### Database Operations
```bash
# Create migrations after model changes
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Show migration status
python manage.py showmigrations

# Revert migrations (development only)
python manage.py migrate appname zero

# Export data as fixture
python manage.py dumpdata appname > fixture.json

# Load fixture data
python manage.py loaddata fixture.json

# SQL for migration (without applying)
python manage.py sqlmigrate appname 0001
```

### User Management
```bash
# Create superuser interactively
python manage.py createsuperuser

# Create superuser non-interactively
python manage.py createsuperuser --username admin --email admin@example.com --noinput

# Change user password
python manage.py changepassword username
```

### Static Files
```bash
# Collect static files to STATIC_ROOT
python manage.py collectstatic

# Collect static files without prompts
python manage.py collectstatic --no-input

# Find static files locations
python manage.py findstatic filename.css
```

### Testing
```bash
# Run all tests
python manage.py test

# Run tests for specific app
python manage.py test appname

# Run tests with verbosity
python manage.py test --verbosity=2

# Keep test database
python manage.py test --keepdb
```

## React / NPM Commands

### Project Setup
```bash
# Create new React app
npx create-react-app app-name

# Install dependencies from package.json
npm install

# Install specific package
npm install package-name

# Install dev dependency
npm install --save-dev package-name

# Install specific version
npm install package-name@1.2.3
```

### Development
```bash
# Start development server (port 3000)
npm start

# Custom port
PORT=3001 npm start

# Build for production
npm run build

# Run tests
npm test

# Run tests in CI mode
CI=true npm test

# Eject from create-react-app (irreversible)
npm run eject
```

### Package Management
```bash
# Update all packages
npm update

# Check for outdated packages
npm outdated

# Remove package
npm uninstall package-name

# List installed packages
npm list

# Clear npm cache
npm cache clean --force
```

## Docker Commands

### Image Management
```bash
# Build image from Dockerfile
docker build -t image-name:tag .

# Build with specific Dockerfile
docker build -f Dockerfile.prod -t image-name:prod .

# Build with build arguments
docker build --build-arg ENV=production -t image-name .

# List images
docker images

# Remove image
docker rmi image-name:tag

# Remove all unused images
docker image prune -a

# Tag image
docker tag source-image:tag target-image:tag

# Push to registry
docker push registry/image-name:tag
```

### Container Management
```bash
# Run container
docker run image-name

# Run in detached mode
docker run -d image-name

# Run with port mapping
docker run -p 8000:8000 image-name

# Run with environment variable
docker run -e DATABASE_URL=postgres://... image-name

# Run with volume mount
docker run -v /host/path:/container/path image-name

# Run with name
docker run --name container-name image-name

# List running containers
docker ps

# List all containers
docker ps -a

# Stop container
docker stop container-id

# Start stopped container
docker start container-id

# Restart container
docker restart container-id

# Remove container
docker rm container-id

# Remove all stopped containers
docker container prune
```

### Container Inspection
```bash
# View logs
docker logs container-id

# Follow logs
docker logs -f container-id

# Execute command in running container
docker exec -it container-id bash

# Inspect container
docker inspect container-id

# View container stats
docker stats container-id

# Copy files from container
docker cp container-id:/path/to/file ./local-path

# Copy files to container
docker cp ./local-file container-id:/path/to/destination
```

### Docker Compose
```bash
# Start services (foreground)
docker-compose up

# Start services (background)
docker-compose up -d

# Stop services
docker-compose down

# Stop and remove volumes
docker-compose down -v

# Build or rebuild services
docker-compose build

# View logs
docker-compose logs

# Follow logs
docker-compose logs -f

# Follow logs for specific service
docker-compose logs -f service-name

# List containers
docker-compose ps

# Execute command in service
docker-compose exec service-name bash

# Run one-off command
docker-compose run service-name python manage.py migrate
```

## Kubernetes Commands (kubectl)

### Cluster Information
```bash
# Cluster info
kubectl cluster-info

# Get nodes
kubectl get nodes

# Describe node
kubectl describe node node-name

# Get namespaces
kubectl get namespaces

# Set default namespace
kubectl config set-context --current --namespace=namespace-name
```

### Deployments
```bash
# Create deployment from YAML
kubectl apply -f deployment.yaml

# Create deployment imperatively
kubectl create deployment name --image=image-name

# List deployments
kubectl get deployments

# Describe deployment
kubectl describe deployment deployment-name

# Edit deployment
kubectl edit deployment deployment-name

# Delete deployment
kubectl delete deployment deployment-name

# Scale deployment
kubectl scale deployment deployment-name --replicas=5

# Update image
kubectl set image deployment/deployment-name container-name=new-image:tag

# Rollout status
kubectl rollout status deployment/deployment-name

# Rollout history
kubectl rollout history deployment/deployment-name

# Rollback deployment
kubectl rollout undo deployment/deployment-name

# Rollback to specific revision
kubectl rollout undo deployment/deployment-name --to-revision=2
```

### Pods
```bash
# List pods
kubectl get pods

# List pods with more details
kubectl get pods -o wide

# Describe pod
kubectl describe pod pod-name

# Delete pod
kubectl delete pod pod-name

# View pod logs
kubectl logs pod-name

# Follow pod logs
kubectl logs -f pod-name

# Logs from specific container in pod
kubectl logs pod-name -c container-name

# Execute command in pod
kubectl exec -it pod-name -- bash

# Copy files to/from pod
kubectl cp local-file pod-name:/path/in/pod
kubectl cp pod-name:/path/in/pod local-file
```

### Services
```bash
# Create service
kubectl expose deployment deployment-name --port=80 --target-port=8000

# Create service from YAML
kubectl apply -f service.yaml

# List services
kubectl get services

# Describe service
kubectl describe service service-name

# Delete service
kubectl delete service service-name

# Port forward to local machine
kubectl port-forward service/service-name 8000:80

# Port forward pod
kubectl port-forward pod/pod-name 8000:8000
```

### ConfigMaps and Secrets
```bash
# Create ConfigMap from literal
kubectl create configmap config-name --from-literal=key=value

# Create ConfigMap from file
kubectl create configmap config-name --from-file=config.txt

# List ConfigMaps
kubectl get configmaps

# Describe ConfigMap
kubectl describe configmap config-name

# Create Secret from literal
kubectl create secret generic secret-name --from-literal=password=mypassword

# Create Secret from file
kubectl create secret generic secret-name --from-file=secret.txt

# List Secrets
kubectl get secrets

# Describe Secret
kubectl describe secret secret-name
```

### Debugging
```bash
# Get events
kubectl get events

# Get events sorted by time
kubectl get events --sort-by=.metadata.creationTimestamp

# Describe resource (generic)
kubectl describe <resource-type> <resource-name>

# Check pod resource usage
kubectl top pods

# Check node resource usage
kubectl top nodes

# Get YAML definition of resource
kubectl get deployment deployment-name -o yaml

# Get JSON definition of resource
kubectl get deployment deployment-name -o json
```

## Git Commands

### Basic Operations
```bash
# Initialize repository
git init

# Clone repository
git clone <url>

# Check status
git status

# Add files
git add file.txt
git add .                    # Add all changes

# Commit changes
git commit -m "Commit message"

# Push changes
git push origin main

# Pull changes
git pull origin main

# View commit history
git log
git log --oneline           # Condensed view
```

### Branching
```bash
# Create branch
git branch branch-name

# Switch to branch
git checkout branch-name

# Create and switch to branch
git checkout -b branch-name

# List branches
git branch

# Delete branch
git branch -d branch-name

# Merge branch
git merge branch-name

# Rebase
git rebase main
```

### Useful Shortcuts
```bash
# Unstage file
git reset HEAD file.txt

# Discard local changes
git checkout -- file.txt

# View diff
git diff
git diff --staged           # Staged changes

# Stash changes
git stash
git stash pop

# View remote URLs
git remote -v

# Add remote
git remote add origin <url>
```

## cURL Commands (API Testing)

### GET Requests
```bash
# Simple GET
curl http://localhost:8000/api/endpoint

# GET with headers
curl -H "Authorization: Bearer token" http://localhost:8000/api/endpoint

# Save response to file
curl -o output.json http://localhost:8000/api/endpoint

# Follow redirects
curl -L http://localhost:8000/api/endpoint

# Verbose output (debugging)
curl -v http://localhost:8000/api/endpoint
```

### POST Requests
```bash
# POST with JSON data
curl -X POST http://localhost:8000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"pass123"}'

# POST with data from file
curl -X POST http://localhost:8000/api/endpoint \
  -H "Content-Type: application/json" \
  -d @data.json

# POST form data
curl -X POST http://localhost:8000/api/endpoint \
  -d "field1=value1&field2=value2"

# POST with file upload
curl -X POST http://localhost:8000/api/upload \
  -F "file=@/path/to/file.pdf"
```

### Other Methods
```bash
# PUT request
curl -X PUT http://localhost:8000/api/resource/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Updated Name"}'

# DELETE request
curl -X DELETE http://localhost:8000/api/resource/1

# PATCH request
curl -X PATCH http://localhost:8000/api/resource/1 \
  -H "Content-Type: application/json" \
  -d '{"field":"new value"}'
```

## Python Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Deactivate
deactivate

# Install requirements
pip install -r requirements.txt

# Generate requirements
pip freeze > requirements.txt

# Install package
pip install package-name

# Upgrade package
pip install --upgrade package-name

# Uninstall package
pip uninstall package-name
```

## PostgreSQL Commands

```bash
# Connect to database
psql -U username -d database_name

# List databases
\l

# Connect to database
\c database_name

# List tables
\dt

# Describe table
\d table_name

# Run SQL file
psql -U username -d database_name -f script.sql

# Dump database
pg_dump database_name > backup.sql

# Restore database
psql database_name < backup.sql

# Create database
createdb database_name

# Drop database
dropdb database_name
```

## Helpful Aliases

Add these to your `.bashrc` or `.zshrc`:

```bash
# Django
alias dj='python manage.py'
alias djrun='python manage.py runserver'
alias djmm='python manage.py makemigrations'
alias djm='python manage.py migrate'
alias djtest='python manage.py test'

# Docker
alias dc='docker-compose'
alias dcu='docker-compose up'
alias dcd='docker-compose down'
alias dcb='docker-compose build'
alias dps='docker ps'

# Kubernetes
alias k='kubectl'
alias kgp='kubectl get pods'
alias kgd='kubectl get deployments'
alias kgs='kubectl get services'
alias kl='kubectl logs'

# Git
alias gs='git status'
alias ga='git add'
alias gc='git commit -m'
alias gp='git push'
alias gl='git pull'
alias gco='git checkout'
```
