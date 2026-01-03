# Interview Assessment Rubrics

This document provides rubrics for evaluating interview responses related to the IBM Full Stack Cloud Developer certificate program.

## How to Use These Rubrics

Rubrics help assess the quality and completeness of interview answers. Each rubric includes:
- **Topic**: The subject being evaluated
- **Levels**: Beginner, Intermediate, Advanced, Expert
- **Criteria**: What defines each level
- **Example**: Sample response at each level

## General Full-Stack Development

### Topic: Explaining Technical Architecture

#### Beginner Level
- **Criteria**: Can describe basic components (frontend, backend, database)
- **Example**: "A full-stack app has a React frontend that talks to a Django backend, which stores data in a database."
- **Score**: 1-2/5

#### Intermediate Level  
- **Criteria**: Explains data flow and interactions between components
- **Example**: "The React frontend makes HTTP requests to Django REST API endpoints. Django processes requests, queries PostgreSQL using the ORM, and returns JSON responses. The frontend updates the UI based on the response."
- **Score**: 3/5

#### Advanced Level
- **Criteria**: Includes design patterns, security considerations, and scalability
- **Example**: "We use MVC pattern with Django handling backend logic. The architecture includes: React SPA for UI, Django REST API with JWT authentication, PostgreSQL with read replicas, Redis for caching, Docker containers deployed on Kubernetes for scalability. CORS is configured for cross-origin requests, and we use HTTPS with proper CSP headers."
- **Score**: 4/5

#### Expert Level
- **Criteria**: Discusses trade-offs, alternatives, and real-world production concerns
- **Example**: "The architecture balances simplicity and scalability. We chose Django over Flask for its batteries-included ORM and admin interface, though it has higher overhead. React's component model enables code reuse. We could use GraphQL instead of REST for more flexible queries, but REST is simpler for our use case. Production includes load balancers, monitoring with Prometheus, and CI/CD via GitHub Actions. Database migrations are versioned and deployed with zero downtime using blue-green deployments."
- **Score**: 5/5

---

## React Development

### Topic: Understanding React Hooks

#### Beginner Level
- Can name basic hooks (useState, useEffect)
- **Example**: "useState lets you add state to functional components."
- **Score**: 1-2/5

#### Intermediate Level
- Explains when and how to use hooks correctly
- **Example**: "useState manages component state. useEffect handles side effects like API calls, running after render. The dependency array controls when useEffect runs - empty array means once on mount."
- **Score**: 3/5

#### Advanced Level
- Discusses optimization and custom hooks
- **Example**: "Beyond useState/useEffect, useCallback memoizes functions to prevent unnecessary re-renders. useMemo memoizes expensive computations. Custom hooks extract reusable logic, like useFetch for data fetching. Dependencies must be carefully managed to avoid stale closures."
- **Score**: 4/5

#### Expert Level
- Deep understanding of hook internals and edge cases
- **Example**: "Hooks rely on call order (why they can't be conditional). useEffect cleanup functions prevent memory leaks from subscriptions. useLayoutEffect runs synchronously after DOM mutations, useful for measuring elements. useReducer is better than multiple useState for complex state logic. React 18's useDeferredValue and useTransition handle concurrent rendering for better UX."
- **Score**: 5/5

---

## Django Development

### Topic: Django ORM and Database Queries

#### Beginner Level
- Can perform basic CRUD operations
- **Example**: "User.objects.all() gets all users. User.objects.create() makes a new user."
- **Score**: 1-2/5

#### Intermediate Level
- Uses filtering, ordering, and relationships
- **Example**: "User.objects.filter(is_active=True).order_by('-date_joined') gets active users newest first. user.posts.all() gets related posts via foreign key."
- **Score**: 3/5

#### Advanced Level
- Optimizes queries and understands N+1 problem
- **Example**: "Use select_related() for foreign keys and prefetch_related() for many-to-many to avoid N+1 queries. Query performance can be checked with .explain(). Aggregations like Count and Avg are database-level. Indexes on filtered/ordered fields improve performance."
- **Score**: 4/5

#### Expert Level
- Handles complex queries, transactions, and database design
- **Example**: "Complex queries use Q objects for OR logic and F objects for field comparisons. Transactions ensure atomicity with atomic() decorator. Database constraints (unique_together, check constraints) enforce data integrity. Partitioning large tables improves query speed. Raw SQL for complex analytics while using ORM for standard CRUD. Connection pooling and query analysis tools like Django Debug Toolbar for optimization."
- **Score**: 5/5

---

## DevOps & Deployment

### Topic: Kubernetes Deployment

#### Beginner Level
- Understands basic concepts
- **Example**: "Kubernetes runs containers. Pods are containers that work together."
- **Score**: 1-2/5

#### Intermediate Level
- Can deploy applications and configure services
- **Example**: "A Deployment manages pods with desired replica count. Services expose pods to network traffic. kubectl apply deploys manifests. ConfigMaps and Secrets manage configuration."
- **Score**: 3/5

