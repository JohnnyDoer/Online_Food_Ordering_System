from django.shortcuts import render
from Customers.models import Order, Address
from .models import Delivery
from django.http import HttpResponse


def index(request):
    return render(request, 'Delivery/index.html')


def signup(request):
    return render(request, 'Delivery/signup.html',)
