from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from app.db.session import Base

class Merchant(Base):
    __tablename__ = "merchants"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(200), unique=True, index=True)
    mcc: Mapped[str] = mapped_column(String(4), default="", index=True)
