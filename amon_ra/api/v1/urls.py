from django.urls import include, path


app_name = "v1"


urlpatterns = [
    path("sensors/", include("amon_ra.api.v1.sensors.urls"), name="sensors"),
    path("settings/", include("amon_ra.api.v1.settings.urls"), name="settings"),
    path("subscription/", include("amon_ra.api.v1.subscriptions.urls"), name="subscription"),
    path("users/", include("amon_ra.api.v1.user.urls"), name="user"),
]
