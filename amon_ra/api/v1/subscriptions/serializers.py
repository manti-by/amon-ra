from rest_framework import serializers

from amon_ra.apps.core.services import check_data_hash
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


class HashedDataSerializer(serializers.Serializer):
    serialize_fields = None
    key = serializers.CharField(max_length=255, write_only=True)
    hash = serializers.CharField(max_length=255, write_only=True)

    def is_valid(self, *, raise_exception: bool = False) -> bool:
        if result := super().is_valid(raise_exception=raise_exception):
            data = self.validated_data
            return check_data_hash(
                data=data,
                data_hash=data.pop("hash"),
                secret_key=str(self.context["request"].api_client.hash),
                raise_exception=raise_exception,
            )
        return result

    def serialize(self):
        if not self.serialize_fields:
            return self.validated_data
        return {field: self.validated_data[field] for field in self.serialize_fields}


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
