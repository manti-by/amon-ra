from django.contrib import admin

from amon_ra.apps.subscriptions.models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("uuid", "user", "created_at")
