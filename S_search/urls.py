from django.urls import path
from . import views
app_name = 'S_search'
urlpatterns = [
    path('', views.result, name='S_search.result'),
    ]

