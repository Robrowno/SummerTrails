from django.urls import path
from . import views
from .views import signup_view


urlpatterns = [
    path("", views.home, name="home"),
    path("teams/", views.teams, name="team"),
    path("login/", views.login_view, name="login"),
    path("signup/", signup_view, name="signup"),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/delete', views.delete_profile, name='delete_profile'),
    path('upload/', views.upload_image, name='upload_image'),
]
