from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Delivery.models import Delivery


class SignUpForm(UserCreationForm):

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class DeliveryGuyProfileInfoForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ('Delivery_Fname',
                  'Delivery_Lname',
                  'Delivery_Num',
                  'Delivery_Area',
                  'Delivery_City',
                  'Delivery_State')

