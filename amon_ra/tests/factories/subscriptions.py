import factory.fuzzy
from factory.django import DjangoModelFactory

from amon_ra.apps.subscriptions.models import Subscription
from amon_ra.apps.subscriptions.services import get_telegram_data_hash


class SubscriptionDictFactory(factory.DictFactory):
    id = factory.Faker("first_name")
    username = factory.Faker("pyint")
    auth_date = factory.Faker("pyint")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    photo_url = factory.Faker("image_url")

    @factory.lazy_attribute
    def hash(self):
        return get_telegram_data_hash(
            {
                "id": self.id,
                "username": self.username,
                "auth_date": self.auth_date,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "photo_url": self.photo_url,
            }
        )


class SubscriptionFactory(DjangoModelFactory):
    user = factory.SubFactory("amon_ra.tests.factories.users.UserFactory")
    data = SubscriptionDictFactory()

    class Meta:
        model = Subscription


class NotificationDictFactory(factory.DictFactory):
    title = factory.Faker("word")
    text = factory.Faker("paragraph")
