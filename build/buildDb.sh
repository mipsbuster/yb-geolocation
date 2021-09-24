./bin/ysqlsh -U yugabyte -d yugabyte -c "CREATE DATABASE yb_demo with ALLOW_CONNECTIONS=true CONNECTION LIMIT=10"
./bin/ysqlsh -U yugabyte -d yugabyte -d yb_demo -a -f ./schema.sql