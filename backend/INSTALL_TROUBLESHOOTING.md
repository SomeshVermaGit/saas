# Backend Installation Troubleshooting Guide

## Fixed Issues

### 1. Removed Duplicate Dependencies
- **Fixed:** `httpx` was listed twice (lines 38 and 53)
- **Solution:** Removed duplicate entry

### 2. Removed Problematic Dependencies
- **Fixed:** `python-magic==0.4.27` can cause issues on Windows
- **Solution:** Removed from requirements.txt
- **Note:** If you need file type detection, use `python-magic-bin` on Windows

## Installation Methods

### Method 1: Clean Install (Recommended)

```bash
# Navigate to backend
cd backend

# Remove old virtual environment if exists
rmdir /s venv  # Windows
rm -rf venv    # macOS/Linux

# Create new virtual environment
python -m venv venv

# Activate
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

### Method 2: Flexible Version Install

If you encounter version conflicts, use the flexible requirements:

```bash
pip install -r requirements-flexible.txt
```

### Method 3: Install in Stages

If still having issues, install in groups:

```bash
# Stage 1: Core FastAPI
pip install fastapi uvicorn pydantic pydantic-settings python-multipart python-dotenv

# Stage 2: Database
pip install sqlalchemy alembic asyncpg psycopg2-binary

# Stage 3: Vector Databases
pip install qdrant-client pymongo motor

# Stage 4: AI/LangChain
pip install langchain langchain-openai langchain-community openai tiktoken sentence-transformers

# Stage 5: Task Queue
pip install celery redis

# Stage 6: Utilities
pip install websockets httpx aiofiles pypdf python-docx openpyxl

# Stage 7: Security & Auth
pip install python-jose passlib bcrypt cryptography

# Stage 8: Development Tools
pip install pytest pytest-asyncio pytest-cov black flake8 mypy
```

## Common Issues & Solutions

### Issue 1: `python-magic` fails on Windows

**Error:**
```
ERROR: Could not find a version that satisfies the requirement python-magic
```

**Solution:**
```bash
# Already removed from requirements.txt
# If you need it, use:
pip install python-magic-bin  # Windows only
```

### Issue 2: `bcrypt` compilation fails

**Error:**
```
ERROR: Failed building wheel for bcrypt
```

**Solution:**
```bash
# Windows: Install Visual C++ Build Tools
# Or use pre-built wheels:
pip install --upgrade pip setuptools wheel
pip install bcrypt --prefer-binary
```

### Issue 3: `psycopg2-binary` issues

**Error:**
```
Error: pg_config executable not found
```

**Solution:**
```bash
# Use binary version (already in requirements)
pip install psycopg2-binary
```

### Issue 4: `cryptography` compilation fails

**Error:**
```
ERROR: Failed building wheel for cryptography
```

**Solution:**
```bash
# Install Rust (required for cryptography >= 3.4)
# Or use older version:
pip install cryptography==41.0.0
```

### Issue 5: LangChain dependency conflicts

**Error:**
```
ERROR: Cannot install langchain-xxx due to conflicting dependencies
```

**Solution:**
```bash
# Install LangChain components in order:
pip install langchain-core
pip install langchain
pip install langchain-openai
pip install langchain-community
```

### Issue 6: Sentence Transformers takes too long

**Note:** `sentence-transformers` is large (~2GB of dependencies). Be patient during installation.

**To skip for now:**
```bash
# Remove from requirements and install manually later
pip install sentence-transformers
```

## Verification

After installation, verify everything works:

```bash
# Check installed packages
pip list

# Check for conflicts
pip check

# Test imports
python -c "import fastapi; print('FastAPI OK')"
python -c "import sqlalchemy; print('SQLAlchemy OK')"
python -c "import langchain; print('LangChain OK')"
python -c "from openai import OpenAI; print('OpenAI OK')"
```

## Testing the Backend

```bash
# Start the backend
uvicorn app.main:app --reload

# In another terminal, test health endpoint
curl http://localhost:8000/health

# Or visit in browser
# http://localhost:8000/docs
```

## Platform-Specific Notes

### Windows
- Ensure Python 3.11+ is installed
- May need Visual C++ Build Tools for some packages
- Use PowerShell or Command Prompt (not Git Bash for venv activation)

### macOS
- May need to install Xcode Command Line Tools: `xcode-select --install`
- Use `python3` instead of `python` if needed

### Linux
- May need to install Python dev packages: `sudo apt-get install python3-dev`
- May need PostgreSQL dev libraries: `sudo apt-get install libpq-dev`

## Alternative: Use Docker

If local installation continues to fail, use Docker:

```bash
# From project root
docker-compose up backend

# Or build and run
cd backend
docker build -t ai-knowledge-backend .
docker run -p 8000:8000 ai-knowledge-backend
```

## Generate Lock File (Advanced)

To create a reproducible environment:

```bash
# Install pip-tools
pip install pip-tools

# Create requirements.in with unpinned versions
# Then generate locked requirements
pip-compile requirements.in -o requirements-lock.txt

# Install from lock file
pip install -r requirements-lock.txt
```

## Getting Help

If issues persist:

1. **Check Python version:** `python --version` (should be 3.11+)
2. **Check pip version:** `pip --version` (should be latest)
3. **Clear pip cache:** `pip cache purge`
4. **Use verbose mode:** `pip install -v -r requirements.txt`
5. **Check error logs** in the terminal output

## Quick Fix Script

Save this as `install.py` in the backend folder:

```python
import subprocess
import sys

def install_packages():
    """Install packages in groups to avoid conflicts"""

    groups = [
        # Core
        ["fastapi", "uvicorn[standard]", "pydantic", "pydantic-settings"],
        # Database
        ["sqlalchemy", "alembic", "asyncpg", "psycopg2-binary"],
        # Vector DBs
        ["qdrant-client", "pymongo", "motor"],
        # AI/ML
        ["langchain", "langchain-openai", "langchain-community", "openai", "tiktoken"],
        # Utilities
        ["httpx", "aiofiles", "pypdf", "python-docx", "openpyxl"],
        # Security
        ["python-jose[cryptography]", "passlib[bcrypt]", "bcrypt", "cryptography"],
        # Task Queue
        ["celery", "redis", "websockets"],
        # Dev Tools
        ["pytest", "pytest-asyncio", "pytest-cov", "black", "flake8"],
    ]

    for i, group in enumerate(groups, 1):
        print(f"\n{'='*60}")
        print(f"Installing Group {i}/{len(groups)}: {', '.join(group)}")
        print('='*60)

        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install"] + group)
            print(f"✓ Group {i} installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"✗ Error installing group {i}: {e}")
            response = input("Continue with next group? (y/n): ")
            if response.lower() != 'y':
                break

    print("\n" + "="*60)
    print("Installation complete!")
    print("="*60)

    # Verify
    subprocess.call([sys.executable, "-m", "pip", "check"])

if __name__ == "__main__":
    install_packages()
```

Run with: `python install.py`
