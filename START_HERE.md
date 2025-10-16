# 🚀 START HERE - Your First Steps

Welcome to your AI Knowledge Workflow Assistant project! Follow these steps to get started.

---

## 📍 You Are Here

```
✅ Project setup complete
✅ All files created
✅ Documentation ready
👉 Next: Get it running!
```

---

## ⚡ 5-Minute Quick Start

### Step 1: Add Your OpenAI API Key (Required)

1. Open `backend/.env` (it was created from the example)
2. Find this line:
   ```
   OPENAI_API_KEY=your-openai-api-key-here
   ```
3. Replace with your actual key:
   ```
   OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx
   ```
4. Get a key here if you don't have one: https://platform.openai.com/api-keys

### Step 2: Start the Databases

```bash
docker-compose up -d postgres mongodb redis
```

Wait ~30 seconds for databases to be ready.

### Step 3: Start the Backend

**Terminal 1:**
```bash
cd backend
python -m venv venv

# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Step 4: Start the Frontend

**Terminal 2:**
```bash
cd frontend
npm install
npm run dev
```

### Step 5: Verify It Works

1. **Backend API:** http://localhost:8000/docs
2. **Frontend:** http://localhost:3000
3. **Health Check:**
   ```bash
   curl http://localhost:8000/health
   ```
   Should return: `{"status":"healthy","version":"0.1.0"}`

---

## ✅ If Everything Works

**Congratulations!** You're ready to start building.

**What to do next:**
1. Read the [6-week roadmap](docs/ROADMAP.md)
2. Start with Week 1: Authentication
3. Begin coding in [backend/app/api/routes/auth.py](backend/app/api/routes/auth.py)

---

## 🔧 Alternative: Docker Everything

If you prefer to run everything in Docker:

```bash
docker-compose --profile full up -d
```

This starts all services including backend and frontend. Then access:
- Frontend: http://localhost:3000
- Backend: http://localhost:8000

---

## 🐛 Troubleshooting

### Problem: Port Already in Use

**Solution:**
```bash
# Check what's using the port
netstat -ano | findstr :8000    # Windows
lsof -i :8000                   # Mac/Linux

# Kill it or change the port in docker-compose.yml
```

### Problem: Database Connection Failed

**Solution:**
```bash
# Check if databases are running
docker-compose ps

# If not healthy, restart them
docker-compose restart postgres mongodb redis

# Check logs
docker-compose logs postgres
```

### Problem: Python Module Not Found

**Solution:**
```bash
# Make sure virtual environment is activated
# You should see (venv) in your terminal

# If not, activate it again:
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Problem: npm install fails

**Solution:**
```bash
# Clear cache and try again
cd frontend
rm -rf node_modules package-lock.json
npm cache clean --force
npm install
```

### Problem: OpenAI API Error

**Solution:**
- Make sure you added your API key to `backend/.env`
- Verify the key is valid at https://platform.openai.com/api-keys
- Make sure you have credits in your OpenAI account

---

## 📚 Documentation Guide

**Start here:**
1. [QUICKSTART.md](QUICKSTART.md) - Quick 5-minute guide
2. [CHECKLIST.md](CHECKLIST.md) - Track your progress

