import os
from peewee import MySQLDatabase
from playhouse.db_url import connect

db_host = os.environ["DB_HOST"]
db_pass = os.environ["DB_PASS"]
db_user = os.environ["DB_USER"]
db_name = os.environ["DB_DB"]
db_port = os.environ["DB_PORT"]

db = MySQLDatabase(None)
db.init(database=db_name, host=db_host, user=db_user, port=db_port, password=db_pass)
