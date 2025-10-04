# Подключаем все модели, чтобы Alembic видел metadata
from app.db.session import Base
from app.models.user import User
from app.models.account import Account
from app.models.category import Category
from app.models.merchant import Merchant
from app.models.transaction import Transaction
