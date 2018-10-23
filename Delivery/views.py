from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is MainPage of Delivery after Logging In")

