from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from amon_ra.api.v1.sensors.serializers import SensorSerializer
from amon_ra.api.views import HashedDataView
from amon_ra.apps.sensors.models import Sensor
from amon_ra.apps.sensors.services import create_sensor


class SensorsView(ListAPIView):
    serializer_class = SensorSerializer

    def get_queryset(self):
        return Sensor.objects.order_by("-created_at")


class SensorsCreateView(HashedDataView):
    serializer_class = SensorSerializer

    def create(self, request, *args, **kwargs):
        data = super().create(request, *args, **kwargs)
        shot = create_sensor(**data)
        serializer = self.get_serializer(shot)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
