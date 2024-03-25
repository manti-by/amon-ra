from django.db import models
from django.utils.translation import gettext_lazy as _


class Notification(models.Model):
    title = models.CharField(max_length=64)
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("notification")
        verbose_name_plural = _("notifications")

    def __str__(self):
        return f"Notification {self.title}"


class Subscription(models.Model):
    user = models.OneToOneField(
        "users.User", related_name="subscription", on_delete=models.CASCADE, null=True, blank=True
    )
    data = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("subscription")
        verbose_name_plural = _("subscriptions")

    def __str__(self):
        return f"Subscription for {self.user}"

    def send_notification(self, notification: Notification):
        pass
