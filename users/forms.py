# -*- coding:UTF-8 -*-

from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class RegisterForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('username','email')

class LoginForm(forms.Form):
	username = forms.CharField(label='用户名')
	password = forms.CharField(label='密码', widget=forms.PasswordInput)