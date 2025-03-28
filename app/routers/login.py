from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from dependencies import search_user, verify_passw, create_jwt

router = APIRouter(tags=["Login"])

@router.post("/api/token")
async def login(form_login: OAuth2PasswordRequestForm = Depends()):
    user = search_user("username", form_login.username)

    if (not user):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Incorrect user or password")
    
    password = verify_passw(form_login.password, user.password)
    
    if (not password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Incorrect user or password")

    token = create_jwt(user.id, user.username)
    
    return {
        "access_token": token,
        "token_type": "bearer"
    }