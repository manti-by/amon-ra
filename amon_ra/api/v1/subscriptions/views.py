from django.db import IntegrityError
from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.response import Response

from amon_ra.apps.subscriptions.services import (
    create_subscription,
    delete_subscription,
    send_notification,
    create_notification,
)
from amon_ra.api.v1.subscriptions.serializers import SubscriptionSerializer, NotificationSerializer


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
        notification = create_notification(**serializer.validated_data)
        send_notification(user=request.user, notification=notification)
        return Response(status=status.HTTP_201_CREATED)
