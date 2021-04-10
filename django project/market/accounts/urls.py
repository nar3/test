from django.urls import path
from django.urls import path
from . import views

app_name = "accounts_url_app"

urlpatterns = [
    path("signup", views.signup, name="signup_redirect"),
    path('login' , views.login , name='login_redirect'),
]
