import random

from sqlalchemy.orm import Session

from db import engine
from faker import Faker
from models import Teacher, Group, Course, Student, Grade

fake = Faker()

teachers = [
    Teacher(name=f"{fake.first_name()} {fake.last_name()}", email=fake.email())
    for _ in range(5)
]

groups = [Group(name=fake.word()) for _ in range(3)]

courses = [Course(name=fake.word(), teacher=random.choice(teachers)) for _ in range(8)]

students = [
    Student(
        name=f"{fake.first_name()} {fake.last_name()}",
        email=fake.email(),
        group=random.choice(groups),
    )
    for _ in range(50)
]

grades: list[Grade] = []

for student in students:
    for course in courses:
        grades.extend(
            [
                Grade(course=course, student=student, value=random.randint(20, 100))
                for i in range(random.randint(1, 3))
            ]
        )


with Session(engine) as session:
    entities = []
    entities.extend(teachers)
    entities.extend(groups)
    entities.extend(courses)
    entities.extend(students)
    entities.extend(grades)

    session.add_all(entities)
    session.commit()
