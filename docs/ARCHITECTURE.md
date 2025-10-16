# System Architecture

## Overview

The AI Knowledge Workflow Assistant is a full-stack application designed to help teams centralize knowledge, chat with company data using AI, and automate repetitive workflows.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                         Frontend Layer                       │
│                                                              │
│  Next.js 14 + TypeScript + Tailwind + Shadcn UI            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │   Chat   │  │ Document │  │ Workflow │  │   Admin  │  │
│  │    UI    │  │  Manager │  │ Dashboard│  │   Panel  │  │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘  │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ REST API / WebSocket
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                         Backend Layer                        │
│                                                              │
│  FastAPI + Python 3.11                                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │   Auth   │  │   RAG    │  │ Workflow │  │   File   │  │
│  │  Service │  │  Service │  │  Engine  │  │ Processor│  │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘  │
└─────────────────────────────────────────────────────────────┘
                            │
                    ┌───────┴───────┐
                    ▼               ▼
┌─────────────────────────┐  ┌─────────────────────────┐
│    Data Layer           │  │   AI Layer              │
│                         │  │                         │
│  PostgreSQL             │  │  LangChain              │
│  ┌──────────────┐      │  │  ┌──────────────┐      │
│  │ Users        │      │  │  │ OpenAI API   │      │
│  │ Documents    │      │  │  │ Embeddings   │      │
│  │ Workflows    │      │  │  └──────────────┘      │
│  │ Chat History │      │  │                         │
│  └──────────────┘      │  │  Vector Store           │
│                         │  │  ┌──────────────┐      │
│  Redis                  │  │  │ MongoDB      │      │
│  ┌──────────────┐      │  │  │ or           │      │
│  │ Cache        │      │  │  │ Qdrant       │      │
│  │ Session      │      │  │  └──────────────┘      │
│  │ Queue        │      │  │                         │
│  └──────────────┘      │  └─────────────────────────┘
└─────────────────────────┘
```

## Component Details

### 1. Frontend Layer (Next.js)

**Technologies:**
- Next.js 14 (App Router)
- TypeScript
- Tailwind CSS
- Shadcn UI components
- Framer Motion for animations
- Zustand for state management
- React Query for data fetching

**Key Features:**
- Server-side rendering for SEO
- Real-time WebSocket connections
- Responsive design
- Dark/light theme support
- File upload with progress tracking

**Pages:**
- `/` - Dashboard/Home
- `/chat` - AI Chat Interface
- `/documents` - Document Management
- `/workflows` - Workflow Automation
- `/admin` - User Management (Admin only)

### 2. Backend Layer (FastAPI)

**Technologies:**
- FastAPI (Python 3.11+)
- SQLAlchemy (async ORM)
- Pydantic for validation
- JWT for authentication
- WebSockets for real-time communication

**API Structure:**
```
/api
├── /auth
│   ├── POST /login
│   ├── POST /register
│   └── POST /refresh
├── /users
│   ├── GET /me
│   ├── GET /
│   └── PUT /{id}
├── /documents
│   ├── POST /upload
│   ├── GET /
│   ├── GET /{id}
│   ├── DELETE /{id}
│   └── POST /{id}/summarize
├── /chat
│   ├── POST /query
│   ├── GET /sessions
│   ├── GET /sessions/{id}
│   └── WS /ws
└── /workflows
    ├── POST /
    ├── GET /
    ├── GET /{id}
    ├── PUT /{id}
    ├── DELETE /{id}
    └── POST /{id}/execute
```

### 3. AI Layer (LangChain + OpenAI)

**RAG Pipeline:**

1. **Document Processing:**
   - Extract text from PDF/DOCX/TXT
   - Split into chunks (1000 chars with 200 overlap)
   - Generate embeddings using OpenAI
   - Store in vector database

2. **Query Processing:**
   - Generate query embedding
   - Vector similarity search (top-k)
   - Retrieve relevant context
   - Generate answer with LLM
   - Return answer + sources

3. **Features:**
   - Semantic search
   - Context-aware responses
   - Source attribution
   - Conversation history
   - Custom prompts per department

**Vector Database Options:**

**MongoDB Atlas Vector Search:**
- Unified database for relational + vector data
- Native vector search capabilities
- Scales with Atlas
- Best for production

**Qdrant:**
- Dedicated vector search engine
- High performance
- Self-hosted option
- Best for high-volume workloads

### 4. Data Layer

**PostgreSQL:**
- User accounts and authentication
- Document metadata
- Workflow definitions
- Chat session history
- Audit logs

**Schema Design:**
```
users
├── id (PK)
├── email (unique)
├── hashed_password
├── full_name
├── role (admin/manager/user)
├── is_active
└── timestamps

