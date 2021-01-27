from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from helios.api.v1.sensors.serializers import SensorSerializer, PhotoSerializer
from helios.apps.sensors.models import Sensor, Photo
from helios.apps.sensors.services import create_sensor, create_photo


class SensorsView(CreateAPIView, ListAPIView):

    serializer_class = SensorSerializer

    def get_queryset(self):
        return Sensor.objects.filter(created_by=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        shot = create_sensor(request.user, **serializer.validated_data)
        serializer = self.get_serializer(shot)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PhotoView(CreateAPIView, ListAPIView):

    serializer_class = PhotoSerializer

    def get_queryset(self):
        return Photo.objects.filter(created_by=self.request.user)

    def create(self, request, *args, **kwargs):
        try:
            file = request.data["file"]
        except KeyError:
            raise ValidationError("Request has no file attached")
        shot = create_photo(request.user, file)
        serializer = self.get_serializer(shot)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
