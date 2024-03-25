from django.conf import settings
from django.shortcuts import render


def index(request):
    return render(request, "index.html", {"telegram_bot_name": settings.BOT_NAME})
