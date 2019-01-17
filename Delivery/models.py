from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from Restaurants.models import Restaurant, FoodCategory, Food

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


class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Area(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Delivery(models.Model):
    Delivery_ID = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Delivery_First_Name = models.CharField(max_length=250)
    Delivery_Last_Name = models.CharField(max_length=250)
    Delivery_Phone_Number = PhoneNumberField()
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)
    Delivery_Pin = models.CharField(max_length=6, default=000000)
    Delivery_Pic = models.ImageField(upload_to='media',
                                     default='media/default_profile.jpg')
