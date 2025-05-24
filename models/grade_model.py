from sqlalchemy import Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.util.preloaded import orm

from db import Base
from models.course_model import Course
from models.student_model import Student


class Grade(Base):
    __tablename__ = "grades"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    value: Mapped[int] = mapped_column(Integer)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))
    course: Mapped["Course"] = relationship(back_populates="courses")
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))
    student: Mapped["Student"] = relationship(back_populates="students")
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    @orm.validates("value")
    def validate_grade(self, key, value):
        if not 0 < value < 100:
            raise ValueError(f"Invalid grade {value}")
        return value

    def __repr__(self) -> str:
        return f"<Grade(id={self.id}, name='{self.name}')>"
