from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Restaurants.models import Restaurant, Food


class SignUpForm(UserCreationForm):

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class RestaurantProfileInfoForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('Restaurant_Name',
                  'Restaurant_Phone_Number',
                  'Restaurant_Area',
                  'Restaurant_City',
                  'Restaurant_State')


class AddItemForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('Food_Name', 'Food_Pic', 'Food_Price', 'Food_Discount','Food_Category_ID', 'Food_Res_ID')