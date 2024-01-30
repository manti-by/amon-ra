from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="subscriptions", on_delete=models.CASCADE)
    endpoint = models.CharField(max_length=255)
    expiration_time = models.DateTimeField(null=True)
    keys = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("subscription")
        verbose_name_plural = _("subscriptions")
        unique_together = ("user", "endpoint")

    def __str__(self):
        return f"Subscription for {self.user}"

    def serialize(self):
        return {"endpoint": self.endpoint, "keys": self.keys}


class Notification(models.Model):
    title = models.CharField(max_length=64)
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("notification")
        verbose_name_plural = _("notifications")

    def __str__(self):
        return f"Notification {self.title}"
