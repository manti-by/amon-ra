from asgiref.sync import async_to_sync
from django.db import models
from django.utils.translation import gettext_lazy as _
from telegram import Message
from telegram.constants import ParseMode

from amon_ra.bot.services.message import send_message


class Notification(models.Model):
    client = models.ForeignKey(
        "clients.Client", related_name="notifications", on_delete=models.CASCADE, null=True, blank=True
    )
    title = models.CharField(max_length=64)
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("notification")
        verbose_name_plural = _("notifications")

    def __str__(self):
        return f"Notification #{self.id} from {self.client.name}"


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

    @async_to_sync
    async def send_notification(self, notification: Notification) -> Message:
        result = await send_message(
            chat_id=self.data["chat_id"],
            text=f"*[{notification.client}] {notification.title}*\n{notification.text}",
            parse_mode=ParseMode.MARKDOWN_V2,
        )
        await SubscriptionNotification.objects.acreate(subscription=self, notification=notification)
        return result


class SubscriptionNotification(models.Model):
    subscription = models.ForeignKey(Subscription, related_name="notification_logs", on_delete=models.CASCADE)
    notification = models.ForeignKey(Notification, related_name="notification_logs", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Sent at"))

    class Meta:
        verbose_name = _("subscription notification")
        verbose_name_plural = _("subscription notifications")
        unique_together = ("subscription", "notification")

    def __str__(self):
        return f"{self.subscription} - {self.notification}"
