from django.shortcuts import render

# Create your views here.
from .models import Order,Food,Items


def result(request):

    objs = Items.objects.all()
    context = {'objs': objs}
    return render(request, 'M_orders/displayorders.html', context=context)

