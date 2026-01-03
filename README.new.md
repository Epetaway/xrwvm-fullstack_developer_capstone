# IBM Full Stack Cloud Developer Career AI Assistant

This repository contains **two distinct projects**:

1. **Best Cars Dealership Portal** (Original Capstone) - Django/React full-stack application
2. **Career AI Assistant** (NEW) - RAG-powered knowledge base and AI assistant for the IBM Full Stack Cloud Developer certificate program

---

## 🎓 Career AI Assistant (NEW)

An intelligent assistant that helps learners navigate the IBM Full Stack Cloud Developer certificate program using a comprehensive knowledge base and RAG (Retrieval-Augmented Generation) technology.

### Features

- **📚 Knowledge Base**: 15 courses with detailed modules, cheatsheets, labs, and references
- **🔍 Semantic Search**: Vector similarity search across all course content
- **💬 AI-Powered Q&A**: Get answers with citations to specific KB sources
- **📈 Study Plans**: Personalized learning paths based on career goals
- **🎯 Interview Prep**: Role-specific interview questions and answers
- **🚫 Citation-First**: No hallucinations - all answers cite KB sources

### Architecture

```
career-ai-assistant/
├── kb/                      # Knowledge Base (15 courses)
│   ├── STYLE_GUIDE.md
│   └── course-XX-name/
│       ├── README.md
│       ├── modules/          # 5 modules per course
│       ├── cheatsheets/      # Commands, patterns, interview Q&A
│       ├── labs/             # Hands-on exercises
│       └── references.md     # External resources
├── apps/
│   ├── api/                 # Express.js RAG API
│   ├── worker/              # KB ingestion & embeddings
│   └── web/                 # Next.js UI
├── packages/
│   └── shared/              # Shared TypeScript types
├── rag/
│   └── prompts/             # System prompts for AI
├── data/
│   ├── roles-taxonomy.json  # Career roles and requirements
│   ├── skills-taxonomy.json # Skills and course mapping
│   └── course-map.json      # Course-to-skill mapping
└── docs/                    # Architecture and guides
```

### Quick Start (Career AI Assistant)

#### Prerequisites
- Node.js 18+
- PostgreSQL with pgvector extension
- OpenAI API key
- Docker & Docker Compose (recommended)

#### Using Docker Compose (Recommended)

1. **Clone and setup**:
```bash
git clone https://github.com/Epetaway/xrwvm-fullstack_developer_capstone.git
cd xrwvm-fullstack_developer_capstone
```

2. **Configure environment**:
```bash
# Copy example files
cp apps/api/.env.example apps/api/.env
cp apps/worker/.env.example apps/worker/.env
cp apps/web/.env.example apps/web/.env

# Edit apps/api/.env and add your OpenAI API key
# OPENAI_API_KEY=sk-...
```

3. **Start all services**:
```bash
docker-compose -f docker-compose.rag.yml up -d
```

4. **Run KB ingestion** (first time only):
```bash
docker-compose -f docker-compose.rag.yml exec worker npm run ingest
```

5. **Access the application**:
- Web UI: http://localhost:3000
- API: http://localhost:3001
- Database: localhost:5432

#### Manual Setup (Without Docker)

1. **Database**:
```bash
# Install PostgreSQL with pgvector
createdb career_ai
psql career_ai < apps/api/sql/schema.sql
```

2. **API**:
```bash
cd apps/api
npm install
cp .env.example .env
# Edit .env with your DATABASE_URL and OPENAI_API_KEY
npm run dev
```

3. **Worker** (in a new terminal):
```bash
cd apps/worker
npm install
cp .env.example .env
# Edit .env with your DATABASE_URL and OPENAI_API_KEY
npm run ingest  # One-time ingestion
```

4. **Web** (in a new terminal):
```bash
cd apps/web
npm install
cp .env.example .env
npm run dev
```

### API Endpoints

#### Search
```bash
POST /v1/search
Content-Type: application/json

{
  "query": "How do I deploy a Django app to Kubernetes?",
  "limit": 10
}
```

Response includes top-k relevant chunks with citations.

#### Answer (RAG)
```bash
POST /v1/answer
Content-Type: application/json

{
  "question": "What is the difference between Docker and Kubernetes?"
}
```

Response includes synthesized answer with KB citations.

#### Study Plan
```bash
POST /v1/study-plan
Content-Type: application/json

{
  "roleId": "full-stack-developer",
  "currentSkills": ["html", "css", "javascript"],
  "weeks": 12
}
```

Returns personalized study plan with KB module paths.

#### Interview Prep
```bash
POST /v1/interview-prep
Content-Type: application/json

{
  "roleId": "backend-developer",
  "difficulty": "intermediate",
  "limit": 10
}
```

Returns interview questions with answers and KB sources.

### Knowledge Base Structure

The KB contains 15 courses matching the IBM Full Stack Cloud Developer certificate:

