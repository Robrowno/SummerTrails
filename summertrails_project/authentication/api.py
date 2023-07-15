from rest_framework import generics
from .serializers import UserSerializer
from .models import User

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
