from rest_framework import serializers


class SettingsSerializer(serializers.Serializer):
    telegram_bot_name = serializers.CharField(max_length=32)
