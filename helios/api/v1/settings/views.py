from django.conf import settings
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny

from helios.api.v1.settings.serializers import SettingsSerializer


class SettingsView(RetrieveAPIView):
    serializer_class = SettingsSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        return {
            "push_public_key": settings.PUSH_PUBLIC_KEY,
        }
