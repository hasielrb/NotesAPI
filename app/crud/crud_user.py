from database import db_client

def create_user(form: dict):
    id = db_client.users.insert_one(form).inserted_id
    return id
