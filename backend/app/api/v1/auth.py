from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.deps import get_db
from app.core.security import get_password_hash, verify_password, create_token, decode_token
from app.core.config import settings
from app.models.user import User
from app.schemas.auth import UserCreate, UserRead, TokenPair

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserRead, status_code=201)
async def register(data: UserCreate, db: AsyncSession = Depends(get_db)):
    q = await db.execute(select(User).where(User.email == data.email))
    if q.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="User already exists")
    user = User(email=data.email, hashed_password=get_password_hash(data.password))
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

@router.post("/login", response_model=TokenPair)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    q = await db.execute(select(User).where(User.email == form_data.username))
    user = q.scalar_one_or_none()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access = create_token(user.email, settings.ACCESS_TOKEN_EXPIRE_MINUTES, token_type="access")
    refresh = create_token(user.email, settings.REFRESH_TOKEN_EXPIRE_MINUTES, token_type="refresh")
    return TokenPair(access_token=access, refresh_token=refresh)

@router.post("/refresh", response_model=TokenPair)
async def refresh_tokens(refresh_token: str):
    try:
        payload = decode_token(refresh_token)
        if payload.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Not a refresh token")
        subject = payload.get("sub")
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    access = create_token(subject, settings.ACCESS_TOKEN_EXPIRE_MINUTES, token_type="access")
    new_refresh = create_token(subject, settings.REFRESH_TOKEN_EXPIRE_MINUTES, token_type="refresh")
    return TokenPair(access_token=access, refresh_token=new_refresh)
