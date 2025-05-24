from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine("postgresql+psycopg://postgres:passwd@localhost:5432/hw02")
# Session = sessionmaker(bind=engine)
# session = Session()


class Base(DeclarativeBase):
    pass
