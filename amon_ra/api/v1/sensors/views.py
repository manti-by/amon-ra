from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from amon_ra.api.v1.sensors.serializers import SensorSerializer
from amon_ra.apps.sensors.models import Sensor
from amon_ra.apps.sensors.services import create_sensor


class SensorsView(CreateAPIView, ListAPIView):
    serializer_class = SensorSerializer

    def get_queryset(self):
        return Sensor.objects.order_by("-created_at")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        shot = create_sensor(**serializer.validated_data)
        serializer = self.get_serializer(shot)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
