from django.db import IntegrityError
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from amon_ra.apps.subscriptions.exceptions import TelegramHashIsInvalidException
from amon_ra.apps.subscriptions.models import TelegramAuthStatus
from amon_ra.apps.subscriptions.services import (
    create_subscription,
    send_notification,
    create_notification,
    link_subscription,
)
from amon_ra.api.v1.subscriptions.serializers import (
    SubscriptionSerializer,
    NotificationSerializer,
    SubscriptionLinkSerializer,
)


class SubscriptionView(RetrieveAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = (AllowAny,)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        response = redirect("index")
        try:
            subscription = create_subscription(data=serializer.validated_data)
            response.set_cookie("telegram_auth", TelegramAuthStatus.OK, max_age=None)
            response.set_cookie("telegram_uuid", subscription.uuid, max_age=None)
        except TelegramHashIsInvalidException:
            response.set_cookie("telegram_auth", TelegramAuthStatus.ERROR, max_age=None)
        except IntegrityError:
            response.set_cookie("telegram_auth", TelegramAuthStatus.EXISTS, max_age=None)
        return response


class SubscriptionLinkView(CreateAPIView):
    serializer_class = SubscriptionLinkSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        link_subscription(user=request.user, **serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)


class NotificationView(CreateAPIView):
    serializer_class = NotificationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        notification = create_notification(**serializer.validated_data)
        send_notification(user=request.user, notification=notification)
        return Response(status=status.HTTP_201_CREATED)
