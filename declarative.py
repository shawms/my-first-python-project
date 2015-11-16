from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

DeclarativeBase = declarative_base()

def create_character_table(engine):
	DeclarativeBase.metadata.create_all(engine)
