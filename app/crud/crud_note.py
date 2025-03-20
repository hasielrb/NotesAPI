from database import db_client
from models.note_model import NoteRequest, NoteDataBase
from dependencies import search_note

def create_welcome_note(id: str):
    welcome_note = NoteDataBase(
        title = "Welcome!!",
        content = "Thank you for registering in our note system",
        id_user = id
    )

    welcome_note = dict(welcome_note)
    db_client.notes.insert_one(welcome_note).inserted_id