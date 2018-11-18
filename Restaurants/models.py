from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MaxValueValidator
# from Delivery.models import Delivery
# from Customers.models import Customer, Address, Order, Item

# Create your models here.


class Restaurant(models.Model):
    Restaurant_ID = models.AutoField(primary_key=True)
    Restaurant_Name = models.CharField(max_length=250)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Restaurant_Logo = models.ImageField(upload_to='Restaurants/Pictures/Logo')
    # + str(Restaurant_ID) + '/' + str(Restaurant_Name))
    Restaurant_Area = models.CharField(max_length=250)
    Restaurant_Pin = models.CharField(max_length=6, default=132658)
    Restaurant_City = models.CharField(max_length=250)
    Restaurant_State = models.CharField(max_length=250)
    Restaurant_Regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                            message="Phone number must be entered in the format:" +
                                            " '+999999999'. Up to 15 digits allowed.")
    Restaurant_Num = models.CharField(validators=[Restaurant_Regex], max_length=17)
    Restaurant_Email = models.CharField(max_length=250)
    Restaurant_Ratings_Count = models.IntegerField(default=0)
    Restaurant_Rating = models.IntegerField(MaxValueValidator(10), default=0)


class FoodCategory(models.Model):
    FoodCategory_ID = models.AutoField(primary_key=True)
    FoodCategory_Name = models.CharField(max_length=250)

class Food(models.Model):
    Food_ID = models.AutoField(primary_key=True)
    Food_Name = models.CharField(max_length=250)
    Food_Pic = models.ImageField(upload_to='Restaurants/Pictures/Food')
    Food_Category_ID = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    Food_Price = models.IntegerField()
    Food_Discount = models.IntegerField(default=0)
    Food_Res_ID = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

