from django.urls import path
from .views import UserRegistrationAPIView
from .api import UserListAPIView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
]
