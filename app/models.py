from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    todo: Mapped[list["Todo"]] = relationship(back_populates="user")

class Todo(Base):
    __tablename__ = "todo"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    description: Mapped[str | None] = mapped_column(String(300))
    create_at: Mapped[datetime] = mapped_column(default= datetime.now)
    is_active: Mapped[bool] = mapped_column(default= True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"),
        unique=True
    )
    user: Mapped["User"] = relationship(back_populates="todo")