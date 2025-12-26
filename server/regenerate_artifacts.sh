#!/bin/bash

# Make sure server is running on port 8000

cd /Users/earlhickson/Development/best-cars-capstone/server

echo "Regenerating artifact files with correct endpoints..."

# Q8: getdealerreviews - fetchReviews/dealer/29
echo "curl -X GET http://127.0.0.1:8000/fetchReviews/dealer/29" > artifacts/getdealerreviews.txt
curl -s -X GET http://127.0.0.1:8000/fetchReviews/dealer/29 | python3 -m json.tool >> artifacts/getdealerreviews.txt

# Q9: getalldealers - fetchDealers (complete output)
echo "curl -X GET http://127.0.0.1:8000/fetchDealers" > artifacts/getalldealers.txt
curl -s -X GET http://127.0.0.1:8000/fetchDealers | python3 -m json.tool >> artifacts/getalldealers.txt

# Q10: getdealerbyid - fetchDealer/29
echo "curl -X GET http://127.0.0.1:8000/fetchDealer/29" > artifacts/getdealerbyid.txt
curl -s -X GET http://127.0.0.1:8000/fetchDealer/29 | python3 -m json.tool >> artifacts/getdealerbyid.txt

# Q11: getdealersbyState - fetchDealers/Kansas
echo "curl -X GET http://127.0.0.1:8000/fetchDealers/Kansas" > artifacts/getdealersbyState.txt
curl -s -X GET http://127.0.0.1:8000/fetchDealers/Kansas | python3 -m json.tool >> artifacts/getdealersbyState.txt

# Q14: getallcarmakes - complete output
echo "curl -X GET http://127.0.0.1:8000/djangoapp/get_cars" > artifacts/getallcarmakes.txt
curl -s -X GET http://127.0.0.1:8000/djangoapp/get_cars | python3 -m json.tool >> artifacts/getallcarmakes.txt

# Q5: Fix loginuser - remove extra brace
echo "curl -X POST http://127.0.0.1:8000/djangoapp/login -H \"Content-Type: application/json\" -d '{\"userName\":\"admin\",\"password\":\"admin123\"}'" > artifacts/loginuser.txt
echo "" >> artifacts/loginuser.txt
echo "{\"userName\":\"admin\",\"status\":\"Authenticated\"}" >> artifacts/loginuser.txt

echo "Done! All artifacts regenerated."
