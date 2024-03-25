from django.conf import settings
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny

from amon_ra.api.v1.settings.serializers import SettingsSerializer


class SettingsView(RetrieveAPIView):
    serializer_class = SettingsSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        return {"telegram_bot_name": settings.BOT_NAME}
