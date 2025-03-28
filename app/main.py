from fastapi import FastAPI
from routers import register, login, notes

app = FastAPI()

# Routers
app.include_router(register.router)
app.include_router(login.router)
app.include_router(notes.router)

@app.get("/", tags=["Root"])
async def root():
    return "Welcome to my API Notes"