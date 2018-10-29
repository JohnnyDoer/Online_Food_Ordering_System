from django.shortcuts import render
from django.http import HttpResponse

cuisines = ["Afghani", "American", "Fried Chicken", "Hawaiian", "Malaysian", "Modern Indian", "Pan Asian",
              "Portuguese", "Salad", "South Indian", "Steak", "Tea", ]


def index(request):
    return render(request, 'Customers/index.html')


def signup(request):
    return render(request, 'Customers/signup.html')


def categories(request):
    context = {'cuisines': cuisines, }
    return render(request, 'Customers/categories.html', context)
