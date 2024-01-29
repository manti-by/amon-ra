from datetime import datetime
from decimal import Decimal

from helios.apps.sensors.models import Sensor


def create_sensor(external_id: int, sensor_id: str, temp: Decimal, humidity: Decimal, created_at: datetime) -> Sensor:
    return Sensor.objects.create(
        external_id=external_id,
        sensor_id=sensor_id,
        temp=temp,
        humidity=humidity,
        created_at=created_at,
    )
