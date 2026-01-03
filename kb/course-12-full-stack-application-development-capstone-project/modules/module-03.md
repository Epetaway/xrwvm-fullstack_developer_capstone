# Module 3: Frontend Development with React

## Objectives
- Build reusable React components following best practices
- Implement client-side routing with React Router
- Manage application state using hooks (useState, useEffect)
- Handle form submissions and user interactions
- Make API calls to backend endpoints using fetch
- Integrate frontend with Django backend API
- Create responsive UI with Bootstrap styling
- Implement session management for user authentication

## Key Concepts

### React Components
Components are the building blocks of React applications:
- **Functional Components**: Modern approach using functions and hooks
- **Props**: Data passed from parent to child components
- **State**: Component-specific data that can change over time
- **JSX**: JavaScript XML syntax for writing HTML-like code in JavaScript

### React Hooks
Hooks let you use state and lifecycle features in functional components:
- **useState**: Manage component state
- **useEffect**: Handle side effects (API calls, subscriptions)
- **useNavigate**: Programmatic navigation (React Router v6)
- **useParams**: Access URL parameters

### Single Page Application (SPA)
React creates SPAs that:
- Load one HTML page and dynamically update content
- Navigate without full page reloads
- Provide faster, more responsive user experience
- Maintain state across navigation

### React Router
Client-side routing library:
```javascript
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/login" element={<Login />} />
  <Route path="/dealers/:id" element={<DealerDetail />} />
</Routes>
```

### Session Storage
Browser API for persisting data across page reloads:
```javascript
// Store user data
sessionStorage.setItem('username', 'john');

// Retrieve user data
const username = sessionStorage.getItem('username');

// Remove user data
sessionStorage.removeItem('username');
```

## Tools & Commands

### React Development

**Install Dependencies**:
```bash
cd frontend

# Install React Router
npm install react-router-dom

# Install additional libraries
npm install axios  # Alternative to fetch
npm install bootstrap  # CSS framework
```

**Development Server**:
```bash
# Start development server (port 3000)
npm start

# Run with custom port
PORT=3001 npm start
```

**Production Build**:
```bash
# Create optimized production build
npm run build

# Output directory: build/
# Files are minified and optimized
```

### Component Development

**Create New Component**:
```bash
mkdir src/components/Dealers
touch src/components/Dealers/Dealers.jsx
```

**Component File Structure**:
```
src/
├── components/
│   ├── Header/
│   │   └── Header.jsx
│   ├── Dealers/
│   │   └── Dealers.jsx
│   ├── Login/
│   │   └── Login.jsx
│   └── Register/
│   │   └── Register.jsx
├── App.js
└── index.js
```

### Debugging Tools

**React Developer Tools**:
```bash
# Browser extension for Chrome/Firefox
# Inspect component tree and state
# Available in browser DevTools after installation
```

**Console Logging**:
```javascript
console.log('Component mounted');
console.log('Props:', props);
console.log('State:', state);
```

## Code Snippets

### Functional Component with Hooks
```javascript
// src/components/Dealers/Dealers.jsx
import React, { useState, useEffect } from 'react';

function Dealers() {
  const [dealers, setDealers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch dealers when component mounts
    fetchDealers();
  }, []); // Empty dependency array = run once

  const fetchDealers = async () => {
    try {
      const response = await fetch('/djangoapp/get_dealers/');
      const data = await response.json();
      setDealers(data.dealers);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching dealers:', error);
      setLoading(false);
    }
  };

  if (loading) {
    return <div>Loading dealers...</div>;
  }

  return (
    <div className="container">
      <h1>Dealerships</h1>
      <div className="row">
        {dealers.map(dealer => (
          <div key={dealer.id} className="col-md-4">
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">{dealer.full_name}</h5>
                <p className="card-text">{dealer.city}, {dealer.state}</p>
                <a href={`/dealer/${dealer.id}`} className="btn btn-primary">
                  View Details
                </a>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Dealers;
```

### Form Handling with State
```javascript
// src/components/Login/Login.jsx
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Login() {
  const [userName, setUserName] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (event) => {
    event.preventDefault();
    
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
        // Store username in session
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
    <div className="container">
      <h2>Login</h2>
      {error && <div className="alert alert-danger">{error}</div>}
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="username" className="form-label">Username</label>
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
          <label htmlFor="password" className="form-label">Password</label>
          <input
            type="password"
            className="form-control"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit" className="btn btn-primary">Login</button>
      </form>
    </div>
  );
}

export default Login;
```

