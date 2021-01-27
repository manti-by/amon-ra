from decimal import Decimal

from django.contrib.auth.models import User

from helios.apps.sensors.models import Sensor, Photo


def create_sensor(
    user: User, temp: Decimal, humidity: Decimal, moisture: Decimal, luminosity: Decimal
) -> Sensor:
    return Sensor.objects.create(
        temp=temp,
        humidity=humidity,
        moisture=moisture,
        luminosity=luminosity,
        created_by=user,
    )


def create_photo(user: User, file: str) -> Photo:
    return Photo.objects.create(file=file, created_by=user)
