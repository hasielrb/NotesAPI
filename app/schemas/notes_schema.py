def note_schema(note) -> dict:
    return {
        "id": str(note["_id"]),
        "title": note["title"],
        "content": note["content"],
        "id_user": note["id_user"]
    }

def notes_schema(notes) -> list:
    return [note_schema(note) for note in notes]