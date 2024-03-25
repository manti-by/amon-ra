from factory.django import DjangoModelFactory

from amon_ra.apps.clients.models import Client
from amon_ra.tests.factories import DEFAULT_CLIENT_HASH, DEFAULT_CLIENT_KEY


class ClientFactory(DjangoModelFactory):
    key = DEFAULT_CLIENT_KEY
    hash = DEFAULT_CLIENT_HASH

    class Meta:
        model = Client
