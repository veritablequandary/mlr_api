import os
from peewee import MySQLDatabase

db_host = os.environ["DB_HOST"]
db_pass = os.environ["DB_PASS"]
db_user = os.environ["DB_USER"]
db_name = os.environ["DB_DB"]
db_port = os.environ["DB_PORT"]

db = MySQLDatabase(f"mysql://${db_user}:${db_pass}@${db_host}:${db_port}/${db_name}")
