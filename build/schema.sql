CREATE TABLE users (
    user_id   INTEGER NOT NULL,
    name varchar NOT NULL,
    geo_partition VARCHAR,
    created_at TIMESTAMP DEFAULT NOW()
) PARTITION BY LIST (geo_partition);

CREATE TABLE accounts (
    user_id   INTEGER NOT NULL,
    account_id INTEGER NOT NULL,
    geo_partition VARCHAR,
    account_type VARCHAR NOT NULL,
    balance NUMERIC NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
) PARTITION BY LIST (geo_partition);

CREATE TABLE transactions (
    user_id   INTEGER NOT NULL,
    account_id INTEGER NOT NULL,
    geo_partition VARCHAR,
    account_type VARCHAR NOT NULL,
    amount NUMERIC NOT NULL,
    txn_type VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
) PARTITION BY LIST (geo_partition);

CREATE TABLESPACE us_east_2_tablespace WITH (
  replica_placement='{"num_replicas": 3, "placement_blocks":
  [{"cloud":"aws","region":"us-east-2","zone":"us-east-2a","min_num_replicas":3}
  ]}'
);

CREATE TABLESPACE eu_central_1_tablespace WITH (
  replica_placement='{"num_replicas": 3, "placement_blocks":
  [{"cloud":"aws","region":"eu_central_1","zone":"eu_central_1-1a","min_num_replicas":3}
  ]}'
);

CREATE TABLE transactions_us
    PARTITION OF transactions
      (user_id, account_id, geo_partition, account_type,
      amount, txn_type, created_at,
      PRIMARY KEY (user_id HASH, account_id, geo_partition))
    FOR VALUES IN ('US') TABLESPACE us_east_2_tablespace;

CREATE TABLE transactions_eu
    PARTITION OF transactions
      (user_id, account_id, geo_partition, account_type,
      amount, txn_type, created_at,
      PRIMARY KEY (user_id HASH, account_id, geo_partition))
    FOR VALUES IN ('EU') TABLESPACE eu_central_1_tablespace;