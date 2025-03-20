from fastapi import HTTPException, status
from bson import ObjectId
from models.user_model import User
from dependencies import search_user, encode_passw
from database import db_client

def create_user(form_register: User):
    user_exist = search_user("username", form_register.username)
    
    if (user_exist):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User already exists")
    
    form_register.password = encode_passw(form_register.password)
    form_register = dict(form_register)

    id = db_client.users.insert_one(form_register).inserted_id
    
    user_exist = search_user("_id", ObjectId(id))
    
    if (not user_exist):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User could not be created")
    
    return str(id)





# def get_user

# def update_user

# def delete_user


