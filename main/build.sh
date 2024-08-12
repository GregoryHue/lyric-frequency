#!/usr/bin/env bash
# Exit on error
set -o errexit

cd main
pip install -r requirements.txt
python manage.py makemigrations django
python manage.py migrate
python manage.py collectstatic --no-input