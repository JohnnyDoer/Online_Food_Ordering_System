from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Customers.models import Profile, Address


# Form for Signing Up.
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


# Takes other information of a user.
class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('Customer_First_Name', 'Customer_Last_Name', 'Customer_Phone_Number')


# Form to get user's address.
class AddressInfoForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('Home', 'Street', 'Area', 'City', 'State', 'Pin')
