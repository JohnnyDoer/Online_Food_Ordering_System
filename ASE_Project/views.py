from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is MainPage where location will be asked and option for Restaurant and Delivery.")

def login(request):
    return HttpResponse("Log In page for ")
