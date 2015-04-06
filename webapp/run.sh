#!/bin/sh

su -m myuser -c "python manage.py migrate --noinput"
su -m myuser -c "python manage.py collectstatic --noinput"
su -m myuser -c "python manage.py compilemessages"
su -m myuser -c "gunicorn wsgi:application -b 0.0.0.0:8000"
