import hashlib
import hmac

from django.conf import settings
from django.http import HttpRequest
from rest_framework.reverse import reverse

from .exceptions import TelegramHashIsInvalidException
from .models import Subscription, Notification
from ..users.models import User


def create_subscription(user: User, **kwargs) -> Subscription:
    return Subscription.objects.create(user=user, **kwargs)


def delete_subscription(user: User) -> tuple[int, int]:
    return user.subscription.delete()


def create_notification(title: str, text: str) -> Notification:
    return Notification.objects.create(title=title, text=text)


def send_notification(user: User, notification: Notification):
    user.subscription.send_notification(notification)


def get_telegram_redirect_url(request: HttpRequest) -> str:
    protocol = "https" if request.is_secure() else "http"
    host = request.get_host()
    path = reverse("api:v1:subscriptions:subscriptions")
    return f"{protocol}://{host}{path}"


def check_telegram_data_hash(data: dict, data_hash: str, raise_exception: bool = True) -> bool:
    data_string = "\n".join([f"{k}={v}" for k, v in sorted(list(data.items()))]).encode()
    secret = hashlib.sha256(settings.BOT_TOKEN.encode()).digest()
    signature = hmac.new(key=secret, msg=data_string, digestmod=hashlib.sha256)
    if raise_exception and signature.hexdigest() != data_hash:
        raise TelegramHashIsInvalidException
    return signature.hexdigest() == data_hash
