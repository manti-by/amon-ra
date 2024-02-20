from django.conf import settings
from django.core.management import BaseCommand
from pywebpush import webpush

from amon_ra.apps.users.models import User


class Command(BaseCommand):
    help = "Send push notifications to all users"

    def handle(self, *args, **options):
        for user in User.objects.all():
            for subscription in user.subscriptions.all():
                webpush(
                    subscription_info=subscription.serialize(),
                    data="Test:Message",
                    vapid_private_key=settings.PUSH_PRIVATE_KEY,
                    vapid_claims={"sub": f"mailto:{settings.PUSH_EMAIL}"},
                )
