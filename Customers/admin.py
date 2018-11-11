from django.contrib import admin
from .models import Profile, Address, Order, Item

# Register your models here.
admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(Item)
