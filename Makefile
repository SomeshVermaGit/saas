# AI Knowledge Workflow Assistant - Makefile

.PHONY: help setup start-db start-all stop logs clean test install dev

# Default target
help:
	@echo "AI Knowledge Workflow Assistant - Available Commands"
	@echo ""
	@echo "Setup:"
	@echo "  make setup        - Initialize project (create .env files)"
	@echo "  make install      - Install all dependencies"
	@echo ""
	@echo "Development:"
	@echo "  make dev          - Start development servers (local)"
	@echo "  make start-db     - Start databases only"
	@echo "  make start-all    - Start all services with Docker"
	@echo "  make stop         - Stop all Docker services"
	@echo "  make restart      - Restart all services"
	@echo ""
	@echo "Utilities:"
	@echo "  make logs         - View Docker logs"
	@echo "  make logs-backend - View backend logs"
	@echo "  make logs-frontend- View frontend logs"
	@echo "  make ps           - Show running containers"
	@echo "  make shell-backend- Open backend shell"
	@echo ""
	@echo "Database:"
	@echo "  make db-migrate   - Run database migrations"
	@echo "  make db-shell     - Open PostgreSQL shell"
	@echo "  make mongo-shell  - Open MongoDB shell"
	@echo ""
	@echo "Testing:"
	@echo "  make test         - Run all tests"
	@echo "  make test-backend - Run backend tests"
	@echo "  make test-frontend- Run frontend tests"
	@echo ""
	@echo "Clean:"
	@echo "  make clean        - Remove containers and volumes"
	@echo "  make clean-all    - Clean everything including node_modules"

# Setup
setup:
	@echo "Setting up environment files..."
	@test -f backend/.env || cp backend/.env.example backend/.env
	@test -f frontend/.env.local || cp frontend/.env.local.example frontend/.env.local
	@echo "✓ Environment files created"
	@echo "⚠ Remember to add your OPENAI_API_KEY in backend/.env"

# Install dependencies
install:
	@echo "Installing backend dependencies..."
	cd backend && pip install -r requirements.txt
	@echo "Installing frontend dependencies..."
	cd frontend && npm install
	@echo "✓ All dependencies installed"

# Development
dev:
	@echo "Starting development servers..."
	@echo "Make sure databases are running: make start-db"
	@echo ""
	@echo "Starting backend on http://localhost:8000"
	@echo "Starting frontend on http://localhost:3000"
	@echo ""
	@trap 'kill 0' INT; \
	cd backend && uvicorn app.main:app --reload & \
	cd frontend && npm run dev & \
	wait

start-db:
	@echo "Starting databases..."
	docker-compose up -d postgres mongodb redis
	@echo "✓ Databases started"
	@echo "  - PostgreSQL: localhost:5432"
	@echo "  - MongoDB: localhost:27017"
	@echo "  - Redis: localhost:6379"

start-all:
	@echo "Starting all services..."
	docker-compose --profile full up -d
	@echo "✓ All services started"
	@echo "  - Frontend: http://localhost:3000"
	@echo "  - Backend: http://localhost:8000"
	@echo "  - API Docs: http://localhost:8000/docs"

stop:
	@echo "Stopping services..."
	docker-compose down
	@echo "✓ Services stopped"

restart:
	@echo "Restarting services..."
	docker-compose restart
	@echo "✓ Services restarted"

# Logs
logs:
	docker-compose logs -f

logs-backend:
	docker-compose logs -f backend

logs-frontend:
	docker-compose logs -f frontend

ps:
	docker-compose ps

shell-backend:
	docker-compose exec backend /bin/bash

# Database
db-migrate:
	@echo "Running database migrations..."
	cd backend && alembic upgrade head
	@echo "✓ Migrations complete"

db-shell:
	docker-compose exec postgres psql -U postgres -d ai_knowledge_db

mongo-shell:
	docker-compose exec mongodb mongosh

# Testing
test: test-backend test-frontend

test-backend:
	@echo "Running backend tests..."
	cd backend && pytest

test-frontend:
	@echo "Running frontend tests..."
	cd frontend && npm test

# Linting
lint-backend:
	@echo "Linting backend..."
	cd backend && black . && flake8

lint-frontend:
	@echo "Linting frontend..."
	cd frontend && npm run lint

# Clean
clean:
	@echo "Cleaning up Docker containers and volumes..."
	docker-compose down -v
	@echo "✓ Cleaned"

clean-all: clean
	@echo "Removing node_modules and Python cache..."
	rm -rf frontend/node_modules
	rm -rf frontend/.next
	rm -rf backend/__pycache__
	rm -rf backend/**/__pycache__
	rm -rf backend/.pytest_cache
	@echo "✓ Deep clean complete"

# Production
build:
	@echo "Building Docker images..."
	docker-compose build

deploy:
	@echo "Deploying to production..."
	@echo "⚠ Make sure you've set production environment variables"
	@echo "This is a placeholder - configure for your deployment platform"
