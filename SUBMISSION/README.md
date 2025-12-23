# Final Submission - Fullstack Developer Capstone

## Project Information
- **Project Name:** Best Cars Dealership
- **Repository:** https://github.com/Epetaway/xrwvm-fullstack_developer_capstone
- **Student:** Epetaway

---

## Submission Checklist (50 Points Total)

### Code & Static Files

| Task | Points | Item | Status | URL/Location |
|------|--------|------|--------|--------------|
| 1 | 1 | README.md with Project name | ✅ | [README.md](https://github.com/Epetaway/xrwvm-fullstack_developer_capstone/blob/main/README.md) |
| 3 | 3 | About.html | ✅ | [About.html](https://github.com/Epetaway/xrwvm-fullstack_developer_capstone/blob/main/server/frontend/static/About.html) |
| 4 | 2 | Contact.html | ✅ | [Contact.html](https://github.com/Epetaway/xrwvm-fullstack_developer_capstone/blob/main/server/frontend/static/Contact.html) |
| 7 | 1 | Register.jsx | ✅ | [Register.jsx](https://github.com/Epetaway/xrwvm-fullstack_developer_capstone/blob/main/server/frontend/src/components/Register/Register.jsx) |

### cURL Command Outputs (To Be Completed)

| Task | Points | File | Status | Location |
|------|--------|------|--------|----------|
| 2 | 1 | django_server | ⏳ | [curl_outputs/django_server.txt](curl_outputs/django_server.txt) |
| 5 | 2 | loginuser | ⏳ | [curl_outputs/loginuser.txt](curl_outputs/loginuser.txt) |
| 6 | 2 | logoutuser | ⏳ | [curl_outputs/logoutuser.txt](curl_outputs/logoutuser.txt) |
| 8 | 2 | getdealerreviews | ⏳ | [curl_outputs/getdealerreviews.txt](curl_outputs/getdealerreviews.txt) |
| 9 | 2 | getalldealers | ⏳ | [curl_outputs/getalldealers.txt](curl_outputs/getalldealers.txt) |
| 10 | 2 | getdealerbyid | ⏳ | [curl_outputs/getdealerbyid.txt](curl_outputs/getdealerbyid.txt) |
| 11 | 2 | getdealersbyState | ⏳ | [curl_outputs/getdealersbyState.txt](curl_outputs/getdealersbyState.txt) |
| 14-15 | 4 | getallcarmakes | ⏳ | [curl_outputs/getallcarmakes.txt](curl_outputs/getallcarmakes.txt) |
| 16 | 2 | analyzereview | ⏳ | [curl_outputs/analyzereview.txt](curl_outputs/analyzereview.txt) |
| 23 | 3 | CICD | ⏳ | [curl_outputs/CICD.txt](curl_outputs/CICD.txt) |
| 24 | 1 | deploymentURL | ⏳ | [curl_outputs/deploymentURL.txt](curl_outputs/deploymentURL.txt) |

### Screenshots (To Be Completed)

| Task | Points | File | Status | Location |
|------|--------|------|--------|----------|
| 12 | 2 | admin_login | ⏳ | [screenshots/admin_login.png](screenshots/) |
| 13 | 1 | admin_logout | ⏳ | [screenshots/admin_logout.png](screenshots/) |
| 17 | 1 | get_dealers | ⏳ | [screenshots/get_dealers.png](screenshots/) |
| 18 | 2 | get_dealers_loggedin | ⏳ | [screenshots/get_dealers_loggedin.png](screenshots/) |
| 19 | 2 | dealersbystate | ⏳ | [screenshots/dealersbystate.png](screenshots/) |
| 20 | 1 | dealer_id_reviews | ⏳ | [screenshots/dealer_id_reviews.png](screenshots/) |
| 21 | 1 | dealership_review_submission | ⏳ | [screenshots/dealership_review_submission.png](screenshots/) |
| 22 | 2 | added_review | ⏳ | [screenshots/added_review.png](screenshots/) |
| 25 | 2 | deployed_landingpage | ⏳ | [screenshots/deployed_landingpage.png](screenshots/) |
| 26 | 2 | deployed_loggedin | ⏳ | [screenshots/deployed_loggedin.png](screenshots/) |
| 27 | 2 | deployed_dealer_detail | ⏳ | [screenshots/deployed_dealer_detail.png](screenshots/) |
| 28 | 2 | deployed_add_review | ⏳ | [screenshots/deployed_add_review.png](screenshots/) |

---

## How to Complete Missing Items

### 1. Run Django Server and Capture Output
```bash
cd server
python manage.py runserver > ../SUBMISSION/curl_outputs/django_server.txt 2>&1
```

### 2. Execute cURL Commands
See [example_curl_commands.md](example_curl_commands.md) for all commands.

### 3. Take Screenshots
- Use your browser's screenshot tool or print screen
- Ensure endpoints are visible in the address bar
- Save all screenshots in the `screenshots/` folder
- Use PNG or JPEG format

### 4. Deploy and Document
- Deploy your application
- Save the deployment URL in `curl_outputs/deploymentURL.txt`
- Take screenshots of the deployed application

---

## Submission URLs

**Main Repository:** https://github.com/Epetaway/xrwvm-fullstack_developer_capstone

**Key Files:**
- README.md: https://github.com/Epetaway/xrwvm-fullstack_developer_capstone/blob/main/README.md
- About.html: https://github.com/Epetaway/xrwvm-fullstack_developer_capstone/blob/main/server/frontend/static/About.html
- Contact.html: https://github.com/Epetaway/xrwvm-fullstack_developer_capstone/blob/main/server/frontend/static/Contact.html
- Register.jsx: https://github.com/Epetaway/xrwvm-fullstack_developer_capstone/blob/main/server/frontend/src/components/Register/Register.jsx

---

## Notes

- ✅ = Completed
- ⏳ = To be completed
- Total Points: 50
