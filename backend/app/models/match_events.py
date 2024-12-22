import uuid
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from results import Result


class MatchEvent(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    match_id: int = Field(foreign_key="result.id", ondelete="CASCADE")
    match: "Result" = Relationship(back_populates="match_events")
    timestamp: int
    team_id: uuid.UUID = Field(foreign_key="team.id")
    player_id: uuid.UUID = Field(foreign_key="player.id")


# class Assist(MatchEvent, table=True):
#     assistant_id: uuid.UUID = Field(foreign_key="player.id")
#
#
# class Goal(MatchEvent, table=True):
#     goal_type: str | None = Field(default=None)  # TODO: make enum
#     is_own_goal: bool = Field(default=False)
#     assist_id: int | None = Field(default=None, foreign_key="assist.id")
