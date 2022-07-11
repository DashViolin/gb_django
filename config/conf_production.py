import os

from .settings import *

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "generate_new_valid_key")

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("PGSQL_DB_NAME"),
        "USER": os.environ.get("PGSQL_DB_USER"),
        "PASSWORD": os.environ.get("PGSQL_DB_PASSWD"),
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

del STATICFILES_DIRS
STATIC_ROOT = BASE_DIR / "static"
