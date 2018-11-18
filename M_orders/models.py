from django.db import models

# Create your models here.


class Order(models.Model):
    Order_ID = models.CharField(max_length=150, primary_key=True)
    Discount = models.FloatField(null=False)
    Total_Price = models.FloatField(null=False)
    Status = models.BooleanField(null=False)


class Food(models.Model):
    Food_ID = models.CharField(max_length=150, primary_key=True)
    Food_Name = models.CharField(max_length=150)
    Food_Discount = models.FloatField(null=False)
    Food_Price = models.FloatField(null=False)
    Keywords = models.CharField(max_length=10000)
    ratings_count = models.FloatField(null=False)
    Rating = models.FloatField(null=False)


class Items(models.Model):
    Item_ID = models.CharField(max_length=150, primary_key=True)
    Order_ID = models.ForeignKey(Order, on_delete=models.PROTECT)
    Food_ID = models.ForeignKey(Food, on_delete=models.PROTECT)
    Quantity = models.FloatField(null=False)
    Price = models.FloatField(null=False)

