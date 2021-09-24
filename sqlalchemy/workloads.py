'''
File contains the SQL and workloads for each use case to be applied to the YB Cluster
Workloads are for geo-location examples
Use Case 1 General load and TPS. Generate a write load on the transactions table. Does not include other tables, FK's, constraints
Use Case 2 Simulate a working database load and TPS. Include all DB tables, transactions, read and write
Use Case 3 Usage of defalut tablepsace with geo-location
Use Case 4 Network partition when applying a load

Included are business process and workloads simulated in SQL
WL1 - make a deposit into account in 1 region
WL2 - make a withdrawl
WL3 - Read Account balance
WL4 - Add new user and account with initial deposit
WL5 - ACID transaction and rollback for deposit then a transfer with a withdrawl
'''

#insert transaction into transactions table

import logging
import random
import decimal
from decimal import Decimal

from sqlalchemy.orm import sessionmaker, relationship
from model import Transactions
import config as cfg
from sqlalchemy import create_engine
import traceback
# generate random integer values
from random import seed
from random import randint
# seed random number generator
import time
from datetime import datetime as dt


account_types = ["saving","checking","debit","credit"]
transaction_types = ["debit","credit"]
geo_locations = ["US","EU"]

def get_random_int():
    return randint(0, 10000000)
def get_random_account_type():
    return random.choice(account_types)
def get_random_trans_type():
    return random.choice(transaction_types)
def get_random_trans_amount():
    return float(decimal.Decimal(random.randrange(15, 88900))/100)
def get_timestamp():
    return dt.now()
def get_random_geolocation():
    return random.choice(geo_locations)


class DataAccessUtil:

    def __init__(self):
        engine = create_engine('postgresql://%s:%s@%s:%s/%s' %
                            (cfg.db_user, cfg.db_password, cfg.db_host, cfg.db_port, cfg.database), echo=True)
        self.Session = sessionmaker(bind=engine)

    def create_transactions(self):
        """
        Creates transactions in the transactions table. These are single table transaction are are not related to user, account or other tables
        Used for load testing and generating simulated transaction load. All fields are generated as fake data
        :param rq_user_id:
        :param products:
        :return:
    userid = Column(Integer, primary_key=True)
    accountid = Column(Integer, primary_key=True)
    account_type = Column(String, primary_key=True)
    amount = Column(NUMERIC)
    geolocation = Column(String)
    txn_type = Column(String)
    created = Column(TIMESTAMP)
        """
        session = self.Session()

        try:
            pass
            #get a class
            new_transactions = Transactions()

            #fill in all the fields with fake data
            new_transactions.user_id = get_random_int()
            new_transactions.account_id = get_random_int()
            new_transactions.account_type = get_random_account_type()
            new_transactions.txn_type = get_random_trans_type()
            new_transactions.amount = get_random_trans_amount()
            new_transactions.geo_partition = get_random_geolocation()
            new_transactions.created_at = get_timestamp()

            #insert record
            session.add(new_transactions)
            session.commit()

        except Exception as e:
            logging.error('*** Exception in create_transaction: %s' % e)
            traceback.print_exc()

            session.rollback()
            raise
        finally:
            session.close()
def test_randon():
    print (get_random_int())
    print (get_random_account_type())
    print (get_random_trans_type())
    print (get_random_trans_amount())
    print (get_timestamp())
    print(get_random_geolocation())

def test_class():
    myTest = DataAccessUtil()
    myTest.create_transactions()

test_class()