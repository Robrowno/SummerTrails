from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer

class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully.'})
        return Response(serializer.errors, status=400)

