"""
core/db.py
-----------
Database setup and session dependency for OpsAICortex.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ops_ai_cortex.config.config import settings

# -------------------------------------------------------------------
# Database URL 
# -------------------------------------------------------------------
DATABASE_URL = settings.DATABASE_URL

# -------------------------------------------------------------------
# SQLAlchemy Engine & Session
# -------------------------------------------------------------------
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# -------------------------------------------------------------------
# Dependency for FastAPI routes
# -------------------------------------------------------------------
def get_db():
    """
    FastAPI dependency for database sessions.
    Ensures sessions are properly opened and closed per request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
