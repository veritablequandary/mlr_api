from peewee import Model
from database import db


class Base(Model):
    class Meta:
        database = db
