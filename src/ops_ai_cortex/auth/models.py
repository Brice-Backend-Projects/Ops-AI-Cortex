"""auth/models.py"""

from sqlalchemy import Column, Integer, String
from ops_ai_cortex.core.db import Base

class User(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    email: str = Column(String, unique=True, index=True, nullable=False)
    hashed_password: str = Column(String, nullable=False)

