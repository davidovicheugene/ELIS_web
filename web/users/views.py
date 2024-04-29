from django.contrib.auth import logout
from django.shortcuts import render, redirect


def user_login():
    pass


def user_logout(request):
    logout(request)
    return redirect('login')


def user_signup():
    pass