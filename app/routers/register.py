from fastapi import APIRouter, status
from models.user_model import UserDataBase
from crud.crud_user import create_user
from crud.crud_note import create_welcome_note

router = APIRouter(tags=["Register"])

@router.post("/api/register", status_code=status.HTTP_201_CREATED)
async def add_user(form_register: UserDataBase): 
    id = create_user(form_register)
    create_welcome_note(id)

    return "User successfully created"