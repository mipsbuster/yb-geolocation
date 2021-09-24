import logging


listen_port = 8080
db_user = 'yugabyte'
db_password = None
database = 'geolocation'
schema = 'public'
db_host = '172.151.0.150'
db_port = 5433

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )