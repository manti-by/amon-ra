from rest_framework import serializers
import urllib.parse

from amon_ra.apps.subscriptions.services import check_telegram_data_hash


class SubscriptionSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255)
    auth_date = serializers.CharField(max_length=255)
    hash = serializers.CharField(max_length=255)

    first_name = serializers.CharField(max_length=255, allow_blank=True, required=False)
    last_name = serializers.CharField(max_length=255, allow_blank=True, required=False)
    photo_url = serializers.CharField(max_length=255, allow_blank=True, required=False)

    def to_internal_value(self, data: dict):
        data._mutable = True
        data["photo_url"] = urllib.parse.unquote(data["photo_url"])
        return super().to_internal_value(data)

    def is_valid(self, *, raise_exception: bool = False) -> bool:
        if result := super().is_valid(raise_exception=raise_exception):
            data = self.validated_data
            data_hash = data.pop("hash")
            return check_telegram_data_hash(data=data, data_hash=data_hash, raise_exception=raise_exception)
        return result


class SubscriptionLinkSerializer(serializers.Serializer):
    uuid = serializers.CharField(max_length=32)


class NotificationSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=64)
    text = serializers.CharField(max_length=255)
