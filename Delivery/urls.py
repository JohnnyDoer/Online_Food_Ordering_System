from django.urls import path, include
from . import views
from django.urls import path, re_path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index , name='Del_index'),
    path('signup/', views.signup, name='Del_signup'),
    path('profile/', views.profile_page, name='Del_profile'),
    re_path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.activate, name='activate'),
]
