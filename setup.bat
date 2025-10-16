@echo off
REM AI Knowledge Workflow Assistant - Quick Setup Script for Windows

echo ==================================
echo AI Knowledge Workflow Assistant
echo Quick Setup Script
echo ==================================
echo.

REM Check if Docker is installed
docker --version >nul 2>&1
if errorlevel 1 (
    echo Error: Docker is not installed.
    echo Please install Docker from https://www.docker.com/get-started
    exit /b 1
)

REM Check if Docker Compose is installed
docker-compose --version >nul 2>&1
if errorlevel 1 (
    echo Error: Docker Compose is not installed.
    exit /b 1
)

echo [OK] Docker and Docker Compose are installed
echo.

REM Create environment files if they don't exist
if not exist backend\.env (
    echo Creating backend\.env from example...
    copy backend\.env.example backend\.env >nul
    echo [OK] Created backend\.env
    echo [WARNING] Remember to add your OPENAI_API_KEY in backend\.env
) else (
    echo [OK] backend\.env already exists
)

if not exist frontend\.env.local (
    echo Creating frontend\.env.local from example...
    copy frontend\.env.local.example frontend\.env.local >nul
    echo [OK] Created frontend\.env.local
) else (
    echo [OK] frontend\.env.local already exists
)

echo.
echo ==================================
echo Starting Services
echo ==================================
echo.

echo What would you like to start?
echo 1) Databases only (for local development)
echo 2) Everything with Docker
echo 3) Exit
set /p choice="Enter your choice (1-3): "

if "%choice%"=="1" goto databases
if "%choice%"=="2" goto full
if "%choice%"=="3" goto end
echo Invalid choice
exit /b 1

:databases
echo.
echo Starting databases...
docker-compose up -d postgres mongodb redis
echo.
echo [OK] Databases started!
echo.
echo Services running:
echo   - PostgreSQL: localhost:5432
echo   - MongoDB: localhost:27017
echo   - Redis: localhost:6379
echo.
echo Next steps:
echo   1. Add your OPENAI_API_KEY to backend\.env
echo   2. cd backend ^&^& pip install -r requirements.txt
echo   3. cd backend ^&^& uvicorn app.main:app --reload
echo   4. In another terminal: cd frontend ^&^& npm install ^&^& npm run dev
goto finish

:full
echo.
echo Starting all services...
docker-compose --profile full up -d
echo.
echo [OK] All services started!
echo.
echo Services running:
echo   - Frontend: http://localhost:3000
echo   - Backend: http://localhost:8000
echo   - API Docs: http://localhost:8000/docs
echo   - PostgreSQL: localhost:5432
echo   - MongoDB: localhost:27017
echo   - Redis: localhost:6379
echo.
echo View logs: docker-compose logs -f
goto finish

:finish
echo.
echo ==================================
echo Setup Complete!
echo ==================================
echo.
echo Useful commands:
echo   - View logs: docker-compose logs -f
echo   - Stop services: docker-compose down
echo   - Restart services: docker-compose restart
echo   - Check status: docker-compose ps
echo.
echo Happy coding!
goto end

:end
