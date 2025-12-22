#!/bin/bash
cd /Users/earlhickson/Development/best-cars-capstone/server

# Start server in background
/Users/earlhickson/Development/.venv/bin/python manage.py runserver 127.0.0.1:8000 > /tmp/django.log 2>&1 &
SERVER_PID=$!

# Wait for server to start
sleep 5

# Test login endpoint
echo "Testing login endpoint..."
echo "================================"
curl -X POST "http://127.0.0.1:8000/djangoapp/login" \
  -H "Content-Type: application/json" \
  -d '{"userName": "admin", "password": "admin123"}'
echo ""
echo "================================"
echo "Test complete!"

# Kill server
kill $SERVER_PID 2>/dev/null
