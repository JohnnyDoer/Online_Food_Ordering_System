from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Cus_index'),
    path('signup/', views.signup, name='Cus_signup'),
    path('profile/', views.profilepage, name='Cus_profile'),
    path('categories/', views.categories, name='Cus_categories'),
]
