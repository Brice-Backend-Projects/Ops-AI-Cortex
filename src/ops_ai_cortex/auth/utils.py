"""auth/utils.py"""

from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from ops_ai_cortex.config.config import settings, yaml_config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = settings.JWT_SECRET_KEY
ALGORITHM = yaml_config["auth"]["jwt"]["algorithm"]
ACCESS_TOKEN_EXPIRE_MINUTES = yaml_config["auth"]["jwt"]["access_token_expire_minutes"]

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
