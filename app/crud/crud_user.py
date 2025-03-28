from fastapi import HTTPException, status
from bson import ObjectId
from models.user_model import UserDataBase
from dependencies import search_user, encode_passw
from database import users_collection

def create_user(form_register: UserDataBase):
    del form_register.id
    user_exist = search_user("username", form_register.username)
    
    if (user_exist):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User already exists")
    
    form_register.password = encode_passw(form_register.password)
    form_register = dict(form_register)

    id = users_collection.insert_one(form_register).inserted_id
    
    user_exist = search_user("_id", ObjectId(id))
    
    if (not user_exist):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User could not be created")
    
    return str(id)
