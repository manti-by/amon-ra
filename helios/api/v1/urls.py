from django.urls import include, path

app_name = "v1"


urlpatterns = [
    path("sensors/", include("helios.api.v1.sensors.urls"), name="sensors"),
    path("settings/", include("helios.api.v1.settings.urls"), name="settings"),
    path("subscriptions/", include("helios.api.v1.subscriptions.urls"), name="subscriptions"),
    path("users/", include("helios.api.v1.user.urls"), name="user"),
]
