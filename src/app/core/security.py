from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hash_password(password: str) -> str:
    """Hash password"""
    hash_pass = pwd_context.hash(password)
    return hash_pass


def validate_password(password: str, hashed_password: str) -> bool:
    """Validate password hash with user db hash."""
    return pwd_context.verify(password, hashed_password)
