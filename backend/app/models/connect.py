from sqlmodel import SQLModel, create_engine

from team import Team
from player import Player
from results import Result
from fixtures import Fixture
from match_events import MatchEvent  # , Goal, Assist

DATABASE_URL = ""

engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    init_db()
