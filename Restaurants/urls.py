from . import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.index, name='Res_index'),
    path('signup/', views.signup, name='Res_signup'),
    path('profile/', views.profile_page, name='Res_profile'),
    re_path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.activate, name='Res_activate'),
<<<<<<< HEAD
    path('info/',views.restaurant,name='Res_info'),
    path('add_item/',views.add_item,name='Res_add_item')
=======
    path('info/', views.restaurant, name='Res_info'),
    path('add_item/', views.add_item, name='Res_add_item')
>>>>>>> f515d156fc8491b61ec73cd82bac65c162e3821c
    ]
