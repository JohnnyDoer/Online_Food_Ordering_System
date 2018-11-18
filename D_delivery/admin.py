from django.contrib import admin

# Register your models here.
from .models import Address,Customer,Order
admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(Order)
