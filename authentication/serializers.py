from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User, PhotoImage


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile_image', 'main_location', 'biography', 'interests', 'password']

    def create(self, validated_data):
        password = make_password(validated_data.pop('password'))
        user = User.objects.create(password=password, **validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128)

class PhotoImageSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = PhotoImage
        fields = ['id', 'user', 'image', 'title', 'content', 'latitude', 'longitude']