from django.shortcuts import render
from . import templates
from django.http import HttpResponse

def index(request):
    return render(request, 'Main/index.html')


