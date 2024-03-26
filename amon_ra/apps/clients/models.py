from django.db import models
from django.utils.translation import gettext_lazy as _

from amon_ra.apps.core.services import generate_uuid


class Client(models.Model):

    name = models.CharField(max_length=255)
    key = models.UUIDField(default=generate_uuid)
    hash = models.UUIDField(default=generate_uuid)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("client")
        verbose_name_plural = _("clients")

    def __str__(self):
        return f"Client #{self.id}"
