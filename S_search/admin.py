from django.contrib import admin

# Register your models here.
from .models import Restaurant,Food_Category,Food
admin.site.register(Restaurant)
admin.site.register(Food_Category)
admin.site.register(Food)
