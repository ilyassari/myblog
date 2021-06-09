from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from account.models import CustomUserModel

class UpdateUserForm(UserChangeForm):
    password = None # bu formla şifre değiştirilmesin

    class Meta:
        model = CustomUserModel
        fields = (
            'email',
            'first_name',
            'last_name',
            'avatar'
        )

class SignUpForm(UserCreationForm):
    password = None # bu formla şifre değiştirilmesin

    class Meta:
        model = CustomUserModel
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'avatar',
            'password1',
            'password2'
        )
