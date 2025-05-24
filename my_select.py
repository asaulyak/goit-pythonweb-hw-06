from sqlalchemy import select, func

from db import session
from models import Student, Grade, Group, Course, Teacher
from logger import logging


def select_1():
    stmt = (
        select(Student.name, func.avg(Grade.value).label("average_grade"))
        .join(Grade, Student.grades)
        .group_by(Student.id)
        .order_by(func.avg(Grade.value).desc())
        .limit(5)
    )

    result = session.execute(stmt)
    for row in result:
        logging.info(f"Student: {row.name}, Average Grade: {row.average_grade:.2f}")


def select_2(course_id: int):
    stmt = (
        select(Student.name, func.avg(Grade.value).label("average_grade"))
        .join(Grade, Student.grades)
        .where(Grade.course_id == course_id)
        .group_by(Student.id)
        .order_by(func.avg(Grade.value).desc())
        .limit(1)
    )

    result = session.execute(stmt)
    for row in result:
        logging.info(f"Student: {row.name}, Average Grade: {row.average_grade:.2f}")


def select_3(course_id: int):
    stmt = (
        select(Group.name, func.avg(Grade.value).label("average_grade"))
        .join(Student, Group.students)
        .join(Grade, Student.grades)
        .where(Grade.course_id == course_id)
        .group_by(Group.id)
        .order_by(func.avg(Grade.value).desc())
    )

    result = session.execute(stmt)
    for row in result:
        logging.info(f"Course: {row.name}, Average Grade: {row.average_grade:.2f}")


def select_4():
    stmt = select(func.avg(Grade.value).label("average_grade"))

    result = session.execute(stmt)
    for row in result:
        logging.info(f"Average Grade: {row.average_grade:.2f}")


def select_5(teacher_id: int):
    stmt = select(Course.name).where(Course.teacher_id == teacher_id)

    result = session.execute(stmt)
    for row in result:
        logging.info(f"Course name: {row.name}")


def select_6(group_id: int):
    stmt = select(Student.name).where(Student.group_id == group_id)

    result = session.execute(stmt)
    for row in result:
        logging.info(f"Student name: {row.name}")


def select_7(group_id: int, course_id: int):
    stmt = (
        select(
            Student.name,
            Grade.value,
            Course.name.label("course_name"),
            Group.name.label("group_name"),
        )
        .join(Grade, Student.grades)
        .join(Course, Grade.course_id == Course.id)
        .join(Group, Student.group_id == Group.id)
        .where(Student.group_id == group_id)
        .where(Course.id == course_id)
    )

    result = session.execute(stmt)
    for row in result:
        logging.info(
            f"Student name: {row.name}, grade: {row.value}, course: {row.course_name}, group: {row.group_name}"
        )


def select_8(teacher_id: int):
    stmt = (
        select(
            Teacher.name,
            func.avg(Grade.value).label("average_grade"),
            Course.name.label("course_name"),
        )
        .join(Course, Teacher.courses)
        .join(Grade, Course.grades)
        .where(Teacher.id == teacher_id)
        .group_by(Teacher.id)
        .group_by(Course.id)
    )

    result = session.execute(stmt)
    for row in result:
        logging.info(
            f"Teacher name: {row.name}, course: {row.course_name}, average grade: {row.average_grade:.2f}"
        )


def select_9(student_id: int):
    stmt = (
        select(Course.name.distinct().label("name"))
        .join(Grade, Course.grades)
        .where(Grade.student_id == student_id)
    )

    result = session.execute(stmt)
    for row in result:
        logging.info(f"Course name: {row.name}")


def select_10(student_id: int, teacher_id: int):
    stmt = (
        select(
            Course.name.distinct().label("course_name"),
            Student.name,
            Teacher.name.label("teacher_name"),
        )
        .join(Grade, Student.grades)
        .join(Course, Grade.course_id == Course.id)
        .join(Teacher, Course.teacher_id == Teacher.id)
        .where(Student.id == student_id)
        .where(Teacher.id == teacher_id)
    )

    result = session.execute(stmt)
    for row in result:
        logging.info(
            f"Student name: {row.name}, teacher: {row.teacher_name}, course: {row.course_name}"
        )


# select_1()
# select_2(1)
# select_3(1)
# select_4()
# select_5(1)
# select_6(1)
# select_7(1, 1)
# select_8(2)
# select_9(2)
# select_10(1, 3)
