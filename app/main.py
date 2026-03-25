from fastapi import FastAPI
from app.core.database import Base, engine
from app.models.user import User

app = FastAPI(
    title="Authentication System API",
    description="A FastAPI project for user registration, login, JWT authentication, protected routes, and role-based access control.",
    version="0.1.0"
)

@app.get("/", tags=["Root"])
def root() -> dict[str, str]:
    return {"message": "Authentication System API is running"}