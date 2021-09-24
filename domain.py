class user:
  def __init__(self, userid,name, geolocation,created):
    self.name = name
    self.userid = userid
    self.geolocation = geolocation
    self.created = created

class account:
    def __init__(self,userid,account_type,accountid,balance,geolocation,created):
        self.userid = userid
        self.accountid = accountid
        self.account_type = account_type
        self,balance = balance
        self.geolocation = geolocation
        self.created = created

class transaction:
    def __init__(self,userid,account_type,accountid,amount,geolocation,txn_type,created):
        self.userid = userid
        self.accountid = accountid
        self.account_type = account_type
        self,amount = amount
        self.geolocation = geolocation
        self.txn_type = txn_type
        self.created = created
