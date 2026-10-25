from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher
from jwt import encode, decode, InvalidTokenError
from app.core.config import settings
from datetime import datetime, timedelta, timezone

password_hash = PasswordHash((Argon2Hasher(),))

def hash_password(password: str) -> str:
    return password_hash.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)

def create_access_token(subject: str) -> str:
    expiry = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expiry_minutes)
    payload = {"sub": subject, "exp": expiry}
    return encode(payload, settings.secret_key, algorithm=settings.algorithm)

def decode_access_token(token: str) -> str | None:
    try:
        payload = decode(token, settings.secret_key, algorithms=[settings.algorithm])
    except InvalidTokenError:
        return None
    return payload.get("sub")
