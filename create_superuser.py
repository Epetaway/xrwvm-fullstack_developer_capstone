#!/usr/bin/env python
import os
import sys
import django
from django.contrib.auth.models import User

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproj.settings')
sys.path.insert(0, '/Users/earlhickson/Development/best-cars-capstone/server')
django.setup()

# Create superuser
try:
    user = User.objects.create_superuser(
        username='admin',
        email='admin@bestcars.com',
        password='admin123'
    )
    print("Superuser 'admin' created successfully!")
    print(f"Username: {user.username}")
    print(f"Email: {user.email}")
except Exception as e:
    print(f"Error: {e}")
