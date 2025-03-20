from fastapi import APIRouter, HTTPException, status
from bson import ObjectId

from models.user_model import User
from dependencies import search_user, encode_passw
from crud.crud_user import create_user

router = APIRouter(tags=["Register"])

@router.get("/register")
async def return_template():
    pass

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def add_user(form: User):
    exist = search_user("username", form.username)

    if exist:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User Already Exists")
    
    form.password = encode_passw(form.password)
    
    id = ObjectId(create_user(dict(form)))

    if search_user("_id", id):
        return "User Successfully Created"