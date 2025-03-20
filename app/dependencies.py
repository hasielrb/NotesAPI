from passlib.context import CryptContext
from database import db_client

crypt = CryptContext(schemes=["bcrypt"])

def search_user(field: str, key: str):
    exist_user = db_client.users.find_one({field: key})
    return exist_user

def encode_passw(password: str):
    password = crypt.hash(password)
    return password