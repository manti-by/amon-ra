import factory.fuzzy
import pytz
from factory.django import DjangoModelFactory

from amon_ra.apps.core.services import get_data_hash
from amon_ra.apps.sensors.models import Sensor
from amon_ra.tests.factories import DEFAULT_CLIENT_HASH, DEFAULT_CLIENT_KEY


class SensorDictFactory(factory.DictFactory):
    key = DEFAULT_CLIENT_KEY
    external_id = factory.Faker("pyint")
    sensor_id = factory.Faker("md5")
    temp = factory.Faker("pydecimal", left_digits=5, right_digits=2, min_value=5, max_value=35)
    humidity = factory.Faker("pydecimal", left_digits=5, right_digits=2, min_value=0, max_value=100)
    created_at = factory.Faker("date_time", tzinfo=pytz.UTC)

    @factory.lazy_attribute
    def hash(self):
        return get_data_hash(
            {
                "key": self.key,
                "external_id": self.external_id,
                "sensor_id": self.sensor_id,
                "temp": self.temp,
                "humidity": self.humidity,
                "created_at": self.created_at,
            },
            DEFAULT_CLIENT_HASH,
        )


class SensorFactory(DjangoModelFactory):
    external_id = factory.Faker("pyint")
    sensor_id = factory.Faker("md5")
    temp = factory.Faker("pydecimal", left_digits=5, right_digits=2, min_value=5, max_value=35)
    humidity = factory.Faker("pydecimal", left_digits=5, right_digits=2, min_value=0, max_value=100)
    created_at = factory.Faker("date_time")

    class Meta:
        model = Sensor
