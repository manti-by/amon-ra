from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

import pytest

from amon_ra.apps.subscriptions.models import Subscription
from amon_ra.tests.factories.subscriptions import SubscriptionDictFactory, SubscriptionFactory


@pytest.mark.django_db
class TestSubscriptionsAPI:

    def setup_method(self):
        self.client = APIClient()
        self.url = reverse("api:v1:subscriptions:subscriptions")

    @pytest.mark.parametrize("method", ["post", "put", "patch", "delete"])
    def test_not_allowed_methods_for_subscription(self, method):
        test_client_callable = getattr(self.client, method)
        response = test_client_callable(self.url, format="json")
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_create_subscription(self):
        data = SubscriptionDictFactory()
        response = self.client.get(self.url, data=data, format="json", follow=True)

        assert response.status_code == status.HTTP_200_OK
        assert Subscription.objects.exists()


@pytest.mark.django_db
class TestSubscriptionLinkAPI:

    def setup_method(self):
        self.client = APIClient()
        self.url = reverse("api:v1:subscriptions:subscription_link")
        self.subscription = SubscriptionFactory()
        self.user = self.subscription.user

    def test_anonymous_user(self):
        response = self.client.get(self.url, format="json")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.parametrize("method", ["get", "put", "patch", "delete"])
    def test_not_allowed_methods_for_subscription(self, method):
        self.client.force_authenticate(self.user)
        test_client_callable = getattr(self.client, method)
        response = test_client_callable(self.url, format="json")
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_link_subscription(self):
        self.client.force_authenticate(self.user)

        response = self.client.post(self.url, data={"uuid": self.subscription.uuid}, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert Subscription.objects.exists()
