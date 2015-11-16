from sqlalchemy import *
from sqlalchemy.engine.url import URL

DATABASE = {
	'drivername': 'postgres',
	'host': 'localhost',
	'port': '5432',
	'username': 'postgres',
	'password': 'postgres',
	'database': 'rpg'
}
def db_connect():
	return create_engine(URL(DATABASE))