documents
├── id (PK)
├── title
├── file_name
├── file_path
├── file_type
├── content (extracted text)
├── summary (AI-generated)
├── vector_id (reference)
├── owner_id (FK -> users)
└── timestamps

workflows
├── id (PK)
├── name
├── description
├── trigger_type
├── actions (JSON)
├── schedule
├── is_active
├── created_by (FK -> users)
└── timestamps

chat_sessions
├── id (PK)
├── user_id (FK -> users)
├── title
├── messages (JSON)
└── timestamps
```

**Redis:**
- Session storage
- Caching (API responses, embeddings)
- Celery task queue
- Rate limiting
- WebSocket connection management

### 5. Security

**Authentication Flow:**
1. User submits credentials
2. Backend verifies with bcrypt
3. Generate JWT token
4. Client stores token
5. Token sent in Authorization header
6. Backend validates on each request

**Authorization:**
- Role-based access control (RBAC)
- User, Manager, Admin roles
- Endpoint-level permissions
- Resource-level ownership checks

**Data Protection:**
- Password hashing with bcrypt
- JWT with expiration
- HTTPS only in production
- CORS configuration
- Input validation with Pydantic
- SQL injection prevention (ORM)

### 6. Workflow Engine

**Workflow Structure:**
```json
{
  "id": "workflow_123",
  "name": "Daily Summary",
  "trigger": {
    "type": "schedule",
    "cron": "0 9 * * *"
  },
  "actions": [
    {
      "type": "aggregate_documents",
      "params": {
        "date_range": "last_24h"
      }
    },
    {
      "type": "generate_summary",
      "params": {
        "template": "daily_summary"
      }
    },
    {
      "type": "send_email",
      "params": {
        "to": "team@company.com",
        "subject": "Daily Knowledge Summary"
      }
    }
  ]
}
```

**Trigger Types:**
- Schedule (cron)
- Document upload
- New user registration
- API webhook
- Manual execution

**Action Types:**
- Query documents
- Generate summary
- Send email
- Create report
- Update database
- Call external API

### 7. Deployment Architecture

**Development:**
```
Docker Compose
├── postgres:5432
├── mongodb:27017
├── redis:6379
├── backend:8000
└── frontend:3000
```

**Production (AWS Example):**
```
┌─────────────────────────────────────┐
│         CloudFront (CDN)            │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│      Application Load Balancer      │
└──────────────┬──────────────────────┘
               │
      ┌────────┴────────┐
      │                 │
┌─────▼─────┐    ┌─────▼─────┐
│  Frontend │    │  Backend  │
│   (ECS)   │    │   (ECS)   │
└───────────┘    └─────┬─────┘
                       │
              ┌────────┴────────┐
              │                 │
        ┌─────▼─────┐    ┌─────▼─────┐
        │    RDS    │    │ MongoDB   │
        │(Postgres) │    │  Atlas    │
        └───────────┘    └───────────┘
```

**Services:**
- Frontend: Vercel / Netlify / S3 + CloudFront
- Backend: ECS / EC2 / Railway
- Database: RDS (PostgreSQL)
- Vector Store: MongoDB Atlas
- Cache: ElastiCache (Redis)
- Storage: S3
- Monitoring: CloudWatch / DataDog

## Scalability Considerations

1. **Horizontal Scaling:**
   - Stateless backend (multiple instances)
   - Load balancer for distribution
   - Redis for shared session storage

2. **Database Scaling:**
   - Read replicas for PostgreSQL
   - Connection pooling
   - Query optimization and indexing

3. **Vector Store Scaling:**
   - MongoDB Atlas auto-scaling
   - Sharding for large collections
   - Index optimization

4. **Caching Strategy:**
   - Redis for frequently accessed data
   - CDN for static assets
   - API response caching

5. **Background Jobs:**
   - Celery for async tasks
   - Separate worker nodes
   - Priority queues

## Monitoring and Observability

1. **Logging:**
   - Structured JSON logs
   - Centralized log aggregation
   - Log levels (DEBUG, INFO, WARN, ERROR)

2. **Metrics:**
   - API response times
   - Database query performance
   - Vector search latency
   - Cache hit rates

3. **Alerting:**
   - Error rate thresholds
   - Resource utilization
   - Service health checks
   - Uptime monitoring

## Future Enhancements

1. Multi-tenancy support
2. Fine-tuned models on company data
3. Voice interface with Whisper
4. Mobile applications
5. Advanced analytics dashboard
6. Integration marketplace (Slack, Teams, etc.)
7. Custom model deployment
8. Advanced workflow DAG editor
