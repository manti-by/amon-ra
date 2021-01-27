from rest_framework import serializers


class SensorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    temp = serializers.IntegerField()
    humidity = serializers.DecimalField(max_digits=5, decimal_places=2)
    moisture = serializers.DecimalField(max_digits=5, decimal_places=2)
    luminosity = serializers.DecimalField(max_digits=5, decimal_places=2)
    created_at = serializers.DateTimeField(read_only=True)


class PhotoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    file = serializers.FileField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
