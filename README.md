My implementation of the Official Django Tutorial!

Before running project adjust your own setting for the local machine in local_settings.py file:

    SECRET_KEY = "Set-your-secret-key"
    DJANGO_DEBUG = set to True/False
    ALLOWED_HOSTS = ['set-allowed-hosts']

    Set your own database settings or use django-sqlite:
    DB_ENGINE = 'django.db.backends.sqlite3' 
    DB_NAME = BASE_DIR / 'db.sqlite3'
    DB_USER = ''
    DB_PASSWORD = ''
    DB_HOST = None

Run  python manage.py populate_polls_db   to populate database with polls!

Run  python manage.py runserver   to start development server!

Take few polls for fun :)