from django.conf import settings
from django.contrib.auth.models import User
from pywebpush import webpush

from .models import Subscription, Notification


def create_subscription(user: User, **kwargs) -> Subscription:
    return Subscription.objects.create(user=user, **kwargs)


def delete_subscription(user: User, endpoint: str) -> tuple[int, int]:
    return Subscription.objects.get(user=user, endpoint=endpoint).delete()


def create_notification(title: str, text: str) -> Notification:
    return Notification.objects.create(title=title, text=text)


def send_notification(user: User, notification: Notification):
    for subscription in user.subscriptions.all():
        webpush(
            subscription_info=subscription.serialize(),
            data=f"{notification.title}:{notification.text}",
            vapid_private_key=settings.PUSH_PRIVATE_KEY,
            vapid_claims={"sub": f"mailto:{settings.PUSH_EMAIL}"},
        )
