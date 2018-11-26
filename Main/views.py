from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from Customers.models import Profile
from django.http import HttpResponse


def index(request):
    return render(request,'Main/index.html')
