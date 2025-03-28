from fastapi import HTTPException, status
from bson import ObjectId
from database import notes_collection
from models.note_model import NoteDataBase
from dependencies import search_note
from schemas.notes_schema import notes_schema

# Get All Notes
def get_all_notes(user_id: str):
    notes =  notes_schema(notes_collection.find({"id_user": user_id}))
    
    for note in notes:
        del note["id_user"]

    return notes

# Create Welcome Note
def create_welcome_note(id: str):
    welcome_note = NoteDataBase(
        title = "Welcome!!",
        content = "Thank you for registering in our note system",
        id_user = id
    )
    del welcome_note.id
    welcome_note = dict(welcome_note)
    notes_collection.insert_one(welcome_note).inserted_id

# Create a Note
def create_note(note: NoteDataBase, user_id: str):
    del note.id
    note.id_user = user_id
    note = dict(note)
    notes_collection.insert_one(note).inserted_id

# Update a Note
def update_note(id: str, user_id: str, note_content: str):
    id = ObjectId(id)
    note = search_note("_id", id)

    if (not note) or (note.id_user != user_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The note does not exist")
    
    note.content = note_content
    note = dict(note)
    notes_collection.find_one_and_replace({"_id": id}, note)

# Delete a Note
def delete_note(id: str, user_id: str):
    id = ObjectId(id)
    note = search_note("_id", id)
    
    if (not note) or (note.id_user != user_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The note does not exist")
    
    notes_collection.delete_one({"_id": id})