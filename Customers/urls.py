from django.urls import path
from . import views

urlpatterns = [
    path('', views.cusindex, name='Cus_index'),
    path('profile/',views.profilepage,name='cus_profile'),
    path('signup/', views.signup, name='Cus_signup'),
    path('categories/', views.categories, name='Cus_categories'),
    path('logout/', views.user_logout, name='logout'),
    path('res_area/',views.restaurants,name='res_area')
]
