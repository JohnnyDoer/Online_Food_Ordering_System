from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator
from Restaurants.models import Restaurant, FoodCategory, Food
from Delivery.models import Delivery
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

Areas = (('Cunninghum Road', 'Cunninghum Road'),
         ('Frazer Town', 'Frazer Town'),
         ('Whitefield', 'Whitefield'),
         ('Church Street', 'Church Street'),
         ('Egmore', 'Egmore'),
         ('Thirumalai', 'Thirumalai'),
         ('Anna Salai', 'Anna Salai'),
         ('Mount Road', 'Mount Road'),
         ('Connaught Place', 'Connaught Place'),
         ('Green Park', 'Green Park'),
         ('Nehru Road', 'Nehru Road'),
         ('Golf Course Road', 'Golf Course Road'),
         ('Park Street', 'Park Street'),
         ('Meredith Street', 'Meredith Street'),
         ('Chittaranjan Avenue', 'Chittaranjan Avenue'),
         ('S.N. Banerjee Road', 'S.N. Banerjee Road'),)

Cities = (('Bangalore', 'Bangalore'),
          ('Chennai', 'Chennai'),
          ('Delhi', 'Delhi'),
          ('Kolkata', 'Kolkata'),
          )

States = (('Karnataka', 'Karnataka'),
          ('Tamil Nadu', 'Tamil Nadu'),
          ('Delhi', 'Delhi'),
          ('West Bengal', 'West Bengal'),
          )


class Profile(models.Model):
    Customer_ID = models.AutoField(primary_key=True, auto_created=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Customer_First_Name = models.CharField(max_length=200)
    Customer_Last_Name = models.CharField(max_length=200)
    Customer_Phone_Number = PhoneNumberField(max_length=13)
    Customer_Picture = models.ImageField(upload_to='media',
                                         default='media/default_res.jpg')
    Customer_Email = models.EmailField(default="asd@rew.com")

    def __str__(self):
        return self.user.username


class Address(models.Model):
    Address_ID = models.AutoField(primary_key=True)
    Customer_ID = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Home = models.CharField(max_length=250)
    Street = models.CharField(max_length=250)
    Area = models.CharField(max_length=250, choices=Areas)
    City = models.CharField(max_length=250, choices=Cities)
    State = models.CharField(max_length=250, choices=States)
    Pin = models.CharField(max_length=6, default=000000)

    def __str__(self):
        return self.Area + ' ' + self.City


class Order(models.Model):
    Order_ID = models.AutoField(primary_key=True)
    Order_Customer_ID = models.ForeignKey(Profile, on_delete=models.PROTECT, null=True)
    Order_Restaurant_ID = models.ForeignKey(Restaurant, on_delete=models.PROTECT, null=True)
    Order_Delivery_ID = models.ForeignKey(Delivery, on_delete=models.PROTECT, null=True)
    Order_Status = models.IntegerField(MaxValueValidator(5), null=True)
    Order_Time = models.DateTimeField(default=timezone.now, null=True)
    Order_Total_Price = models.IntegerField(default=0, null=True)



class Item(models.Model):
    Item_ID = models.AutoField(primary_key=True)
    Item_Order_ID = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    Item_Food_ID = models.ForeignKey(Food, on_delete=models.CASCADE)
    Item_Quantity = models.IntegerField(MaxValueValidator(10))
    Item_Price = models.IntegerField(default=0)


class CartItems(models.Model):
    Cart_ID = models.AutoField(primary_key=True)
    Cart_Customer_ID = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Cart_Food_ID = models.ForeignKey(Food, on_delete=models.CASCADE)
    Quantity = models.IntegerField(MaxValueValidator(5), null=True)