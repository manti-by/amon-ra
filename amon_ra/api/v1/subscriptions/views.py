from django.db import IntegrityError
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.response import Response

from amon_ra.apps.subscriptions.exceptions import TelegramHashIsInvalidException
from amon_ra.apps.subscriptions.models import TelegramAuthStatus
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
        response = redirect("index")
        try:
            create_subscription(user=request.user, data=serializer.validated_data)
            response.set_cookie("telegram_auth", TelegramAuthStatus.OK, max_age=None)
        except TelegramHashIsInvalidException:
            response.set_cookie("telegram_auth", TelegramAuthStatus.ERROR, max_age=None)
        except IntegrityError:
            response.set_cookie("telegram_auth", TelegramAuthStatus.EXISTS, max_age=None)
        return response

    def destroy(self, request, *args, **kwargs):
        delete_subscription(user=request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)


class NotificationView(CreateAPIView):
    serializer_class = NotificationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        notification = create_notification(**serializer.validated_data)
        send_notification(user=request.user, notification=notification)
        return Response(status=status.HTTP_201_CREATED)
