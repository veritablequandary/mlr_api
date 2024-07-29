from base import Base
from pydantic import BaseModel
from peewee import CharField, IntegerField


class Season(Base):
    class Meta:
        table_name = "seasonData"

    league = CharField(primary_key=True)
    season = IntegerField()
    session = IntegerField()


class SeasonDefinition(BaseModel):
    league: str
    season: int
    session: int
