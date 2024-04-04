from rest_framework import status
from rest_framework.response import Response

from amon_ra.api.views import HashedDataView
from amon_ra.apps.subscriptions.services import (
    create_subscription,
    send_notification,
    create_notification,
    get_subscription_by_chat_id,
)
from amon_ra.api.v1.subscriptions.serializers import (
    SubscriptionGetSerializer,
    SubscriptionLinkSerializer,
    NotificationSerializer,
    SubscriptionSerializer,
    SubscriptionUnlinkSerializer,
)
from amon_ra.apps.users.models import User


class SubscriptionView(HashedDataView):
    serializer_class = SubscriptionGetSerializer

    def create(self, request, *args, **kwargs):
        data = super().create(request, *args, **kwargs)
        if subscription := get_subscription_by_chat_id(data["chat_id"], raise_exception=False):
            serializer = SubscriptionSerializer(subscription)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SubscriptionLinkView(HashedDataView):
    serializer_class = SubscriptionLinkSerializer

    def create(self, request, *args, **kwargs):
        data = super().create(request, *args, **kwargs)
        email = data.pop("email").lower()
        queryset = User.objects.filter(email__iexact=email)
        if queryset.exists():
            create_subscription(user=queryset.last(), data=data)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SubscriptionUnlinkView(HashedDataView):
    serializer_class = SubscriptionUnlinkSerializer

    def create(self, request, *args, **kwargs):
        data = super().create(request, *args, **kwargs)
        if subscription := get_subscription_by_chat_id(data["chat_id"], raise_exception=False):
            subscription.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class NotificationView(HashedDataView):
    serializer_class = NotificationSerializer

    def create(self, request, *args, **kwargs):
        data = super().create(request, *args, **kwargs)
        notification = create_notification(client=request.client, **data)
        send_notification(notification=notification)
        return Response(status=status.HTTP_201_CREATED)
