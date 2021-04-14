from .base import *  # noqa

DEBUG = False

SECRET_KEY = "#w2&o&%kx!(k!+j(++om%t7w+af2!5zyf7lex7l09iubr53wrc"

ALLOWED_HOSTS = ["127.0.0.1", "helios.manti.by"]

BASE_URL = "https://helios.manti.by"

STATIC_ROOT = "/var/lib/helios/static/"
MEDIA_ROOT = "/var/lib/helios/media/"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "/var/lib/helios/data/db.sqlite3",
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "helios",
    }
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "app": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "/var/log/helios/app.log",
        },
        "django": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "/var/log/helios/django.log",
        },
        "null": {"class": "logging.NullHandler"},
    },
    "loggers": {
        "": {
            "handlers": ["app"],
            "level": "DEBUG",
            "propagate": True,
            "formatter": "verbose",
        },
        "django": {
            "handlers": ["django"],
            "level": "DEBUG",
            "propagate": True,
            "formatter": "simple",
        },
        "django.template": {"handlers": ["null"]},
        "django.db.backends": {"handlers": ["null"]},
    },
}
