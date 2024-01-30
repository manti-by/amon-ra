from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

import pytest

from amon_ra.apps.subscriptions.models import Subscription
from amon_ra.tests.factories.users import UserFactory
from amon_ra.tests.factories.subscriptions import SubscriptionDictFactory


@pytest.mark.django_db
class TestSubscriptionsAPI:

    def setup_method(self):
        self.client = APIClient()
        self.url = reverse("api:v1:subscriptions:subscriptions")
        self.user = UserFactory()

    def test_anonymous_user(self):
        response = self.client.get(self.url, format="json")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.parametrize("method", ["get", "put", "patch"])
    def test_not_allowed_methods(self, method):
        self.client.force_authenticate(self.user)
        test_client_callable = getattr(self.client, method)
        response = test_client_callable(self.url, format="json")
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_create_and_delete_subscription(self):
        self.client.force_authenticate(self.user)

        self.data = SubscriptionDictFactory()
        response = self.client.post(self.url, self.data, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert Subscription.objects.exists()

        response = self.client.delete(self.url, self.data, format="json")
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Subscription.objects.exists()
