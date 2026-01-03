# Career AI Assistant Architecture

## Overview

The Career AI Assistant is a RAG (Retrieval-Augmented Generation) powered system that helps learners navigate the IBM Full Stack Cloud Developer certificate program. It combines vector similarity search with large language models to provide accurate, citation-backed answers.

## System Components

### 1. Knowledge Base (KB)
- **Location**: `kb/`
- **Contents**: 15 courses, 166 markdown files
- **Structure**: Courses → Modules, Cheatsheets, Labs, References
- **Purpose**: Source of truth for all information

### 2. Ingestion Worker
- **Location**: `apps/worker/`
- **Technology**: Node.js/TypeScript
- **Functions**:
  - Parse markdown files from KB
  - Chunk content by headings
  - Extract skills/tags using taxonomies
  - Generate embeddings via OpenAI API
  - Store in PostgreSQL database

### 3. API Server
- **Location**: `apps/api/`
- **Technology**: Express.js + TypeScript
- **Endpoints**:
  - `/v1/search` - Vector similarity search
  - `/v1/answer` - RAG-based Q&A
  - `/v1/study-plan` - Generate personalized study plans
  - `/v1/interview-prep` - Interview question preparation

### 4. Database
- **Technology**: PostgreSQL + pgvector extension
- **Tables**:
  - `documents` - KB file metadata
  - `chunks` - Text chunks with headings
  - `embeddings` - 1536-dimensional vectors (OpenAI ada-002)
  - `tags` - Skills and topics
  - `chunk_tags` - Many-to-many relationship
  - `queries` - Query logging
  - `study_plans` - Generated plans

### 5. Web UI
- **Location**: `apps/web/`
- **Technology**: Next.js 14 + React + Tailwind CSS
- **Features**:
  - Chat interface for Q&A
  - Study plan generator
  - Interview preparation tool
  - KB browser

## Data Flow

### Ingestion Flow
```
KB Markdown Files
    ↓
Worker reads and parses
    ↓
Split into chunks by headings
    ↓
Tag with skills (using taxonomies)
    ↓
Generate embeddings (OpenAI API)
    ↓
Store in PostgreSQL
```

### Query Flow (Search)
```
User query
    ↓
Generate query embedding
    ↓
Vector similarity search (cosine)
    ↓
Retrieve top-k chunks
    ↓
Return with citations
```

### Query Flow (RAG Answer)
```
User question
    ↓
Generate question embedding
    ↓
Retrieve relevant chunks (top-k)
    ↓
Format context with citations
    ↓
Send to LLM with system prompt
    ↓
LLM generates answer
    ↓
Return answer + citations
```

### Study Plan Flow
```
User inputs (role, skills, weeks)
    ↓
Load role taxonomy
    ↓
Calculate skill gaps
    ↓
Map required skills to courses
    ↓
Use course-map.json for KB paths
    ↓
Generate weekly plan
    ↓
Return with specific module/lab paths
```

## Technology Stack

### Backend
- **Runtime**: Node.js 18+
- **Framework**: Express.js 4.x
- **Language**: TypeScript 5.x
- **Database**: PostgreSQL 15+ with pgvector
- **ORM**: pg (node-postgres)
- **Embeddings**: OpenAI API (text-embedding-ada-002)
- **Vector Search**: pgvector (cosine similarity)

### Frontend
- **Framework**: Next.js 14
- **Language**: TypeScript
- **UI**: React 18 + Tailwind CSS
- **State**: React hooks
- **HTTP**: fetch API

### Infrastructure
- **Containerization**: Docker
- **Orchestration**: Docker Compose
- **Reverse Proxy**: Nginx (production)
- **Monitoring**: (TODO: Add Prometheus/Grafana)

## Security Considerations

### API Security
- Rate limiting on all endpoints
- CORS configuration for frontend origin
- Input validation and sanitization
- SQL injection prevention (parameterized queries)
- XSS protection in UI

### Data Security
- Environment variables for secrets
- No API keys in code or logs
- Database credentials in .env files
- HTTPS in production

### AI Safety
- System prompt prevents hallucinations
- Citation verification before responses
- Rate limiting on OpenAI API calls
- Cost monitoring for embeddings

## Performance Optimization

### Database
- Indexes on frequently queried fields
- Vector index (IVFFlat) for similarity search
- Connection pooling
- Query optimization

### Caching
- (TODO) Redis cache for frequent queries
- (TODO) Embedding cache to avoid re-embedding

### API
- Response compression
- Pagination for large result sets
- Streaming for long responses (TODO)

## Scalability

### Horizontal Scaling
- Stateless API servers
- Load balancer distribution
- Database read replicas

### Vertical Scaling
- Vector index tuning (IVFFlat lists parameter)
- Batch processing for embeddings
- Connection pool sizing

## Monitoring & Observability

### Metrics (TODO)
- Query latency
- Embedding generation time
- Vector search performance
- API response times
- Error rates

### Logging
- Structured JSON logs
- Query logging for analytics
- Error tracking with stack traces

## Development Workflow

### Local Development
1. Clone repository
2. Copy `.env.example` to `.env`
3. Run `docker-compose -f docker-compose.rag.yml up`
4. Run ingestion: `npm run ingest` in worker
5. Access UI at `localhost:3000`

### Testing
- Unit tests: Jest
- Integration tests: Supertest
- E2E tests: (TODO) Playwright

### CI/CD
- (TODO) GitHub Actions workflow
- (TODO) Automated testing on PR
- (TODO) Deployment to staging/production

## Future Enhancements

### Short Term
- [ ] Implement actual API/Worker/Web code
- [ ] Add streaming responses for long answers
- [ ] Implement caching layer
- [ ] Add monitoring and metrics

### Medium Term
- [ ] Multi-user support with authentication
- [ ] Bookmark favorite KB sections
- [ ] Export study plans to calendar
- [ ] Progress tracking

### Long Term
- [ ] Support for other certificate programs
- [ ] Community-contributed KB content
- [ ] Mobile app
- [ ] Offline mode

## References

- pgvector documentation: https://github.com/pgvector/pgvector
- OpenAI embeddings: https://platform.openai.com/docs/guides/embeddings
- RAG architecture patterns: https://www.pinecone.io/learn/retrieval-augmented-generation/
- Next.js documentation: https://nextjs.org/docs
