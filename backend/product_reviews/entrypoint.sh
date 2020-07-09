#!/bin/bash

# wait for PSQL to server to start
sleep 5
echo "Django Configuration"

# prepare init migration
echo "prepare init migration"

source /code/dev.env
python /code/manage.py makemigrations

# migrate db, so we have the latest db schema
echo "migrate db"
python /code/manage.py migrate

echo "Running fixtures data ..."
echo "Loading Products data ..."

python /code/manage.py loaddata ./fixtures/products_data.json

# start development server on public ip interface, on port 8000
python /code/manage.py runserver 0.0.0.0:8000