#### Advanced Level
- Implements monitoring, scaling, and troubleshooting
- **Example**: "HorizontalPodAutoscaler scales based on CPU/memory. Liveness and readiness probes ensure healthy pods. Rolling updates enable zero-downtime deploys. Ingress manages external access. kubectl logs and describe for debugging. Resource limits prevent pods from consuming too much."
- **Score**: 4/5

#### Expert Level
- Designs production-grade clusters with HA and security
- **Example**: "Production requires multi-zone clusters for high availability. Network policies restrict pod-to-pod communication. RBAC controls access. StatefulSets for databases with persistent volumes. Helm charts for complex deployments. Service mesh (Istio) for observability and traffic management. Cluster autoscaler adjusts node count. Cert-manager for TLS certificates. GitOps with ArgoCD for declarative deployments. Cost optimization with spot instances and resource quotas."
- **Score**: 5/5

---

## API Design

### Topic: RESTful API Best Practices

#### Beginner Level
- Uses HTTP methods correctly
- **Example**: "GET retrieves data, POST creates new data, DELETE removes data."
- **Score**: 1-2/5

#### Intermediate Level
- Implements proper status codes and error handling
- **Example**: "Return 200 for success, 201 for created, 404 for not found, 400 for bad request, 500 for server errors. Consistent JSON error format with error codes and messages."
- **Score**: 3/5

#### Advanced Level
- Versioning, pagination, and authentication
- **Example**: "API versioning via URL (/v1/, /v2/) or headers. Pagination with limit/offset or cursor-based. JWT authentication with refresh tokens. Rate limiting to prevent abuse. HATEOAS links for discoverability. Proper CORS configuration."
- **Score**: 4/5

#### Expert Level
- Performance, security, and production patterns
- **Example**: "ETags for conditional requests and caching. Partial responses with field selection. Batch operations reduce roundtrips. Idempotency keys for safe retries. OAuth 2.0 for third-party access. API gateway for rate limiting, authentication, and monitoring. OpenAPI/Swagger documentation. Backwards compatibility strategies. Webhook notifications for events. GraphQL as alternative for complex queries. API analytics for usage patterns."
- **Score**: 5/5

---

## Problem-Solving & Debugging

### Topic: Debugging Production Issues

#### Beginner Level
- Can check logs and error messages
- **Example**: "Look at server logs to see what error occurred."
- **Score**: 1-2/5

#### Intermediate Level
- Systematic approach with common tools
- **Example**: "Check application logs, database logs, and browser console. Reproduce the issue locally. Use debugger breakpoints. Check recent code changes. Verify environment variables and configuration."
- **Score**: 3/5

#### Advanced Level
- Uses monitoring and traces complex issues
- **Example**: "Monitor metrics (CPU, memory, request rate). Distributed tracing shows request flow through services. Log aggregation (ELK) for pattern analysis. Profile performance bottlenecks. Rollback if deployment-related. Check database query performance. Network issues via ping/traceroute."
- **Score**: 4/5

#### Expert Level
- Proactive monitoring and incident response
- **Example**: "Observability with metrics (Prometheus), logs (Loki), and traces (Jaeger). Alerts on SLOs. Incident runbooks for common issues. Chaos engineering to test resilience. Root cause analysis (5 whys). Post-mortems for learning. Circuit breakers prevent cascading failures. Feature flags for quick rollback. Canary deployments minimize blast radius. On-call rotation and escalation procedures."
- **Score**: 5/5

---

## General Assessment Guidelines

### Communication
- **Clear**: Explains concepts without unnecessary jargon
- **Structured**: Logical flow from problem to solution
- **Concise**: Answers the question without rambling
- **Accurate**: Technically correct information

### Depth
- **Beginner**: Basic understanding, needs guidance
- **Intermediate**: Can work independently on common tasks
- **Advanced**: Solves complex problems, mentors others
- **Expert**: Designs systems, makes architectural decisions

### Red Flags
- ❌ Can't explain their own code
- ❌ Blames tools instead of understanding limitations
- ❌ No awareness of trade-offs
- ❌ Memorized answers without understanding
- ❌ Can't give examples from experience

### Green Flags
- ✅ Asks clarifying questions
- ✅ Admits knowledge gaps honestly
- ✅ Explains thought process
- ✅ Mentions alternatives and trade-offs
- ✅ Gives real-world examples
- ✅ Shows continuous learning mindset

---

## Using Rubrics in Interviews

1. **Prepare**: Review role requirements and skills needed
2. **Ask**: Pose open-ended questions that allow depth
3. **Listen**: Let candidate demonstrate knowledge level
4. **Probe**: Ask follow-up questions to gauge understanding
5. **Evaluate**: Compare response to rubric criteria
6. **Score**: Use rubric level (Beginner/Intermediate/Advanced/Expert)
7. **Decide**: Aggregate scores across topics for hiring decision

## References

- These rubrics map to skills in `data/skills-taxonomy.json`
- Interview questions in `data/question-bank/`
- KB content provides expected knowledge per course
