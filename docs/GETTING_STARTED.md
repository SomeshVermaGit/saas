# Getting Started Guide

## Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** 18+ and npm
- **Python** 3.11+
- **Docker** and Docker Compose
- **Git**
- **OpenAI API Key** (or use Ollama for local models)

## Quick Start (Recommended)

The fastest way to get started is using Docker Compose:

### 1. Clone and Setup

```bash
# Navigate to project directory
cd saas

# Copy environment files
cp backend/.env.example backend/.env
cp frontend/.env.local.example frontend/.env.local
```

### 2. Configure Environment Variables

Edit `backend/.env` and add your API keys:

```bash
# Required: Add your OpenAI API key
OPENAI_API_KEY=sk-your-key-here

# Optional: Choose vector database (mongodb or qdrant)
VECTOR_DB_TYPE=mongodb
```

### 3. Start Services

```bash
# Start databases only (for local development)
docker-compose up -d postgres mongodb redis

# OR start everything with Docker
docker-compose --profile full up -d
```

### 4. Access the Application

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000
- **API Documentation:** http://localhost:8000/docs
- **MongoDB:** localhost:27017
- **PostgreSQL:** localhost:5432
- **Redis:** localhost:6379

## Local Development Setup

If you prefer to run services locally without Docker:

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Run database migrations (once implemented)
# alembic upgrade head

# Start the backend
uvicorn app.main:app --reload
```

The backend will be available at http://localhost:8000

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Copy environment file
cp .env.local.example .env.local

# Start the development server
npm run dev
```

The frontend will be available at http://localhost:3000

## Database Setup

### PostgreSQL

The PostgreSQL database will be automatically created when you start Docker Compose. To connect manually:

```bash
psql -h localhost -U postgres -d ai_knowledge_db
# Password: postgres
```

### MongoDB Atlas Vector Search (Recommended for Production)

For production, we recommend using MongoDB Atlas with Vector Search:

1. Create a free account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create a new cluster
3. Enable Vector Search
4. Update `MONGODB_URL` in your `.env` file
5. Create a vector search index (instructions in docs)

### Qdrant (Alternative Vector DB)

To use Qdrant instead of MongoDB:

```bash
# Start Qdrant with Docker
docker-compose --profile qdrant up -d qdrant

# Update backend/.env
VECTOR_DB_TYPE=qdrant
```

## Testing the Setup

### 1. Check Backend Health

```bash
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "healthy",
  "version": "0.1.0"
}
```

### 2. Check API Documentation

Visit http://localhost:8000/docs to see the interactive API documentation.

### 3. Test Frontend

Open http://localhost:3000 in your browser.

## Next Steps

1. **Week 1:** Complete authentication implementation
2. **Week 2:** Implement AI chat interface with RAG
3. **Week 3:** Add document management
4. **Week 4:** Build workflow automation
5. **Week 5:** Add dashboard and analytics
6. **Week 6:** Deploy and polish

## Common Issues

### Port Already in Use

If you get a "port already in use" error:

```bash
# Check what's using the port
# Windows:
netstat -ano | findstr :8000
# macOS/Linux:
lsof -i :8000

# Kill the process or change the port in docker-compose.yml
```

### Database Connection Issues

Make sure all databases are running:

```bash
docker-compose ps
```

All services should show "healthy" status.

### Python Dependencies Issues

If you encounter issues installing Python dependencies:

```bash
# Upgrade pip
pip install --upgrade pip

# Install with verbose output
pip install -r requirements.txt -v
```

## Development Workflow

1. Create a new branch for your feature
2. Make changes
3. Run tests (when implemented)
4. Commit with descriptive messages
5. Push and create a pull request

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Next.js Documentation](https://nextjs.org/docs)
- [LangChain Documentation](https://python.langchain.com/)
- [MongoDB Atlas Vector Search](https://www.mongodb.com/docs/atlas/atlas-vector-search/)

## Getting Help

If you encounter issues:

1. Check the documentation in the `docs/` folder
2. Review the issue tracker
3. Ask in the team chat

Happy coding!
