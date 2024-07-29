from base import Base
from pydantic import BaseModel
from peewee import CharField, IntegerField


class Game(Base):
    class Meta:
        table_name = "gameData"

    league = CharField()
    season = IntegerField()
    session = IntegerField()
    gameID = IntegerField()
    sheetID = CharField(primary_key=True)
    threadURL = CharField()
    umpires = CharField()
    awayTeam = CharField()
    homeTeam = CharField()
    awayScore = IntegerField()
    homeScore = IntegerField()
    inning = CharField()
    outs = IntegerField()
    obc = IntegerField()
    complete = IntegerField()
    winningPitcher = IntegerField()
    losingPitcher = IntegerField()
    save = IntegerField()
    potg = IntegerField()
    honorMention = IntegerField()
    state = CharField()


class GameDefinition(BaseModel):
    league: str
    season: int
    session: int
    gameID: int
    sheetID: str
    threadURL: str
    umpires: str | None = None
    awayTeam: str
    homeTeam: str
    awayScore: int
    homeScore: int
    inning: str
    outs: int
    obc: int
    complete: int
    winningPitcher: int | None = None
    losingPitcher: int | None = None
    save: int | None = None
    potg: int | None = None
    honorMention: int | None = None
    state: str | None = None
