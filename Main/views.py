from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render,redirect
from Customers.models import Profile
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if Profile.objects.filter(user=user).exists():
                return redirect('http://127.0.0.1:8000/customer')
            else:
                return redirect('http://127.0.0.1:8000/customer/profile')
        else:
            return render(request, 'Main/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request,'Main/login.html',{'form': form})

