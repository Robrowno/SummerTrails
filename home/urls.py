from django.urls import path
from . import views
from .views import signup_view


urlpatterns = [
    path("", views.home, name="home"),
    path("teams/", views.teams, name="team"),
    path("login/", views.login_view, name="login"),
    path("signup/", signup_view, name="signup"),
]
