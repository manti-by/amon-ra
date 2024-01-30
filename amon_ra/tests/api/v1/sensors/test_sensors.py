from decimal import Decimal

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

import pytest

from amon_ra.apps.sensors.models import Sensor
from amon_ra.tests.factories.sensors import SensorDictFactory, SensorFactory
from amon_ra.tests.factories.users import UserFactory


@pytest.mark.django_db
class TestSensorsView:

    def setup_method(self):
        self.client = APIClient()
        self.url = reverse("api:v1:sensors:sensors")
        self.user = UserFactory()

    def test_anonymous_user(self):
        response = self.client.get(self.url, format="json")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.parametrize("method", ["put", "patch", "delete"])
    def test_not_allowed_methods(self, method):
        self.client.force_authenticate(self.user)
        test_client_callable = getattr(self.client, method)
        response = test_client_callable(self.url, format="json")
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_sensors_list(self):
        self.client.force_authenticate(self.user)

        SensorFactory()
        response = self.client.get(self.url, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1

        SensorFactory()
        response = self.client.get(self.url, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 2

        SensorFactory()
        response = self.client.get(self.url, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 3

    def test_create_sensor(self):
        self.client.force_authenticate(self.user)

        self.data = SensorDictFactory()
        response = self.client.post(self.url, self.data, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["sensor_id"] == self.data["sensor_id"]
        assert Decimal(response.data["temp"]) == self.data["temp"]
        assert Decimal(response.data["humidity"]) == self.data["humidity"]
        assert Sensor.objects.exists()
