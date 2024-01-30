import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from amon_ra.tests.factories import DEFAULT_USER_PASSWORD
from amon_ra.tests.factories.users import UserFactory


@pytest.mark.django_db
class TestUserAPI:

    def setup_method(self):
        self.client = APIClient()
        self.user = UserFactory()

    def test_login(self):
        data = {"email": self.user.email, "password": DEFAULT_USER_PASSWORD}
        response = self.client.post(reverse("api:v1:user:login"), data=data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["token"]

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {response.json()['token']}")
        response = self.client.get(reverse("api:v1:sensors:sensors"), format="json")
        assert response.status_code == status.HTTP_200_OK
