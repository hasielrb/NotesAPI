# Notes API 📝🔐

**First Project** | A secure notes manager API with authentication and CRUD operations

[![FastAPI](https://img.shields.io/badge/Framework-FastAPI-%2347A248)](https://fastapi.tiangolo.com)
[![MongoDB](https://img.shields.io/badge/DataBase-MongoDB-%2347A248)](https://www.mongodb.com)

## Key Features
- ✅ JWT Authentication
- ✅ User registration/login
- ✅ CRUD operations for notes
- ✅ Protected endpoints with OAuth2
- ✅ MongoDB database

## Tech Stack
- **Backend**: FastAPI
- **Database**: MongoDB
- **Auth**: OAuth2 + JWT
- **Security**: Bcrypt Hashing

## Quick Start

1. Clone repo & install dependencies:
```bash
git clone https://github.com/hasielrb/NotesAPI.git
cd NotesAPI
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
4. Configure environment variables
```bash
cp -n .env_example .env
nano .env
```
4. Run the application
```bash
cd app/
uvicorn main:app --reload
```

## API Documentation

Explore our interactive documentation at **`http://localhost:8000/docs`** featuring:
- Full endpoints description
- Authentication workflows
- Live API testing
- Request/Response schemas
- Error codes reference
