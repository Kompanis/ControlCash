from pydantic import BaseModel, EmailStr

# Ответ при логине/обновлении токенов
class TokenPair(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

# Входные данные при регистрации
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Данные о пользователе для ответа API
class UserRead(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    model_config = {"from_attributes": True}
