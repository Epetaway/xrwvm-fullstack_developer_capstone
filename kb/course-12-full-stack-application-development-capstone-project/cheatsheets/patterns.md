# Design Patterns and Best Practices

Common patterns, best practices, and architectural approaches for full-stack development with Django and React.

## Django Patterns

### 1. Model-View-Template (MVT) Pattern

Django's variant of MVC:
- **Model**: Data layer (database tables)
- **View**: Business logic (request handlers)
- **Template**: Presentation layer (HTML rendering)

```python
# Model
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

# View
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

# Template (products.html)
# {% for product in products %}
#   <div>{{ product.name }} - ${{ product.price }}</div>
# {% endfor %}
```

### 2. Fat Models, Thin Views

Keep business logic in models, keep views simple:

```python
# ❌ Bad: Logic in view
def approve_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.status = 'approved'
    order.approved_at = timezone.now()
    order.approved_by = request.user
    order.save()
    # Send email
    send_mail(...)
    return JsonResponse({'status': 'ok'})

# ✅ Good: Logic in model
class Order(models.Model):
    status = models.CharField(max_length=20)
    
    def approve(self, user):
        self.status = 'approved'
        self.approved_at = timezone.now()
        self.approved_by = user
        self.save()
        self.send_approval_email()
    
    def send_approval_email(self):
        send_mail(...)

def approve_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.approve(request.user)
    return JsonResponse({'status': 'ok'})
```

### 3. Custom Managers and QuerySets

Encapsulate common queries:

```python
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Post(models.Model):
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20)
    
    objects = models.Manager()      # Default manager
    published = PublishedManager()  # Custom manager

# Usage
all_posts = Post.objects.all()
published_posts = Post.published.all()
```

### 4. Service Layer Pattern

Separate business logic from views:

```python
# services.py
class ReviewService:
    @staticmethod
    def create_review(dealer_id, user, text):
        # Analyze sentiment
        sentiment = analyze_sentiment(text)
        
        # Create review
        review = Review.objects.create(
            dealer_id=dealer_id,
            user=user,
            text=text,
            sentiment=sentiment
        )
        
        # Notify dealer
        notify_dealer(dealer_id, review)
        
        return review

# views.py
def add_review(request):
    dealer_id = request.POST.get('dealer_id')
    text = request.POST.get('text')
    
    review = ReviewService.create_review(
        dealer_id=dealer_id,
        user=request.user,
        text=text
    )
    
    return JsonResponse({'id': review.id})
```

### 5. Repository Pattern

Abstract data access:

```python
class DealerRepository:
    @staticmethod
    def get_by_state(state):
        return Dealer.objects.filter(state=state)
    
    @staticmethod
    def get_with_reviews(dealer_id):
        dealer = Dealer.objects.get(id=dealer_id)
        reviews = Review.objects.filter(dealer_id=dealer_id)
        return dealer, reviews
    
    @staticmethod
    def search(query):
        return Dealer.objects.filter(
            Q(name__icontains=query) |
            Q(city__icontains=query)
        )
```

## React Patterns

### 1. Container/Presentational Pattern

Separate logic from presentation:

```javascript
// Presentational Component (UI only)
function DealerCard({ dealer, onSelect }) {
  return (
    <div className="card">
      <h3>{dealer.name}</h3>
      <p>{dealer.city}, {dealer.state}</p>
      <button onClick={() => onSelect(dealer.id)}>
        View Details
      </button>
    </div>
  );
}

// Container Component (logic)
function DealerList() {
  const [dealers, setDealers] = useState([]);
  const navigate = useNavigate();
  
  useEffect(() => {
    fetchDealers().then(setDealers);
  }, []);
  
  const handleSelect = (id) => {
    navigate(`/dealer/${id}`);
  };
  
  return (
    <div>
      {dealers.map(dealer => (
        <DealerCard 
          key={dealer.id}
          dealer={dealer}
          onSelect={handleSelect}
        />
      ))}
    </div>
  );
}
```

### 2. Custom Hooks Pattern

Extract reusable logic:

```javascript
// Custom hook
function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    fetch(url)
      .then(response => response.json())
      .then(data => {
        setData(data);
        setLoading(false);
      })
      .catch(error => {
        setError(error);
        setLoading(false);
      });
  }, [url]);
  
  return { data, loading, error };
}

// Usage
function Dealers() {
  const { data, loading, error } = useFetch('/api/dealers');
  
  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  
  return <div>{/* Render dealers */}</div>;
}
```

