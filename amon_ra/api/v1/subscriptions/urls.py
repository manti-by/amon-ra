from django.urls import path

from amon_ra.api.v1.subscriptions.views import (
    NotificationView,
    SubscriptionLinkView,
    SubscriptionUnlinkView,
    SubscriptionView,
)


app_name = "subscription"


urlpatterns = [
    path("", SubscriptionView.as_view(), name="get"),
    path("link/", SubscriptionLinkView.as_view(), name="link"),
    path("unlink/", SubscriptionUnlinkView.as_view(), name="unlink"),
    path("notification/", NotificationView.as_view(), name="notification"),
]
