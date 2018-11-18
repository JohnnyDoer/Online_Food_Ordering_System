from django.db import models

# Create your models here.

class CustomUser(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    city = models.CharField(max_length=255)
    area = models.CharField(max_length=255,default='abc')
    state = models.CharField(max_length=255,default='abc')
    def __str__(self):
        return self.username