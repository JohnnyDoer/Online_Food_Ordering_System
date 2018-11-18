from django.contrib import admin

# Register your models here.
from .models import Food_Category, Food
admin.site.register(Food_Category)
admin.site.register(Food)
