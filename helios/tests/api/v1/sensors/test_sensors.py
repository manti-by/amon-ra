import io
from decimal import Decimal

from PIL import Image
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

import pytest

from helios.apps.sensors.models import Sensor
from helios.tests.factories.sensors import SensorDictFactory, SensorFactory
from helios.tests.factories.users import UserFactory


@pytest.mark.django_db
class TestSensorsView:
    @pytest.fixture(autouse=True)
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
        assert response.data["count"] == 0

        SensorFactory(created_by=self.user)
        response = self.client.get(self.url, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1

        SensorFactory(created_by=self.user)
        response = self.client.get(self.url, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 2

    def test_create_sensor(self):
        self.client.force_authenticate(self.user)

        self.data = SensorDictFactory()
        response = self.client.post(self.url, self.data, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["temp"] == self.data["temp"]
        assert Decimal(response.data["humidity"]) == self.data["humidity"]
        assert Decimal(response.data["moisture"]) == self.data["moisture"]
        assert Decimal(response.data["luminosity"]) == self.data["luminosity"]
        assert Sensor.objects.exists()


@pytest.mark.django_db
class TestPhotoView:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.client = APIClient()
        self.url = reverse("api:v1:sensors:photos")
        self.user = UserFactory()

        self.file = io.BytesIO()
        image_source = Image.new("RGBA", size=(100, 100), color=(155, 0, 0))
        image_source.save(self.file, "png")
        self.file.name = "test.png"
        self.file.seek(0)

    def test_anonymous_user(self):
        response = self.client.get(self.url, format="json")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.parametrize("method", ["put", "patch", "delete"])
    def test_not_allowed_methods(self, method):
        self.client.force_authenticate(self.user)
        test_client_callable = getattr(self.client, method)
        response = test_client_callable(self.url, format="json")
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_upload_photo(self):
        self.client.force_authenticate(self.user)
        response = self.client.post(self.url, {"file": self.file}, format="multipart")
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["file"]

        response = self.client.get(self.url, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1
