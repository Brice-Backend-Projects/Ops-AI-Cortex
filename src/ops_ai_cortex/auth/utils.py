"""auth/utils.py"""

from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from ops_ai_cortex.config.config import settings, yaml_config


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = settings.JWT_SECRET_KEY

# 🧩 Handle case where yaml_config is empty during early dev
algorithm = "HS256"
expire_minutes = 60
if isinstance(yaml_config, dict):
    algorithm = yaml_config.get("auth", {}).get("jwt", {}).get("algorithm", "HS256")
    expire_minutes = yaml_config.get("auth", {}).get("jwt", {}).get("access_token_expire_minutes", 60)

ALGORITHM = algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = expire_minutes


def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    """Verify a plain password against a hashed one."""
    return pwd_context.verify(plain, hashed)

def create_access_token(data: dict[str, object]) -> str:
    """Create a signed JWT access token."""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