### React Router Setup
```javascript
// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header/Header';
import Home from './components/Home/Home';
import Dealers from './components/Dealers/Dealers';
import DealerDetail from './components/Dealers/DealerDetail';
import Login from './components/Login/Login';
import Register from './components/Register/Register';

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dealers" element={<Dealers />} />
        <Route path="/dealer/:id" element={<DealerDetail />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </Router>
  );
}

export default App;
```

### Using URL Parameters
```javascript
// src/components/Dealers/DealerDetail.jsx
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

function DealerDetail() {
  const { id } = useParams(); // Get :id from URL
  const [dealer, setDealer] = useState(null);
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    fetchDealerDetails();
    fetchReviews();
  }, [id]);

  const fetchDealerDetails = async () => {
    const response = await fetch(`/djangoapp/dealer/${id}/`);
    const data = await response.json();
    setDealer(data.dealer);
  };

  const fetchReviews = async () => {
    const response = await fetch(`/djangoapp/reviews/dealer/${id}/`);
    const data = await response.json();
    setReviews(data.reviews);
  };

  if (!dealer) return <div>Loading...</div>;

  return (
    <div className="container">
      <h1>{dealer.full_name}</h1>
      <p>{dealer.address}, {dealer.city}, {dealer.state} {dealer.zip}</p>
      
      <h2>Reviews</h2>
      {reviews.map(review => (
        <div key={review.id} className="card mb-3">
          <div className="card-body">
            <h5>{review.name}</h5>
            <p>{review.review}</p>
            <span className="badge bg-secondary">{review.sentiment}</span>
          </div>
        </div>
      ))}
    </div>
  );
}

export default DealerDetail;
```

### Bootstrap Integration
```javascript
// src/index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

## Common Pitfalls

### 1. Infinite Loop in useEffect
**Problem**: Component re-renders infinitely
**Solution**: Provide correct dependency array
```javascript
// ❌ Wrong - runs on every render
useEffect(() => {
  setCount(count + 1);
});

// ✅ Correct - runs once on mount
useEffect(() => {
  fetchData();
}, []);

// ✅ Correct - runs when id changes
useEffect(() => {
  fetchDealer(id);
}, [id]);
```

### 2. Async State Updates
**Problem**: State doesn't update immediately
**Solution**: Remember setState is asynchronous
```javascript
// ❌ Wrong - won't work as expected
setCount(count + 1);
console.log(count); // Still old value!

// ✅ Correct - use callback or useEffect
setCount(prevCount => prevCount + 1);
useEffect(() => {
  console.log(count); // New value
}, [count]);
```

### 3. CORS Errors in Development
**Problem**: API calls blocked by CORS policy
**Solution**: Configure proxy in package.json
```json
// package.json
{
  "proxy": "http://localhost:8000"
}
```

Then use relative URLs:
```javascript
// ❌ Wrong - triggers CORS
fetch('http://localhost:8000/djangoapp/dealers')

// ✅ Correct - uses proxy
fetch('/djangoapp/dealers')
```

### 4. Form Submission Page Reload
**Problem**: Form submits and page reloads
**Solution**: Prevent default behavior
```javascript
const handleSubmit = (event) => {
  event.preventDefault(); // Prevent page reload
  // Handle form submission
};
```

### 5. Key Prop Warning
**Problem**: "Each child in a list should have a unique key prop"
**Solution**: Add key prop when mapping arrays
```javascript
// ❌ Wrong
{dealers.map(dealer => <Card>{dealer.name}</Card>)}

