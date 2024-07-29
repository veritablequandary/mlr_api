from models.base import Base
from pydantic import BaseModel
from peewee import CharField, IntegerField, TextField


class Team(Base):
    class Meta:
        table_name = "teamData"

    name = TextField()
    abb = CharField(primary_key=True)
    color = CharField()
    logo_url = TextField()
    webhook_url = TextField()
    league = CharField()
    division = CharField()
    gm = CharField()
    cogm = CharField()
    captain1 = CharField()
    captain2 = CharField()
    captain3 = CharField()
    committee1 = CharField()
    committee2 = CharField()
    awards1 = CharField()
    awards2 = CharField()
    affiliate = CharField()
    role_id = CharField()
    status = IntegerField()


class TeamDefinition(BaseModel):
    name: str
    abb: str
    color: str
    logo_url: str
    webhook_url: str | None = None
    league: str
    division: str | None = None
    gm: str | None = None
    cogm: str | None = None
    captain1: str | None = None
    captain2: str | None = None
    captain3: str | None = None
    committee1: str | None = None
    committee2: str | None = None
    awards1: str | None = None
    awards2: str | None = None
    affiliate: str | None = None
    role_id: str | None = None
    status: int
