from sqlalchemy import Integer, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base


class Group(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    students: Mapped[list["Student"]] = relationship(back_populates="group")
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    def __repr__(self) -> str:
        return f"<Group(id={self.id}, name='{self.name}')>"
