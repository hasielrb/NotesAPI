from fastapi import APIRouter, Depends
from core.security import auth_user
from models.user_model import UserDataBase
from models.note_model import NoteDataBase
from crud.crud_note import get_all_notes, create_note, update_note, delete_note

router = APIRouter(tags=["Notes"])

@router.get("/api/notes")
async def get_notes(user: UserDataBase = Depends(auth_user)):
    notes = get_all_notes(user.id)
    
    return {"notes": notes}
    
@router.post("/api/notes")
async def create_a_note(note: NoteDataBase, user: UserDataBase = Depends(auth_user)):
    create_note(note, user.id)
    
    return "Note correctly created"

@router.put("/api/notes/{id}")
async def update_a_note(id: str, note_content: str, user: UserDataBase = Depends(auth_user)):
    update_note(id, user.id, note_content)

    return "Note correctly updated"

@router.delete("/api/notes/{id}")
async def delete_a_note(id: str, user: UserDataBase = Depends(auth_user)):
    delete_note(id, user.id)

    return "Note correctly deleted"