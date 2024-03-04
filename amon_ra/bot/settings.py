import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

BOT_TOKEN = None
if (BASE_DIR / "bot.token").is_file():
    with open(BASE_DIR / "bot.token") as file:
        BOT_TOKEN = file.read().strip()

DJANGO_HOST = os.getenv("DJANGO_HOST", "http://localhost:8000")
