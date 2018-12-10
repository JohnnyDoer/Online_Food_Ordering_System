from django.shortcuts import render,redirect
from Customers.models import Profile
from Restaurants.models import Restaurant
from Delivery.models import Delivery

def index(request):

    if request.user.is_authenticated:
        if Profile.objects.filter(user=request.user).exists():
            return redirect('Cus_index')
        elif Restaurant.objects.filter(user=request.user).exists():
            return redirect('Res_info')
        elif Delivery.objects.filter(user=request.user).exists():
            return redirect('Del_orders')
    return render(request, 'Main/index.html')
