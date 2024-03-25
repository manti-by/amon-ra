from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

import pytest

from amon_ra.apps.subscriptions.models import Subscription
from amon_ra.tests.factories.client import ClientFactory
from amon_ra.tests.factories.subscriptions import (
    SubscriptionLinkDictFactory,
    SubscriptionFactory,
    SubscriptionGetDictFactory,
    SubscriptionUnlinkDictFactory,
)
from amon_ra.tests.factories.users import UserFactory


@pytest.mark.django_db
class TestSubscriptionAPI:

    def setup_method(self):
        self.client = APIClient()
        self.app_client = ClientFactory()
        self.url = reverse("api:v1:subscription:get")

    def test_subscription_get(self):
        subscription = SubscriptionFactory()
        data = SubscriptionGetDictFactory(chat_id=subscription.data["chat_id"])
        response = self.client.post(self.url, data=data, format="json")
        assert response.status_code == status.HTTP_200_OK

    def test_subscription_get__subscription_does_not_exists(self):
        data = SubscriptionGetDictFactory()
        response = self.client.post(self.url, data=data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_subscription_unlink__unauthorized(self):
        response = self.client.get(self.url, format="json")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.parametrize("method", ["put", "patch", "delete"])
    def test_subscription_get__not_allowed_methods(self, method):
        test_client_callable = getattr(self.client, method)
        response = test_client_callable(self.url, data={"key": self.app_client.key}, format="json")
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
class TestSubscriptionLinkAPI:

    def setup_method(self):
        self.client = APIClient()
        self.app_client = ClientFactory()
        self.url = reverse("api:v1:subscription:link")

    def test_subscription_link(self):
        user = UserFactory()
        data = SubscriptionLinkDictFactory(email=user.email)
        response = self.client.post(self.url, data=data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert Subscription.objects.exists()

    def test_subscription_link__user_does_not_exists(self):
        data = SubscriptionLinkDictFactory()
        response = self.client.post(self.url, data=data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert not Subscription.objects.exists()

    def test_subscription_unlink__unauthorized(self):
        response = self.client.get(self.url, format="json")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.parametrize("method", ["put", "patch", "delete"])
    def test_subscription_link__not_allowed_methods(self, method):
        test_client_callable = getattr(self.client, method)
        response = test_client_callable(self.url, data={"key": self.app_client.key}, format="json")
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
class TestSubscriptionUnlinkAPI:

    def setup_method(self):
        self.client = APIClient()
        self.app_client = ClientFactory()
        self.url = reverse("api:v1:subscription:unlink")

    def test_subscription_unlink(self):
        subscription = SubscriptionFactory()
        data = SubscriptionUnlinkDictFactory(chat_id=subscription.data["chat_id"])
        response = self.client.post(self.url, data=data, format="json")
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Subscription.objects.exists()

    def test_subscription_unlink__subscription_does_not_exists(self):
        data = SubscriptionUnlinkDictFactory()
        response = self.client.post(self.url, data=data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_subscription_unlink__unauthorized(self):
        response = self.client.get(self.url, format="json")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.parametrize("method", ["put", "patch", "delete"])
    def test_subscription_unlink__not_allowed_methods(self, method):
        test_client_callable = getattr(self.client, method)
        response = test_client_callable(self.url, data={"key": self.app_client.key}, format="json")
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
