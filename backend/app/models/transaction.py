import datetime as dt
from decimal import Decimal
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, Numeric, DateTime, func
from app.db.session import Base

class Transaction(Base):
    __tablename__ = "transactions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id", ondelete="CASCADE"), index=True)
    category_id: Mapped[Optional[int]] = mapped_column(ForeignKey("categories.id"), nullable=True)
    merchant_id: Mapped[Optional[int]] = mapped_column(ForeignKey("merchants.id"), nullable=True)

    amount: Mapped[Decimal] = mapped_column(Numeric(14, 2))
    currency: Mapped[str] = mapped_column(String(3), default="KGS")
    description: Mapped[str] = mapped_column(String(500), default="")
    occurred_at: Mapped[dt.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    account = relationship("Account", back_populates="transactions")
