# Module 2: Backend API Development with Django

## Objectives
- Create Django models to represent application data
- Implement RESTful API endpoints for CRUD operations
- Integrate external microservices (Node.js dealers service)
- Handle JSON request/response patterns
- Implement proper error handling and HTTP status codes
- Test API endpoints using curl and automated tests
- Understand Django ORM for database queries

## Key Concepts

### REST API Principles
REST (Representational State Transfer) uses HTTP methods to perform operations:
- **GET**: Retrieve data (e.g., list dealers, get dealer by ID)
- **POST**: Create new resources (e.g., add review, register user)
- **PUT/PATCH**: Update existing resources
- **DELETE**: Remove resources

### Django Views for APIs
Django provides two main approaches for API views:
- **Function-Based Views (FBV)**: Simple Python functions decorated with `@csrf_exempt` for JSON APIs
- **Class-Based Views (CBV)**: Object-oriented approach with methods for different HTTP verbs

### Django Models and ORM
Models define your database schema using Python classes:
```python
class Review(models.Model):
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)
    review = models.TextField()
    sentiment = models.CharField(max_length=20)
```

The ORM (Object-Relational Mapping) translates Python code to SQL:
```python
# Python ORM
reviews = Review.objects.filter(dealer_id=15)

# Equivalent SQL
# SELECT * FROM reviews WHERE dealer_id = 15;
```

### Microservices Integration
External services provide specialized functionality:
- **Dealers Service** (Node.js + MongoDB): Manages dealer data
- **Reviews Service** (Node.js + MongoDB): Handles customer reviews
- **Sentiment Service** (Flask + Watson NLU): Analyzes review sentiment

### JSON Serialization
Converting Python objects to JSON for API responses:
```python
import json
from django.http import JsonResponse

data = {"message": "Success", "count": 5}
return JsonResponse(data, safe=False)
```

## Tools & Commands

### Creating Django Models

**Define Models**:
```bash
# Edit djangoapp/models.py
# Then create migrations
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Verify migrations
python manage.py showmigrations
```

**Django Shell for Testing**:
```bash
# Launch interactive Python shell with Django context
python manage.py shell

# Example queries
>>> from djangoapp.models import Review
>>> Review.objects.all()
>>> Review.objects.create(dealer_id=1, name="John", review="Great service!")
>>> Review.objects.filter(dealer_id=1).count()
```

### Testing API Endpoints with curl

**GET Request**:
```bash
# Get all dealers
curl http://localhost:8000/djangoapp/get_dealers/

# Get dealer by ID
curl http://localhost:8000/djangoapp/dealer/29
```

**POST Request**:
```bash
# Login with JSON data
curl -X POST http://localhost:8000/djangoapp/login \
  -H "Content-Type: application/json" \
  -d '{"userName":"admin","password":"admin123"}'

# Add review
curl -X POST http://localhost:8000/djangoapp/add_review \
  -H "Content-Type: application/json" \
  -d '{
    "dealership": 5,
    "name": "John Doe",
    "review": "Excellent service!",
    "purchase": true,
    "car_make": "Toyota",
    "car_model": "Camry",
    "car_year": 2023
  }'
```

### Database Operations

**Populate Initial Data**:
```bash
# Using Django fixtures
python manage.py loaddata dealers.json

# Using custom management command or script
python populate.py
```

**Inspect Database**:
```bash
# SQLite command line
sqlite3 db.sqlite3
.tables
.schema djangoapp_review
SELECT * FROM djangoapp_review;
```

## Code Snippets

### Django Models
```python
# djangoapp/models.py
from django.db import models
from django.contrib.auth.models import User

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dealer_id = models.IntegerField()
    CAR_TYPES = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('wagon', 'Wagon'),
        ('coupe', 'Coupe'),
        ('hatchback', 'Hatchback'),
    ]
    car_type = models.CharField(max_length=20, choices=CAR_TYPES)
    year = models.IntegerField()
    
    def __str__(self):
        return f"{self.car_make.name} {self.name}"
```

