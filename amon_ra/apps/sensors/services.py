from .models import Sensor


def create_sensor(**kwargs) -> Sensor:
    return Sensor.objects.create(**kwargs)
