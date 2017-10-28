Scripts
=======

This directory is for scripts that are useful in development but inappropriate for deployment.

# populate_db.py
This will populate the database with 4 objects (one for each model) to use for testing.

To run from PyCharm, open the python console (under 'Tools', or by 'Tools'>'Run manage.py Task...' and typing ```shell```) and run the following command:
```python
exec(open("scripts/populate_db.py").read())
```

To run from a command line:
```bash
# Activate django virtual environment
user@host ~/VPDB $ source ~/.virtualenvs/djangodev/bin/activate
# Make migration to current database version
(djangodev) user@host ~/VPDB $ python manage.py makemigrations
# Apply migration to update database
# You don't need to run this if the previous command reports no changes detected
(djangodev) user@host ~/VPDB $ python manage.py migrate
# Enter the interactive django prompt
(djangodev) user@host ~/VPDB $ python manage.py shell
# Actually run the script
>>> exec(open("scripts/populate_db.py").read())
```

If this script is run again, it will just create duplicate objects. To clean up the database and start over, run:
```bash
(djangodev) user@host ~/VPDB $ python manage.py flush
```