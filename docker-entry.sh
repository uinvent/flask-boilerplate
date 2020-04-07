#!/bin/sh

mv .env.sample .env
python manage.py init
python manage.py db upgrade
python manage.py runserver
