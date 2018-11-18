from django.contrib import admin

# Register your models here.
from .models import Order,Food,Items
admin.site.register(Order)
admin.site.register(Food)
admin.site.register(Items)
