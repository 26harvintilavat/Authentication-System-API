from fastapi import FastAPI

from app.api.routes.admin import router as admin_router
from app.api.routes.auth import router as auth_router
from app.api.routes.users import router as users_router
from app.core.database import Base, engine
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Authentication System API",
    description="A FastAPI project for user registration, login, JWT authentication, protected routes, and role-based access control.",
    version="0.1.0"
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(admin_router)

@app.get("/", tags=["Root"])
def root() -> dict[str, str]:
    return {"message": "Authentication System API is running"}