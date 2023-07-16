from django import forms
from authentication.models import User
from django.contrib.auth.forms import UserCreationForm
from authentication.models import PhotoImage



class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = PhotoImage
        fields = ('image', 'title', 'content', 'latitude', 'longitude')