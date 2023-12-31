from django.urls import path
from .views import UserRegistrationAPIView, UserLoginAPIView, UserLogoutAPIView
from .api import UserListAPIView, UserPostsAPIView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('logout/', UserLogoutAPIView.as_view(), name='user-logout'),
    path('users/posts/', UserPostsAPIView.as_view(), name='user_posts'),
]
