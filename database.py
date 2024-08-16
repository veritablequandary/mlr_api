import os
from peewee import MySQLDatabase

db_host = os.environ["DB_HOST"]
db_pass = os.environ["DB_PASS"]
db_user = os.environ["DB_USER"]
db_name = os.environ["DB_DB"]
db_port = int(os.environ["DB_PORT"])

db = MySQLDatabase(db_name, user=db_user, password=db_pass, host=db_host, port=db_port)
