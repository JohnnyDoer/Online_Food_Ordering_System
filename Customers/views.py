from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'Customers/index.html')

def login(request):
    return HttpResponse("Log In page for Customer")
