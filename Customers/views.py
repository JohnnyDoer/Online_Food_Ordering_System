from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import signupform
from django.http import HttpResponse,HttpResponseRedirect
from .forms import UserProfileInfoForm,Addressinfoform
from django.core.mail import send_mail
from .models import Address, Profile
from Main.views import index
from django.contrib.auth.decorators import login_required
from Restaurants.models import ResProfile

# after V

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage


cuisines = ["Afghani", "American", "Fried Chicken", "Hawaiian", "Malaysian", "Modern Indian", "Pan Asian",
              "Portuguese", "Salad", "South Indian", "Steak", "Tea", ]


@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return redirect('http://127.0.0.1:8000/')


@login_required(login_url = 'Main_index')
def profilepage(request):
    if request.method == 'POST':
        profile_form = UserProfileInfoForm(data=request.POST)
        address_form = Addressinfoform(data=request.POST)
        if profile_form.is_valid() and address_form.is_valid() :
            profile = profile_form.save(commit=False)
            address = address_form.save(commit=False)
            profile.user = request.user
            address.username = request.user
            profile.save()
            address.save()
            return redirect('http://127.0.0.1:8000/customer')
        else:
            return render(request, 'customers/profile.html', {'Profile_form': profile_form,'address_form':address_form})
    else:
        profile_form = UserProfileInfoForm()
        address_form=Addressinfoform()
    return render(request, 'customers/profile.html', {'Profile_form': profile_form,'address_form':address_form})


def signup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
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
            #return redirect('http://127.0.0.1:8000/')
            return HttpResponse('Please confirm your email address to complete the registration')
        else:
            return render(request, 'customers/signup.html', {'form': form,})
    else:
        form = signupform()
    return render(request, 'customers/signup.html', {'form': form,})


def categories(request):
    context = {'cuisines': cuisines, }
    return render(request, 'Customers/categories.html', context)


@login_required(login_url='Main_index')
def cusindex(request):
    vals = Address.objects.filter(username=request.user)
    context = {'vals': vals}
    return render(request, 'Customers/index.html', context=context)


@login_required(login_url='Main_index')
def restaurants(req):
    data = req.POST['areas']
    print(data)
    filter_res = ResProfile.objects.filter(Restaurant_Area=data)
    print(filter_res)
    con = {'filter_res':filter_res}
    return render(req,'Customers/res.html',context=con)


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