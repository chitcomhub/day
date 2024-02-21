/backend
  /alembic
  /app
    __init__.py
    main.py           # Entry point for your FastAPI application
    models.py         # SQLAlchemy models that represent your database schema
    schemas.py        # Pydantic models for request and response data validation
    database.py       # Database session management and engine configuration
    crud.py           # CRUD utilities (create, read, update, delete)
    api               # Directory for your API route handlers
    core              # Core settings and configuration
    dependencies.py   # Dependency provider for routes
  requirements.txt    # Python dependencies required for your project
  Dockerfile          # Dockerfile for building your FastAPI application image
