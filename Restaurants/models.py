from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
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


class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Area(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    Restaurant_ID = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Restaurant_Name = models.CharField(max_length=250)
    Restaurant_Street = models.CharField(max_length=250)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)
    Restaurant_Pin = models.CharField(max_length=6, default=132658)
    Restaurant_Phone_Number = PhoneNumberField()
    Restaurant_Logo = models.ImageField(upload_to='media',
                                        default='media/default_res.jpg')
    Restaurant_Ratings_Count = models.IntegerField(default=0)
    Restaurant_Rating = models.IntegerField(MaxValueValidator(10), default=0)

    def __str__(self):
        return str(self.Restaurant_Name) + ' ' + str(self.area.name)


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
    Food_Pic = models.ImageField(upload_to='media',
                                 default='media/default_food.jpg')
    Food_Discount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.Food_Name) + ' in ' + str(self.Food_Category_ID.FoodCategory_Name)\
               + ' from ' + str(self.Food_Res_ID.Restaurant_Name)
