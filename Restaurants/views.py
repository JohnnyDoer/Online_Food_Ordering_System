from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import Restaurant, Food, FoodCategory
from .forms import SignUpForm, RestaurantProfileInfoForm ,AddItemForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.contrib.auth.models import User


def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if Restaurant.objects.filter(user=user).exists():

                return redirect('Res_info')
            else:
                return redirect('Res_profile')
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
            user=form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('Restaurant/emailver.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return render(request,'Restaurant/checkemail.html')
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
            user = profile.user
            if Restaurant.objects.filter(user=user).exists():
               redirect('Res_info')
            else:
                return redirect('http://127.0.0.1:8000/restaurant/profile')
            #redirect('http://127.0.0.1:8000/restaurant/')
            #return render(request, 'Restaurant/res_profile.html')
        else:
            context = {'Profile_form': profile_form}
            return render(request, 'Restaurant/profile.html', context=context)
    else:
        profile_form = RestaurantProfileInfoForm()
        context = {'Profile_form': profile_form}
        return render(request, 'Restaurant/profile.html', context=context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'Restaurant/After_Activation.html')
    else:
        return HttpResponse('Activation link is invalid!')


def restaurant(request):
    data = Restaurant.objects.get(user=request.user)
    food = Food.objects.filter(Food_Res_ID=Restaurant.objects.get(user=request.user))
    context = {'data': data, 'food': food}
    return render(request, 'Restaurant/res_profile.html', context=context)




def add_item(request):
    if request.method == 'POST':
        form =AddItemForm(data=request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('Res_info')
        else:
            context = {'form': form}
            return render(request, 'Restaurant/add_item.html', context=context)
    else:
        form=AddItemForm()
        context={'form':form}
        return render(request,'Restaurant/add_item.html',context=context)