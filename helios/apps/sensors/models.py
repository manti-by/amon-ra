from django.db import models
from django.contrib.auth.models import User

from helios.apps.core.models import BaseModel


class Sensor(BaseModel):

    temp = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    moisture = models.DecimalField(max_digits=5, decimal_places=2)
    luminosity = models.DecimalField(max_digits=5, decimal_places=2)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="sensors",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Sensor {self.created_at}"


class Photo(BaseModel):

    file = models.FileField()
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="photos",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Photo {self.created_at}"
