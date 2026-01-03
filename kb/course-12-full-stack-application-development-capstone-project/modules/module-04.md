# Module 4: User Authentication System

## Objectives
- Implement secure user registration and login functionality
- Use Django's built-in authentication system
- Create session-based authentication for web applications
- Handle user passwords securely with hashing
- Manage user sessions across frontend and backend
- Implement logout functionality
- Validate user inputs and prevent duplicate registrations
- Integrate authentication state with React components

## Key Concepts

### Django Authentication System
Django provides a complete authentication framework:
- **User Model**: Built-in model for user accounts (`django.contrib.auth.models.User`)
- **Authentication**: Verify user credentials (username + password)
- **Authorization**: Control what authenticated users can access
- **Sessions**: Track logged-in users across requests
- **Password Hashing**: Secure password storage using PBKDF2

### Authentication vs. Authorization
- **Authentication**: "Who are you?" - Verifying identity
- **Authorization**: "What can you do?" - Checking permissions

### Session Management
HTTP is stateless, so sessions maintain state:
1. User logs in with credentials
2. Server creates session and sends session ID in cookie
3. Browser sends session cookie with subsequent requests
4. Server uses session ID to identify user

### Password Security
Never store plain-text passwords:
```python
# ❌ NEVER do this
user.password = "mypassword123"

# ✅ Django handles hashing automatically
user = User.objects.create_user(
    username="john",
    password="mypassword123"  # Automatically hashed
)
```

### CSRF Protection
Cross-Site Request Forgery protection:
- Prevents malicious sites from making requests on user's behalf
- Django requires CSRF token for POST requests
- JSON APIs can use `@csrf_exempt` with alternative security (tokens, API keys)

## Tools & Commands

### User Management Commands

**Create Superuser**:
```bash
# Interactive prompts for username, email, password
python manage.py createsuperuser

# Non-interactive (for scripts)
python manage.py createsuperuser \
  --username admin \
  --email admin@example.com \
  --noinput
```

**Create Regular User (Python Shell)**:
```bash
python manage.py shell

>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user('john', 'john@example.com', 'password123')
>>> user.first_name = 'John'
>>> user.last_name = 'Doe'
>>> user.save()
```

**Change Password**:
```bash
python manage.py changepassword username
```

**List Users**:
```bash
python manage.py shell

>>> from django.contrib.auth.models import User
>>> User.objects.all()
>>> User.objects.filter(is_active=True).count()
```

### Testing Authentication Endpoints

**Test Login**:
```bash
curl -X POST http://localhost:8000/djangoapp/login \
  -H "Content-Type: application/json" \
  -d '{"userName":"admin","password":"admin123"}'
```

**Test Registration**:
```bash
curl -X POST http://localhost:8000/djangoapp/register \
  -H "Content-Type: application/json" \
  -d '{
    "userName":"newuser",
    "password":"Pass123!",
    "firstName":"Jane",
    "lastName":"Smith",
    "email":"jane@example.com"
  }'
```

**Test Logout**:
```bash
curl http://localhost:8000/djangoapp/logout
```

## Code Snippets

### Login View
```python
# djangoapp/views.py
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_user(request):
    """
    Authenticate user and create session.
    Expects JSON: {"userName": "...", "password": "..."}
    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get('userName')
            password = data.get('password')
            
            # Authenticate with Django's built-in system
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Create session
                login(request, user)
                return JsonResponse({
                    "userName": username,
                    "status": "Authenticated"
                })
            else:
                # Invalid credentials
                return JsonResponse({
                    "userName": username,
                    "status": "Failed"
                })
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    
    return JsonResponse({"error": "Method not allowed"}, status=405)
```

### Registration View
```python
@csrf_exempt
def registration(request):
    """
    Create new user account.
    Expects JSON: {
        "userName": "...",
        "password": "...",
        "firstName": "...",
        "lastName": "...",
        "email": "..."
    }
    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get('userName')
            password = data.get('password')
            first_name = data.get('firstName')
            last_name = data.get('lastName')
            email = data.get('email')
            
            # Check if user already exists
            if User.objects.filter(username=username).exists():
                return JsonResponse({
                    "status": False,
                    "error": "Already Registered"
                })
            
            # Create new user (password is automatically hashed)
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            
            # Automatically log in the new user
            login(request, user)
            
            return JsonResponse({
                "userName": username,
                "status": True
            })
            
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    return JsonResponse({"error": "Method not allowed"}, status=405)
```

