from sqlalchemy import *
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import settings

DeclarativeBase = declarative_base()

def create_tables(engine):
    DeclarativeBase.metadata.create_all(engine)

def db_connect():
    return create_engine(URL(**settings.DATABASE))

class BankAccount(DeclarativeBase):
    __tablename__ = 'bank_account'
    id = Column(Integer, primary_key=True)
    username = Column('username', String)

class Transaction(DeclarativeBase):
    __tablename__ = "transaction"
    id = Column(Integer, primary_key=True)
    bank_account_id = Column('bank_account_id', Integer, ForeignKey('bank_account.id'))
    amount = Column('amount', Integer)
