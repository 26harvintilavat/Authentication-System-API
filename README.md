# FastAPI Authentication System

This is a simple authentication API built using **FastAPI**.
It provides user registration, login, password hashing, and JWT token based authentication.

## Features

- User Registration
- User Login
- Password Hashing
- JWT Token Authentication
- Protected Routes
- PostgreSQL Database
- Clean Project Structure

## Tech Stack

- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT (python-jose)
- Pydantic
- Uvicorn

## Project Structure

```
app/
 ├── core/
 │    ├── database.py
 │    └── security.py
 ├── models/
 │    └── user.py
 ├── schemas/
 │    ├── auth.py
 │    └── user.py
 └── main.py
```

## Setup

1. Create virtual environment

```
python -m venv venv
```

2. Activate environment

```
venv\Scripts\activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Create `.env` file and add:

```
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. Run server

```
uvicorn app.main:app --reload
```

Open Swagger docs:

```
http://127.0.0.1:8000/docs
```
