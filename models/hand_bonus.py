from models.base import Base
from pydantic import BaseModel
from peewee import CharField, IntegerField, TextField


class HandBonus(Base):
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


class HandBonusDefinition(BaseModel):
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
