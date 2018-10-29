from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'Restaurant/index.html')


def signup(request):
    return render(request, 'Restaurant/signup.html')
