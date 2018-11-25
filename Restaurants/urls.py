from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='Res_index'),
    path('signup/', views.signup, name='Res_signup'),
    path('profile/', views.profile_page, name='Res_profile')
]