from django.urls import path

from helios.api.v1.sensors.views import SensorsView

app_name = "sensors"


urlpatterns = [
    path("", SensorsView.as_view(), name="sensors"),
]
