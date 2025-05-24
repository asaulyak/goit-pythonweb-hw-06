from sqlalchemy import Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base


class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id"))
    teacher: Mapped["Teacher"] = relationship(back_populates="courses")
    grades: Mapped[list["Grade"]] = relationship(back_populates="course")
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )
