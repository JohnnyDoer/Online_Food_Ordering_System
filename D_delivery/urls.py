from django.urls import path
from . import views
app_name = 'D_delivery'
urlpatterns = [
    path('', views.result, name='D_delivery.result'),
    path('result1/', views.result1, name='result1'),
    ]

