from decimal import Decimal

from helios.apps.sensors.models import Sensor


def create_sensor(name: str, temp: Decimal, humidity: Decimal) -> Sensor:
    return Sensor.objects.create(
        name=name,
        temp=temp,
        humidity=humidity,
    )
