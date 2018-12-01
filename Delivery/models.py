from django.db import models
from django.contrib.auth.models import User
from Restaurants.models import Restaurant, FoodCategory, Food
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Delivery(models.Model):
    Delivery_ID = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Delivery_First_Name = models.CharField(max_length=250)
    Delivery_Last_Name = models.CharField(max_length=250)
    Delivery_Phone_Number =PhoneNumberField()
    Delivery_Area = models.CharField(max_length=250)
    Delivery_City = models.CharField(max_length=250)
    Delivery_State = models.CharField(max_length=250)
    Delivery_Pin = models.CharField(max_length=6, default=000000)
    Delivery_Pic = models.ImageField(upload_to='Delivery/static/images/profiles',
                                     default='Delivery/static/images/profiles/default_del.jpg')
