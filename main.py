from db import Base, engine
from models import Student, Course, Teacher, Grade, Group


def main():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