### Logout View
```python
def logout_user(request):
    """
    End user session.
    """
    logout(request)
    return JsonResponse({"userName": ""})
```

### Protected View (Require Authentication)
```python
from django.contrib.auth.decorators import login_required

@login_required
def add_review(request):
    """
    Only authenticated users can add reviews.
    """
    if request.method == "POST":
        # Get username from session
        username = request.user.username
        
        # Process review submission
        # ...
        
        return JsonResponse({"status": "Review added"})
    
    return JsonResponse({"error": "Method not allowed"}, status=405)
```

### React Login Component
```javascript
// src/components/Login/Login.jsx
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Login() {
  const [userName, setUserName] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    try {
      const response = await fetch('/djangoapp/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          userName: userName,
          password: password
        })
      });

      const data = await response.json();
      
      if (data.status === 'Authenticated') {
        // Store username in session storage
        sessionStorage.setItem('username', userName);
        // Redirect to home page
        navigate('/');
      } else {
        setError('Invalid username or password');
      }
    } catch (error) {
      setError('Login failed. Please try again.');
      console.error('Login error:', error);
    }
  };

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-6">
          <div className="card">
            <div className="card-body">
              <h2 className="card-title text-center">Login</h2>
              
              {error && (
                <div className="alert alert-danger" role="alert">
                  {error}
                </div>
              )}
              
              <form onSubmit={handleSubmit}>
                <div className="mb-3">
                  <label htmlFor="username" className="form-label">
                    Username
                  </label>
                  <input
                    type="text"
                    className="form-control"
                    id="username"
                    value={userName}
                    onChange={(e) => setUserName(e.target.value)}
                    required
                  />
                </div>
                
                <div className="mb-3">
                  <label htmlFor="password" className="form-label">
                    Password
                  </label>
                  <input
                    type="password"
                    className="form-control"
                    id="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                  />
                </div>
                
                <button type="submit" className="btn btn-primary w-100">
                  Login
                </button>
              </form>
              
              <div className="text-center mt-3">
                <p>Don't have an account? <a href="/register">Register here</a></p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Login;
```

### React Registration Component
```javascript
// src/components/Register/Register.jsx
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Register() {
  const [formData, setFormData] = useState({
    userName: '',
    firstName: '',
    lastName: '',
    email: '',
    password: '',
    confirmPassword: ''
  });
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    // Validate passwords match
    if (formData.password !== formData.confirmPassword) {
      setError('Passwords do not match');
      return;
    }

    try {
      const response = await fetch('/djangoapp/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          userName: formData.userName,
          password: formData.password,
          firstName: formData.firstName,
          lastName: formData.lastName,
          email: formData.email
        })
      });

      const data = await response.json();
      
      if (data.status === true) {
        // Store username and redirect
        sessionStorage.setItem('username', formData.userName);
        navigate('/');
      } else {
        setError(data.error || 'Registration failed');
      }
    } catch (error) {
      setError('Registration failed. Please try again.');
      console.error('Registration error:', error);
    }
  };

  return (
    <div className="container mt-5">
      <h2>Register</h2>
      {error && <div className="alert alert-danger">{error}</div>}
      
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label className="form-label">Username</label>
          <input
            type="text"
            className="form-control"
            name="userName"
            value={formData.userName}
            onChange={handleChange}
            required
          />
        </div>
        
        <div className="mb-3">
          <label className="form-label">First Name</label>
          <input
            type="text"
            className="form-control"
            name="firstName"
            value={formData.firstName}
            onChange={handleChange}
            required
          />
        </div>
        
        <div className="mb-3">
          <label className="form-label">Last Name</label>
          <input
            type="text"
            className="form-control"
            name="lastName"
            value={formData.lastName}
            onChange={handleChange}
            required
          />
        </div>
        
        <div className="mb-3">
          <label className="form-label">Email</label>
          <input
            type="email"
            className="form-control"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
          />
        </div>
        
        <div className="mb-3">
          <label className="form-label">Password</label>
          <input
            type="password"
            className="form-control"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
          />
        </div>
        
        <div className="mb-3">
          <label className="form-label">Confirm Password</label>
          <input
            type="password"
            className="form-control"
            name="confirmPassword"
            value={formData.confirmPassword}
            onChange={handleChange}
            required
          />
        </div>
        
        <button type="submit" className="btn btn-primary">Register</button>
      </form>
    </div>
  );
}

export default Register;
```

