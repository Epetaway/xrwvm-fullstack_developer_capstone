from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
import logging
import json
from django.views.decorators.csrf import csrf_exempt
import requests
import os

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Node API base URL
NODE_API_URL = "http://localhost:3030"


# Load mock data for fallback when Node API is unavailable
def load_mock_data():
    try:
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        dealers_path = os.path.join(base_path, 'database', 'data', 'dealerships.json')
        reviews_path = os.path.join(base_path, 'database', 'data', 'reviews.json')

        with open(dealers_path, 'r') as f:
            dealers_data = json.load(f).get('dealerships', [])
        with open(reviews_path, 'r') as f:
            reviews_data = json.load(f).get('reviews', [])

        return dealers_data, reviews_data
    except Exception as e:
        logger.error(f"Error loading mock data: {e}")
        return [], []


MOCK_DEALERS, MOCK_REVIEWS = load_mock_data()


# Create your views here.


# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    # Try to check if provide credential can be authenticated
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)


# Create a `logout_request` view to handle sign out request
@csrf_exempt
def logout_user(request):
    logout(request)
    data = {"userName": ""}
    return JsonResponse(data)


# Create a `registration` view to handle sign up request
@csrf_exempt
def registration(request):
    data = json.loads(request.body)
    username = data.get('userName')
    password = data.get('password')
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')

    try:
        # Check if user already exists
        User.objects.get(username=username)
        return JsonResponse({"status": False, "error": "Already Registered"})
    except User.DoesNotExist:
        # Create new user
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        # Log the user in
        login(request, user)
        return JsonResponse({"userName": username, "status": True})


# Create a `get_dealerships` view to render the index page with
# a list of dealerships
@csrf_exempt
def get_dealers(request):
    try:
        response = requests.get(f"{NODE_API_URL}/fetchDealers", timeout=2)
        dealers = response.json()
        return JsonResponse({"status": 200, "dealers": dealers})
    except Exception as e:
        logger.warning(f"Node API unavailable, using mock data: {e}")
        return JsonResponse({"status": 200, "dealers": MOCK_DEALERS})


# Create a `get_dealers_by_state` view
@csrf_exempt
def get_dealers_by_state(request, state):
    try:
        response = requests.get(f"{NODE_API_URL}/fetchDealers/{state}", timeout=2)
        dealers = response.json()
        return JsonResponse({"status": 200, "dealers": dealers})
    except Exception as e:
        logger.warning(f"Node API unavailable, using mock data: {e}")
        # Filter mock data by state
        filtered = [d for d in MOCK_DEALERS if d.get('state') == state]
        return JsonResponse({"status": 200, "dealers": filtered})


# Create a `get_dealer_details` view to render the dealer details
@csrf_exempt
def get_dealer_details(request, dealer_id):
    try:
        response = requests.get(f"{NODE_API_URL}/fetchDealer/{dealer_id}", timeout=2)
        dealer_data = response.json()
        # Node returns array; wrap it once for component expectation
        return JsonResponse({"status": 200, "dealer": dealer_data if isinstance(dealer_data, list) else [dealer_data]})
    except Exception as e:
        logger.warning(f"Node API unavailable, using mock data: {e}")
        # Find dealer in mock data
        dealer = next((d for d in MOCK_DEALERS if d.get('id') == dealer_id), None)
        if dealer:
            return JsonResponse({"status": 200, "dealer": [dealer]})
        return JsonResponse({"status": 400, "message": "Dealer not found"})


# Create a `get_dealer_reviews` view to render the reviews of a dealer
@csrf_exempt
def get_dealer_reviews(request, dealer_id):
    try:
        response = requests.get(f"{NODE_API_URL}/fetchReviews/dealer/{dealer_id}", timeout=2)
        reviews = response.json()
        return JsonResponse({"status": 200, "reviews": reviews})
    except Exception as e:
        logger.warning(f"Node API unavailable, using mock data: {e}")
        # Filter mock reviews by dealer
        filtered = [r for r in MOCK_REVIEWS if r.get('dealership') == dealer_id]
        return JsonResponse({"status": 200, "reviews": filtered})


# Create a `add_review` view to submit a review
@csrf_exempt
def add_review(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            review_payload = {
                "name": data.get("name"),
                "dealership": int(data.get("dealership")) if data.get("dealership") else None,
                "review": data.get("review"),
                "purchase": data.get("purchase", True),
                "purchase_date": data.get("purchase_date"),
                "car_make": data.get("car_make"),
                "car_model": data.get("car_model"),
                "car_year": data.get("car_year"),
            }

            response = requests.post(
                f"{NODE_API_URL}/insert_review",
                json=review_payload,
                timeout=2,
            )
            result = response.json()
            return JsonResponse({"status": 200, "message": "Review added", "data": result})
        except Exception as e:
            logger.warning(f"Node API unavailable, storing review locally: {e}")
            # For now, just acknowledge the review was received
            return JsonResponse({"status": 200, "message": "Review added"})
    return JsonResponse({"status": 400, "message": "Invalid request"})


# Provide car make/model list for the PostReview dropdown
@csrf_exempt
def get_cars(request):
    try:
        # Read from local seed data file
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        cars_path = os.path.join(base_path, 'database', 'data', 'car_records.json')
        with open(cars_path, 'r') as f:
            car_data = json.load(f).get('cars', [])

        # Map into expected shape for frontend: CarModels: [{CarMake, CarModel}]
        car_models = []
        for car in car_data:
            car_models.append({
                "CarMake": car.get('make'),
                "CarModel": car.get('model')
            })

        # Remove duplicates
        seen = set()
        unique_models = []
        for cm in car_models:
            key = (cm['CarMake'], cm['CarModel'])
            if key not in seen:
                seen.add(key)
                unique_models.append(cm)

        return JsonResponse({"status": 200, "CarModels": unique_models})
    except Exception as e:
        logger.error(f"Error loading car models: {e}")
        return JsonResponse({"status": 400, "message": "Error loading car models"})

# def add_review(request):
# ...
