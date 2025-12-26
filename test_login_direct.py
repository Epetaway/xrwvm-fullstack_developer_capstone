#!/usr/bin/env python
import os
import sys
import django
import json
from django.test import RequestFactory
from djangoapp.views import login_user

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproj.settings')
sys.path.insert(0, '/Users/earlhickson/Development/best-cars-capstone/server')
django.setup()

# Create a request factory
factory = RequestFactory()

# Create login POST request with JSON data
login_data = json.dumps({
    "userName": "admin",
    "password": "admin123"
})

request = factory.post(
    '/djangoapp/login',
    data=login_data,
    content_type='application/json'
)

# Call login view
response = login_user(request)

print("=== MODULE 2: USER MANAGEMENT - LOGIN TEST ===")
print(f"Status Code: {response.status_code}")
print("Response Content:")
print(response.content.decode())
print("=" * 50)
