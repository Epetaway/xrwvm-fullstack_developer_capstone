# Final Submission Artifacts

Save all required outputs and screenshots in this folder.

## Screenshots (PNG or JPEG)
- get_dealers: Home page before login; address bar visible.
- get_dealers_loggedin: Home page after login; show username + Review Dealer option.
- dealersbystate: Dealers filtered by state; address bar visible.
- dealer_id_reviews: Dealer details page with reviews; address bar visible.
- dealership_review_submission: Post Review page before submission.
- added_review: Page showing the newly added review.
- admin_login: Admin login page after successful login.
- admin_logout: Admin page after logout.
- deployed_landingpage: Deployed app landing/login page; address bar visible.
- deployed_loggedin: Deployed app after login; username visible.
- deployed_dealer_detail: Deployed dealer details page; address bar visible.
- deployed_add_review: Deployed app showing posted review; address bar visible.

## Terminal Outputs (text files)
- django_server: Output from `manage.py runserver` while app is running.
- loginuser: cURL request + JSON output for login.
- logoutuser: cURL request + JSON output for logout.
- getdealerreviews: cURL output for reviews of a dealer ID.
- getalldealers: cURL output listing all dealers.
- getdealerbyid: cURL output for one dealer by ID.
- getdealersbyState: cURL output for dealers in Kansas.
- getallcarmakes: cURL output listing car makes/models.
- analyzereview: cURL output for sentiment of "Fantastic services".
- CICD: Output showing GitHub Actions workflow run steps.
- deploymentURL: Text file with the deployed app URL.

## Tips
- On macOS: Press `Shift+Cmd+5` to capture a window including the address bar. Name files exactly as above.
- Ensure Node/Mongo backend is running for dealer data. Use docker-compose in `server/database`.
- Use kubectl port-forward for deployed screenshots: `kubectl port-forward deployment.apps/dealership 8000:8000`.
