from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from .forms import *


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('assistance_homepage')
    else:
        form = UserLoginForm()
    return render(request, 'user_login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('user_login')


def user_signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = UserSignupForm()
    return render(request, 'user_signup.html', {'form': form})
