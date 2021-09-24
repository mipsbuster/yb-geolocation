from sqlalchemy import create_engine, Column, Integer, String, NUMERIC,TIMESTAMP
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

def yb_engine():
    engine = engine = create_engine('postgresql+psycopg2://yugabyte:yugabyte@localhost:5433/yb_geodemo')
    return engine

def testConnection():
    myEngine = yb_engine()
    with myEngine.connect() as conn:
        result = conn.execute(text("select 'Connection true'"))
        print(result.all())

def create_demo_table():
    Base = declarative_base()
    class Transaction(Base):
        __tablename__ = 'transactions_single'

        userid = Column(Integer, primary_key=True)
        accountid = Column(Integer, primary_key=True)
        account_type = Column(String,primary_key=True)
        amount = Column(NUMERIC)
        geolocation = Column(String)
        txn_type = Column(String)
        created = Column(TIMESTAMP)

    engine = yb_engine()
    Session = sessionmaker(bind=engine)
    session = Session()


    Base.metadata.create_all(engine)



create_demo_table()