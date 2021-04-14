import factory.fuzzy
from factory.django import DjangoModelFactory

from helios.apps.sensors.models import Sensor


class SensorDictFactory(factory.Factory):
    class Meta:
        model = dict

    temp = factory.Faker("pyint", min_value=-20, max_value=30)
    humidity = factory.Faker(
        "pydecimal",
        left_digits=5,
        right_digits=2,
        min_value=0,
        max_value=100,
    )
    moisture = factory.Faker(
        "pydecimal",
        left_digits=5,
        right_digits=2,
        min_value=0,
        max_value=100,
    )
    luminosity = factory.Faker(
        "pydecimal",
        left_digits=5,
        right_digits=2,
        min_value=0,
        max_value=100,
    )


class SensorFactory(DjangoModelFactory):
    class Meta:
        model = Sensor

    temp = factory.Faker("pyint", min_value=-20, max_value=30)
    humidity = factory.Faker(
        "pydecimal",
        left_digits=5,
        right_digits=2,
        min_value=0,
        max_value=100,
    )
    moisture = factory.Faker(
        "pydecimal",
        left_digits=5,
        right_digits=2,
        min_value=0,
        max_value=100,
    )
    luminosity = factory.Faker(
        "pydecimal",
        left_digits=5,
        right_digits=2,
        min_value=0,
        max_value=100,
    )
