from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Restaurants.models import ResProfile


class signupform(UserCreationForm):

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ( 'username', 'email', 'password1', 'password2', )


class RestaurantProfileInfoForm(forms.ModelForm):
    class Meta:
        model = ResProfile
        fields = ('Restaurant_Name',
                  'Restaurant_Num',
                  'Restaurant_Area',
                  'Restaurant_City',
                  'Restaurant_State')

