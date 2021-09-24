from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey,NUMERIC,TIMESTAMP
from sqlalchemy.orm import sessionmaker, relationship
import config as cfg

Base = declarative_base()
Base.metadata.schema = 'ysql_sqlalchemy'


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
               (self.userid, self.accountid, self.account_type, self.amount, self.geolocation, self.txn_type, self.created)

    def to_json(self):
        transaction_json = {
           "userid": self.userid,
            "accountid": self.accountid,
            "account_type": self.account_type,
            "self_amount": self.amount,
            "geolocation": self.geolocation,
            "txn_type": self.txn_type,
            "created": self.created
        }
        return transaction_json