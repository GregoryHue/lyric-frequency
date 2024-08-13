#!/usr/bin/env bash
# Exit on error
set -o errexit

pip install -r requirements.txt
python manage.py makemigrations django
python manage.py migrate
python manage.py tailwind build
python manage.py collectstatic --no-input