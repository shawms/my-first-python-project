from sqlalchemy import *
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

DeclarativeBase = declarative_base()

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',
    'password': 'postgres',
    'database': 'rpg'
}

def create_character_table(engine):
    DeclarativeBase.metadata.create_all(engine)

def db_connect():
    return create_engine(URL(DATABASE))

def create_character_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class BankAccount(DeclarativeBase):
    __tablename__ = "bank_account"
    username = Column('username', String, primary_key=True)

class Transaction(DeclarativeBase):
    __tablename__ = "transaction"
    username = Column('username', String, ForeignKey('bank_account.username'))
    amount = Column('amount', Integer)
