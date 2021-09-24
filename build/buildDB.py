import psycopg2

# Create the database connection.

conn = psycopg2.connect("host=127.0.0.1 port=5433 dbname=yugabyte user=yugabyte password=yugabyte")

# Open a cursor to perform database operations.
# The default mode for psycopg2 is "autocommit=false".

conn.set_session(autocommit=True)
cur = conn.cursor()

# Create the DB. (It might preexist.)

cur.execute(
  """
  DROP DATABASE IF EXISTS yb_geodemo
  """)
print("Dropped database yb_geodemo")
cur.execute(
  """
  CREATE DATABASE yb_geodemo with ALLOW_CONNECTIONS=true
  """)
print("Created database yb_geodemo")

cur.close()

# Commit and close down.

conn.commit()
cur.close()
conn.close()

#Connect to demo and build schema
# Create the database connection.

conn = psycopg2.connect("host=127.0.0.1 port=5433 dbname=yb_geodemo user=yugabyte password=yugabyte")

# Open a cursor to perform database operations.
# The default mode for psycopg2 is "autocommit=false".

conn.set_session(autocommit=True)
cur = conn.cursor()

# Create the DB. (It might preexist.)

cur.execute(
  """
  CREATE TABLE users (
    user_id   INTEGER NOT NULL,
    name varchar NOT NULL,
    geo_partition VARCHAR,
    created_at TIMESTAMP DEFAULT NOW()
) PARTITION BY LIST (geo_partition)
  """)
print("Created table users")
cur.execute(
  """
  CREATE TABLE accounts (
    user_id   INTEGER NOT NULL,
    account_id INTEGER NOT NULL,
    geo_partition VARCHAR,
    account_type VARCHAR NOT NULL,
    balance NUMERIC NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
) PARTITION BY LIST (geo_partition)
  """)
print("Created table accounts")

cur.execute(
  """
  CREATE TABLE transactions (
    user_id   INTEGER NOT NULL,
    account_id INTEGER NOT NULL,
    geo_partition VARCHAR,
    account_type VARCHAR NOT NULL,
    amount NUMERIC NOT NULL,
    txn_type VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
) PARTITION BY LIST (geo_partition)
  """)
print("Created table accounts")
cur.execute(
  """
  DROP TABLESPACE IF EXISTS us_east_2_tablespace
  """
)
cur.execute(
  """
  CREATE TABLESPACE us_east_2_tablespace WITH (
  replica_placement='{"num_replicas": 3, "placement_blocks":
  [{"cloud":"aws","region":"us-east-2","zone":"us-east-2a","min_num_replicas":1}]}'
)
  """)
print("Created tablespace us_east_2_tablespace")

cur.execute(
  """
  DROP TABLESPACE IF EXISTS eu_central_1_tablespace
  """
)
cur.execute(
  """
  CREATE TABLESPACE eu_central_1_tablespace WITH (
  replica_placement='{"num_replicas": 3, "placement_blocks":
  [{"cloud":"aws","region":"eu_central_1","zone":"eu_central_1-1a","min_num_replicas":1}]}'
)
  """)
print("Created tablespace eu_central_1_tablespace")

cur.execute(
  """
CREATE TABLE transactions_eu
    PARTITION OF transactions
      (user_id, account_id, geo_partition, account_type,
      amount, txn_type, created_at,
      PRIMARY KEY (user_id HASH, account_id, geo_partition))
    FOR VALUES IN ('EU') TABLESPACE eu_central_1_tablespace
 """)
print("Created table transactions_eu")
cur.close()

cur.execute(
  """
CREATE TABLE transactions_us
    PARTITION OF transactions
      (user_id, account_id, geo_partition, account_type,
      amount, txn_type, created_at,
      PRIMARY KEY (user_id HASH, account_id, geo_partition))
    FOR VALUES IN ('USA') TABLESPACE us_east_2_tablespace
 """)
print("Created table transactions_eu")
cur.close()

# Commit and close down.

conn.commit()
cur.close()
conn.close()