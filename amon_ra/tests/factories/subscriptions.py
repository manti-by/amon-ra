import factory.fuzzy
from factory.django import DjangoModelFactory

from amon_ra.apps.core.services import get_data_hash
from amon_ra.apps.subscriptions.models import Subscription
from amon_ra.tests.factories import DEFAULT_CLIENT_KEY, DEFAULT_CLIENT_HASH


class SubscriptionGetDictFactory(factory.DictFactory):
    key = DEFAULT_CLIENT_KEY
    chat_id = factory.Faker("pyint")

    @factory.lazy_attribute
    def hash(self):
        return get_data_hash(
            {
                "key": self.key,
                "chat_id": self.chat_id,
            },
            DEFAULT_CLIENT_HASH,
        )


class SubscriptionLinkDictFactory(factory.DictFactory):
    key = DEFAULT_CLIENT_KEY
    email = factory.Faker("email")
    chat_id = factory.Faker("pyint")
    username = factory.Faker("pyint")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")

    @factory.lazy_attribute
    def hash(self):
        return get_data_hash(
            {
                "key": self.key,
                "email": self.email,
                "chat_id": self.chat_id,
                "username": self.username,
                "first_name": self.first_name,
                "last_name": self.last_name,
            },
            DEFAULT_CLIENT_HASH,
        )


class SubscriptionUnlinkDictFactory(SubscriptionGetDictFactory): ...


class SubscriptionDataDictFactory(factory.DictFactory):
    chat_id = factory.Faker("pyint")
    username = factory.Faker("pyint")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")


class SubscriptionFactory(DjangoModelFactory):
    user = factory.SubFactory("amon_ra.tests.factories.users.UserFactory")
    data = SubscriptionDataDictFactory()

    class Meta:
        model = Subscription


class NotificationDictFactory(factory.DictFactory):
    key = DEFAULT_CLIENT_KEY
    title = factory.Faker("word")
    text = factory.Faker("paragraph")

    @factory.lazy_attribute
    def hash(self):
        return get_data_hash(
            {
                "key": self.key,
                "title": self.title,
                "text": self.text,
            },
            DEFAULT_CLIENT_HASH,
        )