### 3. Compound Components Pattern

Related components that work together:

```javascript
function Select({ children, value, onChange }) {
  return (
    <select value={value} onChange={e => onChange(e.target.value)}>
      {children}
    </select>
  );
}

Select.Option = function SelectOption({ value, children }) {
  return <option value={value}>{children}</option>;
};

// Usage
<Select value={state} onChange={setState}>
  <Select.Option value="CA">California</Select.Option>
  <Select.Option value="TX">Texas</Select.Option>
  <Select.Option value="NY">New York</Select.Option>
</Select>
```

### 4. Render Props Pattern

Share code using a prop whose value is a function:

```javascript
class DataProvider extends React.Component {
  state = { data: null, loading: true };
  
  componentDidMount() {
    fetch(this.props.url)
      .then(response => response.json())
      .then(data => this.setState({ data, loading: false }));
  }
  
  render() {
    return this.props.children(this.state);
  }
}

// Usage
<DataProvider url="/api/dealers">
  {({ data, loading }) => (
    loading ? <Spinner /> : <DealerList dealers={data} />
  )}
</DataProvider>
```

### 5. Higher-Order Components (HOC)

Wrap components to add functionality:

```javascript
function withAuth(Component) {
  return function AuthenticatedComponent(props) {
    const username = sessionStorage.getItem('username');
    
    if (!username) {
      return <Navigate to="/login" />;
    }
    
    return <Component {...props} username={username} />;
  };
}

// Usage
const ProtectedDashboard = withAuth(Dashboard);
```

## API Design Patterns

### 1. RESTful URL Structure

Consistent, predictable URLs:

```
GET    /api/dealers              # List all dealers
GET    /api/dealers/:id          # Get specific dealer
POST   /api/dealers              # Create dealer
PUT    /api/dealers/:id          # Update dealer
DELETE /api/dealers/:id          # Delete dealer

GET    /api/dealers/:id/reviews  # Get reviews for dealer
POST   /api/dealers/:id/reviews  # Add review to dealer
```

### 2. JSON Response Format

Consistent response structure:

```python
# Success
{
    "success": true,
    "data": {
        "id": 1,
        "name": "Dealer Name"
    }
}

# Error
{
    "success": false,
    "error": {
        "code": "DEALER_NOT_FOUND",
        "message": "Dealer with ID 123 does not exist"
    }
}

# List with pagination
{
    "success": true,
    "data": [...],
    "pagination": {
        "page": 1,
        "per_page": 20,
        "total": 150,
        "pages": 8
    }
}
```

### 3. API Versioning

```
# URL versioning
/api/v1/dealers
/api/v2/dealers

# Header versioning
Accept: application/vnd.api+json; version=1
```

### 4. Error Handling

```python
from rest_framework import status
from rest_framework.response import Response

def get_dealer(request, dealer_id):
    try:
        dealer = Dealer.objects.get(id=dealer_id)
        return Response({
            'success': True,
            'data': DealerSerializer(dealer).data
        })
    except Dealer.DoesNotExist:
        return Response({
            'success': False,
            'error': {
                'code': 'NOT_FOUND',
                'message': f'Dealer {dealer_id} not found'
            }
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({
            'success': False,
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'An unexpected error occurred'
            }
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
```

## Database Patterns

### 1. N+1 Query Problem

```python
# ❌ Bad: N+1 queries
dealers = Dealer.objects.all()
for dealer in dealers:
    reviews = dealer.reviews.all()  # Additional query per dealer!

# ✅ Good: Use select_related / prefetch_related
dealers = Dealer.objects.prefetch_related('reviews').all()
for dealer in dealers:
    reviews = dealer.reviews.all()  # No additional query
```

### 2. Soft Delete Pattern

```python
class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

class BaseModel(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    objects = SoftDeleteManager()
    all_objects = models.Manager()  # Include deleted
    
    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()
    
    class Meta:
        abstract = True
```

### 3. Timestamp Mixin

```python
class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Dealer(TimestampMixin):
    name = models.CharField(max_length=200)
    # Automatically gets created_at and updated_at
```

## Security Patterns

### 1. Input Validation

