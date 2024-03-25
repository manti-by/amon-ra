from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

import pytest

from amon_ra.apps.subscriptions.models import Notification
from amon_ra.tests.factories.client import ClientFactory
from amon_ra.tests.factories.subscriptions import NotificationDictFactory


@pytest.mark.django_db
class TestNotificationsAPI:

    def setup_method(self):
        self.client = APIClient()
        self.app_client = ClientFactory()
        self.url = reverse("api:v1:subscription:notification")

    def test_notifications_create(self):
        response = self.client.post(self.url, data=NotificationDictFactory(), format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert Notification.objects.exists()

    def test_subscription_unlink__unauthorized(self):
        response = self.client.get(self.url, format="json")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.parametrize("method", ["put", "patch", "delete"])
    def test_notifications_create__not_allowed_methods(self, method):
        test_client_callable = getattr(self.client, method)
        response = test_client_callable(self.url, data={"key": self.app_client.key}, format="json")
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
