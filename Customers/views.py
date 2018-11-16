from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .forms import SignUpForm
from .forms import UserProfileInfoForm, AddressInfoForm
from django.core.mail import send_mail
from .models import Address

from django.http import HttpResponse

cuisines = ["Afghani", "American", "Fried Chicken", "Hawaiian", "Malaysian", "Modern Indian", "Pan Asian",
            "Portuguese", "Salad", "South Indian", "Steak", "Tea", ]


def index(request):
    vals = Address.objects.all()
    # print(vals)
    return render(request, 'Customers/index.html')


def profile_page(request):
    if request.method == 'POST':
        profile_form = UserProfileInfoForm(data=request.POST)
        address_form = AddressInfoForm(data=request.POST)
        # print(form)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('http://127.0.0.1:8000/customer')
        else:
            return render(request, 'Customers/profile.html', {'Profile_form': profile_form, })
    else:
        profile_form = UserProfileInfoForm()
    return render(request, 'Customers/profile.html', {'Profile_form': profile_form, })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # login(request)
            # send_mail('ASE', 'this is the message.', 'aseproject321@gmail.com', [User.email],
            #         fail_silently=False)
            return redirect('http://127.0.0.1:8000/')
        else:
            return render(request, 'Customers/signup.html', {'form': form, })
    else:
        form = SignUpForm()
    return render(request, 'Customers/signup.html', {'form': form, })


def categories(request):
    context = {'cuisines': cuisines, }
    return render(request, 'Customers/categories.html', context)
