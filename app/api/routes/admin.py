from fastapi import APIRouter, Depends

from app.api.deps import require_role
from app.models.user import User

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/dashboard")
def real_admin_dashboard(
    current_user: User = Depends(require_role("admin")),
) -> dict:
    return {
        "message": f"Welcome to the admin dashboard, {current_user.username}",
        "role": current_user.role, 
    }