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
