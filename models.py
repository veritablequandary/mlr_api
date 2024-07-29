from peewee import Model, CharField, IntegerField, TextField
from pydantic import BaseModel
from database import db


class Base(Model):
    class Meta:
        database = db


class BattingType(Base):
    class Meta:
        table_name = "battingTypes"

    type = CharField(primary_key=True)
    name = TextField()
    rangeHR = IntegerField()
    range3B = IntegerField()
    range2B = IntegerField()
    range1B = IntegerField()
    rangeBB = IntegerField()
    rangeFO = IntegerField()
    rangeK = IntegerField()
    rangePO = IntegerField()
    rangeRGO = IntegerField()
    rangeLGO = IntegerField()


class PitchingType(Base):
    class Meta:
        table_name = "pitchingTypes"

    type = CharField(primary_key=True)
    name = TextField()
    rangeHR = IntegerField()
    range3B = IntegerField()
    range2B = IntegerField()
    range1B = IntegerField()
    rangeBB = IntegerField()
    rangeFO = IntegerField()
    rangeK = IntegerField()
    rangePO = IntegerField()
    rangeRGO = IntegerField()
    rangeLGO = IntegerField()


class HandBonus(Base):
    class Meta:
        table_name = "handBonuses"

    type = CharField(primary_key=True)
    name = TextField()
    rangeHR = IntegerField()
    range3B = IntegerField()
    range2B = IntegerField()
    range1B = IntegerField()
    rangeBB = IntegerField()
    rangeFO = IntegerField()
    rangeK = IntegerField()
    rangePO = IntegerField()
    rangeRGO = IntegerField()
    rangeLGO = IntegerField()


class BattingPitchingTypeDefinition(BaseModel):
    type: str
    name: str
    rangeHR: int
    range3B: int
    range2B: int
    range1B: int
    rangeBB: int
    rangeFO: int
    rangeK: int
    rangePO: int
    rangeRGO: int
    rangeLGO: int


class Season(Base):
    class Meta:
        table_name = "seasonData"

    league = CharField(primary_key=True)
    season = IntegerField()
    session = IntegerField()


class SeasonTypeDefinition(BaseModel):
    league: str
    season: int
    session: int


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


class GameTypeDefinition(BaseModel):
    league: str
    season: int
    session: int
    gameID: int
    sheetID: str
    threadURL: str
    umpires: str
    awayTeam: str
    homeTeam: str
    awayScore: int
    homeScore: int
    inning: str
    outs: int
    obc: int
    complete: int
    winningPitcher: int
    losingPitcher: int
    save: int
    potg: int
    honorMention: int
    state: str
