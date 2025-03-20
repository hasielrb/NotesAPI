from fastapi import HTTPException, status
from passlib.context import CryptContext
from database import db_client

crypt = CryptContext(schemes=["bcrypt"])

def search_user(field: str, key: str):
    return db_client.users.find_one({field: key})

def search_note(field: str, key: str):
    return db_client.notes.find_one({field: key})

def encode_passw(password: str):
    return crypt.hash(password)
