from django.db import models
from django.contrib.auth.models import User
from Restaurants.models import Restaurant, FoodCategory, Food
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


class Delivery(models.Model):
    Delivery_ID = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Delivery_First_Name = models.CharField(max_length=250)
    Delivery_Last_Name = models.CharField(max_length=250)
    Delivery_Phone_Number = PhoneNumberField()
    Delivery_Area = models.CharField(max_length=250, choices=Areas)
    Delivery_City = models.CharField(max_length=250, choices=Cities)
    Delivery_State = models.CharField(max_length=250, choices=States)
    Delivery_Pin = models.CharField(max_length=6, default=000000)
    Delivery_Pic = models.ImageField(upload_to='Delivery/static/images/profiles',
                                     default='Delivery/static/images/profiles/default_del.jpg')
