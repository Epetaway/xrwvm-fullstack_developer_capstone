# Module 1: Project Architecture and Setup

## Objectives
- Understand the full-stack application architecture and component interaction
- Set up a local development environment with all required tools
- Initialize Django and React projects with proper structure
- Configure development databases (SQLite for Django, MongoDB for microservices)
- Establish version control workflows with Git and GitHub
- Plan project requirements and define the application scope

## Key Concepts

### Full-Stack Architecture
A full-stack application consists of three primary layers:
- **Frontend (Client)**: User interface built with React, runs in the browser
- **Backend (Server)**: Business logic and API built with Django, runs on the server
- **Database**: Data persistence layer using SQLite (development) or PostgreSQL (production)

### Monorepo vs. Multi-Repo
This capstone uses a **monorepo** approach where both frontend and backend code live in the same repository:
```
project-root/
├── server/              # Backend code
│   ├── djangoapp/       # Main application
│   ├── djangoproj/      # Project settings
│   ├── frontend/        # React application
│   └── manage.py
└── README.md
```

### Development vs. Production
- **Development**: SQLite database, Django development server, React development server
- **Production**: PostgreSQL/MongoDB, Gunicorn WSGI server, optimized React build, containerized deployment

### Microservices Pattern
The capstone demonstrates microservices by separating concerns:
- **Main Django App**: Handles user management, reviews, dealer data
- **Node.js Service**: Manages dealer and review data with MongoDB
- **Flask Sentiment Service**: Provides AI-powered sentiment analysis
- **Frontend**: Serves the user interface

## Tools & Commands

### Prerequisites Installation

**Python 3.8+**:
```bash
# Check Python version
python --version

# Install pip packages
pip install --upgrade pip
```

**Node.js 14+**:
```bash
# Check Node version
node --version
npm --version
```

**Django Installation**:
```bash
# Install Django 4.0+
pip install django==4.0

# Verify installation
django-admin --version
```

**React Setup**:
```bash
# Create React app (if starting from scratch)
npx create-react-app frontend

# Install dependencies
npm install react-router-dom
```

### Project Initialization

**Starting a Django Project**:
```bash
# Create new Django project
django-admin startproject djangoproj

# Create Django app within project
cd djangoproj
python manage.py startapp djangoapp

# Run initial migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser
```

**Django Development Server**:
```bash
# Run on default port 8000
python manage.py runserver

# Run on specific port
python manage.py runserver 8080

# Run on all network interfaces
python manage.py runserver 0.0.0.0:8000
```

**React Development Server**:
```bash
cd frontend
npm start  # Runs on port 3000 by default
```

### Database Setup

**SQLite (Django default)**:
```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

**MongoDB (for microservices)**:
```bash
# Using Docker
docker run -d -p 27017:27017 --name mongodb mongo:latest

# Or use docker-compose
cd server/database
docker-compose up -d
```

### Version Control

**Git Initialization**:
```bash
# Initialize repository
git init

# Add remote origin
git remote add origin <repository-url>

# Create .gitignore
echo "*.pyc
__pycache__/
db.sqlite3
node_modules/
build/
.env" > .gitignore

# Initial commit
git add .
git commit -m "Initial project setup"
git push -u origin main
```

## Code Snippets

### Django Project Structure
```python
# djangoproj/settings.py - Key configurations
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
DEBUG = True  # Set to False in production
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangoapp',  # Your custom app
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/build'),
    os.path.join(BASE_DIR, 'frontend/build/static'),
]
```

### React App Structure
```javascript
// frontend/src/App.js - Basic routing setup
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home/Home';
import Login from './components/Login/Login';
import Register from './components/Register/Register';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </Router>
  );
}

export default App;
```

### Environment Variables
```bash
# .env file (never commit to Git!)
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:password@localhost/dbname
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Common Pitfalls

### 1. Port Conflicts
**Problem**: `Error: Address already in use`
**Solution**: Kill the process using the port or use a different port
```bash
# Find process using port 8000
lsof -i :8000

# Kill the process
kill -9 <PID>

# Or use different port
python manage.py runserver 8080
```

### 2. CORS Errors
**Problem**: React (port 3000) can't communicate with Django (port 8000)
**Solution**: Install and configure django-cors-headers
```bash
pip install django-cors-headers
```
```python
# settings.py
INSTALLED_APPS = [
    ...
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
```