1. Introduction to Software Engineering
2. Introduction to Cloud Computing
3. Introduction to HTML, CSS, and JavaScript
4. Getting Started with Git and GitHub
5. Developing Front-End Apps with React
6. Developing Back-End Apps with Node.js and Express
7. Python for Data Science, AI, and Development
8. Developing AI Applications with Python and Flask
9. Django Application Development with SQL and Databases
10. Introduction to Containers: Docker, Kubernetes, and OpenShift
11. Application Development using Microservices and Serverless
12. **Full-Stack Application Development Capstone Project** ⭐ (Fully populated)
13. Full-Stack Software Developer Assessment
14. Generative AI: Elevate Your Software Development Career
15. Software Developer Career Guide and Interview Preparation

**Course 12** is fully populated with comprehensive content based on this repository's Django/React capstone project.

Courses 1-11, 13-15 have template structures ready for content population.

### Validation Checklist

- [ ] DB boots: `docker-compose -f docker-compose.rag.yml ps`
- [ ] Schema applied: `docker-compose -f docker-compose.rag.yml exec db psql -U postgres -d career_ai -c "\dt"`
- [ ] Worker ingests KB: `docker-compose -f docker-compose.rag.yml logs worker`
- [ ] /v1/search returns results: `curl -X POST http://localhost:3001/v1/search -H "Content-Type: application/json" -d '{"query":"Django"}'`
- [ ] /v1/answer returns citations: `curl -X POST http://localhost:3001/v1/answer -H "Content-Type: application/json" -d '{"question":"What is Django?"}'`
- [ ] Study plan returns KB paths
- [ ] Interview prep returns questions with sources

---

## 🚗 Best Cars Dealership Portal (Original Capstone)

The original full-stack capstone project demonstrating Django backend, React frontend, and cloud deployment.

### Features
- Dealer directory with state filtering
- User authentication (login/register)
- Review submission with AI sentiment analysis
- Microservices architecture
- Cloud deployment (OpenShift/Kubernetes)

### Tech Stack
- **Backend**: Django 4.0, Python 3.13
- **Frontend**: React 18.2, React Router 6.19
- **Database**: SQLite (dev), PostgreSQL (prod)
- **Services**: Node.js (dealers), Flask (sentiment)
- **Deployment**: Docker, Kubernetes, OpenShift

### Quick Start (Dealership App)

1. **Install dependencies**:
```bash
cd server
pip install -r requirements.txt
cd frontend
npm install
```

2. **Database setup**:
```bash
cd server
python manage.py migrate
python manage.py createsuperuser
```

3. **Run development servers**:
```bash
# Terminal 1: Django backend
cd server
python manage.py runserver

# Terminal 2: React frontend
cd server/frontend
npm start
```

4. **Access**:
- Django app: http://localhost:8000
- React dev server: http://localhost:3000
- Admin panel: http://localhost:8000/admin

### Authentication
- Superuser: admin / admin123
- Test user: testuser2025 / Test123!

### Project Structure (Dealership)
```
server/
├── djangoapp/           # Main Django app
├── djangoproj/          # Project settings
├── frontend/            # React application
│   ├── src/
│   │   └── components/
│   └── build/           # Production build
├── database/            # MongoDB service
├── manage.py
└── requirements.txt
```

### Deployment

See `server/artifacts/` for deployment outputs and screenshots.

Docker deployment:
```bash
cd server
docker build -t dealership-app .
docker run -p 8000:8000 dealership-app
```

Kubernetes deployment:
```bash
kubectl apply -f server/deployment.yaml
kubectl apply -f server/service.yaml
```

---

## 📋 Repository Structure

```
xrwvm-fullstack_developer_capstone/
├── kb/                          # Career AI KB (166 files)
├── apps/                        # Career AI services
├── rag/                         # RAG prompts
├── data/                        # Taxonomies and data
├── docs/                        # Documentation
├── server/                      # Django/React dealership app
├── docker-compose.rag.yml       # Career AI services
├── server/database/docker-compose.yml  # Dealership services
└── README.md
```

## 🤝 Contributing

### Knowledge Base
See `kb/STYLE_GUIDE.md` for KB contribution guidelines:
- No plagiarism or verbatim Coursera content
- Always paraphrase and cite sources
- Follow file naming conventions
- Include practical examples and career notes

### Code
- Follow existing code style
- Write tests for new features
- Update documentation
- Submit PRs with clear descriptions

## 📝 License

This project is licensed under the Apache License 2.0 - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- IBM Full Stack Cloud Developer certificate program
- Django, React, and all open-source dependencies
- OpenAI for embeddings API
- pgvector for vector similarity search

## 📞 Support

For issues or questions:
- Open a GitHub issue
- Check existing documentation in `docs/`
- Review KB style guide: `kb/STYLE_GUIDE.md`

---

**Note**: This repository contains educational content paraphrased from publicly available sources. It does not include copyrighted Coursera materials. For official IBM Full Stack Cloud Developer certificate content, visit:
https://www.coursera.org/professional-certificates/ibm-full-stack-cloud-developer
