from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

import pytest

from amon_ra.apps.subscriptions.models import Notification
from amon_ra.tests.factories.subscriptions import NotificationDictFactory, SubscriptionFactory


@pytest.mark.django_db
class TestNotificationsAPI:

    def setup_method(self):
        self.client = APIClient()
        self.url = reverse("api:v1:subscriptions:notification")
        self.user = SubscriptionFactory().user

    def test_anonymous_user(self):
        response = self.client.get(self.url, format="json")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.parametrize("method", ["get", "put", "patch", "delete"])
    def test_not_allowed_methods(self, method):
        self.client.force_authenticate(self.user)
        test_client_callable = getattr(self.client, method)
        response = test_client_callable(self.url, format="json")
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_create_notification(self):
        self.client.force_authenticate(self.user)

        data = NotificationDictFactory()
        response = self.client.post(self.url, data, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert Notification.objects.exists()
