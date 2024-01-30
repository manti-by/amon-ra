from rest_framework import serializers


class SensorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    external_id = serializers.IntegerField()
    sensor_id = serializers.CharField(max_length=32)
    temp = serializers.DecimalField(max_digits=5, decimal_places=2)
    humidity = serializers.DecimalField(max_digits=5, decimal_places=2)
    created_at = serializers.DateTimeField()
