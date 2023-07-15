from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from .serializers import UserSerializer

class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Handle user permissions
            user.user_permissions.set(serializer.validated_data.get('user_permissions', []))
            return Response({'message': 'User registered successfully.'})
        return Response(serializer.errors, status=400)

class UserLoginAPIView(APIView):
    authentication_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        print(f"Username: {username}")
        print(f"Password: {password}")

        user = authenticate(request, username=username, password=password)
        print(f"User: {user}")

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Delete the authentication token for the current user
        request.user.auth_token.delete()
        return Response({'message': 'Logout successful.'}, status=status.HTTP_200_OK)