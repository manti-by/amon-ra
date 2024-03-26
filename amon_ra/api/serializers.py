from rest_framework import serializers

from amon_ra.apps.core.services import check_data_hash


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
