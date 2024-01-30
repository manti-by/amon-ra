from django.urls import path

from amon_ra.api.v1.settings.views import SettingsView

app_name = "settings"


urlpatterns = [
    path("", SettingsView.as_view(), name="settings"),
]
