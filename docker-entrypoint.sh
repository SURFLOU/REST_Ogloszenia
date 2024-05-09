#!/bin/sh

# Apply Django migrations before starting the server
python manage.py migrate

# Start Gunicorn server
exec gunicorn --bind :8000 --workers 2 ogloszenia_project.wsgi
