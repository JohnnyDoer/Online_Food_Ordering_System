from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .forms import DeliveryGuyProfileInfoForm, SignUpForm
from .models import Delivery
from Customers.models import Order
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
            if Delivery.objects.filter(user=user).exists():
                return render(request, 'Delivery/del_orders.html')
            else:
                return redirect('http://127.0.0.1:8000/delivery/profile')
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
            return render(request,'Delivery/checkemail.html')
        else:
            context = {'form': form, }
            return render(request, 'Delivery/signup.html', context=context)
    else:
        form = SignUpForm()
        context = {'form': form, }
    return render(request, 'Delivery/signup.html', context=context)


def profile_page(request):
    if request.method == 'POST':
        profile_form = DeliveryGuyProfileInfoForm(data=request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return render(request, 'Delivery/filter_order.html')
        else:
            context = {'Profile_form': profile_form}
            return render(request, 'Delivery/profile.html', context=context)
    else:
        profile_form = DeliveryGuyProfileInfoForm()
        context = {'Profile_form': profile_form}
    return render(request, 'Delivery/profile.html', context=context)


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

def del_orders(request):

    orders = Order.objects.filter(Order_Status=1).filter(Order_Customer_ID__address__Area=Delivery.objects.get(user=request.user).Delivery_Area)
    context = {'orders': orders}
    return render(request, 'Delivery/del_orders.html', context=context)

