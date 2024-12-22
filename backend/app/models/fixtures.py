from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel


if TYPE_CHECKING:
    from results import Result
    from team import Team


class Fixture(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    home_team_id: uuid.UUID | None = Field(default=None, foreign_key="team.id", ondelete="CASCADE")
    home_team: Team | None = Relationship(back_populates="home_fixture_matches")
    away_team_id: uuid.UUID | None = Field(default=None, foreign_key="team.id", ondelete="CASCADE")
    away_team: Team | None = Relationship(back_populates="away_fixture_matches")
    datetime: datetime
    referee: str | None = Field(default=None)
    result: Result | None = Relationship(back_populates="fixture")
