# Labs and Hands-On Exercises

This index provides an overview of practical labs and exercises for the Full-Stack Application Development Capstone Project. These hands-on activities reinforce concepts covered in the course modules.

## Lab Overview

The capstone project is itself a comprehensive lab that integrates all learned skills. Below are specific exercises and checkpoints throughout the development process.

## Module 1 Labs: Project Setup

### Lab 1.1: Environment Setup
**Objective**: Set up complete development environment
**Duration**: 45 minutes

**Tasks**:
1. Install Python 3.8+ and verify version
2. Install Node.js 14+ and npm
3. Install Git and configure user details
4. Install Docker Desktop (optional but recommended)
5. Set up code editor (VS Code recommended with Python and React extensions)

**Deliverables**:
- Screenshots of version checks for Python, Node, Git
- Configured `.gitconfig` with user name and email

**Resources**:
- Python installation: https://www.python.org/downloads/
- Node.js installation: https://nodejs.org/
- Git installation: https://git-scm.com/downloads

---

### Lab 1.2: Initialize Django Project
**Objective**: Create and configure Django project
**Duration**: 60 minutes

**Tasks**:
1. Create virtual environment: `python -m venv venv`
2. Install Django: `pip install django`
3. Create project: `django-admin startproject djangoproj`
4. Create app: `python manage.py startapp djangoapp`
5. Run migrations: `python manage.py migrate`
6. Create superuser
7. Test admin interface at `/admin`

**Deliverables**:
- Running Django development server
- Accessible admin interface
- Superuser account created

**Verification**:
```bash
curl http://localhost:8000/admin/
# Should return login page HTML
```

---

### Lab 1.3: Initialize React Frontend
**Objective**: Set up React application within Django project
**Duration**: 45 minutes

**Tasks**:
1. Create React app: `npx create-react-app frontend`
2. Install React Router: `npm install react-router-dom`
3. Install Bootstrap: `npm install bootstrap`
4. Create basic component structure
5. Build React app: `npm run build`
6. Configure Django to serve React build

**Deliverables**:
- React development server running on port 3000
- Production build created in `frontend/build/`
- Django configured to serve React app

**Verification**:
```bash
# React dev server
curl http://localhost:3000/
# Django serving React build
curl http://localhost:8000/
```

## Module 2 Labs: Backend Development

### Lab 2.1: Create Django Models
**Objective**: Define database models for the application
**Duration**: 60 minutes

**Tasks**:
1. Create `CarMake` model with name and description
2. Create `CarModel` model with foreign key to CarMake, type, year
3. Create migrations: `python manage.py makemigrations`
4. Apply migrations: `python manage.py migrate`
5. Register models in admin.py
6. Test in Django admin interface

**Deliverables**:
- Model definitions in `models.py`
- Migration files created
- Models visible in admin interface

**Sample data to add via admin**:
- CarMake: Toyota, Honda, Ford
- CarModel: Camry (Toyota, Sedan, 2023), Civic (Honda, Sedan, 2023)

---

### Lab 2.2: Build REST API Endpoints
**Objective**: Create API endpoints for dealers and reviews
**Duration**: 90 minutes

**Tasks**:
1. Create view function for GET `/get_dealers/`
2. Create view function for GET `/dealer/<id>/`
3. Create view function for POST `/add_review/`
4. Configure URL patterns in `urls.py`
5. Test endpoints with curl commands

**Deliverables**:
- Three working API endpoints
- JSON responses returned correctly
- URL routing configured

**Test commands**:
```bash
# Test get dealers
curl http://localhost:8000/djangoapp/get_dealers/

# Test get dealer by ID
curl http://localhost:8000/djangoapp/dealer/1/

# Test add review
curl -X POST http://localhost:8000/djangoapp/add_review \
  -H "Content-Type: application/json" \
  -d '{
    "dealer_id": 1,
    "name": "John Doe",
    "review": "Great service!",
    "purchase": true
  }'
```

---

### Lab 2.3: Integrate External Microservices
**Objective**: Connect to Node.js dealers service and Flask sentiment service
**Duration**: 75 minutes

**Tasks**:
1. Set up Node.js microservice with MongoDB (provided or use Docker Compose)
2. Create `restapis.py` with helper functions
3. Implement `get_dealers_from_cf()` function
4. Implement `get_dealer_reviews_from_cf(dealer_id)` function
5. Implement `analyze_review_sentiments(text)` function
6. Test integration

**Deliverables**:
- Working connection to dealers microservice
- Working connection to sentiment analysis service
- Helper functions in `restapis.py`

