from pydantic import BaseModel
from typing import Optional

class NoteRequest(BaseModel):
    id: Optional[str] = None
    title: str
    content: str

class NoteDataBase(NoteRequest):
    id_user: Optional[str] = None