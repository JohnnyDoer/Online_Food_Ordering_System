from django.db import models
from django.contrib.auth.models import User
from Customers.models import Profile,Address
Areas = (('thames','thames'),
       ('lambeth', 'lambeth'),
       ('southpark', 'southpark'),
       ('nova', 'nova'))


class Order(models.Model):
    Order_id = models.CharField(max_length=100,unique=True)
    Customer_id = models.ForeignKey(Profile,on_delete=models.CASCADE)
    Address_id = models.ForeignKey(Address,on_delete=models.CASCADE)


class DelProfile(models.Model):
    Delivery_id=models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Delivery_Fname = models.CharField(max_length=200)
    Delivery_Lname = models.CharField(max_length=200)
    Delivery_Num = models.CharField(max_length=10,unique=True)
    Delivery_Area = models.CharField(max_length=105,choices=Areas)
    Delivery_City = models.CharField(max_length=200)
    Delivery_State = models.CharField(max_length=200)
    #order_id = models.ForeignKey(Order,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



