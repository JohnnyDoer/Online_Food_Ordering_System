from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Cus_index'),
    path('profile/',views.profilepage,name='cus_profile'),
    path('signup/', views.signup, name='Cus_signup'),
    path('categories/', views.categories, name='Cus_categories'),
    path('logout/', views.user_logout, name='logout'),
]
