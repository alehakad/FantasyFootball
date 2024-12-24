import os
from pathlib import Path

from dotenv import load_dotenv
from sqlmodel import SQLModel, Session, create_engine

from models_definitions import Team

parent_folder = Path(__file__).resolve().parent.parent.parent

load_dotenv(parent_folder / '.env')

DATABASE_URL = os.getenv("DATABASE_URL")


def get_engine():
    engine = create_engine(DATABASE_URL, echo=True)
    return engine


def init_db():
    engine = get_engine()
    SQLModel.metadata.create_all(engine)


def create_test_data():
    new_team = Team(name="Arsenal", manager="Arteta")
    engine = get_engine()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        session.add(new_team)
        session.commit()


if __name__ == "__main__":
    init_db()
    create_test_data()
