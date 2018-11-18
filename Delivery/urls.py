from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index , name='Del_index'),
    path('signup/', views.signup, name='Del_signup'),
    path('profile/', views.profile_page, name='Del_profile')
]
