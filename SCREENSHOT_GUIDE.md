# Screenshot Capture Guide - Fix Capstone to 100%

## ✅ FIXED - cURL Artifacts (Already Done)
- loginuser.txt ✓
- logoutuser.txt ✓
- getdealerreviews.txt ✓
- getdealerbyid.txt ✓
- getallcarmakes.txt ✓
- getalldealers.txt ✓
- analyzereview.txt ✓

---

## 📸 SCREENSHOTS NEEDED (With URL Bar Visible!)

### Prerequisites:
1. **Django Server Running**: `python manage.py runserver 0.0.0.0:8000` (already running)
2. **Browser Open**: http://localhost:8000/

---

### Q16: `get_dealers.png` (0/1 → 1/1)
**Current Issue**: No dealer list shown, just welcome page

**Steps**:
1. Open http://localhost:8000/
2. Click "View Dealerships" button OR navigate to http://localhost:8000/dealers
3. **CRITICAL**: Ensure URL bar is visible at top showing `http://localhost:8000/dealers`
4. Page should show TABLE with columns: ID, Dealer Name, City, Address, Zip, State
5. Take screenshot (Cmd+Shift+4 → drag to capture browser window)
6. Save as: `get_dealers.png`

**What grader expects**: Dealer list visible BEFORE login, URL bar shown

---

### Q17: `get_dealers_loggedin.png` (0/2 → 2/2)
**Current Issue**: No dealer list OR Review Dealer button visible

**Steps**:
1. Click "Login" in nav bar
2. Enter: Username: `admin`, Password: `admin123`
3. After login, navigate to http://localhost:8000/dealers
4. **CRITICAL**: 
   - URL bar visible: `http://localhost:8000/dealers`
   - Username "admin" visible in top-right
   - Each dealer row should have a "Review Dealer" button/icon
5. Take screenshot
6. Save as: `get_dealers_loggedin.png`

**What grader expects**: Dealer list AFTER login, username visible, Review Dealer option visible, URL bar shown

---

### Q18: `dealersbystate.png` (1/2 → 2/2)
**Current Issue**: No state filter applied, URL bar missing

**Steps**:
1. On dealers page (logged in), find "State" dropdown
2. Select a state (e.g., "Kansas" or "California")
3. Wait for page to filter/reload
4. **CRITICAL**: URL bar visible showing filtered state in URL
5. Only dealers from selected state should be visible
6. Take screenshot
7. Save as: `dealersbystate.png`

**What grader expects**: Filtered dealers by state, URL bar showing state parameter

---

### Q19: `dealer_id_reviews.png` (0/1 → 1/1)
**Current Issue**: URL bar missing

**Steps**:
1. From dealers list, click on a dealer name (e.g., "Fix San Car Dealership")
2. You'll navigate to dealer detail page
3. **CRITICAL**: URL bar visible showing `http://localhost:8000/dealer/29` (or similar ID)
4. Page shows:
   - Dealer name, address
   - List of reviews below
5. Take screenshot
6. Save as: `dealer_id_reviews.png`

**What grader expects**: Dealer details + reviews visible, URL bar shown

---

### Q20: `dealership_review_submission.png` ✅ (1/1 - ALREADY GOOD!)
**Keep existing screenshot** - You already have this one correct!

---

### Q21: `added_review.png` (1/2 → 2/2)
**Current Issue**: Only neutral sentiment icons shown, need variety

**Steps**:
1. After posting review (from Q20), you should see the review listed
2. **CRITICAL**: Review should have a sentiment icon (😊 positive, 😐 neutral, ☹️ negative)
3. Ideally show MULTIPLE reviews with DIFFERENT sentiments
4. Take screenshot showing the posted review WITH sentiment icon
5. Save as: `added_review.png`

**What grader expects**: Posted review visible with clear sentiment representation

---

### Q12: `admin_login.png` (1/2 → 2/2)
**Current Issue**: Shows "admin" user, not "root"

**Steps**:
1. Navigate to http://localhost:8000/admin/
2. Login with: Username: `admin`, Password: `admin123`
3. **CRITICAL**: After login, top-right should show "WELCOME, ADMIN" or similar
4. Take screenshot showing Django admin interface with logged-in user
5. Save as: `admin_login.png`

