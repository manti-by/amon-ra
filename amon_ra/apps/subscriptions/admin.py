from django.contrib import admin

from .models import Subscription, Notification, SubscriptionNotification


class SubscriptionNotificationInline(admin.TabularInline):
    model = SubscriptionNotification
    fields = ("subscription", "notification", "created_at")
    readonly_fields = ("created_at",)
    extra = 0


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at")
    inlines = (SubscriptionNotificationInline,)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("client", "created_at")
    inlines = (SubscriptionNotificationInline,)
