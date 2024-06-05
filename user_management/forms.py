from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'mobile_number', 'address', 'latitude', 'longitude', 'password1', 'password2']
