from fastapi import APIRouter, Depends
from app.core.deps import get_current_user
from app.schemas.auth import UserRead
from app.models.user import User

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=UserRead)
async def read_me(current: User = Depends(get_current_user)):
    return current
