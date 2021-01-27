from django.urls import include, path

app_name = "api"

urlpatterns = [
    path("v1/", include("helios.api.v1.urls", namespace="v1")),
]
