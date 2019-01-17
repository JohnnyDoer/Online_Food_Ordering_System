from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from Customers.models import Order
from .forms import DeliveryGuyProfileInfoForm, SignUpForm
from .models import Delivery, Area
from .tokens import account_activation_token


def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if Delivery.objects.filter(user=user).exists():
                return redirect('Del_orders')
            else:
                return redirect('Del_profile')
        else:
            context = {'form': form}
            return render(request, 'Delivery/index.html', context=context)
    else:
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'Delivery/index.html', context=context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('Delivery/emailver.html', {
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
            return render(request, 'Delivery/checkemail.html')
        else:
            context = {'form': form, }
            return render(request, 'Delivery/signup.html', context=context)
    else:
        form = SignUpForm()
        context = {'form': form, }
    return render(request, 'Delivery/signup.html', context=context)


@login_required(login_url='Del_index')
def profile_page(request):
    if request.method == 'POST':
        profile_form = DeliveryGuyProfileInfoForm(data=request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('Del_orders')
        else:
            context = {'Profile_form': profile_form}
            return render(request, 'Delivery/profile.html', context=context)
    else:
        profile_form = DeliveryGuyProfileInfoForm()
        context = {'Profile_form': profile_form}
    return render(request, 'Delivery/profile.html', context=context)


def load_areas(request):
    city_id = request.GET.get('city')
    areas = Area.objects.filter(city_id=city_id).order_by('name')
    return render(request, 'Delivery/area_dropdown_list_options.html', {'areas': areas})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'Delivery/After_Activation.html')
    else:
        return HttpResponse('Activation link is invalid!')


@login_required(login_url='Del_index')
def del_orders(request):
    if request.method == 'POST':
        order = Order.objects.get(pk=request.POST['Accepted'])
        if order.Order_Status == 2:
            order.Order_Status = 3
            order.Order_Delivery_ID = Delivery.objects.get(user=request.user)
            order.save()
        elif order.Order_Status == 3:
            order.Order_Status = 4
            order.save()
    orders = Order.objects.filter(Order_Status=2).filter(
        Order_Address__area__name=Delivery.objects.get(user=request.user).area.name)
    accepted = Order.objects.filter(Order_Status=3).filter(
        Order_Delivery_ID=Delivery.objects.get(user=request.user))
    context = {'orders': orders, 'accepted': accepted}
    return render(request, 'Delivery/del_orders.html', context=context)


@login_required(login_url='Del_login')
def edit_profile(request):
    print(request.user)
    instance = Delivery.objects.get(user=request.user)
    form = DeliveryGuyProfileInfoForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('Main_index')
    return render(request, 'Delivery/edit_profile.html', {'form': form})
