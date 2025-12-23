# Example cURL Commands for Testing

Replace `localhost:8000` with your actual server URL and adjust IDs as needed.

## Authentication

### Login
```bash
curl -X POST http://localhost:8000/djangoapp/login \
  -H "Content-Type: application/json" \
  -d '{"userName":"testuser","password":"testpass"}' \
  -c cookies.txt \
  -v > SUBMISSION/curl_outputs/loginuser.txt 2>&1
```

### Logout
```bash
curl -X GET http://localhost:8000/djangoapp/logout \
  -b cookies.txt \
  -v > SUBMISSION/curl_outputs/logoutuser.txt 2>&1
```

## Dealer Operations

### Get All Dealers
```bash
curl -X GET http://localhost:8000/djangoapp/get_dealers \
  -v > SUBMISSION/curl_outputs/getalldealers.txt 2>&1
```

### Get Dealer by ID
```bash
curl -X GET http://localhost:8000/djangoapp/get_dealers/1 \
  -v > SUBMISSION/curl_outputs/getdealerbyid.txt 2>&1
```

### Get Dealers by State
```bash
curl -X GET "http://localhost:8000/djangoapp/get_dealers?state=Kansas" \
  -v > SUBMISSION/curl_outputs/getdealersbyState.txt 2>&1
```

### Get Dealer Reviews
```bash
curl -X GET http://localhost:8000/djangoapp/reviews/dealer/1 \
  -v > SUBMISSION/curl_outputs/getdealerreviews.txt 2>&1
```

## Car Operations

### Get All Car Makes
```bash
curl -X GET http://localhost:8000/djangoapp/get_cars \
  -v > SUBMISSION/curl_outputs/getallcarmakes.txt 2>&1
```

## Sentiment Analysis

### Analyze Review
```bash
curl -X POST http://localhost:8000/djangoapp/analyze_review \
  -H "Content-Type: application/json" \
  -d '{"text":"Fantastic services"}' \
  -v > SUBMISSION/curl_outputs/analyzereview.txt 2>&1
```

---

## Tips

1. **Save both command and output**: Each file should contain the cURL command you ran AND the complete output
2. **Use -v flag**: This shows verbose output including headers
3. **Adjust URLs**: Replace localhost:8000 with your actual server
4. **Check authentication**: Some endpoints may require login first
5. **Verify data**: Make sure you have dealers, reviews, and cars in your database

---

## Format Example

Each output file should look like this:

```
=== cURL Command ===
curl -X GET http://localhost:8000/djangoapp/get_dealers -v

=== Output ===
* Trying 127.0.0.1:8000...
* Connected to localhost (127.0.0.1) port 8000
> GET /djangoapp/get_dealers HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.88.1
> Accept: */*
>
< HTTP/1.1 200 OK
< Content-Type: application/json
< ...
[{"id":1,"name":"Best Cars Boston",...}]
```
