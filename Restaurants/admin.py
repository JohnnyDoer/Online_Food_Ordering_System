from django.contrib import admin

from .models import Restaurant, Food, FoodCategory, Area, City

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(FoodCategory)
admin.site.register(City)
admin.site.register(Area)
