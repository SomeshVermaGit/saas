# Quick Start Guide

Get your AI Knowledge Workflow Assistant running in 5 minutes!

## Prerequisites Check

Before starting, make sure you have:
- ✅ Docker & Docker Compose installed
- ✅ OpenAI API key (get one at https://platform.openai.com/api-keys)

## Step 1: Environment Setup

### Windows
```cmd
setup.bat
```

### macOS/Linux
```bash
chmod +x setup.sh
./setup.sh
```

Or manually:
```bash
cp backend/.env.example backend/.env
cp frontend/.env.local.example frontend/.env.local
```

## Step 2: Add Your OpenAI API Key

Edit `backend/.env` and add your API key:
```bash
OPENAI_API_KEY=sk-your-actual-key-here
```

## Step 3: Choose Your Setup

### Option A: Quick Docker Start (Recommended for beginners)

Start everything with Docker:
```bash
docker-compose --profile full up -d
```

Access your app:
- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs

### Option B: Local Development (Recommended for development)

1. Start databases only:
```bash
docker-compose up -d postgres mongodb redis
```

2. Start backend (in one terminal):
```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

3. Start frontend (in another terminal):
```bash
cd frontend
npm install
npm run dev
```

Access your app:
- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000

## Step 4: Verify Setup

### Test Backend Health
```bash
curl http://localhost:8000/health
```

Expected response:
```json
{"status":"healthy","version":"0.1.0"}
```

### Test Frontend
Open http://localhost:3000 in your browser

### Test API Documentation
Visit http://localhost:8000/docs for interactive API docs

## Common Issues & Solutions

### Port Already in Use
```bash
# Stop existing services
docker-compose down

# Or check what's using the port
# Windows:
netstat -ano | findstr :8000

# macOS/Linux:
lsof -i :8000
```

### Database Connection Failed
```bash
# Check if databases are running
docker-compose ps

# Restart databases
docker-compose restart postgres mongodb redis
```

### Frontend Won't Start
```bash
# Clear cache and reinstall
cd frontend
rm -rf node_modules .next
npm install
npm run dev
```

### Backend Import Errors
```bash
# Make sure virtual environment is activated
# Reinstall dependencies
cd backend
pip install --upgrade pip
pip install -r requirements.txt
```

## Next Steps

Now that your environment is set up, you can:

1. **Week 1:** Implement authentication
   - See `docs/ROADMAP.md` for detailed tasks
   - Start with [backend/app/api/routes/auth.py](backend/app/api/routes/auth.py)

2. **Week 2:** Build chat interface with RAG
   - AI service is ready at [backend/app/ai/rag.py](backend/app/ai/rag.py)
   - Create chat UI components in `frontend/`

3. **Read the docs:**
   - [ARCHITECTURE.md](docs/ARCHITECTURE.md) - System design
   - [ROADMAP.md](docs/ROADMAP.md) - Development plan
   - [GETTING_STARTED.md](docs/GETTING_STARTED.md) - Detailed setup

## Useful Commands

### Using Make (if available)
```bash
make help           # Show all commands
make start-db       # Start databases
make dev            # Start local dev servers
make stop           # Stop all services
make logs           # View logs
```

### Using Docker Compose
```bash
docker-compose ps              # Check status
docker-compose logs -f         # Follow logs
docker-compose restart         # Restart services
docker-compose down            # Stop everything
docker-compose down -v         # Stop and remove volumes
```

### Database Access
```bash
# PostgreSQL
docker-compose exec postgres psql -U postgres -d ai_knowledge_db

# MongoDB
docker-compose exec mongodb mongosh

# Redis
docker-compose exec redis redis-cli
```

## Project Structure

```
saas/
├── frontend/              # Next.js frontend
│   ├── app/              # Next.js 14 app directory
│   ├── components/       # React components
│   └── lib/              # Utilities
├── backend/              # FastAPI backend
│   ├── app/
│   │   ├── api/         # API routes
│   │   ├── core/        # Config, security
│   │   ├── models/      # Database models
│   │   ├── ai/          # RAG & vector store
│   │   └── db/          # Database setup
│   └── tests/           # Backend tests
├── docs/                # Documentation
├── docker-compose.yml   # Docker setup
└── README.md           # Project overview
```

## Development Workflow

1. Create a feature branch
2. Make your changes
3. Test locally
4. Commit with descriptive messages
5. Push and create a pull request

## Getting Help

- Check the [docs/](docs/) folder for detailed guides
- Review API docs at http://localhost:8000/docs
- Look at code comments for inline documentation

## What's Already Built

✅ Project structure
✅ Docker setup
✅ Database configuration (PostgreSQL, MongoDB, Redis)
✅ FastAPI backend with route scaffolding
✅ Next.js frontend with Tailwind & Shadcn UI
✅ RAG service with LangChain
✅ Vector store abstraction (MongoDB & Qdrant)
✅ Authentication scaffolding
✅ CI/CD pipeline template

## What's Next to Build

🔲 User authentication (Week 1)
🔲 Chat interface (Week 2)
🔲 Document upload & processing (Week 3)
🔲 Workflow automation (Week 4)
🔲 Dashboard & analytics (Week 5)
🔲 Deploy & polish (Week 6)

See [docs/ROADMAP.md](docs/ROADMAP.md) for the complete plan!

---

**You're all set!** Start building your AI-powered knowledge platform. 🚀

Need help? Check the documentation or review the code comments.
