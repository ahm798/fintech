#!/bin/bash
set -o errexit
set -o pipefail
set -o nounset

python << END
import sys
import time
import psycopg2

suggest_unrecoverable_After =30
start = time.time()
while True:
    try:
        conn = psycopg2.connect(
            dbname='${POSTGRES_DB}',
            user='${POSTGRES_USER}',
            password='${POSTGRES_PASSWORD}',
            host='${POSTGRES_HOST}',
            port='${POSTGRES_PORT}',
        )
        conn.close()
        break
    except psycopg2.OperationalError as e:
        sys.stderr.write(f"Database not ready yet: {e}\n")
        if time.time() - start > suggest_unrecoverable_After:
            sys.stderr.write("Database not ready after 30 seconds, exiting...\n")
            sys.exit(1)
            time.sleep(5)
END

echo >&2 "Database is ready, starting Django server..."

exec "$@"


