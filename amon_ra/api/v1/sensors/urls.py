from django.urls import path

from amon_ra.api.v1.sensors.views import SensorsCreateView, SensorsView


app_name = "sensors"


urlpatterns = [
    path("", SensorsView.as_view(), name="list"),
    path("create/", SensorsCreateView.as_view(), name="create"),
]
