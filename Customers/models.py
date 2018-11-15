from django.db import models
from django.contrib.auth.models import User
Areas=(('thames','thames'),
       ('lambeth', 'lambeth'),
       ('southpark', 'southpark'),
       ('nova', 'nova'))


class Profile(models.Model):
    Customer_id=models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    mobilenumber = models.CharField(max_length=10,unique=True)
    def __str__(self):
        return self.user.username


class Address(models.Model):
    Address_id=models.AutoField(primary_key=True)
    username=models.OneToOneField(User, on_delete=models.PROTECT)
    home=models.CharField(max_length=50)
    society=models.CharField(max_length=300)
    Area=models.CharField(max_length=60,choices=Areas)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=60)