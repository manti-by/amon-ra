import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from amon_ra.tests.factories import DEFAULT_USER_PASSWORD
from amon_ra.tests.factories.users import UserFactory


@pytest.mark.django_db
class TestLoginAPI:

    def setup_method(self):
        self.client = APIClient()
        self.user = UserFactory()
        self.url = reverse("api:v1:user:login")

    @pytest.mark.parametrize("method", ["get", "put", "patch", "delete"])
    def test_login_not_allowed_methods(self, method):
        self.client.force_authenticate(self.user)
        test_client_callable = getattr(self.client, method)
        response = test_client_callable(self.url, format="json")
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_login(self):
        data = {"email": self.user.email, "password": DEFAULT_USER_PASSWORD}
        response = self.client.post(self.url, data=data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["token"]

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {response.json()['token']}")
        response = self.client.get(reverse("api:v1:sensors:list"), format="json")
        assert response.status_code == status.HTTP_200_OK
