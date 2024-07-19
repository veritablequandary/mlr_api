from peewee import Model, CharField, IntegerField, TextField
from database import db


class BaseModel(Model):
    class Meta:
        database = db


class BattingType(BaseModel):
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
