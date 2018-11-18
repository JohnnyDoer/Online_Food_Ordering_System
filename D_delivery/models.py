from django.db import models

# Create your models here.


class Customer(models.Model):
    Customer_ID = models.CharField(max_length=150)


class Address(models.Model):
    Address_ID = models.CharField(max_length=150)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    Order_ID = models.CharField(max_length=150, primary_key=True)
    Discount = models.FloatField(null=False)
    Total_Price = models.FloatField(null=False)
    Status = models.BooleanField(null=False)

