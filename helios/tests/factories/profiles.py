from factory.django import DjangoModelFactory

from helios.apps.profiles.models import Profile


class ProfileFactory(DjangoModelFactory):
    class Meta:
        model = Profile