**Understand the project:**
3. [README.md](README.md) - Project overview
4. [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - What's been built
5. [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) - How it works

**Build features:**
6. [docs/ROADMAP.md](docs/ROADMAP.md) - 6-week development plan
7. [docs/GETTING_STARTED.md](docs/GETTING_STARTED.md) - Detailed guide

---

## 🎯 Week 1 Quick Guide

**Goal:** Build user authentication

**Backend (3-4 hours):**
1. Create Pydantic schemas for User input/output
2. Implement registration endpoint
3. Implement login endpoint with JWT
4. Add authentication middleware
5. Test with API docs at http://localhost:8000/docs

**Frontend (3-4 hours):**
1. Create login page: `frontend/app/login/page.tsx`
2. Create register page: `frontend/app/register/page.tsx`
3. Set up auth state (Zustand store)
4. Add protected route wrapper
5. Build navigation with user menu

**Files to edit:**
- `backend/app/api/routes/auth.py` - Auth endpoints
- `backend/app/schemas/` - Create user schemas (new folder)
- `frontend/app/login/page.tsx` - Login UI (create)
- `frontend/app/register/page.tsx` - Register UI (create)
- `frontend/lib/auth.ts` - Auth utilities (create)

---

## 💡 Helpful Commands

### Development
```bash
# Using Make (recommended)
make start-db      # Start databases only
make dev           # Start backend + frontend locally
make stop          # Stop all Docker services
make logs          # View Docker logs

# Manual
docker-compose up -d postgres mongodb redis    # Start DBs
docker-compose logs -f                         # Follow logs
docker-compose down                            # Stop everything
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

### Testing
```bash
# Backend tests (once you write them)
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

---

## 🌟 Project Highlights

**What makes this project great:**
- ✅ Modern tech stack (Next.js 14, FastAPI, LangChain)
- ✅ Production-ready architecture
- ✅ Complete Docker development environment
- ✅ RAG (AI search) already implemented
- ✅ Comprehensive documentation
- ✅ 6-week clear roadmap

**What you'll learn:**
- Full-stack development
- AI/ML integration (RAG, embeddings, LLMs)
- Vector databases
- Authentication & security
- Workflow automation
- DevOps & deployment

---

## 🎓 Learning Resources

### Required Reading (30 minutes)
1. [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/) - First 10 minutes
2. [Next.js Docs](https://nextjs.org/docs) - App Router section
3. [Your ROADMAP.md](docs/ROADMAP.md) - Week 1 section

### When You Need Them
- [LangChain Docs](https://python.langchain.com/docs/get_started/introduction) - For RAG (Week 2)
- [Shadcn UI](https://ui.shadcn.com/) - For UI components
- [MongoDB Vector Search](https://www.mongodb.com/docs/atlas/atlas-vector-search/) - For vector DB (Week 3)

---

## ✨ Success Checklist

**Setup (Today):**
- [ ] OpenAI API key added to `backend/.env`
- [ ] Databases running (`docker-compose ps` shows healthy)
- [ ] Backend running at http://localhost:8000
- [ ] Frontend running at http://localhost:3000
- [ ] Health check returns success

**Week 1 (This Week):**
- [ ] User can register
- [ ] User can log in
- [ ] JWT tokens work
- [ ] Protected routes functional
- [ ] Login/Register UI complete

**Week 2 (Next Week):**
- [ ] Chat interface built
- [ ] User can query AI
- [ ] RAG returns relevant answers
- [ ] Conversation history saved

---

## 🎯 Your Mission

Build an AI-powered knowledge management platform that helps teams:
- 📚 Centralize company knowledge
- 💬 Chat with documents using AI
- 🤖 Automate repetitive workflows
- 📊 Generate intelligent reports

**Timeline:** 6 weeks to MVP
**Current Status:** Week 0 complete ✅
**Next Milestone:** Authentication (Week 1)

---

## 🚀 Ready to Code?

1. ✅ Verify your setup works (steps above)
2. 📖 Read Week 1 in [docs/ROADMAP.md](docs/ROADMAP.md)
3. 💻 Open [backend/app/api/routes/auth.py](backend/app/api/routes/auth.py)
4. 🎉 Start building!

---

## 📞 Need Help?

**Quick answers:**
- Setup issues → [QUICKSTART.md](QUICKSTART.md)
- How it works → [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- What to build → [docs/ROADMAP.md](docs/ROADMAP.md)
- Task tracking → [CHECKLIST.md](CHECKLIST.md)

**API Documentation:**
- When backend is running: http://localhost:8000/docs
- Interactive API testing included!

---

## 🎊 You've Got This!

Everything is set up and ready. The foundation is solid. Now it's time to build something amazing!

**First task:** Get the setup running (steps above)
**Second task:** Read Week 1 plan
**Third task:** Write your first endpoint

**Happy coding!** 🚀

---

*Pro tip: Keep [docs/ROADMAP.md](docs/ROADMAP.md) open in a tab. It's your guide for the next 6 weeks.*
