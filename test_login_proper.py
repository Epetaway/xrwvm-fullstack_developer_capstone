#!/usr/bin/env python
import os
import sys
import django
import json
from django.test import Client
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproj.settings')
sys.path.insert(0, '/Users/earlhickson/Development/best-cars-capstone/server')
django.setup()

# Verify admin user exists
try:
    admin_user = User.objects.get(username='admin')
    print(f"✓ Admin user found: {admin_user.username} ({admin_user.email})")
except User.DoesNotExist:
    print("✗ Admin user not found - creating...")
    User.objects.create_superuser('admin', 'admin@bestcars.com', 'admin123')
    print("✓ Admin user created")

# Create test client
client = Client()

# Prepare login data
login_data = json.dumps({
    "userName": "admin",
    "password": "admin123"
})

# Test login endpoint
response = client.post(
    '/djangoapp/login',
    data=login_data,
    content_type='application/json'
)

print("\n=== MODULE 2: USER MANAGEMENT - LOGIN TEST ===")
print("Endpoint: POST /djangoapp/login")
print(f"Status Code: {response.status_code}")
print("Response Content:")
print(response.content.decode())
print("=" * 50)

# Try to parse JSON
try:
    resp_json = json.loads(response.content)
    if resp_json.get('status') == 'Authenticated':
        print("✓ LOGIN SUCCESSFUL!")
        print(f"  Username: {resp_json.get('userName')}")
    else:
        print("✗ Login failed")
        print(f"  Response: {resp_json}")
except Exception as e:
    print(f"Error parsing response: {e}")
