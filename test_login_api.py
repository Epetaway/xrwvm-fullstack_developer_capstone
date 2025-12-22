#!/usr/bin/env python
import os
import sys
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproj.settings')
sys.path.insert(0, '/Users/earlhickson/Development/best-cars-capstone/server')
django.setup()

from django.test import Client

# Create test client
client = Client()

# Test login endpoint
login_data = json.dumps({
    "userName": "admin",
    "password": "admin123"
})

response = client.post(
    '/djangoapp/login',
    data=login_data,
    content_type='application/json'
)

print("=== LOGIN TEST RESULTS ===")
print(f"Status Code: {response.status_code}")
print(f"Response Data: {response.content.decode()}")
print("==========================")

# Verify response
response_json = json.loads(response.content)
if response_json.get('status') == 'Authenticated':
    print("✓ Login successful!")
    print(f"Username: {response_json.get('userName')}")
else:
    print("✗ Login failed!")
    print(f"Response: {response_json}")