**Verification**:
```python
# Test in Django shell
from djangoapp.restapis import get_dealers_from_cf
dealers = get_dealers_from_cf()
print(len(dealers))  # Should return list of dealers
```

## Module 3 Labs: Frontend Development

### Lab 3.1: Create React Components
**Objective**: Build reusable React components
**Duration**: 90 minutes

**Tasks**:
1. Create `Header` component with navigation
2. Create `Home` component for landing page
3. Create `Dealers` component to list all dealers
4. Create `DealerDetail` component for single dealer view
5. Implement Bootstrap styling

**Deliverables**:
- Four functional components
- Bootstrap styling applied
- Components rendering correctly

**Component structure**:
```
src/components/
├── Header/Header.jsx
├── Home/Home.jsx
├── Dealers/Dealers.jsx
└── DealerDetail/DealerDetail.jsx
```

---

### Lab 3.2: Implement Client-Side Routing
**Objective**: Set up React Router for navigation
**Duration**: 60 minutes

**Tasks**:
1. Configure routes in `App.js`
2. Add routes: `/`, `/dealers`, `/dealer/:id`
3. Implement navigation links in Header
4. Test navigation between pages

**Deliverables**:
- Working client-side routing
- Navigation without page reloads
- URL parameters working

**Routes to implement**:
```javascript
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/dealers" element={<Dealers />} />
  <Route path="/dealer/:id" element={<DealerDetail />} />
</Routes>
```

---

### Lab 3.3: Fetch Data from Backend API
**Objective**: Integrate frontend with Django API
**Duration**: 75 minutes

**Tasks**:
1. Implement data fetching in `Dealers` component using `useEffect`
2. Display dealer cards with name, city, state
3. Add loading state while fetching
4. Handle errors gracefully
5. Test with actual API

**Deliverables**:
- Dealers list populated from API
- Loading indicator shown
- Error messages displayed when appropriate

**Implementation checklist**:
- [ ] useState for dealers, loading, error
- [ ] useEffect to fetch on component mount
- [ ] fetch() call to `/djangoapp/get_dealers/`
- [ ] Conditional rendering based on state

## Module 4 Labs: Authentication

### Lab 4.1: Implement Login Functionality
**Objective**: Create login system with Django and React
**Duration**: 90 minutes

**Tasks**:
1. Create Django login view with authentication
2. Configure URL for `/login` endpoint
3. Create React Login component with form
4. Implement form submission to Django API
5. Store username in sessionStorage on success
6. Redirect to home page after login

**Deliverables**:
- Django login endpoint working
- React login form functional
- Session management implemented
- Redirect after successful login

**Test scenarios**:
- Valid credentials → successful login
- Invalid credentials → error message
- Session persists across page reloads

---

### Lab 4.2: Implement Registration
**Objective**: Add user registration functionality
**Duration**: 75 minutes

**Tasks**:
1. Create Django registration view
2. Check for duplicate usernames
3. Create React Register component
4. Implement form with validation
5. Auto-login after registration
6. Test duplicate username prevention

**Deliverables**:
- Django registration endpoint
- React registration form
- Client-side validation
- Duplicate username handling

**Form fields**:
- Username (required, unique)
- First Name (required)
- Last Name (required)
- Email (required, valid email format)
- Password (required, min 8 characters)
- Confirm Password (must match password)

---

### Lab 4.3: Add Logout and Session Management
**Objective**: Complete authentication flow
**Duration**: 45 minutes

**Tasks**:
1. Create Django logout view
2. Update Header component to show username when logged in
3. Add logout button
4. Clear sessionStorage on logout
5. Update UI to show login/register links when not authenticated

**Deliverables**:
- Logout functionality working
- Header shows current user
- UI updates based on authentication state

**Verification**:
- Login → header shows username
- Logout → sessionStorage cleared
- Page reload → session persists if logged in

## Module 5 Labs: Deployment

### Lab 5.1: Containerize Application
**Objective**: Create Docker container for the application
**Duration**: 90 minutes

**Tasks**:
1. Write Dockerfile for Django application
2. Create entrypoint script for migrations
3. Build Docker image
4. Run container locally
5. Test application in container

**Deliverables**:
- Working Dockerfile
- Successfully built image
- Container running application
- Application accessible on mapped port

**Build and run commands**:
```bash
docker build -t dealership-app:latest .
docker run -p 8000:8000 dealership-app:latest
curl http://localhost:8000/
```

---

### Lab 5.2: Docker Compose Setup
**Objective**: Set up multi-container environment
**Duration**: 60 minutes