**What grader expects**: Admin page with user logged in (admin acceptable)

---

### Q13: `admin_logout.png` ✅ (1/1 - ALREADY GOOD!)
**Keep existing screenshot**

---

## 🚀 DEPLOYMENT TASKS (Requires OpenShift Access)

### Q24: `deploymentURL.txt` (0/1)
**Current**: Contains placeholder `http://<route-host>`

**Two Options**:

#### Option A: IBM Skills Network Lab (Easiest)
1. Go to your IBM Skills Network course lab environment
2. They provide a temporary OpenShift cluster
3. Follow lab instructions to deploy
4. Get the route URL from the lab

#### Option B: IBM Cloud OpenShift (Your Own Cluster)
1. Install IBM Cloud CLI: `brew install ibmcloud`
2. Login: `ibmcloud login -r us-south`
3. Get cluster config:
   ```bash
   ibmcloud oc clusters
   ibmcloud oc cluster config --cluster <your-cluster-name>
   ```
4. Apply manifests:
   ```bash
   cd /Users/earlhickson/Development/best-cars-capstone/server
   oc apply -f deployment.yaml
   oc apply -f service.yaml
   oc expose service dealership
   oc get route dealership -o=jsonpath='{.spec.host}{"\n"}'
   ```
5. Save route to file:
   ```bash
   echo "http://$(oc get route dealership -o=jsonpath='{.spec.host}')" > artifacts/deploymentURL.txt
   ```

---

### Q25-Q28: Deployed Screenshots (0/2 each)
**After deployment**, repeat screenshots Q16-Q19 but from the **deployed URL** instead of localhost:

- `deployed_landingpage.png` - Home page from deployed URL
- `deployed_loggedin.png` - Logged in page from deployed URL
- `deployed_dealer_detail.png` - Dealer detail from deployed URL
- `deployed_add_review.png` - Review posted on deployed app

**CRITICAL**: All must show the **actual deployment URL** in browser address bar (not localhost)

---

## 📋 Quick Checklist

### Local Screenshots (Do Now):
- [ ] Q16: get_dealers.png (dealer list, pre-login, URL bar)
- [ ] Q17: get_dealers_loggedin.png (dealer list, post-login, Review button, URL bar)
- [ ] Q18: dealersbystate.png (filtered by state, URL bar)
- [ ] Q19: dealer_id_reviews.png (dealer detail + reviews, URL bar)
- [ ] Q21: added_review.png (review with sentiment variety)

### Deployment (Need Cluster Access):
- [ ] Get OpenShift cluster access (Skills Network Lab OR IBM Cloud)
- [ ] Deploy app
- [ ] Get route URL → save to artifacts/deploymentURL.txt
- [ ] Take 4 deployed screenshots with deployment URL visible

---

## 🎯 Expected Final Score After Fixes

| Task | Current | After Fix |
|------|---------|-----------|
| Q1-Q4 | 7/7 ✓ | 7/7 ✓ |
| Q5-Q6 | 0/4 | 4/4 ✓ (Fixed) |
| Q7 | 1/1 ✓ | 1/1 ✓ |
| Q8-Q11 | 3/8 | 8/8 ✓ (Fixed) |
| Q12-Q13 | 2/3 | 3/3 ✓ |
| Q14-Q15 | 3/6 | 6/6 ✓ (Fixed) |
| Q16-Q21 | 3/10 | 10/10 ✓ (After screenshots) |
| Q22 | 2/3 | 3/3 ✓ (CI/CD detail) |
| Q23-Q28 | 0/7 | 7/7 ✓ (After deployment) |
| **TOTAL** | **21/50 (42%)** | **49/50 (98%+)** |

---

## 🛟 Need Help?

- **Can't find dealer list?** Check React app is built: `cd server/frontend && npm run build`
- **Login not working?** Verify Django superuser: `python manage.py createsuperuser`
- **No cluster access?** Use IBM Skills Network lab environment (free, pre-configured)
- **Stuck on deployment?** Share cluster name/region and I'll help with commands
