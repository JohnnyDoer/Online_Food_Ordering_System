from django.db import models
from django.contrib.auth.models import User
from Customers.models import Profile,Address
Areas=(('thames','thames'),
       ('lambeth', 'lambeth'),
       ('southpark', 'southpark'),
       ('nova', 'nova'))

# Create your models here.


class ResProfile(models.Model):
    Restaurant_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Restaurant_Name = models.CharField(max_length=200)
    Restaurant_Num = models.CharField(max_length=10,unique=True)
    Restaurant_Area = models.CharField(max_length=105,choices=Areas)
    Restaurant_City = models.CharField(max_length=200)
    Restaurant_State = models.CharField(max_length=200)
    #Ratings_Count = models.IntegerField()

    def __str__(self):
        return self.user.username
