"""
auth/routes.py
--------------
Authentication routes for OpsAICortex.
"""

from typing import Any, Dict

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ops_ai_cortex.core.db import get_db
from ops_ai_cortex.auth import schemas, utils, models


router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=schemas.UserRead)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)) -> models.User:
    """Register a new user."""
    # Skip DB logic safely if database layer not yet implemented
    if not hasattr(models, "User"):
        raise HTTPException(status_code=503, detail="Database not initialized")

    existing = db.query(models.User).filter(models.User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = utils.hash_password(user.password)
    new_user = models.User(email=user.email, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)) -> Dict[str, Any]:
    """Authenticate user and return JWT access token."""
    if not hasattr(models, "User"):
        raise HTTPException(status_code=503, detail="Database not initialized")

    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or not utils.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    access_token = utils.create_access_token({"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}

