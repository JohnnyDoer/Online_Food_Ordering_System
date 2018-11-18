from django.db import models

# Create your models here.


class Restaurant(models.Model):
    Restaurant_ID = models.CharField(max_length=150, primary_key=True)
    Restaurant_Name = models.CharField(max_length=150)


class Food_Category(models.Model):
    ID = models.CharField(max_length=150, primary_key=True)
    Category_Name = models.CharField(max_length=150)


class Food(models.Model):
    Food_ResID = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    Food_Category_ID = models.ForeignKey(Food_Category, on_delete=models.PROTECT)
    Food_ID = models.CharField(max_length=150, primary_key=True)
    Food_Name = models.CharField(max_length=150)
    Food_Discount = models.FloatField(null=False)
    Food_Price = models.FloatField(null=False)
    Keywords = models.CharField(max_length=10000)

