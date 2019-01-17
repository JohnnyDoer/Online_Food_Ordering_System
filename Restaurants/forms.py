from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Restaurants.models import Restaurant, Food, Area, City


class SignUpForm(UserCreationForm):

    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class RestaurantProfileInfoForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('Restaurant_Name',
                  'Restaurant_Phone_Number',
                  'city',
                  'area',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['area'].queryset = Area.objects.none()
        print(self.fields['area'].queryset)

        if 'city' in self.data:
            try:
                city_id = int(self.data.get('city'))
                self.fields['area'].queryset = Area.objects.filter(
                    city_id=city_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty city queryset
        elif self.instance.pk:
            self.fields['area'].queryset = self.instance.city.area_set.order_by(
                'name')


class AddItemForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('Food_Name', 'Food_Pic', 'Food_Price',
                  'Food_Discount', 'Food_Category_ID', 'Food_Res_ID')


class FoodEditForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('Food_Name', 'Food_Category_ID',
                  'Food_Price', 'Food_Discount', 'Food_Res_ID')
