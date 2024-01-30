from django.urls import path

from amon_ra.api.v1.subscriptions.views import SubscriptionView, NotificationView

app_name = "subscriptions"


urlpatterns = [
    path("", SubscriptionView.as_view(), name="subscriptions"),
    path("notification/", NotificationView.as_view(), name="notification"),
]
