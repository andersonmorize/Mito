#!/bin/sh

set -e # exit if errors happen anywhere
python manage.py collectstatic --noinput
python manage.py migrate
uwsgi --socket :8000 --master --enable-threads --module config.wsgi

