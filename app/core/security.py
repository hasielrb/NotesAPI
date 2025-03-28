from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from dependencies import decode_jwt, search_user

oauth2 = OAuth2PasswordBearer(tokenUrl="/api/token")

async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Invalid authentication credentials",
                            headers={"WWW-Authenticate": "Bearer"})
    
    try:
        username = decode_jwt(token).get("name")
        if username is None:
            raise exception
        
    except JWTError:
        raise exception

    return search_user("username", username)