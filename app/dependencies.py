from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from database import users_collection, notes_collection
from models.user_model import UserDataBase
from models.note_model import NoteDataBase
from schemas.users_schema import user_schema
from schemas.notes_schema import note_schema
from core.config import settings

crypt = CryptContext(schemes=["bcrypt"])

# Search user
def search_user(field: str, key: str):
    user = users_collection.find_one({field: key})

    if (user):
        user = UserDataBase(**user_schema(user))
    
    return user

# Search note
def search_note(field: str, key: str):
    note = notes_collection.find_one({field: key})
    
    if (note):
        note = NoteDataBase(**note_schema(note))

    return note

# Encode password
def encode_passw(password: str):
    return crypt.hash(password)

# Verify password
def verify_passw(password_text: str, password_hashed: str):
    return crypt.verify(password_text, password_hashed)

# Create jwt
def create_jwt(user_id: str, username: str):
    expiration = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_DURATION)

    token = {
        "sub": user_id,
        "name": username,
        "exp": expiration,
    }

    return encode_jwt(token)

# Encode jwt
def encode_jwt(token: dict):
    token_encode = jwt.encode(token, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return token_encode

# Decode jwt
def decode_jwt(token: str):
    token_decode = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    return token_decode