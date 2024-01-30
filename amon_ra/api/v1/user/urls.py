from django.urls import path

from amon_ra.api.v1.user.views import LoginView

app_name = "user"


urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
]
