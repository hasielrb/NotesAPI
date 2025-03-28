from pydantic import BaseModel
from typing import Optional

class UserRequest(BaseModel):
    id: Optional[str] = None
    username: str

class UserDataBase(UserRequest):
    password: str    

