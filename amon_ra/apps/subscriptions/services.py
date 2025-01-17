from ..clients.models import Client
from ..users.models import User
from .models import Notification, Subscription


def create_subscription(**kwargs) -> Subscription:
    return Subscription.objects.create(**kwargs)


def delete_subscription(user: User) -> tuple[int, int]:
    return user.subscription.delete()


def get_subscription_by_chat_id(chat_id: int, raise_exception: bool = True) -> Subscription:
    try:
        return Subscription.objects.get(data__chat_id=chat_id)
    except Subscription.DoesNotExist as e:
        if raise_exception:
            raise e


def create_notification(client: Client, title: str, text: str) -> Notification:
    return Notification.objects.create(client=client, title=title, text=text)


def send_notification(notification: Notification):
    for user in User.objects.filter(subscription__isnull=False):
        user.subscription.send_notification(notification)
