from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["name", "email", "username", "password1", "password2"]

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["name", "email", "bio", "avatar"]