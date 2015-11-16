from models import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = db_connect()
create_tables(engine)
Session = sessionmaker(bind=engine)
session = Session()

shawn_account = BankAccount(username='shawn')
session.add(shawn_account)
session.commit()

def add_transaction(username, amount):
    bank_account = session.query(BankAccount).filter_by(username=username).first()
    new_transaction = Transaction(bank_account_id=bank_account.id, amount=amount)
    print(new_transaction.bank_account_id)
    session.add(new_transaction)
    session.commit()

add_transaction('shawn', -23)
add_transaction('shawn', 12)
add_transaction('shawn', -11)
add_transaction('shawn', 24)
