from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    is_telegram_linked = serializers.BooleanField()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
