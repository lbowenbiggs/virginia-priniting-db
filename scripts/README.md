Scripts
=======

This directory is for scripts that are useful in development but inappropriate for deployment.

# populate_db.py
Run this in a python prompt to populate the database with some objects.

Make sure you are in the django virtual environment, have updated the database to the correct version, and have the `DJANGO_SETTINGS_MODULE` environment variable set to `VPDB.settings`.

For exmaple, on Linux run:
```bash
# Activate django virtual environment
user@host ~/VPDB $ source ~/.virtualenvs/djangodev/bin/activate
# Make migration to current database version
(djangodev) user@host ~/VPDB $ python manage.py makemigrations
# Apply migration to update database
(djangodev) user@host ~/VPDB $ python manage.py migrate
# Set environment variable so the script can import site-specific objects
# On Windows, you would run: set DJANGO_SETTINGS_MODULE=VPDB.settings
(djangodev) user@host ~/VPDB $ export DJANGO_SETTINGS_MODULE=VPDB.settings
# Run script to populate the database
(djangodev) user@host ~/VPDB $ python scripts/populate_db.py
```