### Session-Aware Header Component
```javascript
// src/components/Header/Header.jsx
import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

function Header() {
  const [username, setUsername] = useState(null);

  useEffect(() => {
    // Check session storage on component mount
    const storedUsername = sessionStorage.getItem('username');
    setUsername(storedUsername);
  }, []);

  const handleLogout = async () => {
    try {
      await fetch('/djangoapp/logout');
      sessionStorage.removeItem('username');
      setUsername(null);
      window.location.href = '/';
    } catch (error) {
      console.error('Logout error:', error);
    }
  };

  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <div className="container-fluid">
        <Link className="navbar-brand" to="/">Best Cars</Link>
        
        <div className="navbar-nav ms-auto">
          <Link className="nav-link" to="/dealers">Dealers</Link>
          
          {username ? (
            <>
              <span className="nav-link">Welcome, {username}!</span>
              <button className="btn btn-link nav-link" onClick={handleLogout}>
                Logout
              </button>
            </>
          ) : (
            <>
              <Link className="nav-link" to="/login">Login</Link>
              <Link className="nav-link" to="/register">Register</Link>
            </>
          )}
        </div>
      </div>
    </nav>
  );
}

export default Header;
```

## Common Pitfalls

### 1. Storing Passwords in Plain Text
**Problem**: Security vulnerability
**Solution**: Always use `create_user()` which hashes passwords
```python
# ❌ NEVER do this
user = User(username="john", password="plain123")
user.save()

# ✅ Correct
user = User.objects.create_user(username="john", password="plain123")
```

### 2. Not Checking for Duplicate Users
**Problem**: Database constraint errors on duplicate usernames
**Solution**: Check existence before creating
```python
if User.objects.filter(username=username).exists():
    return JsonResponse({"error": "Username taken"}, status=400)
```

### 3. Missing CSRF Exemption for JSON APIs
**Problem**: 403 Forbidden errors on POST requests
**Solution**: Use `@csrf_exempt` for JSON APIs
```python
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_user(request):
    # Handle JSON login
```

### 4. Not Clearing Session on Logout
**Problem**: User appears logged in after logout
**Solution**: Clear both server session and client storage
```javascript
// Server side
logout(request)

// Client side
sessionStorage.removeItem('username');
```

### 5. Weak Password Validation
**Problem**: Users create easily guessable passwords
**Solution**: Implement password strength requirements
```python
# settings.py
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8}
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
]
```

## Mini Quiz

1. **What's the difference between `authenticate()` and `login()` in Django?**
   - **Answer**: `authenticate()` verifies credentials (username + password) and returns a User object if valid, or None if invalid. It doesn't create a session. `login()` takes an authenticated user and creates a session, allowing the user to make authenticated requests. You must call `authenticate()` first to verify credentials, then `login()` to create the session.

2. **Why should passwords never be stored in plain text?**
   - **Answer**: If the database is compromised, attackers would have immediate access to all user passwords. Many users reuse passwords across sites, so a breach affects their other accounts too. Django uses PBKDF2 hashing with salts, making it computationally infeasible to reverse-engineer passwords even if the database is stolen.

3. **What is a session and how does it work?**
   - **Answer**: A session is server-side storage that maintains user state across HTTP requests. When a user logs in, Django creates a session ID, stores it in a cookie sent to the browser, and saves session data on the server. The browser sends this cookie with each request, allowing Django to identify the user and retrieve their session data. Sessions expire after inactivity or when the user logs out.

4. **What's the purpose of `@csrf_exempt` decorator?**
   - **Answer**: It disables Django's CSRF protection for specific views. CSRF tokens prevent cross-site request forgery by ensuring requests originate from your site. JSON APIs typically use other auth methods (tokens, API keys) and don't send CSRF tokens, so we exempt them. However, always implement alternative security for exempted endpoints.

