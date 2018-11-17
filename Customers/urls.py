from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Cus_index'),
    path('signup/', views.signup, name='Cus_signup'),
    path('profile/', views.profile_page, name='Cus_profile'),
    path('logout/', views.user_logout, name='logout'),
    path('categories/', views.categories, name='Cus_categories'),
    path('res_area/',views.restaurants,name='res_area')
]
