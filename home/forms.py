from django import forms
from authentication.models import User, PhotoImage
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = PhotoImage
        fields = ('image', 'title', 'content', 'latitude', 'longitude')

class ImageForm(forms.ModelForm):
    class Meta:
        model = PhotoImage
        fields = ['image', 'title', 'content', 'latitude', 'longitude']
