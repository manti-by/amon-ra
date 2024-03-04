from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny

from amon_ra.api.v1.settings.serializers import SettingsSerializer
from amon_ra.apps.subscriptions.services import get_telegram_redirect_url


class SettingsView(RetrieveAPIView):
    serializer_class = SettingsSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        return {
            "telegram_redirect_url": get_telegram_redirect_url(self.request)
        }
