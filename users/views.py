# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse, get_object_or_404,HttpResponseRedirect
from .forms import RegisterForm, LoginForm
from .models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)

		if form.is_valid():
			form.save()

			return redirect('/')
	else:
		form = RegisterForm()

	return render(request, 'users/register.html',context={'form':form})

def login_validate(request, username, password):
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			auth_login(request, user)
			return True
	return False

def login(request):
	error = ''
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			try:
				User.objects.get(username=username)
			except Exception as e:
				print e
				error = '用户不存在,请输入正确的用户名'
			else:
				if login_validate(request, username, password):
					user = authenticate(username=username, password=password)
					auth_login(request,user)
					return redirect(reverse('blog:index', args=()))
				else:
					error = '请输入正确的密码'
		else:
			error = '请输入正确的用户名和密码'

	else:
		form = LoginForm()

	return render(request, 'users/login.html', context={'form':form, 'error': error})

def logout(request):  
    auth_logout(request)  
    returnPath = request.META.get('HTTP_REFERER')
    return HttpResponseRedirect(returnPath)

















