import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

BOT_TOKEN = None
if (BASE_DIR / "bot.token").is_file():
    with open(BASE_DIR / "bot.token") as file:
        BOT_TOKEN = file.read().strip()

DJANGO_HOST = os.getenv("DJANGO_HOST", "http://localhost:8000")

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_HANDLERS = os.getenv("LOG_HANDLERS", "console")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s %(levelname)-8s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        "file": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": os.getenv("LOG_PATH", "/var/log/amon-ra/bot.log"),
            "formatter": "standard",
        },
    },
    "loggers": {"": {"handlers": LOG_HANDLERS.split(","), "level": LOG_LEVEL, "propagate": True}},
}
