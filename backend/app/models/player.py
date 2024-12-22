from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Column
from sqlmodel import Enum, Field, Relationship, SQLModel

from positions import PlayerPosition

if TYPE_CHECKING:
    from team import Team


class Player(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    first_name: str = Field(index=True, max_length=100)
    second_name: str = Field(index=True, max_length=100)
    age: int | None = Field(default=None, index=True)
    player_position: PlayerPosition = Field(sa_column=Column(Enum(PlayerPosition)))
    current_price: int | None = Field(default=None)
    team_id: uuid.UUID | None = Field(default=None, foreign_key="team.id", ondelete="SET NULL")
    team: Team | None = Relationship(back_populates="players")
