#!/usr/bin/env python3
"""
Quick script to test if all dependencies are installed correctly
"""

import sys

def test_imports():
    """Test importing all major dependencies"""

    tests = [
        ("FastAPI", "fastapi", "FastAPI"),
        ("Uvicorn", "uvicorn", "uvicorn"),
        ("Pydantic", "pydantic", "pydantic"),
        ("SQLAlchemy", "sqlalchemy", "sqlalchemy"),
        ("Alembic", "alembic", "alembic"),
        ("AsyncPG", "asyncpg", "asyncpg"),
        ("Psycopg2", "psycopg2", "psycopg2"),
        ("Qdrant Client", "qdrant_client", "qdrant_client"),
        ("PyMongo", "pymongo", "pymongo"),
        ("Motor", "motor", "motor"),
        ("LangChain", "langchain", "langchain"),
        ("LangChain OpenAI", "langchain_openai", "langchain_openai"),
        ("OpenAI", "openai", "OpenAI"),
        ("Tiktoken", "tiktoken", "tiktoken"),
        ("Sentence Transformers", "sentence_transformers", "sentence_transformers"),
        ("Celery", "celery", "Celery"),
        ("Redis", "redis", "redis"),
        ("WebSockets", "websockets", "websockets"),
        ("HTTPX", "httpx", "httpx"),
        ("Aiofiles", "aiofiles", "aiofiles"),
        ("PyPDF", "pypdf", "pypdf"),
        ("Python-DOCX", "docx", "python-docx"),
        ("OpenPyXL", "openpyxl", "openpyxl"),
        ("Python-JOSE", "jose", "python-jose"),
        ("Passlib", "passlib", "passlib"),
        ("Bcrypt", "bcrypt", "bcrypt"),
        ("Cryptography", "cryptography", "cryptography"),
        ("Pytest", "pytest", "pytest"),
        ("Black", "black", "black"),
        ("Flake8", "flake8", "flake8"),
        ("MyPy", "mypy", "mypy"),
    ]

    passed = 0
    failed = 0
    failed_packages = []

    print("Testing Python Dependencies...")
    print("=" * 60)

    for name, module, package in tests:
        try:
            __import__(module)
            print(f"✓ {name:<25} OK")
            passed += 1
        except ImportError as e:
            print(f"✗ {name:<25} FAILED: {e}")
            failed += 1
            failed_packages.append((name, package))

    print("=" * 60)
    print(f"\nResults: {passed} passed, {failed} failed")

    if failed_packages:
        print("\nFailed packages - install with:")
        print("pip install " + " ".join([pkg for _, pkg in failed_packages]))
        return False
    else:
        print("\n✓ All dependencies installed successfully!")
        return True

def test_versions():
    """Check versions of key packages"""
    print("\n" + "=" * 60)
    print("Package Versions:")
    print("=" * 60)

    try:
        import fastapi
        print(f"FastAPI: {fastapi.__version__}")
    except: pass

    try:
        import pydantic
        print(f"Pydantic: {pydantic.__version__}")
    except: pass

    try:
        import sqlalchemy
        print(f"SQLAlchemy: {sqlalchemy.__version__}")
    except: pass

    try:
        import langchain
        print(f"LangChain: {langchain.__version__}")
    except: pass

    try:
        import openai
        print(f"OpenAI: {openai.__version__}")
    except: pass

    print("=" * 60)

def check_conflicts():
    """Check for dependency conflicts"""
    print("\nChecking for dependency conflicts...")
    print("=" * 60)

    import subprocess
    result = subprocess.run(
        [sys.executable, "-m", "pip", "check"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print("✓ No dependency conflicts found!")
    else:
        print("✗ Dependency conflicts detected:")
        print(result.stdout)
        print(result.stderr)

    print("=" * 60)

if __name__ == "__main__":
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    print()

    success = test_imports()
    test_versions()
    check_conflicts()

    if success:
        print("\n✓ Installation test passed!")
        print("\nNext steps:")
        print("1. Configure backend/.env with your API keys")
        print("2. Start databases: docker-compose up -d postgres mongodb redis")
        print("3. Run backend: uvicorn app.main:app --reload")
        print("4. Visit: http://localhost:8000/docs")
        sys.exit(0)
    else:
        print("\n✗ Installation test failed!")
        print("See INSTALL_TROUBLESHOOTING.md for help")
        sys.exit(1)
