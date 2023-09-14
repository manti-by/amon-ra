from django.urls import include, path

app_name = "v1"


urlpatterns = [
    path("sensors/", include("helios.api.v1.sensors.urls"), name="sensors"),
    path("users/", include("helios.api.v1.user.urls"), name="user"),
]
