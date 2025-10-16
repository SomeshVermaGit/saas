#!/bin/bash

# AI Knowledge Workflow Assistant - Quick Setup Script

set -e

echo "=================================="
echo "AI Knowledge Workflow Assistant"
echo "Quick Setup Script"
echo "=================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo -e "${RED}Error: Docker is not installed.${NC}"
    echo "Please install Docker from https://www.docker.com/get-started"
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo -e "${RED}Error: Docker Compose is not installed.${NC}"
    echo "Please install Docker Compose"
    exit 1
fi

echo -e "${GREEN}✓ Docker and Docker Compose are installed${NC}"
echo ""

# Create environment files if they don't exist
if [ ! -f backend/.env ]; then
    echo -e "${YELLOW}Creating backend/.env from example...${NC}"
    cp backend/.env.example backend/.env
    echo -e "${GREEN}✓ Created backend/.env${NC}"
    echo -e "${YELLOW}⚠ Remember to add your OPENAI_API_KEY in backend/.env${NC}"
else
    echo -e "${GREEN}✓ backend/.env already exists${NC}"
fi

if [ ! -f frontend/.env.local ]; then
    echo -e "${YELLOW}Creating frontend/.env.local from example...${NC}"
    cp frontend/.env.local.example frontend/.env.local
    echo -e "${GREEN}✓ Created frontend/.env.local${NC}"
else
    echo -e "${GREEN}✓ frontend/.env.local already exists${NC}"
fi

echo ""
echo "=================================="
echo "Starting Services"
echo "=================================="
echo ""

# Ask user what to start
echo "What would you like to start?"
echo "1) Databases only (for local development)"
echo "2) Everything with Docker"
echo "3) Exit"
read -p "Enter your choice (1-3): " choice

case $choice in
    1)
        echo ""
        echo -e "${YELLOW}Starting databases...${NC}"
        docker-compose up -d postgres mongodb redis
        echo ""
        echo -e "${GREEN}✓ Databases started!${NC}"
        echo ""
        echo "Services running:"
        echo "  - PostgreSQL: localhost:5432"
        echo "  - MongoDB: localhost:27017"
        echo "  - Redis: localhost:6379"
        echo ""
        echo "Next steps:"
        echo "  1. Add your OPENAI_API_KEY to backend/.env"
        echo "  2. cd backend && pip install -r requirements.txt"
        echo "  3. cd backend && uvicorn app.main:app --reload"
        echo "  4. In another terminal: cd frontend && npm install && npm run dev"
        ;;
    2)
        echo ""
        echo -e "${YELLOW}Starting all services...${NC}"
        docker-compose --profile full up -d
        echo ""
        echo -e "${GREEN}✓ All services started!${NC}"
        echo ""
        echo "Services running:"
        echo "  - Frontend: http://localhost:3000"
        echo "  - Backend: http://localhost:8000"
        echo "  - API Docs: http://localhost:8000/docs"
        echo "  - PostgreSQL: localhost:5432"
        echo "  - MongoDB: localhost:27017"
        echo "  - Redis: localhost:6379"
        echo ""
        echo "View logs: docker-compose logs -f"
        ;;
    3)
        echo "Exiting..."
        exit 0
        ;;
    *)
        echo -e "${RED}Invalid choice${NC}"
        exit 1
        ;;
esac

echo ""
echo "=================================="
echo "Setup Complete!"
echo "=================================="
echo ""
echo "Useful commands:"
echo "  - View logs: docker-compose logs -f"
echo "  - Stop services: docker-compose down"
echo "  - Restart services: docker-compose restart"
echo "  - Check status: docker-compose ps"
echo ""
echo "Happy coding!"
