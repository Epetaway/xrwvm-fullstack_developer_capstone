#!/usr/bin/env python
import os
import sys
import django
import json

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproj.settings')
sys.path.insert(0, '/Users/earlhickson/Development/best-cars-capstone/server')
django.setup()

from django.test import Client
from django.contrib.auth.models import User

print("=== MODULE 2: USER MANAGEMENT - LOGIN TEST ===\n")

# Verify admin user exists
try:
    admin = User.objects.get(username='admin')
    print(f"✓ Admin user found: {admin.username} ({admin.email})")
except User.DoesNotExist:
    print("✗ Admin user not found!")
    sys.exit(1)

# Create test client with full middleware
client = Client()

# Test endpoint
endpoint = '/djangoapp/login'
payload = {"userName": "admin", "password": "admin123"}

print(f"Endpoint: POST {endpoint}")
print(f"Payload: {json.dumps(payload)}\n")

# Send POST request - encode JSON to bytes
try:
    response = client.post(
        endpoint,
        data=json.dumps(payload).encode('utf-8'),
        content_type='application/json'
    )
    
    print(f"Status Code: {response.status_code}")
    print(f"Content-Type: {response.get('Content-Type', 'Not specified')}\n")
    
    # Try to parse JSON response
    response_data = json.loads(response.content.decode())
    print("Response JSON:")
    print(json.dumps(response_data, indent=2))
    print()
    
    if response.status_code == 200 and response_data.get('status') == 'Authenticated':
        print("=" * 50)
        print("✓ LOGIN SUCCESSFUL!")
        print(f"  Username: {response_data.get('userName')}")
        print("=" * 50)
    else:
        print("✗ Login did not return authenticated status")
        
except json.JSONDecodeError as e:
    print(f"✗ Response is not valid JSON: {e}")
    print(f"Raw response (first 1000 chars):\n{response.content.decode()[:1000]}")
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
