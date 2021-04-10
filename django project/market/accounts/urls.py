from django.urls import path
from django.urls import path
from . import views

app_name = "accounts_url_app"

urlpatterns = [
    path("signup/", views.signup_def, name="signup_redirect"),
    path("login/", views.login_def, name="login_redirect"),
    path("logout/", views.logout_def, name="logout_redirect"),
]
