import hashlib
import hmac

from django.conf import settings
from django.http import HttpRequest
from rest_framework.reverse import reverse

from .exceptions import TelegramHashIsInvalidException
from .models import Subscription, Notification
from ..users.models import User


def create_subscription(**kwargs) -> Subscription:
    return Subscription.objects.create(**kwargs)


def link_subscription(user: User, uuid: str):
    Subscription.objects.filter(uuid=uuid, user__isnull=True).update(user=user)


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


def get_telegram_data_hash(data: dict) -> str:
    data_string = "\n".join([f"{k}={v}" for k, v in sorted(list(data.items()))]).encode()
    secret = hashlib.sha256(settings.BOT_TOKEN.encode()).digest()
    signature = hmac.new(key=secret, msg=data_string, digestmod=hashlib.sha256)
    return signature.hexdigest()


def check_telegram_data_hash(data: dict, data_hash: str, raise_exception: bool = True) -> bool:
    is_hashes_equal = get_telegram_data_hash(data) == data_hash
    if raise_exception and not is_hashes_equal:
        raise TelegramHashIsInvalidException
    return is_hashes_equal
