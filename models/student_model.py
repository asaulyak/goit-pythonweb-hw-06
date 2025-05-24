from sqlalchemy import Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(120), unique=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))
    group: Mapped["Group"] = relationship(back_populates="students")
    grades: Mapped[list["Grade"]] = relationship(back_populates="student")
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
        return f"<Student(id={self.id}, name='{self.name}', group_id={self.group_id}')>"
