from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.http import HttpResponse,HttpResponseRedirect
from .forms import UserProfileInfoForm, AddressInfoForm
from django.core.mail import send_mail
from .models import Address, Profile
#from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from Restaurants.models import Restaurant

cuisines = ["Afghani", "American", "Fried Chicken", "Hawaiian", "Malaysian", "Modern Indian", "Pan Asian",
              "Portuguese", "Salad", "South Indian", "Steak", "Tea", ]


@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return redirect('http://127.0.0.1:8000/')


def index(request):
    #data = Profile.objects.all()
    vals = Address.objects.filter(username=request.user)
    #print(data)
    context = {'vals': vals}
    return render(request, 'Customers/index.html', context=context)


def restaurants(request):
    data = request.POST['area']
    filter_res = Restaurant.objects.filter(Restaurant_Area=data)
    con = {'filter_res': filter_res}
    return render(request, 'Customers/filter_res.html', context=con)


def profile_page(request):
    if request.method == 'POST':
        profile_form = UserProfileInfoForm(data=request.POST)
        address_form = AddressInfoForm(data=request.POST)
        # print(form)
        if profile_form.is_valid() and address_form.is_valid():
            profile = profile_form.save(commit=False)
            address = address_form.save(commit=False)
            profile.user = request.user
            address.username = request.user
            profile.save()
            address.save()
            return redirect('http://127.0.0.1:8000/customer')
        else:
            return render(request, 'customers/profile.html', {'Profile_form': profile_form, 'address_form': address_form})
    else:
        profile_form = UserProfileInfoForm()
        address_form = AddressInfoForm()
    return render(request, 'customers/profile.html', {'Profile_form': profile_form, 'address_form': address_form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            #login(request)
            #send_mail('ASE', 'this is the message.', 'aseproject321@gmail.com', [User.email],
             #         fail_silently=False)
            return redirect('http://127.0.0.1:8000/')
        else:
            return render(request, 'customers/signup.html', {'form': form, })
    else:
        form = SignUpForm()
    return render(request, 'customers/signup.html', {'form': form, })


def categories(request):
    context = {'cuisines': cuisines, }
    return render(request, 'Customers/categories.html', context)

