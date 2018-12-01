from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
# from Delivery.models import Delivery
# from Customers.models import Customer, Address, Order, Item

# Create your models here.


class Restaurant(models.Model):
    Restaurant_ID = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Restaurant_Name = models.CharField(max_length=250)
    Restaurant_Area = models.CharField(max_length=250)
    Restaurant_Street = models.CharField(max_length=250)
    Restaurant_Pin = models.CharField(max_length=6, default=132658)
    Restaurant_City = models.CharField(max_length=250)
    Restaurant_State = models.CharField(max_length=250)
    Restaurant_Phone_Number = PhoneNumberField()
    Restaurant_Logo = models.ImageField(upload_to='Restaurants/static/images/profiles',
                                        default='Restaurants/static/images/profiles/default_res.jpg')
    Restaurant_Ratings_Count = models.IntegerField(default=0)
    Restaurant_Rating = models.IntegerField(MaxValueValidator(10), default=0)

    def __str__(self):
        return str(self.Restaurant_Name) + ' ' + str(self.Restaurant_Area)


class FoodCategory(models.Model):
    FoodCategory_ID = models.AutoField(primary_key=True)
    FoodCategory_Name = models.CharField(max_length=250)

    def __str__(self):
        return str(self.FoodCategory_Name)


class Food(models.Model):
    Food_ID = models.AutoField(primary_key=True)
    Food_Name = models.CharField(max_length=250)
    Food_Res_ID = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    Food_Category_ID = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    Food_Price = models.IntegerField()
    Food_Pic = models.ImageField(upload_to='Restaurants/static/images/food',
                                 default='Restaurants/static/images/food/default_food.jpg')
    Food_Discount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.Food_Name) + ' in ' + str(self.Food_Category_ID.FoodCategory_Name)\
               + ' from ' + str(self.Food_Res_ID.Restaurant_Name)
