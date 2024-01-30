from rest_framework import serializers


class SettingsSerializer(serializers.Serializer):
    push_public_key = serializers.CharField(max_length=255)
