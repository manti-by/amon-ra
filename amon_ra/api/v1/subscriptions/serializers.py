from rest_framework import serializers


class SubscriptionKeysSerializer(serializers.Serializer):
    p256dh = serializers.CharField(max_length=255)
    auth = serializers.CharField(max_length=255)


class SubscriptionSerializer(serializers.Serializer):
    endpoint = serializers.CharField(max_length=255)
    expiration_time = serializers.DateTimeField(allow_null=True, required=False)
    keys = SubscriptionKeysSerializer()


class NotificationSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=64)
    text = serializers.CharField(max_length=255)
