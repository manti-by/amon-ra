from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from pywebpush import webpush


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
