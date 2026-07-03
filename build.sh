#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Running migrations..."
python manage.py migrate

echo "Loading initial data..."
# Use --ignorenonexistent in case the fixture is already loaded and modified
python manage.py loaddata core/fixtures/initial_data.json
