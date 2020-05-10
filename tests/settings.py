import os

from dotenv import load_dotenv

load_dotenv()

APP_NAME = "test"
SECRET_KEY = "secret"

USE_TZ = True
TIME_ZONE = "UTC"
USE_I18N = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT", 5432),
    }
}

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "tests",
)

AUTH_USER_MODEL = "tests.User"
