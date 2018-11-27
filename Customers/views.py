from django.core.mail import send_mail
#from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .models import Address, Profile, CartItems, Item, Order
from .forms import SignUpForm, UserProfileInfoForm, AddressInfoForm
from .tokens import account_activation_token
from Restaurants.models import Restaurant, Food, FoodCategory

cuisines = ['Lunch', 'Brunch', 'Dinner']

def index(request):
    vals = Address.objects.filter(Customer_ID=Profile.objects.get(user=request.user))
    context = {'vals': vals}
    return render(request, 'Customers/index.html', context=context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('Customers/emailver.html', {
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
            # return redirect('http://127.0.0.1:8000/')
            return HttpResponse('Please confirm your email address to complete the registration')
        else:
            context={'form': form, }
            return render(request, 'Customers/signup.html',context=context )
    else:
        form = SignUpForm()
        context={'form': form, }
    return render(request, 'Customers/signup.html',context=context)


def profile_page(request):
    if request.method == 'POST':
        profile_form = UserProfileInfoForm(data=request.POST)
        address_form = AddressInfoForm(data=request.POST)
        # print(form)
        if profile_form.is_valid() and address_form.is_valid():
            profile = profile_form.save(commit=False)
            address = address_form.save(commit=False)
            profile.user = request.user
            profile.save()
            address.Customer_ID = Profile.objects.get(user=request.user)
            address.save()
            return redirect('http://127.0.0.1:8000/customer')
        else:
            return render(request, 'customers/profile.html', {'Profile_form': profile_form, 'address_form': address_form})
    else:
        profile_form = UserProfileInfoForm()
        address_form = AddressInfoForm()
    return render(request, 'customers/profile.html', {'Profile_form': profile_form, 'address_form': address_form})


def loginform(request):
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
            context = {'form': form}
            return render(request, 'Customers/login.html', context=context)
    else:
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'Customers/login.html', context=context)

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        #login(request, user)
        # return redirect('home')
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        return render(request, 'Customers/After_Activation.html')
    else:
        return HttpResponse('Activation link is invalid!')


@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return redirect('http://127.0.0.1:8000/')


def categories(request):
    context = {'cuisines': cuisines, }
    return render(request, 'Customers/categories.html', context)


def restaurants(request):
    global res_id
    if request.GET.get('res_id'):
        res_id=request.GET.get('res_id')
        return redirect('http://127.0.0.1:8000/customer/res_info')
    else:
        data = request.POST['area']
        filter_res = Restaurant.objects.filter(Restaurant_Area=data)
        context = {'filter_res': filter_res, 'data':data}
        return render(request, 'Customers/filter_res.html', context=context)


def res_info(request):
    data = Food.objects.filter(Food_Res_ID=res_id).order_by('Food_ID')
    rest_data = Restaurant.objects.all()
    catg_data = FoodCategory.objects.all()
    context = {'data': data, 'rest_data': rest_data, 'catg_data': catg_data}
    return render(request, 'Customers/res_info.html', context=context)

def add_address(request):
    if request.method == 'POST':
        address_form = AddressInfoForm(data=request.POST)
        if address_form.is_valid():
            address = address_form.save(commit=False)
            address.Customer_ID = Profile.objects.get(user=request.user)
            address.save()
            return redirect('http://127.0.0.1:8000/customer')
        else:
            context={'address_form': address_form}
            return render(request,'Customers/add_address.html',context=context)
    else:
        address_form=AddressInfoForm(data=request.POST)
        context={'address_form': address_form}
        return render(request,'Customers/add_address.html',context=context)


def add_to_cart(request):
    if request.method == 'POST':
        Food_ID = request.POST.get('Food ID')
        cart_object = CartItems()
        cart_object.Cart_Customer_ID = Profile.objects.get(user=request.user)
        cart_object.Cart_Food_ID = Food.objects.get(Food_ID=Food_ID)
        cart_object.Quantity = int(request.POST.get('Quantity'))
        if cart_object.Quantity > 0:
            cart_object.save()
        my_dict = {'items': CartItems.objects.filter(Cart_Customer_ID=Profile.objects.get(user=request.user))}
        return redirect('Cus_resinfo')


def cart(request):
    items = CartItems.objects.filter(Cart_Customer_ID=Profile.objects.get(user=request.user))
    context = {'items': items}
    return render(request, 'Customers/cart.html', context=context)


def delete(request):
    Cart_ID = request.POST.get('Cart ID')
    CartItems.objects.get(Cart_ID=Cart_ID).delete()
    return redirect('Cus_cart')

def receipt(request):
    pass