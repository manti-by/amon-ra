from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

import pytest


@pytest.mark.django_db
class TestSettingsView:
    def setup_method(self):
        self.client = APIClient()
        self.url = reverse("api:v1:settings:settings")

    @pytest.mark.parametrize("method", ["post", "put", "patch", "delete"])
    def test_not_allowed_methods(self, method):
        test_client_callable = getattr(self.client, method)
        response = test_client_callable(self.url, format="json")
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_get_settings(self):
        response = self.client.get(self.url, format="json")
        assert response.status_code == status.HTTP_200_OK
