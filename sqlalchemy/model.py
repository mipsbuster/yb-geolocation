from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, NUMERIC, TIMESTAMP
from sqlalchemy.orm import sessionmaker, relationship
import config as cfg

Base = declarative_base()
Base.metadata.schema = 'ysql_sqlalchemy'

valid_workloads = ["transactions"]


class Transactions(Base):
    __tablename__ = 'transactions'
    __table_args__ = {"schema": "{0}".format(cfg.schema)}

    user_id = Column(Integer, primary_key=True)
    account_id = Column(Integer, primary_key=True)
    account_type = Column(String, primary_key=True)
    amount = Column(NUMERIC)
    geo_partition = Column(String)
    txn_type = Column(String)
    created_at = Column(TIMESTAMP)

    #    orders = relationship('Order', foreign_keys=[user_id], primaryjoin='Order.user_id == User.user_id', uselist=True)

    def __repr__(self):
        return "<transaction(userid=%s accountid='%s', account_type='%s', amount='%s', geolocation='%s', txn_type='%s', created='%s')>" % \
               (self.user_id, self.account_id, self.account_type, self.amount, self.geo_partition, self.txn_type,
                self.created_at)

    def to_json(self):
        transaction_json = {
            "userid": self.user_id,
            "accountid": self.account_id,
            "account_type": self.account_type,
            "self_amount": self.amount,
            "geolocation": self.geo_partition,
            "txn_type": self.txn_type,
            "created": self.created_at
        }
        return transaction_json


class Account(Base):
    __tablename__ = 'accounts'
    __table_args__ = {"schema": "{0}".format(cfg.schema)}

    user_id = Column(Integer, primary_key=True)
    account_id = Column(Integer, primary_key=True)
    account_type = Column(String, primary_key=True)
    amount = Column(NUMERIC)
    geo_partition = Column(String)
    created_at = Column(TIMESTAMP)

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {"schema": "{0}".format(cfg.schema)}

    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    amount = Column(NUMERIC)
    geo_partition = Column(String)
    created_at = Column(TIMESTAMP)


class CountryCodes(Base):
    __tablename__ = 'county_codes'
    __table_args__ = {"schema": "{0}".format(cfg.schema)}

    code_id = Column(Integer, primary_key=True)
    name = Column(String)
    geo_partition = Column(String)
    created_at = Column(TIMESTAMP)