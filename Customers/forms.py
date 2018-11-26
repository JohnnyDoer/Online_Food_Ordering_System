from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Customers.models import Profile, Address


# Form for Signing Up.
class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


# Takes other information of a user.
class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('Customer_FName', 'Customer_LName', 'Customer_Num')


# Form to get user's address.
class AddressInfoForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('Home', 'Society', 'Area', 'City', 'State', 'Pin')
