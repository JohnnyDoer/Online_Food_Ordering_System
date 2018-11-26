from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import Restaurant, Food, FoodCategory
from .forms import SignUpForm, RestaurantProfileInfoForm


def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if Restaurant.objects.filter(user=user).exists():
                data = Restaurant.objects.filter(user=user)
                food = Food.objects.all()
                foodcatg = FoodCategory.objects.all()
                context = {'data': data, 'food': food, 'foodcatg': foodcatg}
                return render(request, 'Restaurant/res_profile.html', context=context)
            else:
                return redirect('http://127.0.0.1:8000/restaurant/profile')
        else:
            context = {'form': form}
            return render(request, 'Restaurant/index.html', context=context)
    else:
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'Restaurant/index.html', context=context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('http://127.0.0.1:8000/restaurant')
        else:
            context = {'form': form}
            return render(request, 'Restaurant/signup.html', context=context)
    else:
        form = SignUpForm()
        context = {'form': form}
    return render(request, 'Restaurant/signup.html', context=context)


def profile_page(request):
    if request.method == 'POST':
        profile_form = RestaurantProfileInfoForm(data=request.POST)
        # print(form)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return render(request, 'Restaurant/res_profile.html')
        else:
            context = {'Profile_form': profile_form}
            return render(request, 'Restaurant/profile.html', context=context)
    else:
        profile_form = RestaurantProfileInfoForm()
        context = {'Profile_form': profile_form}
    return render(request, 'Restaurant/profile.html', context=context)