### API View Functions
```python
# djangoapp/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .restapis import get_dealers_from_cf, get_dealer_by_id_from_cf

# GET endpoint - List all dealers
def get_dealerships(request):
    if request.method == "GET":
        # Call external microservice
        dealers = get_dealers_from_cf()
        return JsonResponse({"status": 200, "dealers": dealers})

# GET endpoint - Dealer by ID
def get_dealer_details(request, dealer_id):
    if request.method == "GET":
        dealer = get_dealer_by_id_from_cf(dealer_id)
        if dealer:
            return JsonResponse({"status": 200, "dealer": dealer})
        else:
            return JsonResponse({"status": 404, "message": "Dealer not found"}, status=404)

# POST endpoint - Login
@csrf_exempt
def login_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get('userName')
        password = data.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({
                "userName": username,
                "status": "Authenticated"
            })
        else:
            return JsonResponse({"userName": username})
    
    return JsonResponse({"error": "Invalid request method"}, status=405)
```

### External Service Integration
```python
# djangoapp/restapis.py
import requests
import os

# Environment variables for service URLs
DEALER_API_URL = os.environ.get('DEALER_API_URL', 'http://localhost:3000')

def get_dealers_from_cf():
    """Fetch all dealers from Node.js microservice"""
    try:
        response = requests.get(f"{DEALER_API_URL}/fetchDealers")
        if response.status_code == 200:
            return response.json()
        else:
            return []
    except Exception as e:
        print(f"Error fetching dealers: {e}")
        return []

def get_dealer_reviews_from_cf(dealer_id):
    """Fetch reviews for a specific dealer"""
    try:
        response = requests.get(f"{DEALER_API_URL}/fetchReviews/dealer/{dealer_id}")
        if response.status_code == 200:
            return response.json()
        else:
            return []
    except Exception as e:
        print(f"Error fetching reviews: {e}")
        return []

def analyze_review_sentiments(text):
    """Send review to Flask sentiment analysis service"""
    SENTIMENT_API_URL = os.environ.get('SENTIMENT_API_URL', 'http://localhost:5000')
    try:
        response = requests.post(
            f"{SENTIMENT_API_URL}/analyze",
            json={"text": text}
        )
        if response.status_code == 200:
            result = response.json()
            return result.get('sentiment', 'neutral')
        else:
            return 'neutral'
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return 'neutral'
```

### URL Configuration
```python
# djangoapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Dealer endpoints
    path('get_dealers/', views.get_dealerships, name='get_dealers'),
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),
    path('reviews/dealer/<int:dealer_id>/', views.get_dealer_reviews, name='dealer_reviews'),
    
    # Review endpoints
    path('add_review/', views.add_review, name='add_review'),
    
    # Auth endpoints
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.registration, name='register'),
    
    # Car endpoints
    path('get_cars/', views.get_cars, name='get_cars'),
]
```

## Common Pitfalls

### 1. CSRF Token Errors
**Problem**: POST requests fail with "CSRF token missing"
**Solution**: Use `@csrf_exempt` decorator for JSON APIs
```python
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def api_view(request):
    # JSON API logic
    pass
```

### 2. JSON Parsing Errors
**Problem**: `JSONDecodeError: Expecting value`
**Solution**: Ensure request body contains valid JSON and Content-Type header is set
```python
try:
    data = json.loads(request.body)
except json.JSONDecodeError:
    return JsonResponse({"error": "Invalid JSON"}, status=400)
```

### 3. Foreign Key Constraints
**Problem**: `IntegrityError` when creating objects with invalid foreign keys
**Solution**: Validate foreign key existence before creating objects
```python
try:
    car_make = CarMake.objects.get(id=make_id)
    car_model = CarModel.objects.create(car_make=car_make, ...)
except CarMake.DoesNotExist:
    return JsonResponse({"error": "Invalid car make"}, status=400)
```

### 4. Microservice Connection Failures
**Problem**: Requests to external services timeout or fail
**Solution**: Implement error handling and fallback responses
```python
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()
except requests.RequestException as e:
    logger.error(f"Service unavailable: {e}")
    return {"error": "Service temporarily unavailable"}
```

### 5. Missing Migrations
**Problem**: Model changes don't reflect in database
**Solution**: Always create and apply migrations after model changes
```bash
python manage.py makemigrations
python manage.py migrate
```

## Mini Quiz

1. **What HTTP method should be used to retrieve a list of dealers, and why?**
   - **Answer**: GET should be used because we're reading data without modifying server state. GET requests are idempotent (can be repeated safely), cacheable, and semantically correct for data retrieval operations according to REST principles.

