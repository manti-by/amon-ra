import factory
from factory.django import DjangoModelFactory

from amon_ra.apps.users.models import User
from amon_ra.tests.factories import DEFAULT_USER_PASSWORD


class UserDictFactory(factory.Factory):
    class Meta:
        model = dict

    email = factory.Faker("email")
    password = DEFAULT_USER_PASSWORD


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", DEFAULT_USER_PASSWORD)
