from django.db import models
from django.contrib.auth.models import User

from helios.apps.core.models import BaseModel


class Profile(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="profile",
    )
    verification_token = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return self.user.email
