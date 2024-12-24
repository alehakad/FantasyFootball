import uuid
from datetime import datetime
from uuid import UUID

from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlmodel import Enum, Field, Relationship, SQLModel, Session

from positions import PlayerPosition


class Team(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(index=True)
    players: list["Player"] = Relationship(back_populates="team")
    stadium: str | None = Field(default=None)
    city: str | None = Field(default=None)
    colors: str | None = Field(default=None)  # TODO: for now comma-separated list, add enum or another model
    image_url: str | None = Field(default=None)
    manager: str = Field(unique=True)
    home_fixture_matches: list["Fixture"] = Relationship(
        back_populates="home_team",
        sa_relationship=relationship("Fixture", foreign_keys="[Fixture.home_team_id]")
    )
    away_fixture_matches: list["Fixture"] = Relationship(
        back_populates="away_team",
        sa_relationship=relationship("Fixture", foreign_keys="[Fixture.away_team_id]")
    )
    # TODO: add image, league


class Result(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    fixture_id: int = Field(foreign_key="fixture.id")
    fixture: "Fixture" = Relationship(back_populates="result")
    match_events: list["MatchEvent"] = Relationship(back_populates="match")
    home_team_score: int
    away_team_score: int


class Fixture(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    home_team_id: UUID | None = Field(default=None, foreign_key="team.id", ondelete="CASCADE")
    home_team: Team | None = Relationship(
        back_populates="home_fixture_matches",
        sa_relationship=relationship("Team", foreign_keys="[Fixture.home_team_id]", overlaps="home_fixture_matches"),
    )
    away_team_id: UUID | None = Field(default=None, foreign_key="team.id", ondelete="CASCADE")
    away_team: Team | None = Relationship(
        back_populates="away_fixture_matches",
        sa_relationship=relationship("Team", foreign_keys="[Fixture.away_team_id]", overlaps="away_fixture_matches")
    )
    datetime: datetime
    referee: str | None = Field(default=None)
    result: Result | None = Relationship(back_populates="fixture")


class Player(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    first_name: str = Field(index=True, max_length=100)
    second_name: str = Field(index=True, max_length=100)
    age: int | None = Field(default=None, index=True)
    player_position: PlayerPosition = Field(sa_column=Column(Enum(PlayerPosition)))
    current_price: int | None = Field(default=None)
    team_id: UUID | None = Field(default=None, foreign_key="team.id", ondelete="SET NULL")
    team: Team | None = Relationship(back_populates="players")
    # TODO: add nationality


class MatchEvent(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    match_id: int = Field(foreign_key="result.id", ondelete="CASCADE")
    match: Result = Relationship(back_populates="match_events")
    timestamp: int
    team_id: UUID = Field(foreign_key="team.id")
    player_id: UUID = Field(foreign_key="player.id")


if __name__ == "__main__":
    pass
