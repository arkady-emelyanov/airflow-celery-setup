#!/usr/bin/env bash
set -eo pipefail

# wait for redis and postgres becomes active
/etc/compose-config/wait-for-it.sh redis:6379
/etc/compose-config/wait-for-it.sh postgres:5432

# perform airflow initialization
/usr/bin/airflow initdb

# start server and scheduler
exec /usr/bin/supervisord -n -c /etc/compose-config/supervisord.conf
