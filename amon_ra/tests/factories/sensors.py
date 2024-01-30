import factory.fuzzy
from factory.django import DjangoModelFactory

from amon_ra.apps.sensors.models import Sensor


class SensorDictFactory(factory.DictFactory):
    external_id = factory.Faker("pyint")
    sensor_id = factory.Faker("md5")
    temp = factory.Faker("pydecimal", left_digits=5, right_digits=2, min_value=5, max_value=35)
    humidity = factory.Faker("pydecimal", left_digits=5, right_digits=2, min_value=0, max_value=100)
    created_at = factory.Faker("date_time")


class SensorFactory(DjangoModelFactory):
    external_id = factory.Faker("pyint")
    sensor_id = factory.Faker("md5")
    temp = factory.Faker("pydecimal", left_digits=5, right_digits=2, min_value=5, max_value=35)
    humidity = factory.Faker("pydecimal", left_digits=5, right_digits=2, min_value=0, max_value=100)
    created_at = factory.Faker("date_time")

    class Meta:
        model = Sensor
