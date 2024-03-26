from rest_framework import serializers

from amon_ra.api.serializers import HashedDataSerializer


class SensorSerializer(HashedDataSerializer):
    serialize_fields = ("external_id", "sensor_id", "temp", "humidity", "created_at")
    external_id = serializers.IntegerField()
    sensor_id = serializers.CharField(max_length=32)
    temp = serializers.DecimalField(max_digits=5, decimal_places=2)
    humidity = serializers.DecimalField(max_digits=5, decimal_places=2)
    created_at = serializers.DateTimeField()
