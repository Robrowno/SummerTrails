from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, UserLoginSerializer, PhotoImageSerializer
from .models import User, PhotoImage

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserLoginAPIView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

class UserPostsAPIView(generics.ListAPIView):
    serializer_class = PhotoImageSerializer
    queryset = PhotoImage.objects.all()