```python
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    
    def clean(self):
        if self.rating < 1 or self.rating > 5:
            raise ValidationError('Rating must be between 1 and 5')
```

### 2. SQL Injection Prevention

```python
# ❌ Bad: String formatting (SQL injection risk)
query = f"SELECT * FROM dealers WHERE name = '{user_input}'"

# ✅ Good: Parameterized queries
Dealer.objects.filter(name=user_input)

# ✅ Good: Raw SQL with params
from django.db import connection
cursor = connection.cursor()
cursor.execute("SELECT * FROM dealers WHERE name = %s", [user_input])
```

### 3. XSS Prevention

```javascript
// React automatically escapes content in JSX
function Comment({ text }) {
  return <div>{text}</div>;  // Safe - auto-escaped
}

// ❌ Dangerous: dangerouslySetInnerHTML
function Comment({ html }) {
  return <div dangerouslySetInnerHTML={{ __html: html }} />;
}

// ✅ Better: Sanitize first
import DOMPurify from 'dompurify';

function Comment({ html }) {
  const sanitized = DOMPurify.sanitize(html);
  return <div dangerouslySetInnerHTML={{ __html: sanitized }} />;
}
```

## Testing Patterns

### 1. AAA Pattern (Arrange-Act-Assert)

```python
def test_dealer_creation():
    # Arrange
    data = {
        'name': 'Test Dealer',
        'city': 'Austin',
        'state': 'TX'
    }
    
    # Act
    dealer = Dealer.objects.create(**data)
    
    # Assert
    assert dealer.name == 'Test Dealer'
    assert dealer.city == 'Austin'
    assert Dealer.objects.count() == 1
```

### 2. Test Fixtures

```python
import pytest

@pytest.fixture
def sample_dealer():
    return Dealer.objects.create(
        name='Test Dealer',
        city='Austin',
        state='TX'
    )

def test_dealer_reviews(sample_dealer):
    review = Review.objects.create(
        dealer=sample_dealer,
        text='Great service'
    )
    assert review.dealer == sample_dealer
```

### 3. Mock External Services

```python
from unittest.mock import patch

@patch('myapp.services.analyze_sentiment')
def test_review_creation(mock_sentiment):
    # Mock the sentiment service
    mock_sentiment.return_value = 'positive'
    
    review = create_review(text='Great!')
    assert review.sentiment == 'positive'
    mock_sentiment.assert_called_once_with('Great!')
```

## Code Organization Patterns

### 1. Django Project Structure

```
project/
├── manage.py
├── project/              # Project settings
│   ├── __init__.py
│   ├── settings/
│   │   ├── base.py       # Common settings
│   │   ├── dev.py        # Development
│   │   └── prod.py       # Production
│   ├── urls.py
│   └── wsgi.py
├── apps/                 # Django apps
│   ├── dealers/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── services.py   # Business logic
│   │   └── tests/
│   └── reviews/
│       └── ...
└── common/               # Shared utilities
    ├── mixins.py
    └── validators.py
```

### 2. React Project Structure

```
src/
├── components/           # Presentational components
│   ├── Button/
│   │   ├── Button.jsx
│   │   ├── Button.test.js
│   │   └── Button.css
│   └── Card/
├── containers/           # Container components
│   ├── DealerList/
│   └── DealerDetail/
├── hooks/                # Custom hooks
│   ├── useFetch.js
│   └── useAuth.js
├── services/             # API calls
│   └── api.js
├── utils/                # Utilities
│   └── formatters.js
├── App.js
└── index.js
```

## Performance Patterns

### 1. Database Indexing

```python
class Dealer(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    state = models.CharField(max_length=2)
    
    class Meta:
        indexes = [
            models.Index(fields=['state', 'city']),
        ]
```

### 2. React Memoization

```javascript
import React, { useMemo, useCallback } from 'react';

function ExpensiveComponent({ data }) {
  // Memoize expensive calculation
  const processedData = useMemo(() => {
    return data.map(item => expensiveOperation(item));
  }, [data]);
  
  // Memoize callback
  const handleClick = useCallback(() => {
    doSomething();
  }, []);
  
  return <div>{/* render */}</div>;
}
```

### 3. Lazy Loading

```javascript
import React, { lazy, Suspense } from 'react';

const DealerDetail = lazy(() => import('./DealerDetail'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <DealerDetail />
    </Suspense>
  );
}
```
