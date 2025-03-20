from fastapi import FastAPI
from routers import register

app = FastAPI()

# Routers
app.include_router(register.router)

# EndPoints
@app.get("/")
async def root():
    return {"message": "Welcome to my api notes"}