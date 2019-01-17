from django.contrib.auth import authenticate, login
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
from .forms import SignUpForm, RestaurantProfileInfoForm, FoodEditForm
from .models import Restaurant, Food, Area, FoodCategory
from .tokens import account_activation_token


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
            user = form.save(commit=False)
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
            return render(request, 'Restaurant/checkemail.html')
        else:
            context = {'form': form}
            return render(request, 'Restaurant/signup.html', context=context)
    else:
        form = SignUpForm()
        context = {'form': form}
    return render(request, 'Restaurant/signup.html', context=context)


@login_required(login_url='Res_index')
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
                return redirect('Res_info')
            else:
                return redirect('http://127.0.0.1:8000/restaurant/profile')
            # redirect('http://127.0.0.1:8000/restaurant/')
            # return render(request, 'Restaurant/res_profile.html')
        else:
            context = {'Profile_form': profile_form}
            return render(request, 'Restaurant/profile.html', context=context)
    else:
        profile_form = RestaurantProfileInfoForm()
        context = {'Profile_form': profile_form}
        return render(request, 'Restaurant/profile.html', context=context)


def load_areas(request):
    city_id = request.GET.get('city')
    areas = Area.objects.filter(city_id=city_id).order_by('name')
    return render(request, 'Restaurant/area_dropdown_list_options.html', {'areas': areas})


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


@login_required(login_url='Res_index')
def restaurant(request):
    data = Restaurant.objects.get(user=request.user)
    food = Food.objects.filter(
        Food_Res_ID=Restaurant.objects.get(user=request.user))
    context = {'data': data, 'food': food}
    return render(request, 'Restaurant/res_profile.html', context=context)


@login_required(login_url='Res_index')
def add_item(request):
    if request.method == 'POST':
        item = Food()
        item.Food_Res_ID = Restaurant.objects.get(user=request.user)
        item.Food_Name = request.POST.get('Food_Name')
        print(request.POST.get('Food_Category'))
        print(type(request.POST.get('Food_Category')))
        item.Food_Category_ID = FoodCategory.objects.get(
            FoodCategory_Name=request.POST.get('Food_Category'))
        item.Food_Price = request.POST.get('Food_Price')
        item.Food_Discount = request.POST.get('Food_Discount')
        item.save()
        return redirect('Res_info')
    else:
        data = FoodCategory.objects.all()
        context = {'data': data}
        return render(request, 'Restaurant/add_item.html', context=context)


@login_required(login_url='Cus_login')
def edit_food(request):
    global data_item
    global instance
    if request.GET.get('food_id'):
        data_item = request.GET.get('food_id')
        instance = Food.objects.get(pk=data_item)
        form = FoodEditForm(request.POST or None, instance=instance)
        context = {'form': form, 'data': instance}
        return render(request, 'Restaurant/edit_food.html', context=context)
    elif request.method == 'POST':
        form = FoodEditForm(data=request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('Res_info')
        else:
            return render(request, 'Restaurant/edit_food.html', {'form': form})


@login_required(login_url='Res_login')
def del_item(request):
    Food_ID = request.POST.get('delete')
    Food.objects.get(Food_ID=Food_ID).delete()
    return redirect('Res_info')


@login_required(login_url='Res_index')
def view_orders(request):
    if request.method == 'POST':
        order = Order.objects.get(pk=request.POST['Accepted'])
        if order.Order_Status == 1:
            order.Order_Status = 2
            order.Order_Restaurant_ID = Restaurant.objects.get(
                user=request.user)
            order.save()
    orders = Order.objects.filter(Order_Status=1).filter(
        Order_Address__area__name=Restaurant.objects.get(user=request.user).area.name)
    context = {'orders': orders, }
    return render(request, 'Restaurant/view.orders.html', context=context)


@login_required(login_url='Res_login')
def edit_profile(request):
    print(request.user)
    instance = Restaurant.objects.get(user=request.user)
    form = RestaurantProfileInfoForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('Main_index')
    return render(request, 'Restaurant/edit_profile.html', {'form': form})
