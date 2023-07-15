from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("teams/", views.teams, name="team"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),

]
