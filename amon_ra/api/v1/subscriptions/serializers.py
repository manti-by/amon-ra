from rest_framework import serializers

from amon_ra.api.serializers import HashedDataSerializer
from amon_ra.apps.subscriptions.models import Subscription


class SubscriptionSerializer(serializers.Serializer):
    chat_id = serializers.IntegerField(source="data.chat_id")
    username = serializers.SerializerMethodField()

    @staticmethod
    def get_username(obj: Subscription) -> str:
        username = (obj.data.get("first_name"), obj.data.get("last_name"))
        if any(username):
            return " ".join(filter(lambda x: x, username))
        return obj.data.get("username")


class SubscriptionGetSerializer(HashedDataSerializer):
    serialize_fields = ("chat_id",)
    chat_id = serializers.IntegerField()


class SubscriptionLinkSerializer(HashedDataSerializer):
    serialize_fields = ("email", "chat_id", "username", "first_name", "last_name")
    email = serializers.CharField(max_length=255)
    chat_id = serializers.IntegerField()
    username = serializers.CharField(max_length=255)
    first_name = serializers.CharField(max_length=255, allow_blank=True, required=False)
    last_name = serializers.CharField(max_length=255, allow_blank=True, required=False)


class SubscriptionUnlinkSerializer(SubscriptionGetSerializer): ...


class NotificationSerializer(HashedDataSerializer):
    serialize_fields = ("title", "text")
    title = serializers.CharField(max_length=64)
    text = serializers.CharField(max_length=255)
