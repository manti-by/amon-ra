from django.urls import path

from amon_ra.api.v1.user.views import UserView, LoginView

app_name = "user"


urlpatterns = [
    path("", UserView.as_view(), name="user"),
    path("login/", LoginView.as_view(), name="login"),
]
