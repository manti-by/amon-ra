import factory.fuzzy
from factory.django import DjangoModelFactory

from helios.apps.sensors.models import Sensor


class SensorDictFactory(factory.DictFactory):
    name = factory.Faker("md5")
    temp = factory.Faker(
        "pydecimal", left_digits=5, right_digits=2, min_value=5, max_value=35
    )
    humidity = factory.Faker(
        "pydecimal", left_digits=5, right_digits=2, min_value=0, max_value=100
    )


class SensorFactory(DjangoModelFactory):
    name = factory.Faker("md5")
    temp = factory.Faker(
        "pydecimal", left_digits=5, right_digits=2, min_value=5, max_value=35
    )
    humidity = factory.Faker(
        "pydecimal", left_digits=5, right_digits=2, min_value=0, max_value=100
    )

    class Meta:
        model = Sensor