2. **Why do we use `@csrf_exempt` decorator for JSON API endpoints?**
   - **Answer**: Django's CSRF protection expects a CSRF token in POST requests to prevent cross-site request forgery attacks. However, JSON APIs typically use other authentication mechanisms (like tokens or session cookies) and are accessed programmatically, not via HTML forms. The `@csrf_exempt` decorator disables CSRF checking for these endpoints. Note: Always implement alternative security measures for exempted endpoints.

3. **What's the difference between `filter()` and `get()` in Django ORM?**
   - **Answer**: `filter()` returns a QuerySet (potentially multiple objects) and never raises an exception if no matches are found (returns empty QuerySet). `get()` returns a single object and raises `DoesNotExist` if no match is found or `MultipleObjectsReturned` if more than one match exists. Use `get()` when expecting exactly one result (like fetching by unique ID).

4. **How does Django's ORM help prevent SQL injection attacks?**
   - **Answer**: Django's ORM automatically parameterizes queries, separating SQL structure from user data. Instead of string concatenation, the ORM uses prepared statements where user input is treated as data, not executable code. For example, `User.objects.filter(username=user_input)` is safe, while raw SQL like `f"SELECT * FROM users WHERE username='{user_input}'"` is vulnerable.

5. **What should an API return when a requested resource doesn't exist?**
   - **Answer**: Return HTTP 404 (Not Found) status code with a descriptive JSON message, for example: `JsonResponse({"error": "Dealer not found", "dealer_id": dealer_id}, status=404)`. This follows REST conventions and helps clients distinguish between different error types (404 for missing resources vs. 400 for bad requests vs. 500 for server errors).

## Practice Task

### Task: Build a Complete REST API for Car Reviews

**Objective**: Create API endpoints for managing car dealership reviews with sentiment analysis.

**Requirements**:
1. Create a `Review` model with fields: dealer_id, name, review, purchase, purchase_date, car_make, car_model, car_year, sentiment
2. Implement GET endpoint to fetch all reviews for a specific dealer
3. Implement POST endpoint to submit a new review
4. Integrate sentiment analysis service to automatically analyze review text
5. Test all endpoints with curl commands

**Steps**:
1. Define the Review model in `models.py`
2. Create and run migrations
3. Implement `get_dealer_reviews(dealer_id)` view function
4. Implement `add_review()` view function with sentiment analysis
5. Configure URL patterns in `urls.py`
6. Test with curl commands
7. Verify data in database

**Expected Outcomes**:
- GET `/reviews/dealer/5` returns all reviews for dealer ID 5
- POST `/add_review` creates new review with sentiment field populated
- Database contains review records with sentiment scores
- API returns proper JSON responses with appropriate HTTP status codes

**Test Commands**:
```bash
# Get reviews
curl http://localhost:8000/djangoapp/reviews/dealer/5

# Add review
curl -X POST http://localhost:8000/djangoapp/add_review \
  -H "Content-Type: application/json" \
  -d '{
    "dealership": 5,
    "name": "Jane Smith",
    "review": "Terrible experience, would not recommend",
    "purchase": false
  }'
```

**Hints**:
- Use `json.loads(request.body)` to parse JSON request data
- Call sentiment analysis service before saving review
- Use `try/except` blocks for error handling
- Return appropriate HTTP status codes (200, 201, 400, 404)

## Career Notes

### Relevant Job Roles
- **Backend Developer**: Designs and implements RESTful APIs
- **Full-Stack Developer**: Builds both API layer and integrates with frontend
- **API Developer**: Specializes in creating scalable, well-documented APIs
- **Integration Engineer**: Connects multiple services and microservices

### Industry Expectations
- Strong understanding of REST principles and HTTP methods
- Ability to design clean, intuitive API endpoints
- Knowledge of proper status codes and error handling
- Experience with ORM/database query optimization
- Familiarity with API versioning and documentation
- Understanding of microservices communication patterns

### Interview Topics
- "Design a RESTful API for a e-commerce system"
- "How would you handle errors in a distributed microservices architecture?"
- "Explain the N+1 query problem and how to prevent it"
- "What's your approach to API versioning?"
- "How do you ensure API security and prevent common vulnerabilities?"

### Skills Demonstrated
- RESTful API design and implementation
- Database modeling and ORM usage
- Error handling and edge case management
- Integration with external services
- JSON serialization and data transformation
- HTTP protocol understanding
- Microservices architecture patterns