**Tasks**:
1. Create `docker-compose.yml`
2. Define services: web (Django) and db (PostgreSQL)
3. Configure environment variables
4. Set up volume for database persistence
5. Test with `docker-compose up`

**Deliverables**:
- docker-compose.yml file
- Both services running
- Database connection working
- Data persisting across restarts

**Services**:
```yaml
services:
  db:
    image: postgres:13
    # configuration
  web:
    build: .
    # configuration
```

---

### Lab 5.3: Deploy to Kubernetes/OpenShift
**Objective**: Deploy application to cloud platform
**Duration**: 120 minutes

**Tasks**:
1. Create deployment.yaml with 2 replicas
2. Create service.yaml to expose application
3. Configure environment variables and secrets
4. Apply configurations to cluster
5. Verify deployment and access application

**Deliverables**:
- Kubernetes manifests (deployment.yaml, service.yaml)
- Application deployed to cluster
- Multiple pods running
- External access configured

**Deployment commands**:
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get pods
kubectl get services
```

---

### Lab 5.4: Set Up CI/CD Pipeline
**Objective**: Automate testing and deployment
**Duration**: 90 minutes

**Tasks**:
1. Create `.github/workflows/deploy.yml`
2. Configure jobs: test, build, deploy
3. Set up repository secrets
4. Push code and verify workflow runs
5. Confirm automatic deployment on push to main

**Deliverables**:
- GitHub Actions workflow file
- Automated tests running on push
- Automatic deployment to production
- Build status badge in README

**Workflow structure**:
```yaml
jobs:
  test:
    # Run Django tests
  build:
    # Build Docker image
  deploy:
    # Deploy to Kubernetes
```

## Integration Lab: Complete Capstone

### Final Integration Lab
**Objective**: Build complete end-to-end functionality
**Duration**: 4-6 hours

**Tasks**:
1. Review submission flow (unauthenticated user experience)
2. Authentication flow (register → login → submit review)
3. Data flow (frontend → Django → microservices → database)
4. Deploy to cloud platform
5. Create comprehensive README documentation

**Features to demonstrate**:
- User can view dealers without logging in
- User must log in to submit reviews
- Reviews show sentiment analysis results
- Dealers can be filtered by state
- Application is accessible via public URL

**Documentation to include**:
- Setup instructions for local development
- Environment variables required
- How to run tests
- Deployment process
- API endpoint documentation

## Testing Labs

### Lab T.1: Unit Testing Django
**Duration**: 60 minutes

**Tasks**:
1. Create test cases for models
2. Create test cases for views
3. Test authentication endpoints
4. Run tests: `python manage.py test`

**Example tests**:
```python
class DealerModelTest(TestCase):
    def test_dealer_creation(self):
        dealer = Dealer.objects.create(name="Test Dealer")
        self.assertEqual(dealer.name, "Test Dealer")
```

---

### Lab T.2: API Testing with cURL
**Duration**: 45 minutes

**Tasks**:
1. Test all GET endpoints
2. Test all POST endpoints
3. Test error cases (404, 400, 500)
4. Document API responses

**Endpoints to test**:
- GET /get_dealers/
- GET /dealer/<id>/
- POST /login
- POST /register
- GET /logout
- POST /add_review

---

### Lab T.3: Frontend Testing
**Duration**: 60 minutes (optional)

**Tasks**:
1. Set up Jest testing framework
2. Write tests for components
3. Test user interactions
4. Run tests: `npm test`

## Troubleshooting Guide

Common issues and solutions encountered during labs:

1. **Port already in use**: Use `lsof -i :8000` to find and kill process
2. **CORS errors**: Install and configure django-cors-headers
3. **Database locked**: Restart server or check for stale connections
4. **Static files not loading**: Run `collectstatic` command
5. **Node modules missing**: Delete node_modules and run `npm install`
6. **Docker build fails**: Check Dockerfile syntax and base image availability

## Additional Resources

- Django Documentation: https://docs.djangoproject.com/
- React Documentation: https://react.dev/
- Docker Documentation: https://docs.docker.com/
- Kubernetes Documentation: https://kubernetes.io/docs/
- MDN Web Docs: https://developer.mozilla.org/

## Lab Completion Checklist

- [ ] All Module 1 labs completed
- [ ] All Module 2 labs completed
- [ ] All Module 3 labs completed
- [ ] All Module 4 labs completed
- [ ] All Module 5 labs completed
- [ ] Integration lab completed
- [ ] Application deployed to cloud
- [ ] README documentation complete
- [ ] All tests passing
