from decimal import Decimal
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, Numeric
from app.db.session import Base

class Account(Base):
    __tablename__ = "accounts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), index=True)
    currency: Mapped[str] = mapped_column(String(3), default="KGS")
    initial_balance: Mapped[Decimal] = mapped_column(Numeric(14, 2), default=0)
    current_balance: Mapped[Decimal] = mapped_column(Numeric(14, 2), default=0)

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    owner = relationship("User", back_populates="accounts")

    transactions = relationship("Transaction", back_populates="account", cascade="all, delete-orphan")
