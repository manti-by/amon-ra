"""
Django settings for emails project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/latest/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "very-secret-key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ("*",)

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "amon_ra.apps.core",
    "amon_ra.apps.clients",
    "amon_ra.apps.sensors",
    "amon_ra.apps.subscriptions",
    "amon_ra.apps.users",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "amon_ra.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "amon_ra.wsgi.application"

BASE_URL = "https://amon-ra.manti.by"

CSRF_TRUSTED_ORIGINS = ("https://amon-ra.manti.by",)

AUTH_USER_MODEL = "users.User"


# Database
# https://docs.djangoproject.com/en/latest/ref/settings/#databases

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "amon_ra",
        "USER": "amon_ra",
        "PASSWORD": "amon_ra",
        "HOST": POSTGRES_HOST,
        "PORT": 5432,
    }
}


# Cache backend
# https://docs.djangoproject.com/en/latest/topics/cache/

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/latest/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Email settings

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = os.getenv("EMAIL_HOST", "localhost")
EMAIL_PORT = os.getenv("EMAIL_PORT", 25)
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", False)

DEFAULT_EMAIL_FROM = "amon-ra@manti.by"


# Internationalization
# https://docs.djangoproject.com/en/latest/topics/i18n/

LANGUAGE_CODE = "en-us"


def _(x):
    return x


LANGUAGES = (
    ("ru-ru", _("Russian")),
    ("en-us", _("English")),
)

LOCALE_PATHS = (BASE_DIR / "apps" / "core" / "locale",)

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/latest/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = (BASE_DIR / "static",)

STATIC_ROOT = "/var/lib/amon-ra/static/"
STATIC_URL = "/static/"

MEDIA_ROOT = "/var/lib/amon-ra/media/"
MEDIA_URL = "/media/"


# Rest Framework
# https://www.django-rest-framework.org/tutorial/quickstart/

REST_FRAMEWORK = {
    "PAGE_SIZE": 15,
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework.authentication.TokenAuthentication",),
}


DEFAULT_AUTO_FIELD = "django.db.models.AutoField"


# Telegram bot settings

BOT_NAME = os.getenv("BOT_NAME", "amon_ra_test_bot")

BOT_TOKEN = None
if (BASE_DIR.parent / "bot.token").is_file():
    with open(BASE_DIR.parent / "bot.token") as file:
        BOT_TOKEN = file.read().strip()
