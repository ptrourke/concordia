#!/bin/bash

set -e -u # Exit immediately for unhandled errors or undefined variables

mkdir -p /app/logs
touch /app/logs/concordia.log

echo Running makemigrations
./manage.py makemigrations --merge --noinput

echo Running migrations
./manage.py migrate

echo "Ensuring our base configuration is present in the database"
./manage.py ensure_initial_site_configuration

echo "Initializing difficulty values"
./manage.py initialize_difficulty_values

echo "Flattening, de-duping and refreshing tag data"
./manage.py flatten_tags
./manage.py dedupe_tags
./manage.py refresh_tags

if [ -v SENTRY_BACKEND_DSN ]; then
    echo "Testing Sentry configuration"
    ./manage.py raven test
fi

echo Running collectstatic
./manage.py collectstatic --clear --noinput -v0

echo Running Django dev server
gunicorn --log-level=warn --bind 0.0.0.0:80 --workers=4 concordia.wsgi
