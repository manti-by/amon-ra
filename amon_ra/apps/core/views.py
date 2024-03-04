from django.shortcuts import render

from amon_ra.apps.subscriptions.services import get_telegram_redirect_url


def index(request):
    return render(request, "index.html", {"telegram_redirect_url": get_telegram_redirect_url(request)})
