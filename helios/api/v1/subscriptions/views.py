from django.db import IntegrityError
from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.response import Response

from helios.apps.subscriptions.services import create_subscription, delete_subscription, create_notification
from helios.api.v1.subscriptions.serializers import SubscriptionSerializer, NotificationSerializer


class SubscriptionView(CreateAPIView, DestroyAPIView):
    serializer_class = SubscriptionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            create_subscription(user=request.user, **serializer.validated_data)
        except IntegrityError:
            return Response(status=status.HTTP_208_ALREADY_REPORTED)
        return Response(status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        delete_subscription(user=request.user, endpoint=serializer.validated_data.get("endpoint"))
        return Response(status=status.HTTP_204_NO_CONTENT)


class NotificationView(CreateAPIView):
    serializer_class = NotificationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_notification(user=request.user, **serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)
