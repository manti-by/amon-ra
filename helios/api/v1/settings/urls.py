from django.urls import path

from helios.api.v1.settings.views import SettingsView

app_name = "settings"


urlpatterns = [
    path("", SettingsView.as_view(), name="settings"),
]
