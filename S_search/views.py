from django.shortcuts import render

# Create your views here.
from .models import Food, Food_Category, Restaurant


def result(request):
######################

########################


    objs = Food.objects.all()
    context = {'objs': objs}
    return render(request, 'S_search/search.html', context=context)
