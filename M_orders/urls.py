from django.urls import path
from . import views
app_name = 'M_orders'
urlpatterns = [
    path('', views.result, name='M_orders.result'),

]

