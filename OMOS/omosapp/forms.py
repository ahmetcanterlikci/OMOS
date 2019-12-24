from django import forms
from django.contrib.auth.models import User

from omosapp.models import SystemUser


class RegisterUser(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)


class RegisterSystemUser(forms.ModelForm):

    class Meta:
        model = SystemUser
        fields = ('gender', 'phone', 'age', 'country', 'city',)


class LoginUser(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password',)

