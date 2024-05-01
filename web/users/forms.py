from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import ImpUser


class UserSignupForm(UserCreationForm):
    class Meta:
        model = ImpUser
        fields = ['username', 'password1', 'password2', 'private_email', 'birth_date']


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Псевдоним")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
