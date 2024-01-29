from django.contrib import admin

from helios.apps.subscriptions.models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("user", "expiration_time", "created_at")
