# Submission Checklist

Use this checklist to track your progress on all 28 tasks.

## Setup Tasks

- [ ] Update main README.md with project name and details
- [ ] Verify all code files are committed
- [ ] Test application locally
- [ ] Deploy application

---

## Task Completion

### Static Pages & Code (7 points)

- [x] **Task 1** (1 pt): README.md with project name
- [x] **Task 3** (3 pts): About.html with CSS, images, team details
- [x] **Task 4** (2 pts): Contact.html with navigation and contact info
- [x] **Task 7** (1 pt): Register.jsx with 5 input fields

### Terminal Outputs (11 points)

- [ ] **Task 2** (1 pt): Django server output → `curl_outputs/django_server.txt`
  - Run: `python manage.py runserver`
  - Save terminal output

- [ ] **Task 5** (2 pts): Login cURL → `curl_outputs/loginuser.txt`
  - Run cURL command for login
  - Include both command and output

- [ ] **Task 6** (2 pts): Logout cURL → `curl_outputs/logoutuser.txt`
  - Run cURL command for logout
  - Include both command and output

- [ ] **Task 8** (2 pts): Get dealer reviews → `curl_outputs/getdealerreviews.txt`
  - Run cURL for any dealer ID
  - Include both command and output

- [ ] **Task 9** (2 pts): Get all dealers → `curl_outputs/getalldealers.txt`
  - Run cURL to fetch all dealers
  - Include both command and output

- [ ] **Task 10** (2 pts): Get dealer by ID → `curl_outputs/getdealerbyid.txt`
  - Run cURL for specific dealer
  - Include both command and output

- [ ] **Task 11** (2 pts): Get dealers by state → `curl_outputs/getdealersbyState.txt`
  - Run cURL for Kansas dealers
  - Include both command and output

- [ ] **Task 14-15** (4 pts): Get car makes → `curl_outputs/getallcarmakes.txt`
  - Run cURL for all makes/models
  - Include both command and output

- [ ] **Task 16** (2 pts): Analyze review → `curl_outputs/analyzereview.txt`
  - Run cURL with "Fantastic services"
  - Include both command and output

- [ ] **Task 23** (3 pts): CI/CD workflow → `curl_outputs/CICD.txt`
  - Copy GitHub Actions success output
  - Show all workflow steps

- [ ] **Task 24** (1 pt): Deployment URL → `curl_outputs/deploymentURL.txt`
  - Save deployment URL

### Screenshots - Admin (3 points)

- [ ] **Task 12** (2 pts): `screenshots/admin_login.png`
  - Show root user logged into admin page
  - Include browser address bar

- [ ] **Task 13** (1 pt): `screenshots/admin_logout.png`
  - Show root user logged out
  - Include browser address bar

### Screenshots - Local Application (11 points)

- [ ] **Task 17** (1 pt): `screenshots/get_dealers.png`
  - Dealers on home page BEFORE login
  - Include browser address bar

- [ ] **Task 18** (2 pts): `screenshots/get_dealers_loggedin.png`
  - Dealers on home page AFTER login
  - Must show: Review Dealer option, username, endpoint

- [ ] **Task 19** (2 pts): `screenshots/dealersbystate.png`
  - Dealers filtered by State
  - Include browser address bar with endpoint

- [ ] **Task 20** (1 pt): `screenshots/dealer_id_reviews.png`
  - Dealer details page with reviews
  - Include browser address bar with endpoint

- [ ] **Task 21** (1 pt): `screenshots/dealership_review_submission.png`
  - Post Review page with entered details
  - Before clicking submit

- [ ] **Task 22** (2 pts): `screenshots/added_review.png`
  - Show the posted review
  - After submission

### Screenshots - Deployed Application (8 points)

- [ ] **Task 25** (2 pts): `screenshots/deployed_landingpage.png`
  - Deployed landing page
  - Include browser address bar

- [ ] **Task 26** (2 pts): `screenshots/deployed_loggedin.png`
  - Deployed page after login
  - Must show username

- [ ] **Task 27** (2 pts): `screenshots/deployed_dealer_detail.png`
  - Dealer details in deployed app
  - Include browser address bar

- [ ] **Task 28** (2 pts): `screenshots/deployed_add_review.png`
  - Review displayed in deployed app
  - Include browser address bar

---

## Final Checks

- [ ] All cURL output files are in `SUBMISSION/curl_outputs/`
- [ ] All screenshots are in `SUBMISSION/screenshots/`
- [ ] All files are committed and pushed to GitHub
- [ ] Main README.md updated with project details
- [ ] All GitHub URLs are accessible
- [ ] Deployment URL is working

---

**Total Points: 50**
