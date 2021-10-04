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
import sys, getopt
from sys import argv

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

def FakeTransaction():
    try:
        # get a class
        new_transactions = Transactions()

        # fill in all the fields with fake data
        new_transactions.user_id = get_random_int()
        new_transactions.account_id = get_random_int()
        new_transactions.account_type = get_random_account_type()
        new_transactions.txn_type = get_random_trans_type()
        new_transactions.amount = get_random_trans_amount()
        new_transactions.geo_partition = get_random_geolocation()
        new_transactions.created_at = get_timestamp()
    except Exception as e:
        logging.error('*** Exception in create_transaction: %s' % e)
        traceback.print_exc()

    return new_transactions

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
            #get a class
            new_transactions = FakeTransaction()

            #fill in all the fields with fake data
            '''
            new_transactions.user_id = get_random_int()
            new_transactions.account_id = get_random_int()
            new_transactions.account_type = get_random_account_type()
            new_transactions.txn_type = get_random_trans_type()
            new_transactions.amount = get_random_trans_amount()
            new_transactions.geo_partition = get_random_geolocation()
            new_transactions.created_at = get_timestamp()
            '''

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

def create_one_transaction(self):

        session = self.Session()

        try:
            #get a class
            new_transactions = FakeTransaction()

            #fill in all the fields with fake data


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

def get_args(argv):
    print('args')
    totalRecords = 1
    run_option = ''
    try:
        print("try")
        opts, args = getopt.getopt(argv, "hi:o:", ["m=", "s="])
        print(opts)
        print(args)
    except getopt.GetoptError:
        print("error")
        print('workloads.py -m <qty> -s ')
        sys.exit(2)
    #for opt, arg in opts:
    opt = opts
    if opt == '-h':
        print('workloads.py -m <qty> -o ')
        sys.exit()
    elif opt == '-m=':
        totalRecords = args[0]
        run_option = 'many'
    elif opt == '-s':
        run_option = 'one'

    print('Insert many is "', run_option)

    print('Insert one is "', run_option)

def run_workload(workload,qty):
    '''
    take the command line value for -w and run the SQL of the workload for a desired workload. in this version simply a number of times to
    run the specific workload.
    Will add options in next versions for time and parallel
    :return:
    '''
    print("Running workload: ",workload," for qty: ",qty)

def run(sysagrs):
    totalRecords = 1
    workload_option = ''

    #print('Number of arguments:', len(sys.argv), 'arguments.')
    #print('Argument List:', str(sys.argv))
    #print('Length of args ',len (sys.argv))

    argumentsListIncludingFileName = sys.argv
    argumentsListExcludingFileName = argumentsListIncludingFileName[1:]
    optionsString = "w:q:h"

    #print(argumentsListIncludingFileName[1:])

    if len(sys.argv) != 5:
        print("Usage: ./workloads.py  -h -m <total_records_to_insert> -s <inster_one>")
        print("Note: enter a note here ','")
        exit(1)
    optionANDvalues, remainingArguments = getopt.getopt(argumentsListExcludingFileName, optionsString)

    for k, v in optionANDvalues:
        try:
            if k == '-h':
                print("command is help")
                print("Usage: ./workloads.py  -m <workload_type> -q <total_records_to_insert>")
                print("Note: enter a note here ','")
            if k == '-w':
                workload_option = v
                print('command for workload type:',workload_option)
                run_workload(workload_option,argv[4])
            if k == '-q':
                totalRecords = v
                print('quantity to insert:',totalRecords)
        except:
            print("error")
            print('workloads.py -m <workload_type> -q <total_records_to_insert>')

if __name__ == "__main__":
   run(sys.argv[1:])