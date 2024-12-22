import uuid

from sqlmodel import Field, Relationship, SQLModel

from fixtures import Fixture
from player import Player


class Team(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(index=True)
    players: list["Player"] = Relationship(back_populates="team")
    stadium: str | None = Field(default=None)
    city: str | None = Field(default=None)
    colors: str | None = Field(default=None)  # TODO: for now comma-separated list, add enum or another model
    image_url: str | None = Field(default=None)
    manager: str = Field(unique=True)
    home_fixture_matches: list["Fixture"] = Relationship(back_populates="home_team")  # Back-populates
    away_fixture_matches: list["Fixture"] = Relationship(back_populates="home_team")  # Back-populates
    # TODO: add image, league
