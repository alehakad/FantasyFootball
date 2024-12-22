from __future__ import annotations

from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from fixtures import Fixture
    from match_events import MatchEvent


class Result(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    fixture_id: int = Field(foreign_key="fixture.id")
    fixture: "Fixture" = Relationship(back_populates="result")
    match_events: list[MatchEvent] = Relationship(back_populates="match")
    home_team_score: int
    away_team_score: int
