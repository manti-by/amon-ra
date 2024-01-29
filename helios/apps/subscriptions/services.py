from django.conf import settings
from django.contrib.auth.models import User
from pywebpush import webpush

from .models import Subscription


def create_subscription(user: User, **kwargs) -> Subscription:
    return Subscription.objects.create(user=user, **kwargs)


def delete_subscription(user: User, endpoint: str) -> tuple[int, int]:
    return Subscription.objects.get(user=user, endpoint=endpoint).delete()


def create_notification(user: User, title: str, text: str):
    for subscription in user.subscriptions.all():
        webpush(
            subscription_info=subscription.serialize(),
            data=f"{title}: {text}",
            vapid_private_key=settings.PUSH_PRIVATE_KEY,
            vapid_claims={"sub": f"mailto:{settings.PUSH_EMAIL}"},
        )
