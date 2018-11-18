from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DeliveryGuyProfileInfoForm, SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import Delivery


def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if Delivery.objects.filter(user=user).exists():
                return render(request, 'Delivery/filter_order.html')
            else:
                return redirect('http://127.0.0.1:8000/delivery/profile')
        else:
            return render(request, 'Delivery/index.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'Delivery/index.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('http://127.0.0.1:8000/delivery')
        else:
            return render(request, 'Delivery/signup.html', {'form': form,})
    else:
        form = SignUpForm()
    return render(request, 'Delivery/signup.html', {'form': form,})


def profile_page(request):
    if request.method == 'POST':
        profile_form = DeliveryGuyProfileInfoForm(data=request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return render(request, 'Delivery/filter_order.html')
        else:
            return render(request, 'Delivery/profile.html', {'Profile_form': profile_form})
    else:
        profile_form = DeliveryGuyProfileInfoForm()
    return render(request, 'Delivery/profile.html', {'Profile_form': profile_form})