### 3. Static Files Not Loading
**Problem**: CSS/JS not loading in production
**Solution**: Run collectstatic and configure STATIC_ROOT
```bash
python manage.py collectstatic --no-input
```
```python
# settings.py
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

### 4. Migration Conflicts
**Problem**: Database migrations fail or create conflicts
**Solution**: Check migration dependencies and run migrations in order
```bash
# Show all migrations
python manage.py showmigrations

# Reset migrations (development only)
python manage.py migrate <app> zero

# Create new migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### 5. Node Modules Missing
**Problem**: React app fails to start after cloning
**Solution**: Install dependencies
```bash
cd frontend
npm install
```

## Mini Quiz

1. **What is the purpose of `manage.py` in a Django project?**
   - **Answer**: `manage.py` is a command-line utility that provides various management commands for the Django project, such as running the development server (`runserver`), creating migrations (`makemigrations`), applying migrations (`migrate`), creating superusers (`createsuperuser`), and collecting static files (`collectstatic`).

2. **Why do we use a monorepo structure for full-stack projects?**
   - **Answer**: A monorepo structure keeps frontend and backend code in the same repository, making it easier to coordinate changes across the stack, share configuration files, maintain consistent version history, and simplify deployment pipelines. It's particularly useful for small to medium projects where frontend and backend are tightly coupled.

3. **What's the difference between `npm start` and `npm run build` for a React application?**
   - **Answer**: `npm start` launches a development server with hot-reloading and unoptimized code for rapid development. `npm run build` creates an optimized production build with minified code, removed debugging features, and better performance, which is what gets deployed to production servers.

4. **How does Django handle database changes without manual SQL?**
   - **Answer**: Django uses a migrations system. When you modify models, you run `makemigrations` to create migration files that describe the changes. Then `migrate` applies those changes to the database. This provides version control for database schema and enables team collaboration without manual SQL scripts.

5. **What environment variables should never be committed to Git?**
   - **Answer**: Secret keys, database passwords, API keys, authentication tokens, and any production credentials should never be committed. Instead, use `.env` files (added to `.gitignore`) and provide `.env.example` templates with placeholder values.

## Practice Task

### Task: Initialize a Full-Stack Development Environment

**Objective**: Set up a complete development environment for the capstone project.

**Steps**:
1. Install Python 3.8+, Node.js 14+, and Git
2. Create a new directory for your project
3. Initialize a Django project named `djangoproj`
4. Create a Django app named `djangoapp`
5. Create a React app in `frontend/` directory
6. Configure Django to serve React's build files
7. Set up Git repository with appropriate `.gitignore`
8. Create a superuser for Django admin
9. Run both Django and React development servers simultaneously
10. Verify you can access Django admin at `localhost:8000/admin`

**Expected Outcomes**:
- Django server runs on port 8000
- React development server runs on port 3000
- Django admin is accessible and you can log in
- Git repository is initialized with clean commit history
- `.gitignore` excludes sensitive files and dependencies

**Hints**:
- Use `django-admin startproject` for Django initialization
- Use `npx create-react-app` for React initialization
- Check official documentation for any installation issues
- Test each component independently before integration

**Verification**:
```bash
# Check Django
curl http://localhost:8000/admin/

# Check React
curl http://localhost:3000/

# Check Git status
git status
```

## Career Notes

### Relevant Job Roles
- **Full-Stack Developer**: Requires setting up and managing both frontend and backend environments
- **DevOps Engineer**: Manages development environments, CI/CD pipelines, and infrastructure setup
- **Software Architect**: Designs system architecture and technology stack decisions
- **Technical Lead**: Guides teams through project initialization and establishes development standards

### Industry Expectations
- Employers expect full-stack developers to quickly set up development environments without extensive guidance
- Understanding of monorepo vs. multi-repo tradeoffs is common in technical interviews
- Familiarity with Docker and containerization is increasingly essential
- Version control proficiency (Git) is a baseline requirement for all software roles

### Interview Topics
- "Describe your ideal development environment setup"
- "How do you handle environment differences between development and production?"
- "What's your approach to managing dependencies in a full-stack project?"
- "How do you ensure team members can easily set up the project locally?"

### Skills Demonstrated
- Environment configuration and dependency management
- Understanding of full-stack architecture patterns
- Version control and collaboration workflows
- Command-line proficiency
- Problem-solving and debugging setup issues