// ✅ Correct
{dealers.map(dealer => <Card key={dealer.id}>{dealer.name}</Card>)}
```

## Mini Quiz

1. **What's the purpose of the `useState` hook in React?**
   - **Answer**: `useState` allows functional components to manage local state. It returns an array with two elements: the current state value and a function to update it. For example, `const [count, setCount] = useState(0)` creates a state variable `count` initialized to 0, and `setCount` is used to update it. State updates trigger re-renders of the component.

2. **When does the code inside `useEffect` run?**
   - **Answer**: It depends on the dependency array. With no dependencies `useEffect(() => {})`, it runs after every render. With an empty array `useEffect(() => {}, [])`, it runs once after the first render (like componentDidMount). With dependencies `useEffect(() => {}, [id])`, it runs when any dependency value changes.

3. **How do you pass data from a parent component to a child component?**
   - **Answer**: Through props. The parent passes data as attributes: `<Child name="John" age={25} />`. The child receives them as a props object: `function Child(props) { return <div>{props.name}</div>; }` or using destructuring: `function Child({ name, age }) { ... }`.

4. **What's the difference between `sessionStorage` and `localStorage`?**
   - **Answer**: `sessionStorage` persists data for the duration of the page session (cleared when tab closes), while `localStorage` persists indefinitely until explicitly cleared. Both store string key-value pairs and are limited to ~5-10MB. Use sessionStorage for temporary authentication state, localStorage for user preferences.

5. **Why do we use `event.preventDefault()` in form handlers?**
   - **Answer**: By default, HTML forms trigger a page reload on submission. `event.preventDefault()` stops this default behavior, allowing JavaScript to handle the submission via fetch/axios without interrupting the single-page application experience. This is essential for SPAs built with React.

## Practice Task

### Task: Build a Dealer Review Submission Form

**Objective**: Create a React component that allows authenticated users to submit reviews for a specific dealer.

**Requirements**:
1. Create a `PostReview` component
2. Include form fields: name, review text, purchase (checkbox), car make, car model, car year
3. Validate form inputs before submission
4. POST review data to Django API endpoint
5. Show success/error messages
6. Redirect to dealer detail page after successful submission
7. Check if user is logged in (from sessionStorage)

**Steps**:
1. Create `PostReview.jsx` component file
2. Set up form state using `useState` for each field
3. Implement form validation
4. Create `handleSubmit` function that POSTs to `/djangoapp/add_review`
5. Handle response and show appropriate message
6. Add route in `App.js`: `/postreview/:dealer_id`
7. Test the component by submitting a review

**Expected Outcomes**:
- Form displays all required fields
- Validation prevents empty submissions
- Successful submission shows confirmation message
- Review appears in dealer detail page
- Unauthenticated users are redirected to login

**Starter Code**:
```javascript
import React, { useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

function PostReview() {
  const { dealer_id } = useParams();
  const navigate = useNavigate();
  const [review, setReview] = useState('');
  const [purchase, setPurchase] = useState(false);
  
  // Add more state variables for other fields
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    // TODO: Implement submission logic
  };
  
  return (
    // TODO: Implement form JSX
  );
}

export default PostReview;
```

**Hints**:
- Check `sessionStorage.getItem('username')` for authentication
- Use controlled components (value + onChange)
- Clear form after successful submission
- Handle errors gracefully with try/catch

## Career Notes

### Relevant Job Roles
- **Frontend Developer**: Specializes in React and modern JavaScript frameworks
- **UI/UX Developer**: Builds interactive user interfaces with focus on user experience
- **Full-Stack Developer**: Works on both React frontend and backend APIs
- **JavaScript Developer**: Expert in JavaScript, React, and related ecosystem

### Industry Expectations
- Proficiency with React hooks (useState, useEffect, custom hooks)
- Understanding of component lifecycle and re-rendering
- Knowledge of state management (Context API, Redux for larger apps)
- Ability to integrate frontend with RESTful APIs
- Familiarity with modern JavaScript (ES6+, async/await, destructuring)
- Experience with build tools (Webpack, npm scripts)
- Understanding of responsive design and CSS frameworks

### Interview Topics
- "Explain the Virtual DOM and how React uses it"
- "What's the difference between controlled and uncontrolled components?"
- "How would you optimize a React application for performance?"
- "Describe the component lifecycle in functional components with hooks"
- "When would you use Context API vs. props drilling vs. Redux?"

### Skills Demonstrated
- Modern React development with functional components
- State management and data flow
- API integration and asynchronous operations
- Form handling and validation
- Client-side routing
- Error handling and user feedback
- Responsive UI development
- Session and authentication management

### Portfolio Tips
- Include working examples of React components
- Show before/after screenshots of your UI
- Demonstrate responsive design on mobile/desktop
- Highlight any performance optimizations
- Explain your state management choices
- Show error handling and edge cases
