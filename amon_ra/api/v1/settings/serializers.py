from rest_framework import serializers


class SettingsSerializer(serializers.Serializer):
    telegram_redirect_url = serializers.CharField(max_length=255)