5. **How can you protect routes that require authentication in React?**
   - **Answer**: Create a ProtectedRoute component that checks `sessionStorage.getItem('username')`. If not present, redirect to login. Wrap protected routes with this component: `<Route path="/add-review" element={<ProtectedRoute><PostReview /></ProtectedRoute>} />`. Note: Client-side checks are for UX only; always validate authentication on the server for actual security.

## Practice Task

### Task: Implement Complete Authentication Flow

**Objective**: Build a fully functional authentication system with registration, login, and protected routes.

**Requirements**:
1. Create Django endpoints for login, logout, and registration
2. Build React components for Login and Register pages
3. Implement session management with sessionStorage
4. Create a protected route that requires authentication
5. Add logout functionality to the header
6. Display appropriate messages for success/error states
7. Prevent duplicate user registrations

**Steps**:
1. Implement `login_user()`, `logout_user()`, and `registration()` views in Django
2. Configure URL patterns for auth endpoints
3. Create Login component with form and error handling
4. Create Register component with password confirmation
5. Update Header component to show username when logged in
6. Test all flows: register → login → access protected route → logout
7. Verify session persistence across page reloads

**Expected Outcomes**:
- New users can register successfully
- Registered users can log in with correct credentials
- Invalid credentials show error messages
- Logout clears session and returns to anonymous state
- Protected routes redirect unauthenticated users to login
- Session persists across page navigation

**Test Scenarios**:
```bash
# Test registration
curl -X POST http://localhost:8000/djangoapp/register \
  -H "Content-Type: application/json" \
  -d '{"userName":"testuser","password":"Test123!","firstName":"Test","lastName":"User","email":"test@example.com"}'

# Test login
curl -X POST http://localhost:8000/djangoapp/login \
  -H "Content-Type: application/json" \
  -d '{"userName":"testuser","password":"Test123!"}'

# Test duplicate registration
curl -X POST http://localhost:8000/djangoapp/register \
  -H "Content-Type: application/json" \
  -d '{"userName":"testuser","password":"Test123!","firstName":"Test","lastName":"User","email":"test@example.com"}'
# Should return error: "Already Registered"
```

**Hints**:
- Use Django's `User.objects.filter(username=x).exists()` to check for duplicates
- Always hash passwords with `create_user()`, never set password directly
- Test both successful and failed login attempts
- Verify session cookies in browser DevTools

## Career Notes

### Relevant Job Roles
- **Full-Stack Developer**: Implements end-to-end authentication systems
- **Security Engineer**: Ensures authentication systems are secure and compliant
- **Backend Developer**: Builds robust authentication and authorization logic
- **Frontend Developer**: Creates intuitive login/registration user experiences

### Industry Expectations
- Understanding of authentication vs. authorization
- Knowledge of session management and cookies
- Familiarity with OAuth, JWT, and token-based auth (beyond basic sessions)
- Awareness of common security vulnerabilities (SQL injection, XSS, CSRF)
- Ability to implement password reset and email verification
- Understanding of multi-factor authentication (MFA)
- Knowledge of role-based access control (RBAC)

### Interview Topics
- "Explain how session-based authentication works"
- "What are the differences between session-based and token-based authentication?"
- "How do you prevent common authentication vulnerabilities?"
- "Describe how you would implement password reset functionality"
- "What's the difference between authentication and authorization?"
- "How would you implement SSO (Single Sign-On)?"

### Skills Demonstrated
- Secure password handling and hashing
- Session management across client and server
- Form validation and error handling
- User experience design for auth flows
- Security best practices (CSRF, password strength)
- Integration of frontend and backend authentication
- State management for user sessions

### Real-World Variations
- **JWT Tokens**: Stateless authentication for APIs and mobile apps
- **OAuth 2.0**: Third-party authentication (Login with Google/GitHub)
- **Multi-Factor Authentication**: SMS codes, authenticator apps
- **Role-Based Access**: Admin vs. regular user permissions
- **Password Reset**: Email-based verification flows
- **Account Verification**: Email confirmation before activation
