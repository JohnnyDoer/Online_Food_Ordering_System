from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from Restaurants.models import Restaurant, FoodCategory, Food
from phonenumber_field.modelfields import PhoneNumberField
# from Customers.models import Address, Order, Item, Profile

# Create your models here.


class Delivery(models.Model):
    Delivery_ID = models.AutoField(primary_key=True)
    Delivery_Fname = models.CharField(max_length=250)
    Delivery_Lname = models.CharField(max_length=250)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Delivery_Num =PhoneNumberField()
    Delivery_Area = models.CharField(max_length=250)
    Delivery_Pin = models.CharField(max_length=6, default=000000)
    Delivery_City = models.CharField(max_length=250)
    Delivery_State = models.CharField(max_length=250)
    Delivery_Pic = models.ImageField(upload_to='Delivery/static/images/profiles',
                                     default='Delivery/static/images/profiles/default_del.jpg')
