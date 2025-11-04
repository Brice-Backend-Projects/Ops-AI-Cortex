"""
auth/dependencies.py
--------------------
Reusable authentication dependencies for route protection.
"""

from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from ops_ai_cortex.auth.models import User
from ops_ai_cortex.core.db import get_db
from ops_ai_cortex.config.config import settings, yaml_config


def get_current_user(token: str, db: Session = Depends(get_db)) -> User:
    """Validate JWT and return current user from DB."""
    SECRET_KEY = settings.JWT_SECRET_KEY

    algorithm = "HS256"
    if isinstance(yaml_config, dict):
        algorithm = yaml_config.get("auth", {}).get("jwt", {}).get("algorithm", "HS256")

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[algorithm])
        email = payload.get("sub")
        if not isinstance(email, str):
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise credentials_exception

    return user


