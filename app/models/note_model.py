from pydantic import BaseModel

class NoteRequest(BaseModel):
    title: str
    content: str

class NoteDataBase(NoteRequest):
    id_user: str